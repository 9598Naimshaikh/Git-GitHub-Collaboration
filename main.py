# write a function to calculate factorial of the given number.
def factorial_calc(num):
    # write down your logic here..
    fact = 1
    if num < 0:
        print("Please enter positive number.")
    else:
        for i in range(num):
            fact = num * fact
            num = num-1
    print(fact)



# write a function to calculate n number of times to calculate fibonacchi number.
def fibonacchi_calc(num):
    # write down your logic here..
    if num < 0:
        print("The fibonacchi number does not exist for negative number.")
    elif num == 0 or num == 1:
        return num
    else:
        return fibonacchi_calc(num-1) + fibonacchi_calc(num-2)


# write a function to check given number is palindrome or not.
def palindrome_checker(num):
    # write down your logic here..
    pass


if __name__ == "__main__":
    factorial_calc(5)

    num = int(input("Enter a number: "))
    for n in range(num+1):
        print(fibonacchi_calc(n))


