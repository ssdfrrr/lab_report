def profmx(dnastr):
    if not dnastr or not dnastr[0]:
        print("Ошибка: Пустой список последовательностей или первая последовательность пустая.")
        return None

    seq_length = len(dnastr[0])
    mx = {
        'A': [0] * seq_length,
        'T': [0] * seq_length,
        'G': [0] * seq_length,
        'C': [0] * seq_length,
    }
    for dna in dnastr:
        if len(dna) != seq_length:
            print("Ошибка: Последовательности разной длины. Ожидаемая длина:", seq_length, "Длина текущей:", len(dna))
            return None
        for i, nuc in enumerate(dna):
            if nuc in mx:
                mx[nuc][i] += 1
            else:
                print("Ошибка: Недопустимый нуклеотид:", nuc)
                return None

    return mx


def findcons(mx):
    if mx is None:
        return None
    cons = ""
    seq_length = len(mx['A'])
    for i in range(seq_length):
        max_count = 0
        maxnuc = ''
        for nuc in ['A', 'T', 'G', 'C']:
            if mx[nuc][i] > max_count:
                max_count = mx[nuc][i]
                maxnuc = nuc
        cons += maxnuc
    return cons


a = "AATCG"
b = "ATGCA"

if a is None or b is None:
    print("Не удалось прочитать один или оба файла. Программа завершена.")
else:
    dnastr = [a, b]
    pr = profmx(dnastr)

    if pr is None:
        print("Не удалось создать матрицу профилей. Программа завершена.")
    else:
        conseq = findcons(pr)
        print("Консенсусная последовательность:", conseq)
        print("Матрица профилей:")
        for nuc in ['A', 'T', 'G', 'C']:
            print(f"{nuc}: {pr[nuc]}")
