 #count the frequency of each charcter in string
text = input("Enter a string: ")
for char in text:
    if text.count(char) > 0:
        print(char, ":", text.count(char))
        text = text.replace(char, "")



#sample output
Enter a string: ramsita
r : 1
a : 2
m : 1
s : 1
i : 1
t : 1
