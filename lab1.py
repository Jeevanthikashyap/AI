#program to check the age criteria of a person through else if ladder

age = int(input("Please enter your age:"))
if age <= 0:
	print('Invalid input')
elif age >= 1 and age <= 5:
	print('Infant')
elif age >= 6 and age <= 11:
	print('Child')
elif age >= 12 and age <=17:
	print('Teen')
elif age >= 18 and age <=59:
	print('Adult')
else:
	print('Senior Citizen')

#program to print the multiplication table for any given number

number = int(input ("Enter the number of which the user wants to print the multiplication table: "))      
print ("The Multiplication Table of: ", number)    
for count in range(1, 11):      
   print (number, 'x', count, '=', number * count)

#program to print the patern: 1223334444...

n = int(input("Enter the number for the pattern: "))
for i in range(1,n+1):
    for j in range(1, i+1):
        print(i, end='')

#program to print the pattern 1121231234....

m = int(input("Enter the number for the pattern: "))    
for i in range(1, m+1):    
    for j in range(1, i + 1):    
        print(j, end='')  
       
#program to reverse any given number

number = int(input("Enter the integer number: "))  
revs_number = 0  
  
while (number > 0):   
    remainder = number % 10  
    revs_number = (revs_number * 10) + remainder  
    number = number // 10   
print("The reverse number is :", (revs_number))


#program to demonstrate bubble sort

nums = []
print("Enter the Size of List: ")
total = int(input())

print("Enter " + str(total) + " Numbers: ")
for i in range(total):
    nums.insert(i, int(input()))

for i in range(total-1):
    for j in range(total-i-1):
        if nums[j]>nums[j+1]:
            temp = nums[j]
            nums[j] = nums[j+1]
            nums[j+1] = temp

print("The Sorted List is:")
for i in range(total):
    print(nums[i])