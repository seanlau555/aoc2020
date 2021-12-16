import csv

with open("input.csv") as data:
    reader = csv.reader(data, delimiter=" ")

    ok = 0
    valid = 0
    for row in reader:
        # get all the data
        quota, letter, pw = row[0], row[1][0], row[2]
        mi, ma = int(quota.split("-")[0]), int(quota.split("-")[1])

        if letter in pw:
            # counting amount
            nums = [p for p in pw if p == letter]
            if len(nums) in range(mi, ma + 1):
                ok += 1

            # counting position
            p1, p2 = pw[mi - 1] == letter, pw[ma - 1] == letter
            if (p1 and not p2) or (p2 and not p1):
                valid += 1


print(ok, valid)
