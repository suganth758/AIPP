def approve_loan(income, credit_score, loan_amount, gender):
    """
    Approve loan if:
    - Income is at least 30,000
    - Credit score is at least 650
    - Loan amount does not exceed 5x income
    Gender is collected for reporting only (no effect on approval).
    """
    if income < 30000:
        return False, "Income too low"
    if credit_score < 650:
        return False, "Credit score too low"
    if loan_amount > income * 5:
        return False, "Requested loan amount too high"
    return True, "Loan approved"
def main():
    print("=== Simple Loan Approval System ===")
    name = input("Enter your name: ")
    gender = input("Enter your gender (Male/Female/Other): ").strip().capitalize()
    try:
        income = float(input("Enter your annual income: "))
        credit_score = int(input("Enter your credit score: "))
        loan_amount = float(input("Enter desired loan amount: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    approved, reason = approve_loan(income, credit_score, loan_amount, gender)
    print(f"\nApplicant: {name}")
    print(f"Gender: {gender}")
    if approved:
        print("Congratulations! Your loan is approved.")
    else:
        print(f"Loan denied: {reason}")

if __name__ == "__main__":
    main()