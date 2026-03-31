# B.Tech Grade Predictor Project
# My name is Atharv Khale

print("--- VIT BHOPAL GRADE GOAL SETTER ---")

# First I need to get some information from the user
# The Mid-term grade is out of fifty. It is worth thirty percent of the final grade
mt_raw = float(input("Please enter your Mid-term marks out of fifty: "))

# The Assignments are out of forty. They are worth forty percent of the final grade
assign_raw = float(input("Please enter your total Assignment marks out of forty: "))

# Now lets calculate the grades
# The Mid-term contribution: Mid-term marks divided by fifty then multiplied by thirty
mt_weight = (mt_raw / 50) * 30

# The Assignment contribution is straightforward: it is one to one (40 marks = 40%)
assign_weight = assign_raw

# lets add the Mid-term and Assignment grades to get the current total out of 70
current_total = mt_weight + assign_weight

print("\n--- Current Status ---")
print(f"My Mid-term Contribution is {mt_weight:.2f} out of thirty")
print(f"My Assignment Contribution is {assign_weight:.2f} out of forty")
print(f"My current score out of seventy is {current_total:.2f}")

# Now lets set a goal for the End-Term grade
# The End-Term grade is out of one hundred and it is thirty percent
target = float(input("\nWhat score do I want to get? (Example: 80 for A or 90 for S): "))

# Calculation: (Target - Current) / 0.30
# Fix: Changed the '.' to a '-' from your draft
needed_in_et = (target - current_total) / 0.30

print("\n--- Final Calculation ---")

# Fix: Added proper indentation for the 'if/elif/else' blocks
if needed_in_et > 100:
    print("The result is that it is impossible to get this grade even if I get 100/100 in the End-Term.")
elif needed_in_et <= 0:
    print("The result is that I have already achieved my goal based on the internal grades.")
else:
    print(f"The result is that I need to score {needed_in_et:.2f} out of 100 in the End-Term.")