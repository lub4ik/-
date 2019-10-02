def gcd(num1,num2):
    while (num2):
	    num1, num2 = num2, num1%num2
    return num1

def lcm(num1,num2):
    lcm = (num1*num2)//gcd(num1,num2)
    return lcm
while True:
    try:
        num1=int(input("Введите первое целое число: "))
        
    except ValueError:
        print("Введенное вами число не является целым. Попробуйте снова!")
        continue
    else:
        break
while True:
    try:
        num2=int(input("Введите второе целое число: "))
        
    except ValueError:
        print("Введенное вами число не является целым. Попробуйте снова!")
        continue
    else:
        break
print("НОД чисел", num1, "и", num2," равен:", gcd(num1,num2))
print("НОК чисел", num1, "и", num2," равно:", lcm(num1,num2))

