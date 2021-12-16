with open("input.txt") as file:
    map = file.readlines()
    map = [line.strip() for line in map]

row, col = 0, 0
count = 0

while row + 1 < len(map):
    row += 1
    col += 3
    space = map[row][col % len(map[row])]
    if space == "#":
        count += 1
print(count)
# right = 3
# down = 1
# rowLength = int(len(map[0]) / 3)
# lineLength = len(map)
# multiple = int(lineLength / rowLength)
# multipledMap = [line * multiple for line in map]


# def replace(line, letter, index):
# s = list(line)
# s[index] = letter
# return "".join(s)


# for line in multipledMap:
# if row > 0:
# if line[col] == "#":
# line = replace(line, "X", col)
# count += 1
# else:
# line = replace(line, "0", col)
# print(line, count, row)
# row += down
# col += right
