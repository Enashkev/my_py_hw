# ==============================================================================================================
# Home work 4.1
# -------------
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
##============================================ RESTART: D:\Python\Training\Test_EvN.py ============================================
##Введите первое число: 4
##Введите второе число: 7
##Номер операции:
##1) +
##2) -
##3) *
##4) /
##4
##0.5714285714285714
##>>>
# ==============================================================================================================
# Home work 4.2
# -------------
#
def Leap_Year(Lyear):
    if Lyear < 1582:
        return False
    elif Lyear % 4 != 0:        
        return False    
    elif (Lyear % 100 == 0) and (Lyear % 400 != 0):        
        return False
    else:
        return True
## End of Leap_Year
    
while True:
    stop = input('Enter a year number or "EXIT" to stop : ')
#
    if stop.upper() == 'EXIT':
        print('Completed ...')
        break
    else:
        print('You entered: ', stop, ' Is it a leap year? : ', Leap_Year(int(stop)))
    # EndIf
#
# WhileEnd
##============================================ RESTART: D:\Python\Training\Test_EvN.py ============================================
##Enter a year number or "EXIT" to stop : 1200
##You entered:  1200  Is it a leap year? :  False
##Enter a year number or "EXIT" to stop : 1981
##You entered:  1981  Is it a leap year? :  False
##Enter a year number or "EXIT" to stop : 2000
##You entered:  2000  Is it a leap year? :  True
##Enter a year number or "EXIT" to stop : 1960
##You entered:  1960  Is it a leap year? :  True
##Enter a year number or "EXIT" to stop : 2015
##You entered:  2015  Is it a leap year? :  False
##Enter a year number or "EXIT" to stop : exit
##Completed ...
##>>>
# ==============================================================================================================
# Home work 4.3
# -------------
#
def Leap_Year(Lyear):
    if Lyear < 1582:
        return False
    elif Lyear % 4 != 0:        
        return False    
    elif (Lyear % 100 == 0) and (Lyear % 400 != 0):        
        return False
    else:
        return True
## End of Leap_Year

##В Январе, Марте, Мае, Июле, Августе, Октябре и Декабре - 31 день

def DaysInMonth(year, month):
    MonthCheck = (1,3,5,7,8,10,12)
    mo_yr = [0, 0]

    if (month == 2) and Leap_Year(year):
        mo_yr[0] = year; mo_yr[1] = 29
        return mo_yr
    elif (month == 2) and not(Leap_Year(year)):
        mo_yr[0] = year; mo_yr[1] = 28
        return mo_yr
    else:
        pass    
## IfEnd 1
    if month in MonthCheck:
        mo_yr[0] = year; mo_yr[1] = 31
        return mo_yr
    else:
        mo_yr[0] = year; mo_yr[1] = 30
        return mo_yr
## IfEnd 2
## End of DaysInMonth()

test_year = [1900, 2000, 2016, 1987]
test_month = [2, 2, 1, 11]
test_result = [28, 29, 31, 30]

for i in range(len(test_year)):
    yr = test_year[i]
    mo = test_month[i]
    print(yr, mo, '->', end = '')
    result = DaysInMonth(yr, mo)
     
    if test_result[i] == result[1]:
        print('Ok')
        print(result)
    else:
        print('Failed')
        print(result)
##============================================ RESTART: D:\Python\Training\Test_EvN.py ============================================
##1900 2 ->Ok
##[1900, 28]
##2000 2 ->Ok
##[2000, 29]
##2016 1 ->Ok
##[2016, 31]
##1987 11 ->Ok
##[1987, 30]
##>>> 
# ==============================================================================================================
# Home work 4.4
# -------------
#
def Leap_Year(Lyear):
    if Lyear < 1582:
        return False
    elif Lyear % 4 != 0:        
        return False    
    elif (Lyear % 100 == 0) and (Lyear % 400 != 0):        
        return False
    else:
        return True
## End of Leap_Year

##В Январе, Марте, Мае, Июле, Августе, Октябре и Декабре - 31 день

def DaysInMonth(year, month):
    MonthCheck = (1,3,5,7,8,10,12)
    mo_yr = [0]

    if (month == 2) and Leap_Year(year):
        mo_yr[0] = 29
        return mo_yr
    elif (month == 2) and not(Leap_Year(year)):
        mo_yr[0] = 28
        return mo_yr
    else:
        pass    
## IfEnd 1
    if month in MonthCheck:
        mo_yr[0] = 31
        return mo_yr
    else:
        mo_yr[0] = 30
        return mo_yr
## ********************
## Check Input Function
## ********************

def CheckInp(YrMoDa):
#
# YrMoDa is a list containing YYYY mM dD members:
# CheckInp returns True if the Input is correct otherwise None
#
    if (type(YrMoDa[0]) != type(1)) or (YrMoDa[0] < 1600):
        return

    if not(YrMoDa[1] >= 1 and YrMoDa[1] <= 12):
        return

    if not(YrMoDa[2] > 0 and YrMoDa[2] <= DaysInMonth(YrMoDa[0], YrMoDa[1])[0]):
        return

    return True
## End of CheckInp Function
##

print('Please enter Years > 1600, Months & Days. Apply only integer numbers.')
print()

while True:
    InpList = []
    prompt = ['Year: ', 'Month :', 'Day: ']
    
    for i in range(len(prompt)):
        InpList.append(int(input(prompt[i])))

    if CheckInp(InpList) is None:
        print('Sorry, you entered incorrect combination, please reEnter.')
    else:
        break
## EndWhile
#
sum_days = 0

for i in range(1, InpList[1]):    
    sum_days = sum_days + DaysInMonth(InpList[0], i)[0]

sum_days = sum_days + InpList[2]

print('sum_days = ', sum_days)

##Please enter Yesr > 1600, Month & Day. Apply only integer numbers.
##
##Year: 1960
##Month :4
##Day: 10
##sum_days =  101
##>>> 
##============================================ RESTART: D:\Python\Training\Test_EvN.py ============================================
##Please enter Years > 1600, Months & Days. Apply only integer numbers.
##
##Year: 2000
##Month :12
##Day: 31
##sum_days =  366
##>>> 
##============================================ RESTART: D:\Python\Training\Test_EvN.py ============================================
##Please enter Years > 1600, Months & Days. Apply only integer numbers.
##
##Year: 2007
##Month :11
##Day: 12
##sum_days =  316
##>>> 
##============================================ RESTART: D:\Python\Training\Test_EvN.py ============================================
##Please enter Years > 1600, Months & Days. Apply only integer numbers.
##
##Year: 2013
##Month :5
##Day: 6
##sum_days =  126
##>>> 
##============================================ RESTART: D:\Python\Training\Test_EvN.py ============================================
##Please enter Years > 1600, Months & Days. Apply only integer numbers.
##
##Year: 2009
##Month :0
##Day: 0
##Sorry, you entered incorrect combination, please reEnter.
##Year: 2020
##Month :08
##Day: 09
##sum_days =  222
##>>> 
# ==============================================================================================================
