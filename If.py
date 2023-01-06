# Write a program that asks user to enter a number and program should tell if the number is even or odd?

def a(a1):
    a1 = int(a1)
    if a1%2==0:
        print("{} is even".format(a1))
    else:
            print("{} is odd".format(a1))


a(input("enter a number:"))



# Write a program which asks user to enter a dish name and it should print which cuisine is that dish?

indian = ["samosa", "daal", "naan"]
chinese = ["egg roll", "pot sticker", "fried rice"]
italian = ["pizza", "pasta", "risotto"]


dish = input("enter a dish name:")
if dish in indian:
    print("indian")
elif dish in chinese:
    print("chinese")
elif dish in italian:
    print("italian")
else:
    print("i dont know")