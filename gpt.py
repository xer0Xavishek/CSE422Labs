import math


def minimax(position, depth, alpha, beta, maximizingPlayer):
    if depth == 0 or game_over(position):
        return static_evaluation(position)

    if maximizingPlayer:
        maxEval = -math.inf
        for child in children_of(position):
            eval = minimax(child, depth - 1, alpha, beta, False)
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return maxEval
    else:
        minEval = math.inf
        for child in children_of(position):
            eval = minimax(child, depth - 1, alpha, beta, True)
            minEval = min(minEval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return minEval


# ----- Required helper functions -----
def game_over(position):
    # Game ends if there's only 1 item left or the list is empty
    return len(position) <= 1


def static_evaluation(position):
    # If the list is empty, return 0. Otherwise, return the sum.
    return sum(position) if position else 0


def children_of(position):
    # We must return a LIST of new states. 
    # Let's pretend a move is either removing the first element OR the last element.
    if len(position) > 1:
        return [position[1:], position[:-1]]
    return []


# ----- Initial call example -----

currentPosition = [3, -5, 2, 9]
result = minimax(currentPosition, 3, -math.inf, math.inf, True)
print(f"The best guaranteed outcome for the Maximizer is: {result}")




import math

def minimax(position, depth, maximizingPlayer):
    # Base case: if we've reached the target depth or the game is over
    if depth == 0 or is_terminal(position):
        return static_evaluation(position)

    # Maximizing player's turn
    if maximizingPlayer:
        maxEval = -math.inf
        for child in get_children(position):
            eval = minimax(child, depth - 1, False)
            maxEval = max(maxEval, eval)
        return maxEval
        
    # Minimizing player's turn
    else:
        minEval = math.inf
        for child in get_children(position):
            eval = minimax(child, depth - 1, True)
            minEval = min(minEval, eval)
        return minEval
    

    import math

# 1. Define the Game Tree
# This represents the possible moves. 
# Strings with lists are branches (internal nodes). 
# Strings with integers are the end of the game (leaf nodes).
game_tree = {
    'Root': ['Node B', 'Node C'],
    'Node B': ['Leaf 1', 'Leaf 2'],
    'Node C': ['Leaf 3', 'Leaf 4'],
    'Leaf 1': 3,  # Terminal state worth 3 points
    'Leaf 2': 5,  # Terminal state worth 5 points
    'Leaf 3': 2,  # Terminal state worth 2 points
    'Leaf 4': 9   # Terminal state worth 9 points
}

# 2. Define the Helper Functions
def is_terminal(position):
    # A position is terminal if its value in the dictionary is an integer (a score)
    return isinstance(game_tree[position], int)

def static_evaluation(position):
    # Returns the integer score of the terminal node
    return game_tree[position]

def get_children(position):
    # Returns the list of next possible moves/states from the dictionary
    return game_tree[position]

# 3. The Minimax Algorithm
def minimax(position, depth, maximizingPlayer):
    # Base case: if we've reached the target depth or the game is over
    if depth == 0 or is_terminal(position):
        return static_evaluation(position)

    # Maximizing player's turn
    if maximizingPlayer:
        maxEval = -math.inf
        for child in get_children(position):
            eval = minimax(child, depth - 1, False)
            maxEval = max(maxEval, eval)
        return maxEval
        
    # Minimizing player's turn
    else:
        minEval = math.inf
        for child in get_children(position):
            eval = minimax(child, depth - 1, True)
            minEval = min(minEval, eval)
        return minEval

# 4. The Initial Call
# Start at the 'Root', look 2 levels deep, and the Maximizing player goes first.
best_score = minimax('Root', 2, True)

print(f"The best guaranteed score for the Maximizer is: {best_score}")