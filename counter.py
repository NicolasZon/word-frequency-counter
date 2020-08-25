import sys


def counting_words(text: str) -> None:

    characters = len(text) - text.count("\n")
    text = text.split()
    total_words = len(text)

    print(total_words, "words")
    print(characters, "characters\n")

    words = {}

    for word in text:
        words[word] = words.get(word, 0) + 1

    for k, v in sorted(words.items(), key=lambda item: item[1], reverse=True):
        print(k+":", v)


def read_file(file: str) -> str:
    print("Reading", file + "...\n")
    try:
        f = open(file, "r")
        return f.read()
    except:
        print("File", file, "NOT found")
        return ""


args = sys.argv[1:]

if not len(args):
    args.append("input")

for file in args:
    counting_words(read_file(file))
    print("\n---")
