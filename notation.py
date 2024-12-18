def convert_to_base(num, base):
    digits = "0123456789ABCDEF" #Запишем все возможные символы систем счисления
    if num < base:
        return digits[num] #Если число меньше базы, то оно напрямую соответствует одному из символов в строке digits
    return convert_to_base(num // base, base) + digits[num % base] #Алгоритм перевода числа в произвольную систему счисления
print('Введите число для перевода и систему счисления')
inpt=input()
inpt=inpt.split()
number=int(inpt[0])
base=int(inpt[1])
result = convert_to_base(number, base)
print('Число',number,'в системе счисления с основанием',base, '=',result)
