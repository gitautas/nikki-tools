#!/usr/bin/env python3

from pathlib import Path

types = ["asset", "fbx", "prefab" ]

p = Path(".")

for ext in types:
    for assetfile in list(p.glob("**/*." + ext)):
        with assetfile.open("rb") as momo:
            data = momo.read()[8:]
            momo.write(data)
            momo.close()
