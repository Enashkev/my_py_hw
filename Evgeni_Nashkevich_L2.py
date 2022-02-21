# Home work 3.1
# -------------
#
num_list = []
user_input = input('Enter four integer numbers, please: ')
num_list = user_input.split()
#
largest = -99999999999999999

for i in range(0, len(num_list)):
    if int(num_list[i]) >= largest:
        largest = int(num_list[i])
        # End If

print('The largest number is :', largest)
##========================================== RESTART: D:\Python\Training\Test_EvN.py ======================================
##Enter four integer numbers, please: 99 101 4 -1
#The largest number is : 101
##=========================================================================================================================
# Home work 3.2
# ----------------------
#
num_list = []
user_input = input('Enter six integer numbers, please: ')
num_list = user_input.split()
largest = -999999999999999999
#
if largest <= max(int(num_list[0]),int(num_list[1]),int(num_list[2]),int(num_list[3]),int(num_list[4]),int(num_list[5])):
    largest = max(int(num_list[0]),int(num_list[1]),int(num_list[2]),int(num_list[3]),int(num_list[4]),int(num_list[5]))
else:
    largest = max(int(num_list[0]),int(num_list[1]),int(num_list[2]),int(num_list[3]),int(num_list[4]),int(num_list[5]))
# EndIf
#
print(largest)
##======================================== RESTART: D:\Python\Training\Test_EvN.py ========================================
##Enter six integer numbers, please: 4 -22 56 1 9 69
##69
##=========================================================================================================================
# Home work 3.3
# -------------
#
while True:
    plant = input('Enter word "Spathiphyllum" in upper case : ')
#
    if plant.isupper():
        print('Great, well done. You entered the word in the UPPERCASE : ', plant)
        break
    else:
        print('Youa are wrong. You entered the word in the lowercase. Please redo : ', plant)        
    # EndIf
##========================================== RESTART: D:\Python\Training\Test_EvN.py ===============================
##Enter word "Spathiphyllum" in upper case : Spathiphyllum
##Youa are wrong. You entered the word in the lowercase. Please redo :  Spathiphyllum
##Enter word "Spathiphyllum" in upper case : SPATHIPHYLLUM
##Great, well done. You entered the word in the UPPERCASE :  SPATHIPHYLLUM
##=========================================================================================================================
# Home work 3.4
# -------------
#
for i in range(0, 4):
    income = float(input('What is your income ? '))
    print('Your income is ', income, 'You must pay tax : ', round(income/100*15, 2))
#
##========================================== RESTART: D:\Python\Training\Test_EvN.py =======================================
##What is your income ? 55000
##Your income is  55000.0 You must pay tax :  8250.0
##What is your income ? 12349576
##Your income is  12349576.0 You must pay tax :  1852436.4
##What is your income ? 1
##Your income is  1.0 You must pay tax :  0.15
##What is your income ? 56
##Your income is  56.0 You must pay tax :  8.4
##=========================================================================================================================
# Home work 3.5
# -------------
#
while True:
    stop = input('Enter a year number or "EXIT" to stop : ')
#
    if stop.upper() == 'EXIT':
        print('Completed ...')
        break
    else:
        year = int(stop)
    # EndIf

    if year < 1582:
        print ('Year ', year, ' is out of Gregorian calendar !')
    elif year % 4 != 0:
        print ('Year ', year, ' is a common year.')
    elif year % 100 != 0:
        print ('Year ', year, ' is a leap year.')
    elif year % 100 != 0:
        print ('Year ', year, ' is a common year.')
    else:
        print ('Year ', year, ' is a leap year.')
#
# WhileEnd
##==================================== RESTART: D:\Python\Training\Test_EvN.py ====================================
##Enter a year number or "EXIT" to stop : 1240
##Year  1240  is out of Gregorian calendar !
##Enter a year number or "EXIT" to stop : 1600
##Year  1600  is a leap year.
##Enter a year number or "EXIT" to stop : 2014
##Year  2014  is a common year.
##Enter a year number or "EXIT" to stop : exit
##Completed ...
##=========================================================================================================================
# Home work 3.6
# -------------
#
mNum = int(13)
#
while True:
    youNum = int(input('Hey you, guess my integer number : '))
    #
    if mNum == youNum:
        print('Great! You have gussed my mumber. It is ', mNum, '. You are free.')
        break
    elif mNum > youNum:
        print("Ha ha! You're stuck in my loop! My number is greater then yours.")
    else:
        print("Ha ha! You're stuck in my loop! My number is less then yours.")
