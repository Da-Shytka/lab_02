N = int(input("Введите число: "))

mas = [i for i in range(N + 1)]
mas[1] = 0
i = 2

while i <= N:
    if mas[i] != 0:
        j = i + i
        while j <= N:
            mas[j] = 0
            j = j + i
    i += 1
mas = [i for i in mas if i != 0]

print(mas)