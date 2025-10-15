import random


def random_range(_range):
    """ Choose a random number from '_range'. """

    return random.randint(_range[0], _range[len(_range)-1])


def random_choice(_range):
    """ Choose a random number list from '_range'. """

    return random.sample(_range, 6)


def set_solver():
    """ Set the operator to use. """

    _input = input(f"Select a solver in {SOLVER} : ")

    if _input in SOLVER:
        _input = pick_number(_input)

    return _input


def pick_number(_solver):
    """ Select 2 numbers in the available ones with '_solver' operator.

    :param _solver: The operator used.
    :return: Returns the calculated number.
    """

    _n1 = input(f"Select a number in {cards} : ")
    while _n1 not in str(cards):
        _n1 = input(f"Select a number in {cards} : ")
    _n1 = int(_n1)
    cards.pop(cards.index(_n1))

    _n2 = input(f"Select another number in {cards} : ")
    while _n2 not in str(cards):
        _n2 = input(f"Select another number in {cards} : ")
    _n2 = int(_n2)
    cards.pop(cards.index(_n2))

    _new_number = solve_number(_n1, _n2, _solver)
    cards.append(_new_number)

    return _new_number


def solve_number(_n1, _n2, _solver):
    """ Solve between '_n1' and '_n2' with '_solver' operator. """

    _result = 0

    match _solver:
        case "+":
            _result = _n1+_n2
        case "-":
            _result = _n1-_n2
        case "*":
            _result = _n1*_n2
        case "/":
            _result = _n1/_n2

    return _result


NUMBER_RANGE = [101, 999]
CARDS = [x for x in range(1, 11)] * 2 + [25, 50, 75, 100]
SOLVER = ["+", "-", "*", "/"]

reader = ""
cards = random_choice(CARDS)

if __name__ == "__main__":
    number_to_guess = random_range(NUMBER_RANGE)

    while len(cards) != 1:
        set_solver()
        print()
    else:
        print(f"Final result : {cards[0]}")
        print("Correct" if cards[0] == number_to_guess else "False",
              f"Number to guess was : {number_to_guess}.")