#
##==================================== RESTART: D:\Python\Training\Test_EvN.py ====================================
##Hey you, guess my integer number : -5
##Ha ha! You're stuck in my loop! My number is greater then yours.
##Hey you, guess my integer number : 100
##Ha ha! You're stuck in my loop! My number is less then yours.
##Hey you, guess my integer number : 13
##Great! You have gussed my mumber. It is  13 . You are free.
##=========================================================================================================================
# Home work 3.7
# -------------
#
import time
#
for i in range(0, 5):
    print('Iteration # is ', i+1, '. Mississippi')
    time.sleep(1)
# ForEnd
print('Ready or not, here I come!')
#
##==================================== RESTART: D:\Python\Training\Test_EvN.py ====================================
##Iteration # is  1 . Mississippi
##Iteration # is  2 . Mississippi
##Iteration # is  3 . Mississippi
##Iteration # is  4 . Mississippi
##Iteration # is  5 . Mississippi
##Ready or not, here I come!
##=========================================================================================================================
# Home work 3.9
# -------------
#
word = input('Enter any word, please : ')
vowels = 'AEIOU '
#
for i in range(0, len(word)):
    if word[i].upper() in vowels:
        continue
    else:
        print(word[i].upper())
##==================================== RESTART: D:\Python\Training\Test_EvN.py ====================================
##Enter any word, please : Evgeni Nashkevich
##V
##G
##N
##N
##S
##H
##K
##V
##C
##H
##>>> 
##=========================================================================================================================
# Home work 3.10
# --------------
#
word = input('Enter any word, please : ')
vowels = 'AEIOU '
out_string = ''
#
for i in range(0, len(word)):
    if word[i].upper() in vowels:
        continue
    else:
        out_string = out_string + word[i].upper()
# IfEnd
# ForEnd
print(out_string)
##==================================== RESTART: D:\Python\Training\Test_EvN.py ====================================
##Enter any word, please : Evgeni Nashkevich
##VGNNSHKVCH
##>>>
##=========================================================================================================================
# Home work 3.11
# --------------
#
c0 = int(input('Enter positive integer number: '))
i = 0
while True:
    i = i + 1
    if c0 % 2 == 0:
        c0 = int(c0/2)
    else:
        c0 = 3 * c0 + 1
    # IfEnd
    print(c0)
    if c0 == 1:
        print('Steps =', i)
        break
# WhileEnd
##==================================== RESTART: D:\Python\Training\Test_EvN.py ====================================
##Enter positive integer number: 15
##46
##23
##70
##35
##106
##53
##160
##80
##40
##20
##10
##5
##16
##8
##4
##2
##1
##Steps = 17
##>>> 
##=========================================================================================================================
# Home work 3.12
# --------------
#
# Операции над двумя числами
def sum(a, b):
    return a + b
def sub(a, b):
    return a - b
def mult(a, b):
    return a * b
def div(a, b):
    return a / b

def main():
    while True:
        try:
            #Вводим числа
            a = float(input("Введите первое число: "))
            b = float(input("Введите второе число: "))
            c = int(input("Номер операции:\n1) +\n2) -\n3) *\n4) /\n"))
        except:
            print("Нужно ввести число, попробуйте ещё раз ...\n")
            continue # Повторяем ввод, если введено не число
        break # Выходим из цикла, если числа введены правильно
    # Применяем нужную операцию в зависимости от ввода
    cond = {1 : sum(a, b),
            2 : sub(a, b),
            3 : mult(a, b),
            4 : div(a, b)}
    # Выводим результат операции
    print(cond[c])

main()
##======================================= RESTART: D:\Python\Training\Test_EvN.py =======================================
##Введите первое число: 12365964
##Введите второе число: 1235
##Номер операции:
##1) +
##2) -
##3) *
##4) /
##4
##10012.926315789473
##>>> 
