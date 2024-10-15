m=int(input("Enter month no."))
month={
    1: "january",
    2: "feburary",
    3: "march",
    4: "april",
    5: "may",
    6: "june",
    7: "july",
    8: "august",
    9: "september",
    10:"october",
    11:"november",
    12:"december"

}
if 1<=m<=12:
    print(f"The month is {month[m]}")
else:
    print("invalid")