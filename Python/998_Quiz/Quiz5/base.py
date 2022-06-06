sent = input("What is your favorite number? (Please answer in a complete sentence): ")
age = input("How old are you? ")
for x in range(0,len(sent)-22):
    a = x+23
    num = sent[22:a]
print(int(num)*int(age))