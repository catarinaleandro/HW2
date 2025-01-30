print("Welcome to the net salary calculator!")

try:
    gross_salary = int(input("What is your gross salary? "))
    number_children = int(input("How many children do you have? "))

    if gross_salary < 1000:
        tax_rate = 10
    elif gross_salary < 2000:
        tax_rate = 12
    elif gross_salary < 4000:
        tax_rate = 14
    else:
        tax_rate = 18

    if gross_salary < 2000:
        tax_reduction = number_children * 1
    else:
        tax_reduction = number_children * 0.5

    final_tax_rate = tax_rate - tax_reduction
    net_salary = gross_salary * (1 - final_tax_rate / 100)

    print(f"Your net salary is: {net_salary}")

except ValueError:
    print("Invalid input. Please enter numeric values for salary and number of children.")

print("Thank you for using the salary calculator!")
