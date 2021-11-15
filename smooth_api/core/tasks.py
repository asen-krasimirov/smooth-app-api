import random


def generate_token(length):
    sample_string = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    return ''.join((random.choice(sample_string)) for _ in range(length))
