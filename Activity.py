print("======================Analyzer======================\n")

number=input("Enter a number:                               ") #8
reversed=""

for char in number:
    reversed=char+reversed

if reversed==number:
    print("The number you have entered is a palindrome!")

else:
    print("The number you have entered is not a palindrome..")

print("\n=====================================================\n")


num1=int(input("Enter the 1rst number:                               "))
num2=int(input("Enter the 2nd number:                                "))

num1_factors=[]
num2_factors=[]

for i in range(1, num1+1):
    if num1%i==0:
        num1_factors.append(i)

for i in range(1, num2+1):
    if num2%i==0:
        num2_factors.append(i)

new_num1=set(num1_factors)
new_num2=set(num2_factors)

common_factors=new_num1.intersection(num2_factors)

hcf=0
for i in common_factors:
    if i>hcf:
        hcf=i

print("\n=====================================================\n")

print(f'The HCF of {num1} and {num2} is {hcf}')

lcm=(num1*num2)/hcf
print(f"The LCM of {num1} and {num2} is {int(lcm)}")

print("\n=====================================================\n")