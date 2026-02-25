nutrient_medium_name = input("Введите название питательной среды: ")
agar_concentration = input("Введите концентрацию агара (%): ")
sterilization_temperature = input("Введите температуру стерилизации: ")

with open('recipe.txt', 'w',  encoding='utf-8') as recipe:
    recipe.write(f"{nutrient_medium_name}\n\nКонцентрация агара (%):\t\t{agar_concentration}\nТемпература стерилизации:\t{sterilization_temperature}")

print("Файл 'recipe.txt' успешно сформирован!")