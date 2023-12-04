contact=["Nurlan","Hasbik","Emin"]
a=int(input(" 1=Добавить, 2=Удалить, 3=Изменить: "))

if a==1:
    new_contact=input("Напишите новый контакт: ")
    contact.append(new_contact)
    print(f'Ваш контакт - {new_contact} успешно добавлен!')
elif a==2:
    delete_contact=input("Введите контакт, который хотите удалить:  ")
    contact.remove(delete_contact)
    print("Ваш контакт удален")
elif a==3:
    old_name=input("Введите контакт,который хотите изменить: ")
    new_name=input("Введите новый контакт: ")
    if old_name in contact:
        index=contact.index(old_name)
        contact[index]=new_name
        print("Контакт успешно заменен!")
    else:
        print("Контакта не найдено в списке!")