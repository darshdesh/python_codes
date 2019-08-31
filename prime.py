num = int(input("Enter a number: "))
for i in range(2, num):
    if (num % i) == 0:
        print(num, "Is Not a Prime Number")
        break
else:
    print(num, "Is Prime Number")
