Part 1 - Histogram for Exam Marks 

The University requires a graphical display to show how many students received different grade categories for a module assessment. You are required to write a program in Python that achieves this.   
 
•	Flow Diagram - Note that before you start to program your solution you should create your flow diagram that represents your algorithm in a structured manner. 
•	A set of test cases will be provided for you to test your program solution. 
 
Part A: Basic Program 
•	The program should allow the tutor to enter in the various marks awarded, until the tutor enters in a negative mark (e.g., -1).   
•	When a negative mark is entered, the program should display a histogram where each star represents a student who achieved a module mark in the category range:  0-29, 30-39, 40-69 and 70-100.  
This example shows the output distribution for 20 marks.  Your program should work with any number of marks entered. 
 
0-29 	***       
30-39   	***** 
40-69   	******** 
70-100  	****      20 students in total. 
 
•	A counter should count the number of student’s marks which have been entered. 
•	The display should be neatly formatted.   
•	Make use of ‘loops’ for the display of the stars for each category. 
Part B: Statistics    
Extend your program so that the following statistics display after the histogram. 
a)	Average mark. 
b)	Number of students with a pass mark (mark of 40 or above).  
c)	Highest mark 
d)	Lowest mark. 
 
Part C: Input Validation  
Valid marks are integers 0 to 100.  
•	Your program should display an appropriate message if a non-numeric character is entered.   
•	Your program should display an appropriate message if a number over 100 is entered. 
 
(Optional) Part D: Vertical histogram (Extension) 
Should only be attempted if you are confident with your programming skills.  No tutor help will be provided. The part 1 histogram shows each category horizontally across the screen.  Extend your program to add an additional histogram that displays vertically so the stars in a category should go downwards and not across the screen, e.g.:   
 
0-29   30-39   40-69   70-100 
*	*          *          *            (as a line is printed decide if each category needs a star or space)  
*	* 

Part 2 - Encoding / Decoding Strings 

This assignment will involve the use of strings and functions. 
Create a Python program that will apply a simple encoding and decoding of a message.   
 
The program should prompt the user to enter a message and then enter a key (the shift value).  The key should be in the range 1 to 25.  The program will then produce an encoded string by applying the key (shift value) to the alphabetic characters in the message.  The shift amount instructs the program on how many places in one direction to move to find the encoding of any letter of the alphabet. 
Examples: A key of 3 will shift each character 3 characters to the right. 
•	the character 'a' as the character 'd',  
•	the character 'b' as 'e', etc.,  
•	the string ‘this’ becomes the string ‘wklv’ using a rotation of 3. 
Wrap the encoding around the alphabetic characters, so that 'w' is encoded as 'z', 'x' is encoded as 'a', 'y' is encoded as 'b', and 'z' is encoded as 'c' etc. 
 
Important note:  
•	There are various solutions to this type of challenge on the internet.  These solutions convert a letter to ASCII code using ord() and convert an ASCII code to a letter using chr(). Instead your solution should be built around rotating a character in string. E.g.,  
 
ALPHABET = 'abcdefghijklmnopqrstuvwxyz' 
 
•	Any code solutions submitted using the ord() and chr() approach will receive a mark of zero. 
 
Part A: Encoding 
The program prompts for a string to encode and a rotation integer in the range of 1-25. The program then returns the encoded string.  Important, the program should not encode any letter that is not in the lower case alphabet. Those letters should simply be passed through to the encoded string.  E.g., 
•	the string ‘*this!’ becomes the string ‘*wklv!’ using a rotation of 3. 
 
(Optional) Part B: Decoding 
•	The program should prompt the user for one of three commands: 
•	‘e’ to encode a string 
•	‘d’ to decode a string 
•	‘q’ to quit 
 
•	If the command is encode, then the program runs as for Part A: Encoding. 
•	If the command is decode, then the program should prompt for a string to decode and key and the program displays the encrypted/decrypted message. 
•	Any other command should raise an error and reprompt. 
 
(Optional) Part C: Decoding (Extension) 
Should only be attempted if you are confident with your programming skills.  No tutor help will be provided. If the command is decode, then the program should prompt for a string to decode and a plain-text word that appears in the text (decoded string). The output should be the rotation needed to decode the string and the decoded string.  Example: 
If the encoded string is:  khoor zruog and the plain-text word is:  hello 
 	The program should work out the rotation was 3 and the decoded string is 'hello world' 
