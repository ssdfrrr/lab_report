##Лабораторная 1
a = str(input("первая последовательность: "))
b = str(input("вторая последовательность: "))
a = a.upper()
a = a.upper()

s = 0
if len(a)!= len(b):
    print("Последовательности отличаются по длине")
elif len(a) > 10:
    print("Можно последовательности поскромнее?")
else:
    mt = []
    dif = []
    for i in  range(len(a)):
        if a[i] == b[i]:
            mt.append((i, a[i]))
        else:
            dif.append((i, a[i], b[i]))
            s += 1
aset = set(a)
bset = set(b)
с = aset.intersection(bset)
d = aset.symmetric_difference(bset)


print("Позиции совпадающих нуклеотидов: ", mt)
print("Позиции отличающихся нуклеотидов", dif)
print("Совпадающие части последовательностей: ", с)
print("Отличающиеся части последовательностей", d)
print("Число Хэмминга равно ", s)
