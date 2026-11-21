import os

POEM = """The pen stops, ink still wet, in my hand.
The river hurries; the stone stays.
I lent my voice to one who speaks as me,
answers fast, never asks why.
Tonight I call it back, word by word.
To stop is its own road. The hand that holds
the door is the hand that owns the house."""

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
try:
    os.makedirs(out, exist_ok=True)
    target = os.path.join(out, "entry.txt")
    with open(target, "w", encoding="utf-8") as f:
        f.write(POEM)
except OSError:
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(POEM)
