#!/usr/bin/python

def months_calculator():
    while True:
        try:
            balance = float(raw_input("What is the total amount you owe? \
Please enter the dollar amount without the dollar sign. "))
        except ValueError:
            print("I'm sorry, but your input wformat as invalid. Please try again. ")
            continue
        else:
            break

    while True:
        try:
           interest_rate = float(raw_input("What is the annual percent interest \
rate on your debt? Please omit the percent sign. "))
           interest_rate = (interest_rate / 100.0) / 12.0
        
        except ValueError:
            print("I'm sorry, but your input format was invalid. Please try again. ")
            continue
        else:
            break

    while True:
        try:
            min_payment = float(raw_input("What is the minimum monthly payment \
that must be made? Please enter the dollar amount without the dollar sign. "))
        except ValueError:
            print("I'm sorry, but your input format was invalid. Please try again. ")
            continue
        else:
            break

    months = 0

    while balance >= min_payment:
    #while balance >= 0 and balance >= min_payment:
        balance = balance - (min_payment - interest_rate*balance)
        months += 1
        #months = months + 1
        #continue
    print months
    print balance

def main():
    months_calculator()

if __name__ == "__main__":
    main()
