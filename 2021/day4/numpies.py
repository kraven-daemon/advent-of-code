# smaller dataset
import numpy as n
import io

# read and format the first line as the draw
file = io.open("dataset", "r", encoding="utf-8")
draw = n.loadtxt(io.StringIO(file.readline()), delimiter=',', dtype=int)
# all the cardboards
data = n.loadtxt("dataset", dtype=int, skiprows=2)
file.close()

# 5x5
cardboards = int(len(data) / 5)
# reshape the set into 3D => (card, row, column)
dt = data.reshape((cardboards, 5, 5))

# create `punch card` validation
# initialize the booleen mask to false/0 to the actual data-table shape
mask = n.zeros(dt.shape, dtype=bool)

# now mutate the mask
# chain the first 4
for v in range(0, 4):
    # new booleen mask
    nmask = dt == draw[v]
    # merge the newly drawed True to the previous mask
    mask = n.logical_or(nmask, mask)

# potential winner after 5
print("before \n", mask[1])

# i dont remember how to do this with numpy
# lets just do it from scratch

win_order = []  # lookup table/memoization

# card #
for v in range(4, len(draw)):
    # check the draw in a new mask
    nmask = dt == draw[v]
    # get the first card that match a full row/col on the grid
    for card in range(0, cardboards):
        # reset match position inbetween cards

        pos = {"x": 0, "y": 0}
        for i in range(0, 5):
            for j in range(0, 5):
                if nmask[card][i][j] == True:
                    pos["x"] = i
                    pos["y"] = j
        # here update the nmask to mask and check row/col for match
        mask[card] = n.logical_or(nmask[card], mask[card])
        # just check row and col
        row = 0
        for i in range(0, 5):
            # all true
            if mask[card][pos["x"]][i] == True:
                row += 1
        if row == 5:
            print("WINNER is card : ", card)
            # now compute result
            # sum unmarked and, multiply by the number that was `called`
            # so at curr card, (diff dt from mask) * (num at pos in dt)
            print("win from index : ", pos)
            print(nmask[card])
            print("Result")
            print(mask[card])
            print("Numbers")
            print(dt[card])
            print(draw[:v+1])
            sum = n.ma.array(dt[card], mask=mask[card]).sum()
            nwin = dt[card][pos["x"]][pos["y"]]
            print("Sum : ", sum)
            print("Winning number : ", nwin)
            print("Answer = ", sum * nwin)
            win_order.append(card)
            

        else:
            col = 0
            for i in range(0, 5):
                if mask[card][i][pos["y"]] == True:
                    col += 1
            if col == 5:
                print("WINNER is card : ", card)
                # now compute result
                # sum unmarked and, multiply by the number that was `called`
                # so at curr card, (diff dt from mask) * (num at pos in dt)
                print("win from index : ", pos)
                print(nmask[card])
                print("Result")
                print(mask[card])
                print("Numbers")
                print(dt[card])
                print(draw[:v+1])
                sum = n.ma.array(dt[card], mask=mask[card]).sum()
                nwin = dt[card][pos["x"]][pos["y"]]
                print("Sum : ", sum)
                print("Winning number : ", nwin)
                print("Answer = ", sum * nwin)
                win_order.append(card)
                
    # break from nested loops
    # else:
    #     continue
    # break

# i guess im getting lazy
output = []
for x in win_order:
    if x not in output:
        output.append(x)
# pipe this output into | grep "WINNER is card :  21" , answer is below
print(output[-1])



