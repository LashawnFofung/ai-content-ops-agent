"""Voiceover mastering: trim, tighten pauses, clean, EQ, de-ess, compress, two-pass loudness."""
import json, re, subprocess
import numpy as np

m = json.load(open("vo/map.json"))  # {"1": "path/to/part1.m4a", "2": ...}
SR = 48000

CHAIN = ",".join([
    "highpass=f=80:poles=2",                          # rumble / desk thumps
    "afftdn=nr=8:nf=-70:tn=1",                        # gentle broadband noise reduction (tracks the floor)
    "equalizer=f=200:t=q:w=1.2:g=-2.5",               # clear low-mid mud / room boxiness
    "equalizer=f=3200:t=q:w=1.0:g=2.5",               # presence / intelligibility
    "highshelf=f=10000:g=1.5",                        # air
    "deesser=i=0.35:m=0.5:f=0.5",                     # tame sibilance after the presence lift
    "acompressor=threshold=-22dB:ratio=3:attack=8:release=140:makeup=2:knee=4",
    "alimiter=limit=0.89:attack=3:release=60",
])
# drop leading/trailing silence, shorten any internal pause longer than 0.7 s to 0.45 s
TRIM = ("silenceremove=start_periods=1:start_threshold=-48dB:start_silence=0.05,"
        "areverse,silenceremove=start_periods=1:start_threshold=-48dB:start_silence=0.12,areverse,"
        "silenceremove=stop_periods=-1:stop_duration=0.7:stop_threshold=-48dB:stop_silence=0.45")


def run(args):
    return subprocess.run(args, capture_output=True, text=True, stdin=subprocess.DEVNULL)


info = {}
for n in sorted(m, key=int):
    src, mid, out = m[n], f"vo/{int(n):02d}_pre.wav", f"vo/{int(n):02d}.wav"
    run(["ffmpeg", "-y", "-i", src, "-ac", "1", "-ar", str(SR), "-af", TRIM + "," + CHAIN, mid])
    # two-pass loudnorm to -16 LUFS (dialogue target; final mix is checked against -14)
    e = run(["ffmpeg", "-i", mid, "-af", "loudnorm=I=-16:TP=-1.5:LRA=7:print_format=json", "-f", "null", "-"]).stderr
    j = json.loads(e[e.rfind("{"):e.rfind("}") + 1])
    ln = (f"loudnorm=I=-16:TP=-1.5:LRA=7:measured_I={j['input_i']}:measured_TP={j['input_tp']}:"
          f"measured_LRA={j['input_lra']}:measured_thresh={j['input_thresh']}:offset={j['target_offset']}:linear=true")
    run(["ffmpeg", "-y", "-i", mid, "-af", ln, "-ar", str(SR), "-ac", "1", out])
    # pauses (for cueing reveals) and duration
    pcm = subprocess.run(["ffmpeg", "-v", "error", "-i", out, "-f", "s16le", "-ac", "1", "-ar", "16000", "-"],
                         capture_output=True, stdin=subprocess.DEVNULL).stdout
    a = np.frombuffer(pcm, np.int16).astype(float) / 32768
    w = a[:len(a) // 320 * 320].reshape(-1, 320)            # 20 ms windows
    db = 20 * np.log10(np.sqrt((w ** 2).mean(1)) + 1e-9)
    quiet = db < -45
    pauses, start = [], None
    for i, q in enumerate(quiet):
        if q and start is None:
            start = i
        if not q and start is not None:
            if (i - start) * .02 >= .25:
                pauses.append((round(start * .02, 2), round((i - start) * .02, 2)))
            start = None
    dur = len(a) / 16000
    e = run(["ffmpeg", "-i", out, "-af", "ebur128=peak=true", "-f", "null", "-"]).stderr
    I = re.findall(r"I:\s+(-?[\d.]+) LUFS", e)[-1]
    tp = re.findall(r"Peak:\s+(-?[\d.]+) dBFS", e)[-1]
    info[n] = {"dur": round(dur, 2), "pauses": pauses}
    print(f"{int(n):2d}  {dur:5.1f}s  I {I} LUFS  TP {tp}  pauses {pauses}")
json.dump(info, open("vo/info.json", "w"), indent=1)
