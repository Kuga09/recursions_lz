divisor=1
sum_divisors=0
def is_perfect_number(n, divisor, sum_divisors): #Начинаем делить число с единицы
    if divisor == n: 
        return sum_divisors == n #Сравниваем сумму делителей с числом
    if n % divisor == 0: #Если divisor делит n без остатка, добавляем его к сумме
        sum_divisors += divisor
    return is_perfect_number(n, divisor + 1, sum_divisors) #Рекурсивно проверяем следующий делитель
print('Введите число, чтобы узнать, является ли оно совершенным')
n=int(input())
if is_perfect_number(n,divisor,sum_divisors) is True:  
    print('Число',n,'является совершенным')
else:
    print('Число',n,'не является совершенным')  