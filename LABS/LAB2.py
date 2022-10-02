alph="abcdefghljklmnopqrstuvwxyzabcdefghljklmnopqrstuvwxyz"   ###В шифре замыкается алфавит

a,b = {},{}                                                   ###Создадим словари с алфавитом и номером символов

for i in range(len(alph)):                                    ###Заполним их так, чтобы в одном ключи были - символы, в другом - их номера
    ch = alph[i]
    a[ch]=i
for i in range(len(alph)):
    b[i]=alph[i]

code = int(input())
stroke = input()
decode=""
for i in stroke:
    decode+=b[a[i]+code]

print(decode)