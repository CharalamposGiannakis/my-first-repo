# Create a function that calculates the tip based on total bill and tip percentage
def calculate_tip(total_bill, tip_percentage):
    """
    Calculate the tip based on total bill and tip percentage.

    Parameters:
    total_bill (float): The total bill amount.
    tip_percentage (float): The tip percentage to be applied.

    Returns:
    float: The calculated tip amount.
    """
    return total_bill * (tip_percentage / 100)
if __name__ == "__main__":
    try:
        total = float(input("Enter the total bill amount: "))
        percent = float(input("Enter the tip percentage: "))
        tip = calculate_tip(total, percent)
        print(f"Tip amount: ${tip:.2f}")
    except ValueError:
        print("Please enter valid numbers.")