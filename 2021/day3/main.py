# This is advent of code day 3
import io


# mesure gamma and epsilon
# or most occurent vs less occurent bit
# then multiply them

file = io.open("dataset", "r", encoding="utf-8")

# initialize an accumulator that match the size of the input
line = file.readline()
input_size = len(line)-1
acc = []
for i in range(0, input_size):
    acc.append([0, 0])


# compile or treat a row, or a line..
def treat(chunk):
    for i in range(0, input_size):
        if chunk[i] == "0":
            acc[i][0] += 1
        else:
            acc[i][1] += 1


treat(line)

# compile all the rest
for li in file:
    treat(li)
file.close()

# time to rate gamma and epsilon
result = {"gamma": [], "epsilon": []}

for i in range(0, input_size):
    if acc[i][0] > acc[i][1]:
        result["gamma"].append(0)
        result["epsilon"].append(1)
    else:
        result["gamma"].append(1)
        result["epsilon"].append(0)

# now to binary
gamma, epsilon = 0, 0
bit_pos = input_size-1
# these are bit so add the power of 2 according to unit position
for i in range(0, input_size):
    gamma += result["gamma"][i] * 2 ** bit_pos
    epsilon += result["epsilon"][i] * 2 ** bit_pos
    bit_pos -= 1

print(gamma, " * ", epsilon, " = ", gamma*epsilon)
