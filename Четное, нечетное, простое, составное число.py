while True:
    try:
        num=int(input("Введите любое целое число: "))
    except ValueError:
        print("Введенное число не является целым. Попробуйте снова!")
        continue
    else:
        break
if num != 0 or 1:
    for i in range(2,num):
        if (num%i)==0:
            print(num, "это составное число") 
            break
    else:
        print(num, "это простое число")
    
elif num == 0 or 1:
        print(num, "это ни простое, ни составное число")
        
if (num%2)==0:
            print (num, "это четное число")
if (num%2)!=0:
        print(num, "это нечетное число")
