"""""
#RETURNING VALUES
def square(x):
    return x * x
result = square(4)
print(result)
"""
"""""
#DEFAULT PARAMATER VALUES
def greet(name="Guest"):
    print (f"Hello, {name}!")
greet()
greet("Luka")
"""
""""
def opis(name, age):
    print(f"My name is {name}, and i am {age} years old.")
opis(age=24, name="Kristjan")
"""
"""""
def stevila(*numbers):
    return sum(numbers)
stevila(1, 2, 3, 4)
print(stevila(1, 2, 3, 4))
"""
"""""
def profil(**info):
    for key, value in info.items():
        print(f"{key}: {value}")
profil(name="Kris", age = 10, grade = "1st year collage")
"""
"""""
def stats(x, y):
    return x+y, x*y
sum_, product = stats(2,3)
print(sum_, product)
"""
"""""
def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(5))
"""
"""""
n = int(input("Vnesi eno stevilo vecje od 0: "))

def is_even(n):
    if n % 2 == 0:
        print(f"The number {n} is even")
    else:
        print(f"{n} is a odd number")    
is_even(n)
"""
"""""
def biggest(*numbers):
    return max(numbers)
print(biggest(2, 11, 21, 8, 9))
"""
"""""
def biggest(*numbers):
    biggest = numbers[0]
    for num in numbers:
        if num > biggest:
            biggest = num
    return biggest

print(biggest(2, 5, 12, 18))
"""     
"""""       
def show_profil(**info):
    for key, value in info.items():
        print(f"{key} : {value}")
show_profil(name="Kris", age=22, grade=2)
"""
square = lambda x: x**2
print(square(2))