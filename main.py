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
def fibonacchi_calc(num_of_term):
    # write down your logic here..
    pass


# write a function to check given number is palindrome or not.
def palindrome_checker(num):
    # write down your logic here..
    pass


if __name__ == "__main__":
    factorial_calc(5)