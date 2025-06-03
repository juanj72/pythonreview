class VocableCount:

    VOCABLES = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

    def __init__(self, vocable: str):
        self.vocable = vocable

    def count_vocables(self) -> int:
        count = 0
        vocables_list = list(self.vocable)
        for char in vocables_list:
            if char in self.VOCABLES:
                count += 1
        return count


if __name__ == "__main__":
    prompt = input(
        "Enter a string to count the number of vocables (or type 'exit' to quit): "
    )
    while prompt.lower() != "exit":
        vocable_counter = VocableCount(prompt)
        count = vocable_counter.count_vocables()
        print(f"The number of vocables in '{prompt}' is: {count}")
        prompt = input(
            "Enter a string to count the number of vocables (or type 'exit' to quit): "
        )
