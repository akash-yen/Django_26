from pathlib import Path

pt = Path(__file__)
print(pt.resolve().parent.parent)