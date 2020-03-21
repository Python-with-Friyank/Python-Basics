print(" Enter your message")
message = input("> ")
wordsList = message.split(' ')
emojisDict = {
    ":)" : "😊",
    ":(" : "😢",
    ":B" : "😎",
    ":P" : "😜",
    ":O" : "😃",
    ":M" : "😘",
    ":K" : "🙌",
}
output = ""
for word in wordsList:
    output += emojisDict.get(word,word) + " "
print(output)