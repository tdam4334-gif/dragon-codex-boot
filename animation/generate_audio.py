"""Generate the original, quiet synthesizer cue for the startup film."""
from pathlib import Path
import wave

import numpy as np

RATE = 44100
DURATION = 14.4
t = np.arange(int(RATE * DURATION), dtype=np.float64) / RATE
audio = np.zeros_like(t)


def note(start: float, duration: float, frequency: float, gain: float) -> None:
    local = t - start
    active = (local >= 0) & (local < duration)
    x = local[active]
    envelope = np.minimum(x / 0.08, 1.0) * np.minimum((duration - x) / 0.75, 1.0)
    tone = np.sin(2 * np.pi * frequency * x) + 0.26 * np.sin(2 * np.pi * frequency * 2 * x)
    audio[active] += gain * envelope * tone


for start, freq in [(0.3, 110), (1.4, 164.81), (2.5, 220), (4.7, 293.66),
                    (5.3, 110), (6.2, 146.83), (7.1, 220), (8.2, 329.63),
                    (10.4, 164.81), (11.3, 220), (12.35, 329.63)]:
    note(start, 1.9 if start < 10 else 2.0, freq, 0.052)
note(12.5, 1.75, 440, 0.025)
audio = np.clip(audio, -0.8, 0.8)
target = Path(__file__).parent / "assets" / "boot.wav"
target.parent.mkdir(parents=True, exist_ok=True)
with wave.open(str(target), "wb") as wav:
    wav.setnchannels(1)
    wav.setsampwidth(2)
    wav.setframerate(RATE)
    wav.writeframes((audio * 32767).astype("<i2").tobytes())
print(target)
