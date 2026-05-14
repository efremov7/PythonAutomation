alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don\'t much care where ——" said Alice.\n"Then it doesn\'t matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'

# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних ліній
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк

print(alice_in_wonderland)

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""

black_sea_area = 436402
azov_sea_area = 37800
total_area = black_sea_area + azov_sea_area
print(f"Площа Чорного та Азовського морів разом: {total_area} км2")


# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""

total_goods = 375291
goods_in_first_and_second_warehouse = 250449
goods_in_second_and_third_warehouse = 222950

goods_in_third_warehouse = total_goods - goods_in_first_and_second_warehouse
goods_in_first_warehouse = total_goods - goods_in_second_and_third_warehouse
goods_in_second_warehouse = total_goods - goods_in_first_warehouse - goods_in_third_warehouse

print(f"Кількість товарів на першому складі: {goods_in_first_warehouse}")
print(f"Кількість товарів на другому складі: {goods_in_second_warehouse}")
print(f"Кількість товарів на третьому складі: {goods_in_third_warehouse}")



# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""

credit_length_months = 18
monthly_payment = 1179
computer_cost = credit_length_months * monthly_payment
print(f"Вартість комп'ютера: {computer_cost} грн")


# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
def remainder(a, b):
    return a % b

print(f"Остача від ділення 8019 на 8: {remainder(8019, 8)}")
print(f"Остача від ділення 9907 на 9: {remainder(9907, 9)}")
print(f"Остача від ділення 2789 на 5: {remainder(2789, 5)}")
print(f"Остача від ділення 7248 на 6: {remainder(7248, 6)}")
print(f"Остача від ділення 7128 на 5: {remainder(7128, 5)}")
print(f"Остача від ділення 19224 на 9: {remainder(19224, 9)}")


# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""

big_pizza_price = 274
medium_pizza_price = 218    
juice_price = 35
cake_price = 350
water_price = 21

big_pizza_total = big_pizza_price * 4
medium_pizza_total = medium_pizza_price * 2
juice_total = juice_price * 4
cake_total = cake_price * 1
water_total = water_price * 3

total_cost = big_pizza_total + medium_pizza_total + juice_total + cake_total + water_total
print(f"Загальна вартість замовлення: {total_cost} грн")



# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""

total_photos = 232
photos_per_page = 8
pages_needed = total_photos // photos_per_page
if total_photos % photos_per_page != 0:
    pages_needed += 1

print(f"Ігорю знадобиться {pages_needed} сторінок, щоб вклеїти всі фото.")

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""


total_distance_km = 1600
fuel_consumption_per_100km = 9
fuel_tank_capacity = 48
total_fuel_needed = (total_distance_km / 100) * fuel_consumption_per_100km
refills_needed = total_fuel_needed / fuel_tank_capacity

print(f"Для подорожі знадобиться {int(total_fuel_needed)} літрів бензину.")
print(f"Родині необхідно заїхати на заправку щонайменше {int(refills_needed)} разів.")