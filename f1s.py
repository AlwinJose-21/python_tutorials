with open('wiki','r') as file:
    text=file.read()
words = text.split()
dict={}
for word in words:
    word = word.strip('.,!?"').lower()

    if word in dict:
        dict[word]+=1
    else:
        dict[word]=1
for word, count in dict.items():
    print(f"{word}:{count}")
word_count=len(words)
print("Number of words",word_count)