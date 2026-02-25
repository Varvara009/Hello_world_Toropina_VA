proteins = float(input("Введите массу белков (в граммах): "))
fats = float(input("Введите массу жиров (в граммах): "))
carbs = float(input("Введите массу углеводов (в граммах): "))

calories = (proteins * 4) + (fats * 9) + (carbs * 4)

print(f"\nКалорийность продукта: {calories} ккал")