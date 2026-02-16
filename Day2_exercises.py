#grade calculation
mark=int(input("Enter the marks:"))
if mark>=90:
  print("Grade:A")
elif mark>=75 and mark<=89:
  print("Grade:B")
elif mark>=50 and mark<=74:
  print("Grade:C")
else:
  print("Fail")

#Leap year check
year=int(input("Enter the year:"))
if year%400==0 or (year%100!=0 and year%4==0):
  print("%d is a leap year"%year)
else:
  print("%d is not a leap year"%year)

#Calculator using if-elif
a=int(input("Enter number 1:"))
b=int(input("Enter number 2:"))
op=input("Enter the operator(+,-,/,*):")
if op=="+":
  print("Addition:",a+b)
elif op=="-":
  print("Subtraction:",a-b)
elif op=="*":
  print("Multiplication:",a*b)
elif op=="/":
   if b==0:
      print("Error!Division by zero!")
   else:
     print("Division:",a/b)
else:
 print("Invalid operator!")

#To check positive/negative/zero
n=int(input("Enter a number:"))
if n>0:
  print("%d is a positive number."%n)
elif n<0:
  print("%d is a negative number."%n)
else:
  print("The given number is zero.")									
#Loops
#sum of digits and count digits in a number
n=int(input("Enter a number:"))
temp=n
sum=0
digit_number=0
while temp>0:
   digit=temp%10
   digit_number+=1
   sum+=digit
   temp=temp//10
print("Sum of the digits:",sum)
print("Number of digits:",digit_number)

#To check the given number is prime or not
n=int(input("Enter a number:"))
prime=1
if n<=1:
  print("Not prime")

else:	
   for i in range(2,n//2 +1):
      if n%i==0:
          prime=0
          break
   if prime:
      print("Prime")
   else:
      print("Not prime")    								
#Fibonacci series
n=int(input("Enter the number of terms you need in fibonacci series:"))    		
if n==1:
   print("Fibonacci series:0")
elif n==2:
   print("Fibonacci series:0,1")
elif n>=3:
   pre=0
   suc=1
   print("Fibonacci series:")
   print(pre)
   print(suc)	
   for i in range (3,n+1):
       next=pre+suc
       pre=suc
       suc=next
       print(next)        	
else:
   print("Enter a positive number.")							
#armstrong
n=int(input("Enter a number to check armstrong number or not:"))
temp=n
digit_number=0
sum=0
while temp>0:
   digit=temp%10
   digit_number+=1
   temp=temp//10
temp=n
while temp>0:
   digit=temp%10
   sum+=digit**digit_number
   temp=temp//10
if sum==n:
   print("Armstrong number.")
else:
   print("Not a armstrong number.")
#patterns
n=int(input("Enter the number of rows of stars to be generated:"))
for i in range(1, n+1):
    for j in range(1, i+1):
        print("*", end="")
    print()
    
n=int(input("Enter the number of rows of stars to be generated:"))
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end="")
    print()    
#reverse  a number
temp=int(input("Enter a number to be reversed:"))  
rev=0
n=temp
while n>0:
	digit=n%10
	rev=rev*10+digit  
	n=n//10
print("Reversed number is:",rev)	
if rev==temp:
	print("The given number is palindrome")
else:
	print("Not a palindrome.")	