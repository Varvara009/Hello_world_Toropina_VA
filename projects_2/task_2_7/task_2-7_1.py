files = ["seq1", "seq2", "seq3", "seq4"]
date = ["27.02.2025","13.12.2024","15.03.2026","04.05.1998"]
for name in files:
   for day in date:
    new_name = name + "_" + day + ".fasta"
    print(f"{new_name}")