x = int(input())

stick_list = [64, 32, 16, 8, 4, 2, 1]
count = 0

for i in range(len(stick_list)):
    if x >= stick_list[i]:
        count += 1
        x -= stick_list[i]

    if x == 0:
        break

print(count)