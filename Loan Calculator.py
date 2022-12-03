# My solution to JetBrains Academy Loan Calculator Project


import math
import argparse


# creating parser
def create_parser():
    parser = argparse.ArgumentParser(description="Loan Calculator")

    # parser arguments
    parser.add_argument("--type", help="Annuity or Differential types of payments")
    parser.add_argument("--payment", help="Monthly payment", type=int)
    parser.add_argument("--principal", help="Loan principal", type=int)
    parser.add_argument("--periods", help="Number of months", type=int)
    parser.add_argument("--interest", help="Rate of interest", type=float)
    args = parser.parse_args()


    # checking conditions to choose function
    if args.type == "diff" and args.payment is not None:
        print("Incorrect parameters")
        exit(0)
    elif args.type not in ["annuity", "diff"]:
        print("Incorrect parameters")
        exit(0)
    else:
        # case for annuity payments
        if args.type == "annuity":
            # case for n
            if (args.principal is not None) and (args.payment is not None) and (args.interest is not None):
                number_of_monthly_payments_calculator(args.principal, args.payment, args.interest)
            # case for a
            elif (args.principal is not None) and (args.periods is not None) and (args.interest is not None):
                annuity_monthly_payment_calculator(args.principal, args.periods, args.interest)
            # case for p
            elif (args.payment is not None) and (args.periods is not None) and (args.interest is not None):
                loan_principal_calculator(args.payment, args.periods, args.interest)
        # case for differentiated payments
        else:
            # case for d
            if (args.principal is not None) and (args.periods is not None) and (args.interest is not None):
                differentiated_payments_calculator(args.principal, args.periods, args.interest)
            else:
                print("Incorrect parameters")


# program loop
def start_program():
    while True:
        print("What do you want to calculate?")
        print("type 'n' - for number of monthly payments,")
        print("type 'a' - for annuity monthly payment amount,")
        print("type 'p' - for the monthly payment,")
        print("type 'd' - for differentiated payments,")
        print("type 'exit' - to exit the program:")
        user_input = input()
        # cases
        match user_input:
            case "m":
                loan_principal = get_loan_principal()
                monthly_payment = int(input("Enter the monthly payment: \n"))
                loan_interest = get_loan_interest()
                number_of_monthly_payments_calculator(loan_principal, monthly_payment, loan_interest)
            case "a":
                loan_principal = get_loan_principal()
                periods = get_number_of_periods()
                loan_interest = get_loan_interest()
                annuity_monthly_payment_calculator(loan_principal, periods, loan_interest)
            case "d":
                loan_principal = get_loan_principal()
                periods = get_number_of_periods()
                loan_interest = get_loan_interest()
                differentiated_payments_calculator(loan_principal, periods, loan_interest)
            case "p":
                annuity_payment = float(input("Enter the annuity payment: \n"))
                periods = get_number_of_periods()
                loan_interest = get_loan_interest()
                loan_principal_calculator(annuity_payment, periods, loan_interest)
            case "exit":
                exit()
            case _:
                print("Enter the correct option \n")


# getting loan principal
def get_loan_principal():
    loan_principal = int(input("Enter the loan principal: \n"))
    return loan_principal


# getting loan interest
def get_loan_interest():
    loan_interest = float(input("Enter the loan interest: \n"))
    loan_interest = ((loan_interest / 12) / 100)
    return loan_interest


# getting number of periods (months)
def get_number_of_periods():
    periods = int(input("Enter the number of periods: \n"))
    return periods


# getting and printing overpayment
def get_overpayment(paid, loan_principal):
    overpayment = paid - loan_principal
    return int(overpayment)


def number_of_monthly_payments_calculator(loan_principal, monthly_payment, loan_interest):
    # calculating months to repay the loan and rounding the result
    months_to_repay = math.ceil(
        math.log((monthly_payment / (monthly_payment - (loan_interest * loan_principal))), 1 + loan_interest))

    # calculating years and months
    years_to_repay = 0
    if months_to_repay > 11:
        years_to_repay = math.floor(months_to_repay / 12)
        months_to_repay = (months_to_repay - (years_to_repay * 12))

    # calculating overpayment
    overpayment = get_overpayment(monthly_payment * (years_to_repay * 12 + months_to_repay), loan_principal)

    # cases for multiple or single months and years
    if years_to_repay > 1 and months_to_repay > 1:
        print(f"It will take {years_to_repay} years and {months_to_repay} months to repay the loan")
    elif years_to_repay == 1 and months_to_repay == 1:
        print(f"It will take {years_to_repay} year and {months_to_repay} month to repay the loan")
    elif years_to_repay > 1 and months_to_repay == 0:
        print(f"It will take {years_to_repay} years to repay the loan")
    elif years_to_repay == 1 and months_to_repay == 0:
        print(f"It will take {years_to_repay} year to repay the loan")
    elif years_to_repay == 0 and months_to_repay > 1:
        print(f"It will take {months_to_repay} months to repay the loan")
    else:
        print(f"It will take {months_to_repay} month to repay the loan")

    # printing overpayment
    print(f"Overpayment = {overpayment}")


def annuity_monthly_payment_calculator(loan_principal, periods, loan_interest):
    # calculating payment for every month
    annuity_payment = math.ceil(loan_principal * ((loan_interest * math.pow((1 + loan_interest), periods)) / (
                math.pow((1 + loan_interest), periods) - 1)))

    # calculating overpayment
    overpayment = get_overpayment(annuity_payment * periods, loan_principal)

    # printing monthly payment and overpayment
    print(f"Your monthly payment = {annuity_payment}")
    print(f"Overpayment = {overpayment}")


# calculating loan principal
def loan_principal_calculator(annuity_payment, periods, loan_interest):
    # calculating loan principal
    loan_principal = math.floor(annuity_payment / ((loan_interest * math.pow((1 + loan_interest), periods)) / (
                math.pow((1 + loan_interest), periods) - 1)))

    # calculating overpayment
    overpayment = get_overpayment(annuity_payment * periods, loan_principal)

    # printing loan principal and overpayment
    print(f"Your loan principal = {loan_principal}")
    print(f"Overpayment = {overpayment}")


# calculating differentiated payments
def differentiated_payments_calculator(loan_principal, periods, loan_interest):
    overpayment = 0
    month_counter = 1
    while month_counter < (periods + 1):
        differentiated_monthly_payment = math.ceil((loan_principal / periods) + (loan_interest * (loan_principal - (
                    loan_principal * (month_counter - 1) / periods))))
        # printing payments for every month
        print(f"Month {month_counter}: payment is {differentiated_monthly_payment}")
        overpayment += differentiated_monthly_payment
        month_counter += 1

    # calculating and printing overpayment
    overpayment = get_overpayment(overpayment, loan_principal)
    print(f"Overpayment = {overpayment}")


# starting program and choosing program's feature
create_parser()
# start_program()
