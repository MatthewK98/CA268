print("Enter numbers (-1 to end): ", end="")
appeared_num = []
prev = []
while True:
    num = int(input())
    if num == -1:
        break
    elif num in appeared_num:
        print(str(num) + " ", end="")
    else:
        appeared_num.append(num)
print ()