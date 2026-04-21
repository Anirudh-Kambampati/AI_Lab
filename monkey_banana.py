class State:
    def __init__(self, monkey, box, banana):
        self.monkey = monkey
        self.box = box
        self.banana = banana

    def __str__(self):
        return f"Monkey:{self.monkey}, Box:{self.box}, Banana:{self.banana}"

def push_box(state):
    if not state.box and not state.monkey:
        return State(state.monkey, True, state.banana)
    return state

def climb_box(state):
    if state.box and not state.monkey:
        return State(True, state.box, state.banana)
    return state

def grab_banana(state):
    if state.monkey and state.banana:
        print("Banana grabbed!")
        return State(state.monkey, state.box, True)
    return state

def run():
    state = State(False, False, False)
    print("Initial:", state)

    state = push_box(state)
    print("After push:", state)

    state = climb_box(state)
    print("After climb:", state)

    state = grab_banana(state)

run()