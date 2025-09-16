def capitalize(paragraph):
    if not paragraph:
        return ""

    result = list(paragraph)  # Converte a string para uma lista de caracteres para facilitar a modificação
    capitalize_next = True

    for i in range(len(result)):
        char = result[i]

        # Verifica se o caractere atual é uma letra
        is_letter = ('a' <= char <= 'z') or ('A' <= char <= 'Z')

        if capitalize_next and is_letter:
            result[i] = char.upper()
            capitalize_next = False
        elif char in '.?!':
            capitalize_next = True

    return "".join(result) # Junta a lista de caracteres de volta em uma string

    print(capitalize("this is a simple sentence."))
# Saída: This is a simple sentence.

print(capitalize("hello world. how are you?"))
# Saída: Hello world. How are you?

print(capitalize("i did today's coding challenge... it was fun!!"))
# Saída: I did today's coding challenge... It was fun!!

print(capitalize("crazy!!!strange???unconventional...sentences."))
# Saída: Crazy!!!Strange???Unconventional...Sentences.

print(capitalize("there's a space before this period . why is there a space before that period ?"))
# Saída: There's a space before this period . Why is there a space before that period ?


