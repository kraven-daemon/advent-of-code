# This is advent of code day 3
# part 2

import io

# same dataset but now we filter out result
# as an oxygen vs CO2 sensor data

# unlike part 1 we need to perform multiple operations on the same dataset so
# for that one lets just preload the data into memory
# and inside a function to let the gc do its job. ;P
# and cycle through functions so gc free the mem between filters..


def load_this():
    file = io.open("dataset", "r", encoding="utf-8")
    data = []
    for line in file:
        data.append(line)
    file.close()
    return data


# we'll need to return 2 filtered array and move the pointer
# in the corresponding : most_common,least_common
# lets just make it a dictionnary


def split_it(data):
    ones, zeros = [], []
    acc = [0, 0]
    for v in data:
        if v[0] == '0':
            zeros.append(v)
            acc[0] += 1
        else:
            ones.append(v)
            acc[1] += 1
    splitted = {"ismost": [], "isleast": []}
    if acc[0] > acc[1]:
        splitted["ismost"] = zeros
        splitted["isleast"] = ones
    else:
        splitted["ismost"] = ones
        splitted["isleast"] = zeros
    return splitted


darray = load_this()
bound = len(darray[0]) - 1

splitted = split_it(darray)
# split recusively, rebinding the dict pointer
# to subsequent array as we filter to the remaining conditions


def re_filter(dict, key, index):
    ones, zeros = [], []
    acc = [0, 0]
    for v in dict[key]:
        if v[index] == '0':
            zeros.append(v)
            acc[0] += 1
        else:
            ones.append(v)
            acc[1] += 1
    if key == "ismost":
        if acc[0] > acc[1]:
            dict[key] = zeros
        elif acc[0] <= acc[1]:
            dict[key] = ones
    elif key == "isleast":
        if acc[0] <= acc[1]:
            dict[key] = zeros
        elif acc[0] > acc[1]:
            dict[key] = ones


# print(len(splitted["ismost"]), " ", splitted["ismost"])

for i in range(1, 12):
    print(i, " ", len(splitted["ismost"]))
    if len(splitted["ismost"]) == 1:
        break
    else:
        re_filter(splitted, "ismost", i)

print(splitted["ismost"])
# print(len(splitted["ismost"]), " ", splitted["ismost"])

for i in range(1, 12):
    print(i, " ", len(splitted["isleast"]))
    if len(splitted["isleast"]) == 1:
        break
    else:
        re_filter(splitted, "isleast", i)


o = 0
c = 0
bit_pos = bound - 1
# # now to binary
for i in range(0, bound):
    o += int(splitted["ismost"][0][i]) * 2 ** bit_pos
    c += int(splitted["isleast"][0][i]) * 2 ** bit_pos
    bit_pos -= 1

# this is the end
print("Result {} * {} = {}".format(o, c, o * c))
