import random


def shuffle(string):
    templist = list(string)
    random.shuffle(templist)
    return "".join(templist)


def gen():
    capitals = ""
    digits = ""
    chars = ""
    lowers = ""
    nums = ""
    while len(capitals) < 10:
        capitals = capitals + chr(random.randint(65, 90))

    while len(digits) < 10:
        digits = digits + chr(random.randint(33, 64))

    while len(chars) < 10:
        chars = chars + chr(random.randint(91, 96))

    while len(lowers) < 10:
        lowers = lowers + chr(random.randint(97, 122))

    while len(nums) < 10:
        nums = nums + chr(random.randint(48, 57))

    long = capitals + digits + chars + lowers + nums
    long = shuffle(long)
    long = long[:15]
    return long

gen()