user_text = input("Введите вашу строку: ")

user_text_set = set(user_text)

user_text_set_length = len(user_text_set)

if user_text_set_length > 10:
    print(True) 
else:
    print(False)


