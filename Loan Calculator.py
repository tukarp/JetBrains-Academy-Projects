# My solution to JetBrains Academy Loan Calculator Project


import math
import argparse


# creating parser
parser = argparse.ArgumentParser(description="Loan Calculator")

# parser arguments
parser.add_argument("--type", help = "Annuity or Differential types of payments", choices = ["annuity", "diff"])
parser.add_argument("--payment", help = "Monthly payment", type = int)
parser.add_argument("--principal", help = "Loan principal", type = int)
parser.add_argument("--", help = "Number of months", type = int)
parser.add_argument("--interest", help = " ", type = float)
args = parser.parse_args()
args_list = [args.type, args.payment, args.principal, args.periods, args.interest]

# checking conditions to choose function
if args.type != ["annuity", "diff"]:
    print("Incorrect parameters")
    exit()
else:
    # case for annuity payments
    if args.type == "annuity":
        pass
    # case for differentiated payments
    else:
        pass


# program loop
def start_program():
    while True:
        print("What do you want to calculate?")
        print("type 'n' - for number of monthly payments,")
        print("type 'a' - for annuity monthly payment amount,")
        print("type 'p' - for the monthly payment,")
        # print("type 'exit' - to exit the program:")
        user_input = input()
        # cases
        match user_input:
            case "n":
                number_of_monthly_payments_calculator()
            case "a":
                annuity_monthly_payment_calculator()
            case "d":
                differentiated_payments_calculator()
            case "p":
                loan_principal_calculator()
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


# case n
def number_of_monthly_payments_calculator():
    # asking for loan principal
    loan_principal = get_loan_principal()

    # asking for monthly payment
    monthly_payment = int(input("Enter the monthly payment: \n"))

    # asking for loan interest
    loan_interest = get_loan_interest()

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
        print(f"It will take {years_to_repay} years and {months_to_repay} months to repay the loan!")
    elif years_to_repay == 1 and months_to_repay == 1:
        print(f"It will take {years_to_repay} year and {months_to_repay} month to repay the loan!")
    elif years_to_repay > 1 and months_to_repay == 0:
        print(f"It will take {years_to_repay} years to repay the loan!")
    elif years_to_repay == 1 and months_to_repay == 0:
        print(f"It will take {years_to_repay} year to repay the loan!")
    elif years_to_repay == 0 and months_to_repay > 1:
        print(f"It will take {months_to_repay} months to repay the loan!")
    else:
        print(f"It will take {months_to_repay} month to repay the loan!")
    # printing overpayment
    print(f"Overpayment = {overpayment}!")


# case a
def annuity_monthly_payment_calculator():
    # asking for loan principal
    loan_principal = get_loan_principal()

    # asking for number of periods
    periods = get_number_of_periods()

    # asking for loan interest
    loan_interest = get_loan_interest()

    # calculating payment for every month
    annuity_payment = math.ceil(loan_principal * ((loan_interest * math.pow((1 + loan_interest), periods)) / (
                math.pow((1 + loan_interest), periods) - 1)))

    # calculating overpayment
    overpayment = get_overpayment(annuity_payment * periods, loan_principal)

    # printing monthly payment and overpayment
    print(f"Your monthly payment = {annuity_payment}!")
    print(f"Overpayment = {overpayment}!")


# case d
def differentiated_payments_calculator():
    # asking for loan principal
    loan_principal = get_loan_principal()

    # asking for number of periods
    periods = get_number_of_periods()

    # asking for loan interest
    loan_interest = get_loan_interest()

    # calculating differentiated payments
    overpayment = 0
    month_counter = 1
    while month_counter < (periods + 1):
        differentiated_payments = math.ceil((loan_principal / periods) + (loan_interest * (loan_principal - (
                    loan_principal * (month_counter - 1) / periods))))
        # printing payments for every month
        print(f"Month {month_counter}: payment is {differentiated_payments}")
        overpayment += differentiated_payments
        month_counter += 1

    # calculating and printing overpayment
    overpayment = get_overpayment(overpayment, loan_principal)
    print(f"Overpayment = {overpayment}!")


# case p
def loan_principal_calculator():
    # asking for annuity payment
    annuity_payment = float(input("Enter the annuity payment: \n"))

    # asking for number of periods
    periods = get_number_of_periods()

    # asking for loan interest
    loan_interest = get_loan_interest()

    # calculating loan principal
    loan_principal = math.floor(annuity_payment / ((loan_interest * math.pow((1 + loan_interest), periods)) / (
                math.pow((1 + loan_interest), periods) - 1)))

    # calculating overpayment
    overpayment = get_overpayment(annuity_payment * periods, loan_principal)

    # printing loan principal and overpayment
    print(f"Your loan principal = {loan_principal}!")
    print(f"Overpayment = {overpayment}!")


# starting program and choosing program's feature
start_program()
