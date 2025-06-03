class SumCadenceNumbers:
    NUMBERS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    def __init__(self, cadence: str):
        self.cadence = cadence

    def sum_cadence_numbers(self):
        list_numbers = list(self.cadence)

        for i in range(len(list_numbers)):
            if list_numbers[i] not in [str(num) for num in self.NUMBERS]:
                raise ValueError(
                    f"Invalid character '{list_numbers[i]}' in cadence. Only digits 0-9 are allowed."
                )
        return sum(int(num) for num in list_numbers)


if __name__ == "__main__":
    prompt = input("Enter a cadence of numbers (or type 'exit' to quit): ")
    while prompt.lower() != "exit":
        try:
            cadence_sum = SumCadenceNumbers(prompt)
            total = cadence_sum.sum_cadence_numbers()
            print(f"The sum of the numbers in the cadence '{prompt}' is: {total}")
        except ValueError as e:
            print(e)
        prompt = input("Enter a cadence of numbers (or type 'exit' to quit): ")
