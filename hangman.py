def read():
    words = []
    with open("./data.txt", "r", encoding="utf-8") as f:
        for line in f:
            words.append(line)
    print(words)

def run():
    read()


if __name__ == '__main__':
    run()