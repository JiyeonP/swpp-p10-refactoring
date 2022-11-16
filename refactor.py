def censorWord(word, text):
    # tmp = text
    # while word in tmp:
    #     tmp = tmp[:tmp.find(word)] + "*" * len(word) + tmp[tmp.find(word) + len(word):]
    # return text
    return text.replace(word, "*")

def alertText(text):
    if (text.count("*") > 5):
        print("More than five *")

if __name__ == "__main__":
    text = """Because he's the hero Gotham deserves but not the one it needs right now.
So we will hunt him, because he can take it. Because he's not out hero.
He is a silent guardian, a watchful protector... a dark knight."""

    word1 = "hero"
    word2 = "silent"

    # TODO: 4. Consider general usage
    # TODO: 3. Substitute algorithm

    text = censorWord(word1, text)
    alertText(text)
    text = censorWord(word2, text)
    alertText(text)

    print(text)