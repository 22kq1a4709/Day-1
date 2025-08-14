 #count the frequency of each charcter in string
text = input("Enter a string: ")
for char in text:
    if text.count(char) > 0:
        print(char, ":", text.count(char))
        text = text.replace(char, "")
