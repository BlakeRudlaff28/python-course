
# Self-Assessment
# 1. I found bugs by checking the code and looking at errors.
# Print statements helped me understand what the variables were doing.
# 2. apply_discount(price, tier) takes a price and a membership tier,
# applies the correct discount, and returns the discounted price.
# 3. AI disclosure: I used ChatGPT to help write and understand Python functions.

# --- Exercise 1 ---
def calculate_tax(price, rate):
    return price * rate

print(f"Tax on $100 at 7%: ${calculate_tax(100, 0.07):.2f}")
print(f"Tax on $250 at 8%: ${calculate_tax(250, 0.08):.2f}")

# --- Exercise 2 ---
def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price

for tier in ["gold", "silver", "bronze", "none"]:
    print(f"{tier}: ${apply_discount(200, tier):.2f}")

# --- Exercise 3 ---
def final_price(price, tier, tax_rate):
    discounted_price = apply_discount(price, tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax

discounted = apply_discount(200, "gold")
print(f"After gold discount: ${discounted:.2f}")

taxed = discounted + calculate_tax(discounted, 0.07)
print(f"After tax: ${taxed:.2f}")

print(f'final_price(200, "gold", 0.07) = ${final_price(200, "gold", 0.07):.2f}')

# --- Exercise 4 ---
orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]

for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")

# --- Exercise 5 ---
sales = [120, 80, 250, 175, 90]

# Bug 1 fix: Add each sale to the total instead of replacing the total.
total = 0
for sale in sales:
    total += sale

print(f"Total: ${total}")

# Bug 2 fix: Add a colon after the for loop.
count = 0
for sale in sales:
    count += 1

print(f"Count: {count}")

# Bug 3 fix: Use < instead of <= to avoid going past the list's last index.
i = 0
while i < len(sales):
    print(sales[i])
    i += 1

# --- Exercise 6 ---
x = 100  # Global variable

def double_it():
    x = 999  # Local variable
    return x * 2

print(x)  # Prints 100
print(double_it())  # Prints 1998
print(x)  # Prints 100

# Scope determines where a variable can be accessed.
# The local x inside double_it() is separate from the global x,
# so changing the local variable does not change the global variable.
