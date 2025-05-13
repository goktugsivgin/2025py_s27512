# s27512_2025.py
# This script generates a random DNA sequence and saves it in FASTA format.
# The user provides sequence length, ID, description, and name (which is inserted in the sequence).
# The script also calculates and displays nucleotide statistics.

import random
import re

# Get input from user
length = int(input("Enter the sequence length: "))
seq_id = input("Enter the sequence ID: ")
description = input("Provide a description of the sequence: ")
name = input("Enter your name: ")

# Generate random DNA sequence
nucleotides = ['A', 'C', 'G', 'T']

# ORIGINAL:
# sequence = ''.join(random.choices(nucleotides, k=length))
# MODIFIED (adds potential for weights in future if needed):
sequence = ''.join(random.choices(nucleotides, weights=[1, 1, 1, 1], k=length))

# Insert name into sequence (name doesn't count towards stats)
insert_pos = random.randint(0, length)
sequence_with_name = sequence[:insert_pos] + name + sequence[insert_pos:]

# Save to FASTA file
# ORIGINAL:
# filename = f"{seq_id}.fasta"
# MODIFIED (in case of special characters in ID):
seq_id_clean = re.sub(r'[^A-Za-z0-9_\-]', '_', seq_id)
filename = f"{seq_id_clean}.fasta"

with open(filename, "w") as f:
    f.write(f">{seq_id} {description}\n")
    # ORIGINAL:
    # f.write(sequence_with_name + "\n")
    # MODIFIED (formats the sequence in 60-char lines like standard FASTA):
    f.write('\n'.join([sequence_with_name[i:i+60] for i in range(0, len(sequence_with_name), 60)]) + '\n')

print(f"\nThe sequence was saved to the file {filename}")

# Calculate statistics (exclude name)
a = sequence.count('A')
c = sequence.count('C')
g = sequence.count('G')
t = sequence.count('T')

total = length
a_pct = (a / total) * 100
c_pct = (c / total) * 100
g_pct = (g / total) * 100
t_pct = (t / total) * 100
cg_pct = ((c + g) / total) * 100

print("Sequence statistics:")
print(f"A: {a_pct:.1f}%")
print(f"C: {c_pct:.1f}%")
print(f"G: {g_pct:.1f}%")
print(f"T: {t_pct:.1f}%")
print(f"%CG: {cg_pct:.1f}")
