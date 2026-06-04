text_input = input("Waiting for a word with letter 'h': ")


while "h" not in text_input.lower():
    text_input = input("Waiting for a word with letter 'h': ")


print(f"Word with letter 'h': {text_input}")