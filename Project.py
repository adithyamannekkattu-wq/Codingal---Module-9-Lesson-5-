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

lcm=(num1*num2)/hcf
print(f"The LCM of {num1} and {num2} is {int(lcm)}")

