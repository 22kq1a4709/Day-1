 #count the frequency of each charcter in string
s = input("Enter a string: ")
 for ch in set(s):
print(f"{ch}: {s.count(ch)}")
