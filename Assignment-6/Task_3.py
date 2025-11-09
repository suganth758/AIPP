def classify_age(age):
  """Classifies age into different groups using nested if-elif-else."""
  if age < 0:
    return "Invalid age"
  elif age < 13:
    return "Child"
  elif age < 20:
    return "Teenager"
  else:
    if age < 65:
      return "Adult"
    else:
      return "Senior"
    # Example usage:
print(f"Age 5: {classify_age(5)}")
print(f"Age 15: {classify_age(15)}")
print(f"Age 30: {classify_age(30)}")
print(f"Age 70: {classify_age(70)}")