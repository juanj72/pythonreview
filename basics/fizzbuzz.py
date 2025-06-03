# ejercicio basico de progrmaacion
class FizzBuzz:
    def __init__(self):
        pass

    def fizzbuzz(self)->list:

        for i in range(1,101):
            if i % 3 == 0 and i % 5 == 0:
                print(i," FizzBuzz \n")
            if i % 3 == 0:
                print(i," Fizz \n")
            if i % 5 == 0:
                print(i," Buzz \n")
            
            print(i, "\n")
        print("Fin del programa \n")

if __name__ == "__main__":
    fb = FizzBuzz()
    fb.fizzbuzz()
