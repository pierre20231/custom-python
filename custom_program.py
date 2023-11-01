valid_ids = ['111']

def main():
    while True:

        id_in, amount, expense = input_data()
        remainder = calcs(amount, expense)
        output(id_in, amount, expense, remainder)
        break

def input_data():
    while True:
        id_in = input("Enter your password here ")
        if len(id_in) < 3 :
            print("Your password as to be more than 3 characters")
        if id_in in valid_ids:
           break
        else:
            print("Invalid password try again ")
    while True:
        try:
            amount = float(input("Enter your income here "))
            break
        except ValueError as e:
            print("Income has to be a number please try again ")
    while True:
        try:
            expense = float(input("How much did you spend over the month? "))
            break
        except ValueError as e :
            print("Income cannot be a number, Try again")

    return id_in, amount, expense

def calcs(amount, expense):
    remainder = amount - expense

    return remainder


def output(id_in, amount, expense, remainder):
    print(f" ID        Income      Expenses       Balance ")
    print(f" {id_in}       ${amount}      ${expense}           cat${remainder}")

    match remainder:
        case remainder if remainder < 100:
            print("Your balance is low")
        case remainder if remainder > 100:
            print("Your balance is in good shape")



main()

