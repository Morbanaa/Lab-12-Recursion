#Teddy Rodd
#Morbanaa Studios
#Lab 12 Recursion

def main():

    ############################################
    # Question One: Recursive Printing
    ############################################
    print("Question One: Recursive Printing")
    while True:
        counter = 1
        try:
            value1 = int(input("Enter a positive number greater than 1: "))
            if value1 < 2:
                print("The number must be greater than 1!")
                continue
            break
        except ValueError:
            print("Must be a number!")
    
    print(f"\nValues 1 - {value1}:")
    recursive_printing(value1,counter)


    ############################################
    # Question Two: Recursive Multiplication
    ############################################
    print("\nQuestion Two: Recursive Multiplication")
    counter = 0
    total = 0
    while True:
        try:
            x = int(input("Enter a positive non zero integer for X: "))
            if x < 1:
                print("X must be greater than zero!")
                continue
            break
        except ValueError:
            print("Value Error! X must be a positive non zero integer!")

    while True:
        try:
            y = int(input("Enter a positive non zero integer for Y: "))
            if y < 1:
                print("Y must be greater than zero!")
                continue
            break
        except ValueError:
            print("Value Error! Y must be a postive non zero integer!")

    print(f"\nTotal {x} X {y} = {recursive_multiplication(x,y,counter,total)}")


    ############################################
    # Question Three: Recursive Lines
    ############################################
    print("\nQuestion Three: Recursive Lines")
    while True:
        counter = 1
        x=0
        y=0
        try:
            n = int(input("Enter a postive non zero integer for N: "))
            if n < 1:
                print("N must be greater than zero!")
                continue
            break
        except ValueError:
            print("N Must be a none zero integer!")
    print()
    recursive_lines(n,x,y,counter)
    print()


def recursive_printing(number,counter):
    if counter == number + 1:
        return
    else:
        print(counter)
        return recursive_printing(number,counter + 1)


def recursive_multiplication(x,y,counter,total):
    if counter == x:
        return total
    else:
        return recursive_multiplication(x,y,counter + 1,total + y)


def recursive_lines(n,x,y,counter):
    if y == n:
        return
    elif x < counter:
        print("*",end="")
        return recursive_lines(n,x + 1,y,counter)
    else:
        print()
        x = 0
        return recursive_lines(n,x,y + 1,counter + 1)
        


if __name__ == "__main__":
    main()