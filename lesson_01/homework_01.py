# task 01 == Виправте синтаксичні помилки
print("Hello", end = " ")
print("world!")


# task 02 == Виправте синтаксичні помилки
hello = "Hello"
world = "world"
if True:
    print(f"{hello} {world}!")

# task 03  == Вcтавте пропущену змінну у ф-цію print
for letter in "Hello world!":
    print(letter)

# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
apples = 2
banana = apples * 4
print(f"У мене є {apples} яблук та {banana} банан")

# task 05 == виправте назви змінних
storona_1 = 1
storona_2 = 2
сторона_3 = 3
storona_4 = 4



# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
storona_1 = 1
storona_2 = 2
storona_3 = 3
storona_4 = 4

perimetery = storona_1 + storona_2 + storona_3 + storona_4
print(f"Периметр фігури: {perimetery}")


# task 07
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""
apples = 4
pears = apples + 5
plums = apples + 5 - 2
total_trees = apples + pears + plums
print(f"У саду посадили {total_trees} дерев")

# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""
temperature_before_lunch = 5
temperature_after_lunch = temperature_before_lunch - 10
temperature_in_the_evening = temperature_after_lunch + 4
print(f"Температура надвечір: {temperature_in_the_evening} градусів")

# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""
boys = 24
girls = boys // 2
total_children = boys + girls - 1 - 2
print(f"Сьогодні у театральному гуртку {total_children} дітей")

# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""
book_1 = 8
book_2 = book_1 + 2
book_3 = (book_1 + book_2) / 2
total_cost = book_1 + book_2 + book_3
print(f"Загальна вартість книг: {total_cost} грн.")