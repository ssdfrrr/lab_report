def fast(path):
    sequence = {}
    with open(path) as fasta:
        ann = None
        seq = []
        for line in fasta:
            line = line.strip()
            if line.startswith('>'):
                if ann is not None:
                    sequence[ann] = ''.join(seq)
                ann = line[1:]
                seq = []
            else:
                seq.append(line)
        if ann is not None:
            sequence[ann] = ''.join(seq)
    return sequence


result = fast("C:/Users/lalin/Downloads/AY883926.fasta")

if result:
    for accession, sequence in result.items():
        print(f"Accession: {accession}\tLength: {len(sequence)}")
        print(f"Sequence:\n{sequence}\n")  
else:
    print("Файл пуст или не содержит последовательностей.")