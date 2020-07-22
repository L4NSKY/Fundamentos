word = input("Dame el string: ")
newString = ""

for i in range(len(word) -1, -1, -1):
    newString += word[i]

print(newString)