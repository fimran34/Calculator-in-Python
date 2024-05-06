def add(m,n):
    return m + n

def sub(m,n):
    return m - n

def mul(m,n):
    return m * n

def div(m,n):
    return m / n





while True:
    print("Choose an option from the list below")
    print("Choose 'a/A' for addition")
    print("Choose 's/S' for subtraction")
    print("Choose 'm/M' for multiplication")
    print("Choose 'd/D' for division")
    answer = input("Enter your answer")
    if answer in ('a','A','s','S','d','D','m','M'):
        if answer=='a' or answer=='A':
            a=int(input('Enter the first number: '))
            b=int(input('Enter the second number: '))
            print("The answer is:",add(a,b))
            print('Do you want to continue or not?')
            continue1=input('Type Y/y for yes and N/n for no: ')
            if continue1=='y' or continue1=='Y':
                continue
            elif continue1=='n' or contine1=='N':
                break

        elif answer=='s' or answer=='S':
            a=int(input('Enter the first number: '))
            b=int(input('Enter the second number: '))
            print("The answer is:",sub(a,b))
            print('Do you want to continue or not?')
            continue1 = input('Type Y/y for yes and N/n for no: ')
            if continue1 == 'y' or continue1 == 'Y':
                continue
            elif continue1 == 'n' or contine1 == 'N':
                break

        elif answer=='m' or answer=='M':
            a=int(input('Enter the first number: '))
            b=int(input('Enter the second number: '))
            print("The answer is:",mul(a,b))
            print('Do you want to continue or not?')
            continue1 = input('Type Y/y for yes and N/n for no: ')
            if continue1 == 'y' or continue1 == 'Y':
                continue
            elif continue1 == 'n' or contine1 == 'N':
                break

        elif answer=='d' or answer=='D':
            a=int(input('Enter the first number: '))
            b=int(input('Enter the second number: '))
            print("The answer is:",div(a,b))
            print('Do you want to continue or not?')
            continue1 = input('Type Y/y for yes and N/n for no: ')
            if continue1 == 'y' or continue1 == 'Y':
                continue
            elif continue1 == 'n' or contine1 == 'N':
                break

    else:
        print("Invalid option")
        print('Choose from the list')
        continue