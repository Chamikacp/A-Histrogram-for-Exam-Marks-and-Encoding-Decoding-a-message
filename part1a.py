counter = 0
mark = 0
range1 = 0
range2 = 0
range3 = 0
range4 = 0
mark = int(input("Enter a mark:"))
while mark >= 0:
    if mark > 69:
        range4 += 1
    elif mark > 39:
        range3 += 1
    elif mark > 29:
        range2 += 1
    else:
        range1 += 1
    counter += 1
    mark = int(input("Enter a mark:"))
print("0-29  ="  ,'*' * range1)
print("30-39 ="  ,'*' * range2)
print("40-69 ="  ,'*' * range3)
print("70-100="  ,'*' * range4)
print(counter)
