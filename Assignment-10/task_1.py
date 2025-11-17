
def apply_discount(price, rate):
    """Applies a discount rate to a given price."""
    return price * rate

def discount(price, category):
    """Returns the discounted price based on category and price."""
    
    discount_rules = {
        "student": lambda p: apply_discount(p, 0.9 if p > 1000 else 0.95),
        "regular": lambda p: apply_discount(p, 0.85 if p > 2000 else 1.0),
    }

    # Default to regular if category does not exist
    rule = discount_rules.get(category, discount_rules["regular"])
    return rule(price)


# ---------------------------------------------------------
# Sample Inputs / Test Calls
# ---------------------------------------------------------

if __name__ == "__main__":
    print("Test Cases:")
    print("500, student  →", discount(500, "student"))       # 475.0
    print("1500, student →", discount(1500, "student"))      # 1350.0
    print("1800, regular →", discount(1800, "regular"))      # 1800.0
    print("2500, regular →", discount(2500, "regular"))      # 2125.0
    print("1200, vip     →", discount(1200, "vip"))          # 1200.0 (treated as regular)
