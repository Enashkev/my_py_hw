# Home work 3.1
# -------------
#
num_list = [1, 2, 3, 4, 5]
print('See the list named as num_list: ', num_list)

replace = int(input('Please enter an integer number to rplace the midle element of the list printed above: '))
num_list[len(num_list)//2] = replace

print(num_list)
del num_list[len(num_list) - 1]
print(num_list)

print('This is length: ', len(num_list), ' of the num_list list: ', num_list)
#
##See the list named as num_list:  [1, 2, 3, 4, 5]
##Please enter an integer number to rplace the midle element of the list printed above: 100
##[1, 2, 100, 4, 5]
##[1, 2, 100, 4]
##This is length:  4  of the num_list list:  [1, 2, 100, 4]
##>>> 
##=========================================================================================================================
# Home work 3.2
# -------------
#
# Step 1:
beatles = []
# Step 2:
beatles.append('John Lennon')
beatles.append('Paul Maccartney')
beatles.append('George Harrison')
# Step 3:
for i in range(0, 1):
    beatles.append(input('Add Stu Sutcliffe : '))
    beatles.append(input('Add  Pete Best : '))
# ForEnd
print(beatles)

# Step 4:
del beatles[beatles.index('Stu Sutcliffe')]
del beatles[beatles.index('Pete Best')]
print(beatles)

# Step 5:
beatles.insert(0, 'Ringo Starr')
print(beatles)
##=========================================== RESTART: D:\Python\Training\Test_EvN.py ==========================================
##Add Stu Sutcliffe : Stu Sutcliffe
##Add  Pete Best : Pete Best
##['John Lennon', 'Paul Maccartney', 'George Harrison', 'Stu Sutcliffe', 'Pete Best']
##['John Lennon', 'Paul Maccartney', 'George Harrison']
##['Ringo Starr', 'John Lennon', 'Paul Maccartney', 'George Harrison']
##>>> 
##=========================================================================================================================
# Home work 3.3
# -------------
#
li = []
method = int(input('Which kind of the sorting you prefer: Enter 1 for "increased" or 2 for "reversed":'))
n = int(input('How many integer numbers you would like to sort? '))
#
for i in range(0, n):
    prompt = 'Enter your ' + str(i + 1) + ' integer number: '
    member = int(input(prompt))
    li.append(member)
# ForEnd

print('You have entered the following list: ', li)

if method == 1:
    li.sort()
else:
    li.sort()
    li.reverse()
# EndIf

print('Please see the result of the sorting: ', li)
##=========================================== RESTART: D:\Python\Training\Test_EvN.py ==========================================
##Which kind of the sorting you prefer: Enter 1 for "increased" or 2 for "reversed":2
##How many integer numbers you would like to sort? 13
##Enter your 1 integer number: 13
##Enter your 2 integer number: 888
##Enter your 3 integer number: 3
##Enter your 4 integer number: 0
##Enter your 5 integer number: 0
##Enter your 6 integer number: 0
##Enter your 7 integer number: 23
##Enter your 8 integer number: 4
##Enter your 9 integer number: 7
##Enter your 10 integer number: 8
##Enter your 11 integer number: 9
##Enter your 12 integer number: 1
##Enter your 13 integer number: 3
##You have entered the following list:  [13, 888, 3, 0, 0, 0, 23, 4, 7, 8, 9, 1, 3]
##Please see the result of the sorting:  [888, 23, 13, 9, 8, 7, 4, 3, 3, 1, 0, 0, 0]
##>>>
##=========================================================================================================================
# Home work 3.4
# -------------
#
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

unique_list = []

for i in range(len(my_list)):
    if my_list[i] not in unique_list:
        unique_list.append(my_list[i])
    else:
        pass
    # IfEnd
# ForEnd

print('It is my_list : ', my_list)
print('It is unique_list :', unique_list)
##=========================================== RESTART: D:\Python\Training\Test_EvN.py ==========================================
##It is my_list :  [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
##It is unique_list : [1, 2, 4, 6, 9]
##>>>
##=========================================================================================================================
# Home work 3.5
# -------------
#
s = input('Enter a string of integer numbers separated by blanks: ')
li1 = s.split()
li = []

for i in li1:
    li.append(int(i))

print('You entered this string: ', s)
print('Here is the sum of all the numbers: ', sum(li))
=========================================== RESTART: D:\Python\Training\Test_EvN.py ===========================================
##Enter a string of integer numbers separated by blanks: 1 -5749 2345 894 1
##You entered this string:  1 -5749 2345 894 1
##Here is the sum of all the numbers:  -2508
##>>> 
##=========================================================================================================================
# Home work 3.6
# -------------
#
s = input('Enter a string of integer numbers separated by blanks: ')
ini_li = s.split()
print('You entered: ', ini_li)
work_li = []

for i in range(len(ini_li)):
    if ini_li[i] in ini_li[i+1:len(ini_li)]:
        if ini_li[i] not in work_li:
            work_li.append(ini_li[i])
        else:
            pass
    else:
        pass
#
print('Here are the non-unique numbers you entered: : ',work_li)
##======================================== RESTART: D:\Python\Training\Test_EvN.py =======================================
##Enter a string of integer numbers separated by blanks: 11 11 12 12 3 45 68 66 88 5 5 5 5 10
##You entered:  ['11', '11', '12', '12', '3', '45', '68', '66', '88', '5', '5', '5', '5', '10']
##Here are the non-unique numbers you entered: :  ['11', '12', '5']
##>>> 
##=========================================================================================================================
# Home work 3.7
# -------------
#
s = input('Enter a string of any numbers separated by blanks: ')
ini_num = s.split()
num_list = []
#
for i in ini_num:
    num_list.append(float(i))
#
print('You enterd the following list of numbers: ', num_list)
print('Here is their average: ', sum(num_list)/len(num_list))
##======================================== RESTART: D:\Python\Training\Test_EvN.py =======================================
##Enter a string of any numbers separated by blanks: -1 99 100 -67 34
##You enterd the following list of numbers:  [-1.0, 99.0, 100.0, -67.0, 34.0]
##Here is their average:  33.0
##>>> 
##=========================================================================================================================
# Home work 3.8
# -------------
#
num_3 = input('Enter a string of any numbers separated by blanks. Inclual at least one times three entry: ')
ini_num = num_3.split()
num_list = []
sum_3 = []
#
for i in ini_num:
    num_list.append(float(i))
#
for i in range(len(num_list)):
    if num_list[i] % 3 == 0.0:
        sum_3.append(num_list[i])
    else:
        pass
#
print("This is an avarage of times three entries", ' ::: ', sum(sum_3)/len(sum_3))
##======================================== RESTART: D:\Python\Training\Test_EvN.py =======================================
##Enter a string of any numbers separated by blanks. Inclual at least one times three entry: 0 3 6 7 8 33 4
##This is an avarage of times three entries  :::  10.5
##>>> 
