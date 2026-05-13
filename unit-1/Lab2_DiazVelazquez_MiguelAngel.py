
def multiply(a, b):
    return a * b

print("=== CODE 1 ===")
print(multiply(3, 4)) 
print("\n=== CODE 2 ===")
counter = 0
for i in range(4):          
    counter = counter + 1
print(counter)              
counter2 = 0
for i in range(10):         
    counter2 = counter2 + 1

print("Con range(10):", counter2)  


print("\n=== CODE 3 Corregido")
age = int(input("ingresa tu edad: "))

if age >= 18:              
    print("Adulto")
else:
    print("Menor")          
print("\n=== CODE 4 ===")

a = 3
b = 4

temp = a    # temp = 3
a = b       # a = 4
b = temp    # b = 3

print(a)    # Output: 4
print(b)    # Output: 3