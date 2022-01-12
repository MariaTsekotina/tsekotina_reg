from random import *
from module1 import *
login=["Ari", "Taeli"]
login=["Nivans_9", "Ko0_"]
while True:
    print("1 - Авторизация")
    print("2 - Регистрация")
    print("3 - Выход")
    try:
        a=int(input(":"))
    if a==1:
        LogAnswer=input("У вас есть существующий аккаунт? Да/Нет: ")
        if LogAnswer=="Нет":
            LogCreate=input("Желаете создать аккаунт? Да/Нет: ")
            if LogCreate=="Нет":
                print("Хорошо, до встречи.")
                break
            elif LogCreate=="Да":
                Log=input("Пожалуйста, введите логин. Не более 8 символов: ")
                if len (log) <= 8:
                    login.append(log)
                    print(log)



