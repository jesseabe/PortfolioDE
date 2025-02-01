import random
import time

def random_number():
    num = random.randint(1,10)
    print(num)
    with open('numeros.txt', 'a') as file:
        file.write(f"{num}\n")


if __name__ == "__main__":
    while True:
        random_number()
        time.sleep(5)