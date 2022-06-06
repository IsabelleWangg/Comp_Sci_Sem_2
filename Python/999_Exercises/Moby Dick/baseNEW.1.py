sentence = "whale hello there. Don't we all love whales? I absolutely love whales! whales are so huge!!!"
whale = 0
for x in range(0,len(sentence)):
    a = sentence[x:x+5]
    if a == "whale":
        whale = whale+1
print(str(whale))

whale = 0
with open('moby.txt') as f:
    for line in f:
        sentence = line.strip()
        for x in range(0,len(sentence)):
            a = sentence[x:x+5]
            if a == "whale" or a == "Whale" or a == "WHALE":
                whale = whale+1
#or you can just do sentence[x:x+5].lower()
print(str(whale))
f.close()


