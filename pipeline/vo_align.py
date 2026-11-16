"""Tighten long pauses (>0.65 s -> 0.5 s, crossfaded) and get rough word timings with pocketsphinx."""
import json, subprocess, wave
import numpy as np
from pocketsphinx import Decoder, Config, get_model_path
import os

SR = 48000
info = json.load(open("vo/info.json"))


def read(p):
    a = subprocess.run(["ffmpeg", "-v", "error", "-i", p, "-f", "f32le", "-ac", "1", "-ar", str(SR), "-"],
                       capture_output=True, stdin=subprocess.DEVNULL).stdout
    return np.frombuffer(a, np.float32).copy()


def write(p, a):
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "f32le", "-ar", str(SR), "-ac", "1", "-i", "-",
                    "-c:a", "pcm_s24le", p], input=a.astype(np.float32).tobytes(), check=True)


def tighten(a, max_gap=.65, keep=.5, thr=-45):
    win = int(SR * .02)
    n = len(a) // win
    db = 20 * np.log10(np.sqrt((a[:n * win].reshape(n, win) ** 2).mean(1)) + 1e-9)
    quiet = db < thr
    out, last, i, removed = [], 0, 0, 0.0
    xf = int(SR * .01)
    while i < n:
        if quiet[i]:
            j = i
            while j < n and quiet[j]:
                j += 1
            gap = (j - i) * .02
            if gap > max_gap and i > 0 and j < n:
                cut_from = i * win + int(SR * keep / 2)
                cut_to = j * win - int(SR * keep / 2)
                seg = a[last:cut_from].copy()
                if out:
                    seg[:xf] *= np.linspace(0, 1, xf)
                seg[-xf:] *= np.linspace(1, 0, xf)
                out.append(seg)
                last = cut_to
                removed += (cut_to - cut_from) / SR
            i = j
        else:
            i += 1
    seg = a[last:].copy()
    if out:
        seg[:xf] *= np.linspace(0, 1, xf)
    out.append(seg)
    # 80 ms of room tone at the head, 150 ms at the tail
    return np.concatenate([np.zeros(int(SR * .08)), *out, np.zeros(int(SR * .15))]), removed


mp = get_model_path()
cfg = Config(hmm=os.path.join(mp, "en-us", "en-us"), lm=os.path.join(mp, "en-us", "en-us.lm.bin"),
             dict=os.path.join(mp, "en-us", "cmudict-en-us.dict"), loglevel="FATAL")
dec = Decoder(cfg)

for n in sorted(info, key=int):
    k = f"{int(n):02d}"
    raw = read(f"vo/{k}.wav")
    # remove the spoken slate ("Scene N, title"): everything before the first pause >= 0.85 s in the first 5 s
    slate = next(((s0, d) for s0, d in info[n]["pauses"] if s0 < 5 and d >= .85), None)
    if slate:
        cut = slate[0] + slate[1] - .12
        raw = raw[int(cut * SR):]
        info[n]["slate_cut"] = round(cut, 2)
    a, removed = tighten(raw)
    write(f"vo/{k}_final.wav", a)
    pcm = subprocess.run(["ffmpeg", "-v", "error", "-i", f"vo/{k}_final.wav", "-f", "s16le", "-ac", "1", "-ar", "16000", "-"],
                         capture_output=True, stdin=subprocess.DEVNULL).stdout
    dec.start_utt(); dec.process_raw(pcm, full_utt=True); dec.end_utt()
    words = [(s.word, round(s.start_frame / 100, 2)) for s in dec.seg() if not s.word.startswith(("<", "["))]
    info[n]["final_dur"] = round(len(a) / SR, 2)
    info[n]["words"] = words
    print(f"{n:>2} {len(a)/SR:5.1f}s (-{removed:.1f}s pauses) :: " + " ".join(f"{w}@{t}" for w, t in words))
json.dump(info, open("vo/info.json", "w"), indent=1)
