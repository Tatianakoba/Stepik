#
# x = int(input())
# y = int(input())
# print(x*60 + y)

# X = int(input())
# print(X//60)
# print(X%60)
#
# X = int(input())
# H = int(input())
# M = int(input())
# print((X + M)//60+H)
# print((X + M)%60)

# A = int(input())
# B = int(input())
# H = int(input())
# if A <= H <= B:
#     print('Это нормально')
# elif H < A:
#     print('Недосып')
# elif H > B:
#     print('Пересып')

# n = int(input())
# if n % 4 == 0 and n % 100 != 0:
#     print('Високосный')
# elif n % 400 == 0:
#     print('Високосный')
# else:
#     print('Обычный')

# a = int(input())
# b = int(input())
# c = int(input())
# p = (a + b + c) / 2
# S = (p*(p - a)*(p - b)*(p - c)) ** 0.5
# print(S)


# a = int(input())
# if -15 < a <= 12 or 14 < a < 17 or 19 <= a:
#     print('True')
# else:
#     print('False')

#
# a = float(input())
# b = float(input())
# oper = str(input())
# if oper == '+':
#     print(a + b)
# elif oper == '-':
#     print(a - b)
# elif oper == '*':
#     print(a * b)
# elif oper == '/':
#     if b != 0:
#         print(a / b)
#     else:
#         print('Деление на 0!')
# elif oper == 'mod':
#     if b != 0:
#         print(a % b)
#     else:
#         print('Деление на 0!')
# elif oper == 'pow':
#     print(a ** b)
# elif oper == 'div':
#     if b != 0:
#         print(a // b)
#     else:
#         print('Деление на 0!')
# else:
#     print('Неподдерживаемая операция')

# figure = str(input())
# if figure == 'треугольник':
#     a = int(input())
#     b = int(input())
#     c = int(input())
#     p = (a + b + c) / 2
#     S = (p*(p - a)*(p - b)*(p - c)) ** 0.5
#     print(S)
# elif figure == 'прямоугольник':
#     a = int(input())
#     b = int(input())
#     S = a*b
#     print(S)
# elif figure ==  'круг':
#     p = 3.14
#     r = int(input())
#     S = p*r**2
#     print(S)

# a = int(input())
# b = int(input())
# c = int(input())
# if a == b == c:
#     print(a, b, c, sep="\n")
# elif a == b < c:
#     print(c, a, b, sep="\n")
# elif a == b > c:
#     print(a, c, b, sep="\n")
# elif a < b == c:
#     print(b, a, c, sep="\n")
# elif a > b == c:
#     print(a, b, c, sep="\n")
# elif a == c < b:
#     print(b, a, c, sep = "\n")
# elif a == c > b:
#     print(a, b, c, sep="\n")
# elif a > b > c:
#     print(a, c, b, sep="\n")
# elif a > b < c and a > c:
#     print(a, b, c, sep="\n")
# elif a > b < c and a < c:
#     print(c, b, a, sep="\n")
# elif a < b < c:
#     print(c, a, b, sep="\n")
# elif a < b > c and a < c:
#     print(b, a, c, sep="\n")
# elif a < b > c and a > c:
#     print(b, c, a, sep="\n")

#
# Если вторая с конца цифра 1, то всегда -ов
#
# Иначе если последняя цифра 0, 5-9, то -ов;
# если 1, то -ст; если 2-4, то -ста
#
# Получить вторую с конца цифру: (n % 100) // 10
#
# Получить последнюю: n % 10

# s = int (input())
# n1 =" программистов"
# n2 =" программист"
# n3 =" программиста"
# if  s>=0:
#   if s==0:
#     print(str(s) + n1)
#   elif s%100>=10 and s%100<=20:
#     print(str(s) + n1)
#   elif s%10==1:
#     print(str(s) + n2)
#   elif s%10>=2 and s%10<=4:
#     print(str(s) + n3)
#   else:
#     print(str(s) + n1)

# s = str(input())
# a = int(s[0])
# b = int(s[1])
# c = int(s[2])
# d = int(s[3])
# e = int(s[4])
# f = int(s[5])
# if a+b+c == d+e+f:
#     print('Счастливый')
# else:
#     print('Обычный')
#
# i = 0
# while i < 5:
#     print('*')
#     if i % 2 == 0:
#         print('**')
#     if i > 2:
#         print('***')
#     i = i + 1
#     print(i)

# x = int(input())
# s = 0
# while x != 0:
#     s += x
#     x = int(input())
# print(s)

# a = int(input())
# b = int(input())
# d = 1
# while d % a != 0 or d % b != 0:
#     d += 1
# else:
#     print(d)

