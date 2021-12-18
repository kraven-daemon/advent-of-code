# This is advent of code day 1 puzzle solution in python
# been a while not scripting in python :P
import io

file = io.open("dataset", "r", encoding="utf-8")

# initialize list
alist = []
readable = True
while readable:
    nex = file.readline()
    if nex:
        alist.append(int(nex))
    else:
        readable = False
file.close()


# affect next three value to the sub-list
def affect3(trinity, bigl, atindex):
    for i in range(0, 3):
        trinity[i] = bigl[atindex+i]


# return the sum of the sublist
def sum3(trinity):
    acc = 0
    for n in trinity:
        acc += n
    return acc


# sub list for comparison to be summed
trio = [0, 0, 0]
# affect the first round
affect3(trio, alist, 0)
psum = sum3(trio)
nsum = 0
inc = 0
# stop the sub list trio affectation before it breaks
length = len(alist)
to = length - (length % 3)

# just iter the list comparing previous sum with the next one
for i in range(1, to):
    affect3(trio, alist, i)
    nsum = sum3(trio)
    if psum < nsum:
        inc += 1
    psum = nsum

print("Result : ", inc)
