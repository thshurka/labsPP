alph = "abcdefghljklmnopqrstuvwxyzabcdefghljklmnopqrstuvwxyz"  ###В шифре замыкается алфавит

a, b = {}, {}  ###Создадим словари с алфавитом и номером символов

for i in range(len(alph)):  ###Заполним их так, чтобы в одном ключи были - символы, в другом - их номера
    ch = alph[i]
    a[ch] = i
for i in range(len(alph)):
    b[i] = alph[i]


def ce():  # обработчик ошибки ввода сдвига
    while True:
        try:
            code = int(input("Введите сдвиг шифра числом "))
            return code
        except ValueError:
            print("Нужно ввести цифру")


def st():  # обработчик ошибки ввода строки
    while True:
        st = input("Введите строку для дешифрования ")
        if st.isdigit() == 1:
            print("Введите строку")
        else:
            return st


decode = ""
cd = ce()

for i in st(): #дешифрование
    decode += b[a[i] + cd]

print(decode) #вывод
