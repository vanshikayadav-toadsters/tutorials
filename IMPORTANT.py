# #Print odd numbers between 1,50
# for i in range(1,51):
#      if i % 2 != 0 :
#          print(i)
    

# #MUltiplication table
# n=int(input("Enter number: "))
# for i in range(1,11):
#     print(n ,"X ", i ,"=", n*i)

# #count of digits
# n=int(input("Enter number : "))
# count=0
# while n>=0:
#     count +=1
# print(count)


# n=int(input("Enter the number upto which you want to print: "))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*", end="")
        
#     print()
    
# #Pyramid straight   
# n=int(input("Enter the number upto which you want the pattern: "))
# for i in range(n):
#     print(f"{i+1}"*(i+1))
    
    
    
# n = int(input("Enter the number: "))
# for i in range(n):
#     m=(n-1)*2+1
#     print(" "*i + "*" *(m-i*2)+" "*i)
    
# for i in range(1,n+1):
#     print(""*i)
# for i in range(n):
#     m=''
#     number_of_star = ((n-1)*2+1)-i*2
#     for j in range((n-1)*2+1):
#         if j==i:
#             m+="*"*number_of_star
#             break
#         else:
#             m+=" "
#     print(m)


# #numbers from 1 to 100
# for i in range(1,101):
#     print(i)

# #numbers from 100 to 1
# i=101
# while i<=101:
#     i -= 1 
#     while i == 1:
#         break
#     print(i)
   
# #even numbers b/w 1,50
# for i in range(1,51):
#     if i%2==0:
#         print (i)


# #odd numbers b/w 1 to 50
# for i in range(1,51):
#     if i % 2 != 0:
#         print(i)
            
            
# #numbers divisible from 1 to 100
# for i in range(1,101):
#     if i % 5 == 0:
#         print(i)

 
#  #squares of numbers
# for i in range(1,101):
#     print(i * i )
    

# #cube of numbers
# for i in range(1,101):
#     print(i*i*i)


# #each character of string using for
# string="Hello"
# for ch in string:
#     print(ch)


# #count characters of a string
# string="Hello"
# count=0
# for ch in string:
#     count+=1
# print(count)

# print no 1 to 20 except multiples of 3
# for i in range(1,21):
#     if i%3!=0:
#         print(i)
    
# #Sum of numbers from 1 to n 
# n=int(input("Enter number upto which you want the count: "))
# sum=0
# for i in range(1,n+1):
#     sum += i
# print(sum)


# #Sum of even numbers from 1 to n 
# n=int(input("Enter numbers upto which you want total: "))
# sum=0

# for i in range(2,n+2,2):
#     sum+=i
# print(sum)


# #sum of odd numbers from 1 to n 
# n=int(input("Enter numbers upto which you want total: "))
# sum=0
# for i in range(1,n+1):
#     if i%2 !=0:
#         sum +=i
# print(sum)


# #product of numbers from 1 to n 
# n=int(input("ENter the numbers: "))
# product=1
# for i in range(1,n+1):
#     product *=i
# print(product)

# print multiplication table 
# n=int(input("Enter the number: "))
# ifor i in range(1,11):
#     print(n ,"x", i ,"=", n*i)


# #COUNT THE NUMBER OF VOWELS And consonants
# string = "Alphabets"
# temp=str.upper(string)
# count=0
# for ch in temp:
#     if ch not in ["A","E","I","O","U"]:   #consonants
#         count += 1
#     if ch in ["A","E","I","O","U"]:      #vowels
#          count += 1
    
# print(count)

# #LArgest number from a lst
# l1=[2,4,5,6,7,56,67,54,67,78]
# largest=l1[0]
# for i in l1:
#     if i > l1[0]:
#         largest=i
# print(largest)

# #Smallest number in a list
# l1=[34,56,78,23,45,90]
# smallest=l1[0]
# for i in l1:
#     if i < l1[0]:
#         smallest=i
# print(smallest)


# #Average of the numbers of the list
# l1=[2,3,4,5,6,7,8]
# sum=0
# count=0
# for i in l1:
#     sum +=i
#     count += 1
# Average=sum/count
# print(Average)

# #Factorial of a number
# n=int(input("Enter the number: "))
# fact=1
# for i in range(1,n+1):
#     fact*=i
# print(fact)


# #Check prime
# n=int(input("Enter the number: "))

# def check_prime(n):
#     if n > 1:
#         for i in range(2,n):
#             if n % i == 0:
#                 return "non Prime"
#     return "prime"
    
# print(check_prime(n))
    
        


# #print all prime numbers between 1 to 100
# for i in range(2,101):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#          print(i)

# #Reverse a string using a for loop
# s=input("Enter string:")
# rev=""
# for ch in s :
#     rev= ch +rev
# print(rev)


# #Reverse a number using loop
# n=int(input("Enter the number: "))
# rev=0
# while n:
#     rev=rev*10 + n %10
#     n //=10
# print(rev)

# check palindrome 
# n=int(input("Enter the number: "))
# temp=n
# rev=0
# while n:
#     rev=rev*10 + n %10
#     n //=10

# if temp==rev:
#     print("Palindrome")
# else:
#     print("Not a palindrome")


# #check character in string
# s=input("Enter string: ")
# ch=input("Enter character: ")
# count=0
# for i in s :
#     if i == ch :
#         count +=1
        
# print(count)



    



    

    




        
    
    
