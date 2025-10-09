#6.	Annotating the sequence 
dna = 'atgcgatgcgatgcg'
exons = [(2,5), (10,12)]

dna_lower = list(dna.lower())

for start, end in exons:
    for i in range(start, end):
        dna_lower[i] = dna_lower[i].upper()

modified_dna = ''.join(dna_lower)

print("The modified DNA sequence is", modified_dna) 


#7.Counting how many times each nucleotide (A,T,G,C) occurs in the DNA string.
dna = 'atgcgatgcgatgcg'
counts = {nuc: dna.upper().count(nuc) for nuc in 'ATGC'}

print(counts)


#8.Reversing a DNA sequence and printing it.
dna = 'atgcgatgcgatgcg'
print(dna[::-1])



