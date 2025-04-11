# задание на время пробега
c = 0
s = 0
try:
        while True:
            c += 1
            run = float(input("Введите время пробега: "))
            s += run
            avt = f"Среднее время пробега равно {s / c:.2f}"
except ValueError:
    print(avt)
