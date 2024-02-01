import random

testing_key = 5


def encode(data, key, usablechar):
    result = ""
    chars = list(usablechar)
    length = len(usablechar)

    if isinstance(key,int):
        key = (int(key)**2) % length
    else:
        random.seed(key)
        key = (random.randint(0,length))

    for c in data:
        result += chars[(ord(c) + key) % length]

    return result

def decode(data, key, usablechar):
    result = ""
    chars = list(usablechar)
    length = len(usablechar)

    if isinstance(key,int):
        key = (int(key)**2) % length
    else:
        random.seed(key)
        key = (random.randint(0,length))
    
    for c in data:
        result += chars[((ord(c) - key + length)+31) % length]

    return result

def test(key):
    text = ""
    usablechar = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"

    with open("test_text.txt", 'r') as file:
        text = file.read()

    encoded = encode(text, key, usablechar)
    decoded = decode(encoded, key, usablechar)

    print("Encoded:", encoded)
    print("Decoded:", decoded)

if __name__ == "__main__":
    test(testing_key)
