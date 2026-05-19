

adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

string_adv_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")
print(string_adv_tom_sawer)


# task 02 ==
""" Замініть .... на пробіл
"""



string_2 = string_adv_tom_sawer.replace("....", " ")
print(string_2)


# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""


adv_tom_sawer = string_2.split()

join_adv_tom_sawer = ' '.join(adv_tom_sawer)
print(join_adv_tom_sawer)


# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""

letter_h_count = 0

for i in join_adv_tom_sawer:
    if i == "h":
        letter_h_count += 1
print(f"Number of letter h: {letter_h_count}")
   

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
num_upper_case_words = 0

for i in join_adv_tom_sawer:
    if i.istitle():
        num_upper_case_words += 1
print(f"Number of upper case words: {num_upper_case_words}")
   


# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""

index = join_adv_tom_sawer.find("Tom",1)
if index != -1:
    print(f"Знайдено на позиції {index}.")
else:
    print("Підстрічка не знайдена.")



# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = join_adv_tom_sawer.split(". ")

print(adwentures_of_tom_sawer_sentences)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
print(adwentures_of_tom_sawer_sentences[3].lower())

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
for i, sentence in enumerate(adwentures_of_tom_sawer_sentences):
    if sentence.startswith("By the time"):
        print(f"Номер: {i}\nРечення: {sentence}")

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""

words_sentence_num_4 = adwentures_of_tom_sawer_sentences[-1].split()
print(len(words_sentence_num_4))