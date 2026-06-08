# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    multiplier = 1

    while True:
        result = number * multiplier
        if  result > 25:
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        multiplier += 1

multiplication_table(3)


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""

def sum_2_numbers(value1: int | float, value2: int | float):
    return value1 + value2


print(sum_2_numbers(10,15.5))


# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""


lst = [1, 2, 3, 4, 5,6,80,26]





def avg_value(lst):
    sum_numbers = 0
    avg_value = 0  
    for number in lst:
             
        sum_numbers += number
    avg_value = sum_numbers / len(lst)
    return avg_value


print(avg_value(lst))



# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""

text = input("Please enter your sentence: ")



def text_reverse(text):
    
    reverse_text = text[: :-1]

    return reverse_text


print(text_reverse(text))



# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""


lst = []

num_words = int(input("Please enter num of words you want to add: "))

while len(lst) != num_words:
    words = input("Please enter your word: ")
    lst.append(words)

def longest_word(lst):
    return max(lst, key=len) 


print(longest_word(lst))



# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    return str1.find(str2)

    


str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1


# task 7
user_text = input("Введите вашу строку: ")



def num_uniques_symb(user_text):
    """
    Func count num of unique symbols
    If num is greater than 10 we return true otherwise false
    """
    user_text_set = set(user_text)
    user_text_set_length = len(user_text_set)


    if user_text_set_length > 10:
        return True
    else:
        return False
    

print(num_uniques_symb(user_text))

# task 8
list_value = list(range(100))


def sum_even_numb(list_value):
    """
    We already have a list of numbers
    Now we need to calculate sum of all even numbers in the list
    And print it
    """
    total = 0
    for item in list_value:
        if item % 2 == 0:
            total += item
    return f"Сумма всех четных чисел: {total}"
    


print(sum_even_numb(list_value))






# task 9
text_input = input("Waiting for a word with letter 'h': ")


def find_h_letter(text_input):
    """
    We are waiting for user to enter a word with letter 'h'
    And our cycle will not finish until user will do it
    """
    while "h" not in text_input.lower():
        text_input = input("Waiting for a word with letter 'h': ")
    return f"Word with letter 'h': {text_input}"


print(find_h_letter(text_input))

# task 10
lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']

lst2 = []


def list_type_str(lst1):
    """
    We have a list1 with different type values and we need 
    To create a list2 that contains only str type values from list1
    """
    for items in lst1:
        if type(items) == str:
            lst2.append(items)
    return f"List with type str: {lst2}" 


print(list_type_str(lst1))