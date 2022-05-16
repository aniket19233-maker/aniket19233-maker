seqList = ['ATCCGTTGAAGCCGCGGGC','TTAACTCGAGG','TTAAGTACTGCCCG','ATCTGTGTCGGG','CGACTCCCGACACA','CACAGATCCGTTGAAGCCGCGGG','CTCGAGTTAAGTA','CGCGGGCAGTACTT']
n = len(seqList[0])
profile = { 'T':[0]*n,'G':[0]*n ,'C':[0]*n,'A':[0]*n }

for seq in seqList:

    for i, char in enumerate(seq):
        profile[char][i] += 1

consensus = ""
for i in range(n):
    max_count = 0
    max_nt = 'x'
    for nt in "ACGT":
        if profile[nt][i] > max_count:
            max_count = profile[nt][i]
            max_nt = nt
    consensus += max_nt
print(consensus)
for key, value in profile.items():
     print(key,':', " ".join([str(x) for x in value] ))
'''
bestseqs = [[]]
for i in range(n):
    d = {N:profile[N][i] for N in ['T','G','C','A']}
    m = max(d.values())
    l = [N for N in ['T','G','C','A'] if d[N] == m]
    bestseqs = [ s+[N] for N in l for s in bestseqs ]

for s in bestseqs:
    print(''.join(s))
    '''
        
