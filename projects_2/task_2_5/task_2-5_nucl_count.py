print("\n=== Анализ последовательности ДНК ===")

dna = input("Введите последовательность ДНК: ").upper()
total = len(dna)

a_percent = dna.count("A") / total * 100
t_percent = dna.count("T") / total * 100
g_percent = dna.count("G") / total * 100
c_percent = dna.count("C") / total * 100

print(f"Последовательность в верхнем регистре: {dna}")

print("Подсчёт нуклеотидов: ")
print(f"А: {dna.count("A")}")
print(f"Т: {dna.count("T")}")
print(f"Г: {dna.count("G")}")
print(f"С: {dna.count("C")}")

print(f"Количество нуклеотидов: {total} ")

print("Процентное содержание нуклеотидов в последовательности: ")
print(f"А: {a_percent:.2f}% ")
print(f"Т: {t_percent:.2f}% ")
print(f"Г: {g_percent:.2f}% ")
print(f"С: {c_percent:.2f}% ")