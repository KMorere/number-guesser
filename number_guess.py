import random


def random_range(_range):
    """ Choose a random number from '_range'. """

    return random.randint(_range[0], _range[len(_range)-1])


def set_solver():
    """ Set the operator to use. """

    _input = set_input(f"Select a solver in {SOLVER} : ")

    if _input in SOLVER:
        _input = pick_number(_input)

    return _input


def pick_number(_solver):
    """ Select 2 numbers in the available ones with '_solver' operator.

    :param _solver: The operator used.
    :return: Returns the calculated number.
    """

    _n1 = set_input(f"Select a number in {cards} : ")
    while _n1 not in str(cards):
        _n1 = set_input(f"Select a number in {cards} : ")
    _n1 = int(_n1)
    cards.pop(cards.index(_n1))

    _n2 = set_input(f"Select another number in {cards} : ")
    while _n2 not in str(cards):
        _n2 = set_input(f"Select another number in {cards} : ")
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
            _result = add(_n1, _n2)
        case "-":
            _result = sub(_n1, _n2)
        case "*":
            _result = multiply(_n1, _n2)
        case "/":
            _result = divide(_n1, _n2)

    return abs(_result)


def solve_ai():
    """ Use numbers randomly. """
    global cards

    _n1 = random.choice(cards)
    cards.pop(cards.index(_n1))

    _n2 = random.choice(cards)
    cards.pop(cards.index(_n2))

    _solver = random.choice(SOLVER)

    _new_number = solve_number(_n1, _n2, _solver)
    cards.append(_new_number)

    return _new_number


def set_input(_text):
    """ Used to set input and check if the user wants to end. """
    _input = input(_text)

    if _input == "stop":
        cards.clear()
        cards.append(0)

    return _input


def init_game():
    """ Initialize the start of the game. """
    global NUMBER_TO_GUESS
    NUMBER_TO_GUESS = random_range(NUMBER_RANGE)

    global CARDS
    CARDS = [x for x in range(1, 11)] * 2 + [25, 50, 75, 100]

    global cards
    cards = random.sample(CARDS, 6)

    print("-----[Guess the number using the cards, type 'stop' to end the program !]-----\n")

    return set_mode()


def set_mode():
    """ Set the mode between user guess or AI guess. """
    _mode = ""

    while _mode not in MODES and _mode != "stop":
        _mode = set_input(f"Select mode {MODES} : ")

    return _mode.lower()


def end_game():
    """ Display end results. """

    if cards[0] == NUMBER_TO_GUESS:
        print(f"Final result : {cards[0]}")
        print(f"Spot on !")
    else:
        print(f"Final result : {cards[0]}")
        print(f"You are {abs(cards[0] - NUMBER_TO_GUESS)} away.")

    cards.clear()


add = lambda x,y:x+y
sub = lambda x,y:x-y
multiply = lambda x,y:x*y
divide = lambda x,y:x//y


NUMBER_RANGE = [101, 999]
NUMBER_TO_GUESS = random_range(NUMBER_RANGE)
CARDS = [x for x in range(1, 11)] * 2 + [25, 50, 75, 100]
SOLVER = ["+", "-", "*", "/"]
MODES = ["guess", "solve"]

reader = ""
cards = random.sample(CARDS, 6)

if __name__ == "__main__":
    mode = init_game()

    while len(cards) > 1:
        print(f"Number to guess is : [{NUMBER_TO_GUESS}]")
        print(f"Cards : {cards}")

        if mode == MODES[0]:
            print(set_solver())
        else:
            print(solve_ai())
    else:
        end_game()