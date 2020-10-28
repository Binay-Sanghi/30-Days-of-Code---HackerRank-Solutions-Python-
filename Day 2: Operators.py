meal_cost = float(input())
tip_percent = int(input())
tax_percent = int(input())
final_cost = meal_cost + ((tip_percent + tax_percent) * meal_cost) / 100
print(round(final_cost))
