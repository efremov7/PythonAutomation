list_value = list(range(10))
total = 0


for item in list_value:
    if item % 2 == 0:
        total += item


print(f"Сумма всех четных чисел: {total}")

