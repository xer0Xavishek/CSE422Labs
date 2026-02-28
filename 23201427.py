import math

def is_terminal(pos):
    return len(pos) == 2

def static_evaluation(pos):
    return sum(pos)

def get_children(pos):
    return [pos[1:], pos[:-1]]

def minmax(pos, maxPlr):
    if is_terminal(pos):
        return static_evaluation(pos)
    if maxPlr:
        maxeval = -math.inf
        for c in get_children(pos):
            eval = minmax(c, False)
            maxeval = max(maxeval, eval)
        return maxeval
    else:
        mineval = math.inf
        for c in get_children(pos):
            eval = minmax(c, True)
            mineval = min(mineval, eval)
        return mineval


n = int(input().strip())
chests = list(map(int, input().strip().split()))
result = minmax(chests, True)
print(f"Alice can gain a maximum of {result} gold coins.")

