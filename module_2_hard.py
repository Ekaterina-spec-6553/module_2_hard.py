number = int(input("Введите число из первой вставки: "))

def password_selection():
    couple = ''
    for i in range(1, number):
        for j in range(i+1, number):
            if number % (i + j) == 0:
                couple += str(i)+ str(j)
    return couple

couple = password_selection()
print("Пароль:", couple)
