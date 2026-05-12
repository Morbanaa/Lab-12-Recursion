#Teddy Rodd
#Morbanaa Studios
#Lab 12 Recursion

def main():
    counter = 1
    print("Question One: Recursive Printing")
    while True:
        try:
            value1 = int(input("Enter a positive number greater than 1: "))
            if value1 < 2:
                print("The number must be greater than 1!")
                continue
            break
        except ValueError:
            print("Must be a number!")

    recursive_printing(value1,counter)

    print("\nQuestion Two: Recursive Multiplication")
    recursive_multiplication()

    print("\nQuestion Three: Recursive Lines")
    recursive_lines()
    print()

def recursive_printing(number,counter):
    if counter == number + 1:
        return
    else:
        print(counter)
        return recursive_printing(number,counter + 1)


def recursive_multiplication():
    pass


def recursive_lines():
    pass


if __name__ == "__main__":
    main()