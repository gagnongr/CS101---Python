sentence = "Broccoli is delicious."
word = 1
secondWord = ""

for x in sentence:
    if x == " ":
        word += 1
    if word == 2:
        secondWord += secondWord.join([x])

secondWord = secondWord.strip()
