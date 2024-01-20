def find_concatenated_words(word: str, word_list: list[str]) -> list[str]:
    result = list()
    for w in word_list:
        if w != word:
            min_len = min(len(word), len(w))
            for i in range(min_len, 0, -1):
                if word.endswith(w[:i]):
                    result.append(word + w[i:])
                    break
    return result


if __name__ == "__main__":
    try:
        with open("./pack_words.txt", "r", encoding="utf-8") as file:
            word_list = [line.strip() for line in file]
        print(f"Choose one word: {' ,'.join(word_list)}")
        input_word = input("Enter word: ")
        res = find_concatenated_words(input_word, word_list)
        if res:
            for w in res:
                print(f"Result: {w}")
        else:
            print("Sorry, cannot find suitable word")
    except FileNotFoundError:
        print("File not found")
    except KeyboardInterrupt:
        print("Bye")
    except Exception as e:
        print(f"Unexpected error: {e}")
