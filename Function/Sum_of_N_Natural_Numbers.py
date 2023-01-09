"""Python Program to find the sum of first N natural numbers (use
recursive function)"""

def NaturalSum(terms):
    if terms>1:
        return terms+NaturalSum(terms-1)
    elif terms==1:
        return 1

terms = int(input("Enter the Number of Terms:\n"))
print(f"The sum of {terms} natural numbers is {NaturalSum(terms)}")