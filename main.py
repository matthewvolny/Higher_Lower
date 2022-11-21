from art import logo, vs
from data import data
import random

print(logo)

def shuffle_data():
    for i in range(len(data)):
        rand_index = random.randint(0, len(data) - 1)
        temp = data[rand_index]
        data[rand_index] = data[i]
        data[i] = temp

shuffle_data()

