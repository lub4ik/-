userString=str(input("Введите ваш текст: "))
result = len(userString.split())
alphabet = sorted(userString.split(),key=str.lower)
zaglavn = userString.title()
print ("Число слов в предложении: ", result)
print ("Слова по алфавиту: ", alphabet)
print ("Теперь все слова с заглавной буквы, смотрите: ", zaglavn)
