reagent_name = input("Введите название реагента: ")
amount_of_reagent = input("Введите количество поступившего реагента: ")

result = f"Реактив {reagent_name} поступил на склад в количестве {amount_of_reagent} шт."

print(result)

with open('inventory.txt', 'a', encoding='utf-8') as file:
    file.write(result + '\n')