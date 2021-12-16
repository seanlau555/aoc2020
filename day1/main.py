inputs = [
    1721,
    979,
    366,
    299,
    675,
    1456,
]

with open("input.txt") as f:
    lines = f.readlines()

nums = [int(line.strip()) for line in lines]

# 2 vectors
largest2 = 0
for i in range(len(nums) - 1):
    for j in range(i + 1, len(nums)):
        num1 = nums[i]
        num2 = nums[j]
        if num1 + num2 == 2020:
            balance = num1 * num2

            if balance > largest2:
                largest2 = balance
print(largest2)


largest3 = 0
for i in range(len(nums) - 1):
    for j in range(i + 1, len(nums)):
        for k in range(j + 1, len(nums)):
            num1 = nums[i]
            num2 = nums[j]
            num3 = nums[k]
            if num1 + num2 + num3 == 2020:
                balance = num1 * num2 * num3

                if balance > largest3:
                    largest3 = balance

print(largest3)
