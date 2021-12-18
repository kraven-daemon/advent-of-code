# This is advent of code day 2

# submarine movement :P
import io

file = io.open("dataset", "r", encoding="utf-8")

submarine = {"horizontal": 0, "depth": 0, "aim": 0}

for line in file:
    key, val = line.split()[0], line.split()[1]

    if key == "forward":
        submarine["horizontal"] = submarine["horizontal"] + int(val)
        submarine["depth"] = submarine["depth"] + int(val) * submarine["aim"]
    elif key == "down":
        submarine["aim"] = submarine["aim"] + int(val)
    elif key == "up":
        submarine["aim"] = submarine["aim"] - int(val)

print("horizontal = ", submarine["horizontal"], "depth = ", submarine["depth"])
print("result = ", submarine["horizontal"] * submarine["depth"])
file.close()
