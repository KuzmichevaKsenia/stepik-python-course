old_alphabet = input()
new_alphabet = input()
str_to_encode = input()
str_to_decode = input()
encoded_str = ""
decoded_str = ""
for i in range(len(str_to_encode)):
    encoded_str += new_alphabet[old_alphabet.index(str_to_encode[i])]
for i in range(len(str_to_decode)):
    decoded_str += old_alphabet[new_alphabet.index(str_to_decode[i])]
print(encoded_str)
print(decoded_str)
