def monthly_payment():
    princaple= float(input("Enter the loan amount : \n"))
    apr= float(input("Enter the annual interests rate : \n"))
    years= int(input("Enter the amount of years : \n"))

    monthly_rate= apr/1200
    amount_of_months=years*12
    monthly_pay = princaple*monthly_rate/ (1-(1+monthly_rate) **(-amount_of_months))

    print(f"the monthly payment for loan is :   {monthly_pay :.2f}")


monthly_payment()
