"""
    Name: Dan Shaw w0190983
    Program Title: Restaurant Bill
    Program Description: Calculates tax and tip for a restaurant bill
"""

#PROG 1700 – Tech Check #1
#Variables, Operators, Input/Output & Casting

# Restaurant Bill 
# You will create a console-based Python program that will calculate the amount of the tip, the tax, and the 
# total amount of a restaurant bill. The program will prompt the user to input the original amount of the bill. 
# The program will then output the amount of the tax (15% of the original amount) and a tip (20% of the original amount). 
# Finally, the program will output the new total of the bill.

TAX_RATE = 0.15
TIP_RATE = 0.2

def main():
    # Access global level variables
    global TAX_RATE
    global TIP_RATE

    print("THE RESTAURANT BILL CALCULATOR")
    # Prints 30 '-'
    print("-" * 30)
    
    # Take in user input and convert to float
    baseBill = float(input("Please enter the base amount of your bill, excluding tax and tip: "))

    # Perform bill calculations
    taxAmount = calculateValue(baseBill, TAX_RATE)
    tipAmount = calculateValue(baseBill, TIP_RATE)
    total = baseBill + taxAmount + tipAmount

    # Output formatted text
    print("""Your Base Bill is: ${0:.2f}
    The tax rate is {1}%, for a total tax amount of: ${2:.2f}
    Your tip rate is {3}% for a total tip of: ${4:.2f}
    Your total is: ${5:.2f}""".format(baseBill, int(TAX_RATE * 100), taxAmount, int(TIP_RATE * 100), tipAmount, total))

# Calculates tip and tax based on modifier
def calculateValue(bill, modifier):
    return bill * modifier

if __name__ == "__main__":
    main()