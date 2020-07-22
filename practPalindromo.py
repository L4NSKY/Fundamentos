word = input("Dame el string: ")
palindrome = True

for i in range(0, len(word), 1):
    if word[i] != word[(len(word)-1) - i]:
        palindrome = False

print("Es un palindromo?", palindrome)

