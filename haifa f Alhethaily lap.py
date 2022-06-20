#Haifa Alhethaily 742
'''program iterates the integers from 1 to 30'''

def numbers(num1,num2):
    for i in range(num1,num2):
        if i % 3==0 and i %5==0:
            print("FizzBuzz")
        elif i % 5==0:
            print("Buzz")
        elif i % 3==0 :
            print("Fizz")
        else:
            print(i)
numbers(1,31)
