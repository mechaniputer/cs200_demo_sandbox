def func1():
    lst = []
    print('Enter numbers one at a time. Enter 0 to stop.')
    myNum = int(input('num:'))
    while myNum != 0:
        lst.append(myNum)
        myNum = int(input('num:'))
    print('You added ', len(lst), ' Numbers')
    return lst


def func2(info):
    print('Here is the data:')
    print(info)
    response = ''
    while True:
        response = input('Select an option. 1-sum  2-min  3-max  4-quit')
        if response == '1':
            print('The sum is', sum(info))
        elif response == '2':
            print('Not supported yet')
        elif response == '3':
            print('Not supported yet')
        elif response == '4':
            print('Goodbye')
            return


def main():
    print("Hello, World!")
    print('Hello World Again')
    print('Hello World Again')
    print('Hello World Again')
    print('Hello World Again')
    print('Hello World Again')
    print('Hello World Again')
    print('Hello World Again')
    print('Hello World Again')
    print('Hello World Again')
    print('Hello World Again')
    print('Hello World Again')
    print('Hello World Again')
    print('Hello World Again')
    print('Hello World Again')
    print('Hello World Again')
    print('Hello World Again')
    print('Hello World Again')
    print('Hello World Again')
    print('Hello World Again')
    print('Hello World Again')
    print('Hello World Again')
    print('Hello World Again')
    data = func1()
    func2(data)


if __name__ == "__main__":
    main()
