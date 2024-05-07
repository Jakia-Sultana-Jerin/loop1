
# Assignment 1: Write a function that calculates compound interest using the formula A = P(1 + r/n)^(nt).


def compound_interest(principal, rate, time, compounds_per_year):
    """
    Calculate compound interest.
    
    Args:
        principal (float): The initial amount of money.
        rate (float): The annual interest rate (in decimal).
        time (float): The number of years the money is invested or borrowed for.
        compounds_per_year (int): The number of times interest is compounded per year.

    Returns:
        float: The amount of money accumulated after the given time period.
    """
    amount = principal * (1 + rate / compounds_per_year) ** (compounds_per_year * time)
    return amount

# Example usage:
principal = 1000  # initial amount
rate = 0.05  # annual interest rate (5%)
time = 5  # number of years
compounds_per_year = 12  # interest compounded monthly
result = compound_interest(principal, rate, time, compounds_per_year)
print("Compound interest after 5 years:", round(result, 2))