def pyramid(n):
    for i in range(n):
        for j in range(i,n):
            print(" ", end="")
        for j in range(i + 1):
            print("*", end="")
        for j in range(i):
            print("*", end="")
        print("")
pyramid(6)

num = int(input("enter odd number: "))
spaces= num // 2
stars = 1
for i in range(spaces + 1):
    print(spaces*" " + "*"*stars)
    spaces-= 1
    stars+=2
stars = num -2
spaces = 1
for i in range(num//2):
    print(spaces*" " + "*"*stars)
    stars-=2
    spaces+=1