class PrimeNumber:
    def __init__(self, number: int):
        self.number = number

    def is_prime(self) -> bool:

        if self.number <= 1:
            return False

        if self.number % self.number == 0 and self.number % 1 == 0:
            for i in range(2, int(self.number**0.5) + 1):
                if self.number % i == 0:
                    return False

            return True


if __name__ == "__main__":
    prompt = input("Enter a number to check if it's prime (or type 'exit' to quit): ")
    while prompt != "exit":
        try:

            if prompt.lower() == "exit":
                break
            number = int(prompt)
            prime_checker = PrimeNumber(number)
            if prime_checker.is_prime():
                print(f"{number} is a prime number.")
            else:
                print(f"{number} is not a prime number.")
            prompt = input(
                "Enter a number to check if it's prime (or type 'exit' to quit): "
            )
        except ValueError:
            print("Please enter a valid integer.")
