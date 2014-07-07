# Establish 4 blocks
# Red = 1, Blue = 10, Green = 100, White = 1000
# Front, Right, Back, Left, Top, Bottom
blocks = []
blocks.append([100,1,100,10,1000,10]) # first cube
blocks.append([1000,100,1,1000,1,10]) # second cube
blocks.append([1,1000,100,100,1000,10]) # third cube
blocks.append([100,1,1,1,1000,10])  # fourth cube
#print block

# Check correct results
def check(cubelist):
    correct_sides = 0
    for i in range(4):
        if (cubelist[0][i] + cubelist[1][i] + cubelist[2][i] + cubelist[3][i] == 1111):
            correct_sides += 1
    if correct_sides == 4:
        return True
    else:
        return False


# Turn cube
def spin(cube): # Spin cube on Y axis
    new_cube = []
    new_cube = [cube[1],cube[2],cube[3],cube[0],cube[4],cube[5]]
    return new_cube
#print spin(blocks[0])

def rotateZ(cube): # Rotate cube on Z axis
    new_cube = [cube[0],cube[4],cube[2],cube[5],cube[3],cube[1]]
    return new_cube
#print rotate(blocks[0])

def rotateX(cube):
    new_cube = [cube[4],cube[1],cube[5],cube[3],cube[2],cube[0]]
    return new_cube
#print rotateX(blocks[0])

def printcube(cubelist):
    print "[ \tFront \tRight  \tBack \tLeft \tTop \tBottom \t]"
    for i in cubelist:
        print "[ ",
        for j in i:
          if j == 1:
            print "\tRed ",
          if j == 10:
            print "\tBlue ",
          if j == 100:
            print "\tGreen ",
          if j == 1000:
            print "\tWhite ",
        print "\t]"

# Solve puzzle
for i in range(24):
    print i
    for j in range(24):
        for k in range(24):
            for l in range(24):
                if l % 4 == 0 and l != 12:
                    blocks[3] = rotateZ(blocks[3])
                elif l % 12 == 0:
                    blocks[3] = rotateX(blocks[3])
                else:
                    blocks[3] = spin(blocks[3])
                if check(blocks):
                    print "SUCCESS!"
                    printcube(blocks)
                    break
            if check(blocks):
                break
            if k % 4 == 0 and k != 12:
                blocks[2] = rotateZ(blocks[2])
            elif k % 12 == 0:
                blocks[2] = rotateX(blocks[2])
            else:
                blocks[2] = spin(blocks[2])
        if check(blocks):
            break
        if j % 4 == 0 and j != 12:
            blocks[1] = rotateZ(blocks[1])
        elif j % 12 == 0:
            blocks[1] = rotateX(blocks[1])
        else:
            blocks[1] = spin(blocks[1])
    if check(blocks):
        break
    if i % 4 == 0 and i != 12:
        blocks[0] = rotateZ(blocks[0])
    elif i % 12 == 0:
        blocks[0] = rotateX(blocks[0])
    else:
        blocks[0] = spin(blocks[0])