#
# i = 0
# s = 0
# while i < 10:
#     i = i + 1
#     s = s + i
#     if s > 15:
#         break
#     i = i + 1
#     print(i)
#
# i = 0
# s = 0
# while i < 10:
#     i = i + 1
#     s = s + i
#     if s > 15:
#         continue
#     i = i + 1
#     print(i)


# while True:
#     a = int(input())
#     if a < 10:
#         continue
#     elif a > 100:
#         break
#     print(a)
#

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# if c <= d <= 10 and a <= b <= 10:
#     for g in range(c, d + 1):
#         print('\t' + str(g), end='')
#     print(end='\n')
#     for i in range(a, b + 1):
#         print(str(i) + '\t', end='')
#         for j in range(c, d + 1):
#             print(str(i * j), end='\t')
#         print(end='\n')
# else:
#     print('Неверно введены числа')

# a, b = (int(i) for i in input().split())
# s = 0
# if a % 2 == 0:
#     a += 1
# for i in range(a, b + 1, 2):
#     s += i
# print(s)

# a, b = (int(i) for i in input().split())
# s = 0
# j = 0
# for i in range(a, b + 1):
#     if i % 3 == 0:
#         j += 1
#         s = s + i
# m = s / j
# print(m)
#
# genome = input()
# b = len(genome)
# G = genome.upper().count('G')
# C = genome.upper().count('C')
# S = (G + C) / b * 100
# print(S)


# s = str(input())
# l = len(s) - 1
# c = 1
# t = ''
# if len(s) == 1:
#     t = t + s + str(c)
# else:
#     for i in range(0, l):
#         if s[i] == s[i + 1]:
#             c += 1
#         elif s[i] != s[i + 1]:
#             t = t + s[i] + str(c)
#             c = 1
#     for j in range(l, l + 1):
#         if s[-1] == s[-2]:
#             t = t + s[j] + str(c)
#         elif s[-1] != s[-2]:
#             t = t + s[j] + str(c)
#             c = 1
# print(t)
#
# s = input()
# cnt = 0         #счетчик повторений
# shifr = ''     #итоговый результат
# for i in range(len(s)):
#     sim = s[i]
#     cnt += 1
#     if i == len(s) - 1:
#         shifr = shifr + s[i] + str(cnt)
#         break
#     if s[i] != s[i+1]:
#         shifr = shifr + s[i] + str(cnt)
#         cnt = 0
# print (shifr)

# a = [int(i) for i in input().split()]
# s = 0
# for i in a:
#     s += i
# print(s)

# print(sum(map(int, input('>> ').split())))

# a = [int(i) for i in input().split()]
# x = []
# if len(a) == 1:
#     print(a[0])
# else:
#     y = [a[1] + a[-1], x, a[-2] + a[0]]
#     for i in range(len(a)):
#         if i == 0 or i == (len(a) - 1):
#             continue
#         else:
#             x += [a[i - 1] + a[i + 1]]
#     z = ""
#     for j in range(len(x)):
#         z += str(x[j])
#         if j != (len(x) - 1):
#             z += ' '
#     print(y[0], z, y[2])

# a = [int(i) for i in input().split()] '''Ввод списка и разделение на целые числа'''
# y = [] '''Создание нового списка'''
# for i in range(len(a)): '''Для элемента из списка а'''
#     if a.count(a[i]) > 1 and a[i] not in y: '''Если символ в списке попадается более 1 раза и символа нет в списке уже'''
#         y.append(a[i]) '''Добавляем в список'''
#     # print(a[i], a.count(a[i])) '''Печатьт элемента и напротив печать количества повторов этого элемента'''
#     print(*y) '''Печать каждого отдельного элемента из списка в строку0'''

# # сапер
# n, m, k = (int(i) for i in input().split())
# a = [[0 for j in range(m)] for i in range(n)]
# # инициализируем двумерный массив (генерируем n списков, соответсвующих n строкам, в каждой строке генерируем m нулевых значений), заполняем все поле 0
# for i in range(k):  # ставим бомбочки
#     row, col = (int(i) - 1 for i in input().split())
#     a[row][col] = -1
# for i in range(n):  # заполняем клетки вокруг бобюочек числами, соответсвующими колчеству бомбочек
#     for j in range(m):
#         if a[i][j] == 0:  # проверяем нет ли мины в ячейке
#             for di in range(-1, 2):
#                 for dj in range(-1, 2):
#                     ai = i + di
#                     aj = j + dj
#                     #проверяем находится ли клетка внутри поля и она равна -1
#                     if 0 <= ai < n and 0 <= aj < m and a[ai][aj] == -1:
#                         a[i][j] += 1
# #выводим список
# for i in range(n):
#     for j in range(m):
#         if a[i][j] == -1:
#             print('*', end='') #указываем, что не переходим на следующую строчку
#         elif a[i][j] == 0:
#             print('.', end='')
#         else:
#             print(a[i][j], end='')
#     print()

