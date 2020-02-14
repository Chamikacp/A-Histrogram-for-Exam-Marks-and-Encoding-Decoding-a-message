counter = 0
range1 = 0
range2 = 0
range3 = 0
range4 = 0
total_marks = 0
average_of_marks = 0
mark = int(input("Enter marks:"))
highest_mark = mark
lowest_mark = mark
while mark >= 0:
        if mark > highest_mark and mark <= 100:
            highest_mark = mark
        if mark < lowest_mark and mark <= 100:
            lowest_mark = mark
        if mark > 69:
            range4 += 1
        elif mark > 39:
            range3 += 1
        elif mark > 29:
            range2 += 1
        else:
            range1 += 1
        counter += 1
        total_marks = total_marks + mark
        average_of_marks = total_marks / counter
        mark = int(input("Enter a mark:"))
print("0-29  ="  ,'*' * range1)
print("30-39 ="  ,'*' * range2)
print("40-69 ="  ,'*' * range3)
print("70-100="  ,'*' * range4)
print("Number of students are",counter)
print("Average is",average_of_marks)
print("Number of students with a pass mark are",range3 + range4)
print("The highst mark is",highest_mark)
print("The lowest mark is",lowest_mark)

