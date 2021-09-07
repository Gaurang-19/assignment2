number = int(input("Enter a number: "))
if number > 1:
   for i in range(2,number):
       if (number % i) == 0:
           print("Not Prime")
           break
   else:
        print("Prime")
else:
   print("Not Prime")