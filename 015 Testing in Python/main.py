from multiprocessing.sharedctypes import Value


def addition(a, b):
    return a+b


def guess_number(answer, guess):
    try:
        int(guess)
        if 0 < guess < 11:
            if guess == answer:
                return True
            else:
                return False

        else:
            return False

    except ValueError:
        return ValueError
