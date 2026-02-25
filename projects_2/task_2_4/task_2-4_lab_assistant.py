volume = int(input("Нужный объем (мл): "))
mass = volume * 0.009
main = "отсчет по приготовлению:".upper()

with open("recipe.txt", "w", encoding="utf-8") as recipe:
    print(main, file = recipe)
    print("-" * len(main), file = recipe)
    print(f"Общий объем: {volume} мл", file = recipe)
    print(f"Масса соли: {mass:.2f} г", file = recipe)
    print(f"Общий воды: {volume} мл", file = recipe)