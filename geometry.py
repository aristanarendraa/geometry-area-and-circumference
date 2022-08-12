from re import M
from turtle import width


#AREA
def a_rectangle():
    print('Calculating area of rectangle')
    length=int(input('Length: '))
    width=int(input('Width: '))
    print('Area: ', str(length*width))

def a_triangle():
    print('Calculating area of triangle')
    base=int(input('Base: '))
    height=int(input ('Height: '))
    print('Area: ', str(base*height/2))

def a_kite():
    print("Calculating area of kite")
    diagonal1=int(input('Diagonal 1 length: '))
    diagonal2=int(input('Diagonal 2 length: '))
    print('Area: ', str(diagonal1*diagonal2/2))

def a_trapezium():
    print('Calculating area of trapezium')
    upper_base=int(input('Upper base: '))
    lower_base=int(input('Lower base: '))
    height=int(input('Height: '))
    print('Area: ', str((upper_base + lower_base)*height/2))

def a_square():
    print('Calculating area of square')
    side=int(input('Side: '))
    print('Area: ', str(side**2))

def a_show_menu():
    print('\n')
    print('---------- Select Geometry ----------')
    print('--------- Type number only! ---------')
    print('1. Rectangle')
    print('2. Triangle')
    print('3. Kite')
    print('4. Trapezium')
    print('5. Square')
    print('6. Back')

#CIRCUMFERENCE
def c_rectangle():
    print('Calculating circumference of rectangle')
    length=int(input('Length: '))
    width=int(input('Width: '))
    print('Circumference: ', 2*(length + width))

def c_triangle():
    print('Calculating circumference of triangle')
    side1=int(input('Side 1: '))
    side2=int(input('Side 2: '))
    side3=int(input('Side 3: '))
    print('Circumference: ', side1 + side2 + side3)\

def c_kite():
    print('Calculating circumference of kite')
    side1=int(input('Side 1: '))
    side2=int(input('Side 2: '))
    side3=int(input('Side 3: '))
    side4=int(input('Side 4: '))
    print('Circumference: ', side1 + side2 + side3 + side4)

def c_trapezium():
    print('Calculating circumference of trapezium')
    side1=int(input('Side 1: '))
    side2=int(input('Side 2: '))
    side3=int(input('Side 3: '))
    side4=int(input('Side 4: '))
    print('Circumference: ', side1 + side2 + side3 + side4)

def c_square():
    print('Calculating circumference of square')
    side=int(input('Side: '))
    print('Cirumference: ', 4*side)

def c_show_menu():
    print('\n')
    print('---------- Select Geometry ----------')
    print('--------- Type number only! ---------')
    print('1. Rectangle')
    print('2. Triangle')
    print('3. Kite')
    print('4. Trapezium')
    print('5. Square')
    print('6. Back')

#SELECTION
def select():
    print('----------------------------')
    print('Select calculation below: ')
    print('1. Area')
    print('2. Circumference')
    print('3. Exit program')
    print('----------------------------')
    selection=int(input('Which one do you choose?: '))
    if selection == 1:
        a_show_menu()
    elif selection == 2:
        c_show_menu()
    elif selection == 3:
        exit()
    else:
        print('Please select between 1-3!!!')
        select()
        
select()

menu=int(input('Select geometry: '))

#AREA SUMMON
if menu == 1:
    a_rectangle()
elif menu == 2:
    a_triangle()
elif menu == 3:
    a_kite()
elif menu == 4:
    a_trapezium()
elif menu == 5:
    a_square()
elif menu == 6:
    select()
else:
    print('Wrong options, please select number 1-6!')

print('Area calculation program')
answer = 'y'
while(answer == 'y'):
    a_show_menu()
    answer = input('Do you want to repeat? (y/n): ')
    if answer == 'y':
        break
    elif answer == 'n':
        select()
    else:
        print('Y/N?')

#CIRCUMFERENCE SUMMON1
if menu == 1:
    c_rectangle()
elif menu == 2:
    c_triangle()
elif menu == 3:
    a_kite()
elif menu == 4:
    a_trapezium()
elif menu == 5:
    a_square()
elif menu == 6:
    select()
else:
    print('Wrong options, please select number 1-6!')

print('Circumference calculation program')
answer = 'y'
while(answer == 'y'):
    c_show_menu()
    answer = input('Do you want to repeat? (y/n): ')
    if answer == 'y':
        break
    elif answer == 'n':
        select()
    else:
        print('Y/N?')
