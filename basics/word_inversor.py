class WordInversor():
    def __init__(self, word: str):
        self.word = word


    def inverse_word(self) ->str:
        list_word = list(self.word)
        new_word = ""
        for i in range(len(list_word), 0, -1):
            new_word += list_word[i-1]
        return new_word
    

if __name__ == "__main__":
    prompt = input("Enter a word to inverse (or type 'exit' to quit): ")
    while prompt.lower() != "exit":
        inversor = WordInversor(prompt)
        inverted_word = inversor.inverse_word()
        print(f"The inverted word is: {inverted_word}")
        prompt = input("Enter a word to inverse (or type 'exit' to quit): ")