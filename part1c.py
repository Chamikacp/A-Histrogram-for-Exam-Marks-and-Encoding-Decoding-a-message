print("###Histrogram for Exam Marks###")
print("Please enter a mark")
print("If you want to EXIT enter a negative number")

counter = 0
range1 = 0
range2 = 0
range3 = 0
range4 = 0
total_marks = 0
average_of_marks = 0
highest_mark = 0
lowest_mark = 0
 
while True:
          try:
                 mark = int(input("Enter a mark:"))
                 
                 #If we want to end the programme in the begining
                 if mark < 0:
                   break
               
                 highest_mark = 0
                 lowest_mark = mark

                 while mark >= 0:

                         #To find out the highest mark 
                         if mark > highest_mark and mark <= 100:
                                 highest_mark = mark
                                 
                         #To find out the lowest mark
                         if mark < lowest_mark and mark <= 100:
                                 lowest_mark = mark
                                 
                         #If the mark we entered is over 100        
                         if mark > 100:
                                 print("This mark is not valid,Try again.")
                                 
                         #To find out the range that mark in       
                         if mark > 69 and mark <= 100:
                                 range4 += 1
                                 
                         elif mark > 39 and mark <= 69:
                                 range3 += 1
                                 
                         elif mark > 29 and mark <= 39:
                                 range2 += 1
                                 
                         elif mark >= 0 and mark <= 29:
                                 range1 += 1
                                 
                         #If the mark we entered between 0-100 to calculate following statistics         
                         if mark >= 0 and mark <= 100:        
                                 counter += 1
                                 total_marks = total_marks + mark
                                 average_of_marks = (total_marks / counter)
                                 
                         mark = int(input("Enter a mark:"))
                         
                 break
                
          #When we entered a non-numeric character   
          except ValueError:
                 print("This mark is not valid,Try again")
             
                 continue
                
#To make use of loops             
print("\n0-29   ",end="")
for x in range(0,range1):
    print('*',end="")
print("\n30-39  ",end="")
for y in range(0,range1):
    print('*',end="")
print("\n40-69  ",end="")
for z in range(0,range1):
    print('*',end="")
print("\n70-100 ",end="")
for i in range(0,range1):
    print('*',end="")
print("\n")   

print("Number of students are",counter)
print("Average is",average_of_marks)
print("Number of students with a pass mark are",range3 + range4)
print("The highst mark is",highest_mark)
print("The lowest mark is",lowest_mark)
