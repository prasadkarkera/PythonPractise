dictionary = {"mobile" : "1",
              "samsung": "1",
              "sam": "1",
              "sung": "1",
              "man": "1",
              "mango": "1",
              "icecream": "1",
              "and": "1",
              "go": "1",
              "i": "1",
              "like": "1",
              "ice": "1",
              "cream": "1"}

def word_break(string):

    length = len(string)

    if length == 0:
        return True
    for i in range(1, len(string) + 1):
        if dictionary.get(string[0:i]) and word_break(string[i:length]):
            return True

    return False


print(word_break('ilikesamsung'))
print(word_break('ilikelikeimangoiii'))


