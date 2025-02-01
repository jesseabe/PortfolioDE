import random
import time

def random_number():
    return random.randint(1,10)

def double_number(num):
    return num *2

if __name__ == "__main__":
    while True:
        num = random_number()
        result = double_number(num)
        print(f"O dobro de {num} é {result}")
        time.sleep(3)
