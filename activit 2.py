#AYASHA MARGAUX L. MUSCARA
#8- SAMPAGUITA

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

def calculate_sum():
   global sum
   sum = num1 +  num2

def calculate_difference():
    global difference
    difference = num1 - num2

calculate_sum()
calculate_difference()

print(f"Sum: {sum}")
print(f"Difference: {difference}")