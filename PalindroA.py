a=input("Введите слово: ")

if a.lower()==a[::-1].lower():
    print("Палиндрома")
else:
    print("Не палиндрома")