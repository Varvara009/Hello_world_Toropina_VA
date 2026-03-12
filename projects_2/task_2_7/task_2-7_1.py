files = ["seq1", "seq2", "seq3", "seq4"]
date = ["27.02.2025","13.12.2024","15.03.2026","04.05.1998"]
for i in range(len(files)):
    new_name = files[i] + "_" + date[i] + ".fasta"
   
    print(new_name)
