weight = float(input("Введите ваш вес (кг): "))
height = float(input("Введите ваш рост (см): "))

bmi = weight / ((height / 100) ** 2)

print("\n--- Отчет о состоянии здоровья ---")
print(f"Рост:\t{height:.1f} см")
print(f"Вес:\t{weight:.1f} кг")
print(f"Индекс массы тела:\t{bmi:.2f}")