grammar = [
    ("S", ["P"]),
    ("P", ["(", "P", ")"]),
    ("P", []),
]

tokens = ["(", "(", ")", ")"]

def addtochart(chart, index, state):
    if state not in chart[index]:
        chart[index].append(state)
        return True
    return False

def closure (grammar, i, x, ab, cd):
    next_states = [(rule[0],[],rule[1], i)
                    for rule in grammar
                    if cd != [] and rule[0] == cd[0]]
    return next_states

def shift (tokens, i, x, ab, cd, j):
    if cd != [] and cd[0] == tokens[i]:
        return (x, ab + [cd[0]], cd[1:], j)
    else:
        return None

def reductions(chart, i, x, ab, cd, j):
    return [(state[0], state[1] + [x], state[2][1:], state[3])
            for state in chart[j]
            if cd == []
            if state[2] != [] and state[2][0] == x
            ]

def parse(tokens, grammar):
    tokens = tokens + ["end_of_input_marker"]
    chart = {}
    start_rule = grammar[0]
    for i in range(len(tokens)+1):
        chart[i] = []
    start_state = (start_rule[0], [], start_rule[1], 0)
    chart[0] = [start_state]
    for i in range(len(tokens)):
        while True:
            changes = False
            for state in chart[i]:
                x = state[0]
                ab = state[1]
                cd = state[2]
                j = state[3]

                next_states = closure(grammar, i, x, ab, cd)
                for next_state in next_states:
                    changes = addtochart(chart, i, next_state) or changes

                next_state = shift(tokens, i, x, ab, cd, j)
                if next_state != None:
                    any_changes = addtochart(chart, i+1, next_state) or any_changes

                next_states = reductions(chart, i, x, ab, cd, j)
                for next_state in next_states:
                    changes = addtochart(chart, i, next_state) or changes

            if not changes:
                break

    for i in range(len(tokens)):
        print "== chart " + str(i)
        for state in chart[i]:
            x = state[0]
            ab = state[1]
            cd = state[2]
            j = state[3]
            print " " + x + " ->",
            for sym in ab:
                print " " + sym,
            print " .",
            for sym in cd:
                print " " + sym,
            print " from " + str(j)

    accepting_state = (start_rule[0], start_rule[1], [], 0)
    return accepting_state in chart[len(tokens)-1]

result = parse(tokens, grammar)
print result