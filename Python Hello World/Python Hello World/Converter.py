def convert(message):
    wordsList = message.split(' ')
    emojisDictio = {
        ":)": "😊",
        ":(": "😢",
        ":B": "😎",
        ":P": "😜",
        ":O": "😃",
        ":M": "😘",
        ":K": "🙌",
    }
    output = ""
    for word in wordsList:
        output += emojisDictio.get(word, word) + " "
    return output
