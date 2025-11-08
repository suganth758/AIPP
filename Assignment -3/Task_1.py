# TGNPDCL Electricity Bill Generator
# Author: <Your Name>
# Date: <Date>
# Tool: Python 3.x (VS Code / Colab compatible)

def calculate_bill():
    print("🔹 TGNPDCL Electricity Bill Generator 🔹")

    # Input data
    PU = float(input("Enter Previous Reading (in units): "))
    CU = float(input("Enter Current Reading (in units): "))
    customer_type = input("Enter Type of Customer (Domestic/Commercial/Industrial): ").strip().lower()

    # Calculate consumed units
    units = CU - PU
    if units < 0:
        print("Error: Current reading cannot be less than previous reading.")
        return

    # Initialize charges
    EC = FC = CC = ED = 0

    # Tariff calculation based on customer type
    if customer_type == "domestic":
        if units <= 100:
            EC = units * 1.95
            FC = 50
            CC = 10
        elif units <= 200:
            EC = (100 * 1.95) + ((units - 100) * 3.10)
            FC = 75
            CC = 15
        elif units <= 400:
            EC = (100 * 1.95) + (100 * 3.10) + ((units - 200) * 4.50)
            FC = 100
            CC = 20
        else:
            EC = (100 * 1.95) + (100 * 3.10) + (200 * 4.50) + ((units - 400) * 6.00)
            FC = 125
            CC = 25

    elif customer_type == "commercial":
        EC = units * 7.50
        FC = 200
        CC = 25

    elif customer_type == "industrial":
        EC = units * 8.00
        FC = 500
        CC = 50

    else:
        print("Invalid customer type entered.")
        return

    # Electricity Duty (6% of EC)
    ED = EC * 0.06

    # Total bill
    total_bill = EC + FC + CC + ED

    # Print bill summary
    print("\n===== ELECTRICITY BILL =====")
    print(f"Previous Reading (PU): {PU:.2f}")
    print(f"Current Reading  (CU): {CU:.2f}")
    print(f"Units Consumed: {units:.2f}")
    print(f"Customer Type: {customer_type.capitalize()}")
    print("--------------------------------")
    print(f"Energy Charges (EC): ₹{EC:.2f}")
    print(f"Fixed Charges (FC): ₹{FC:.2f}")
    print(f"Customer Charges (CC): ₹{CC:.2f}")
    print(f"Electricity Duty (ED): ₹{ED:.2f}")
    print("--------------------------------")
    print(f"Total Bill Amount: ₹{total_bill:.2f}")
    print("===============================")

# Run the program
if __name__ == "__main__":
    calculate_bill()
