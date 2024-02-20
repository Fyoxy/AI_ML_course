import random

class NQPosition:

    def __init__(self, N):
        # choose some internal representation of the NxN board
        # put queens on it
        self.N = N # size of the board
        self.board = [0] * N
        
        # place queens on board randomly
        for i in range(N):
            self.board[i] = random.randint(0, N-1)
    
    def value(self):
        # calculate number of conflicts (queens that can capture each other)
        value = 0
        
        # loop through all the queens
        for i in range(self.N):
            for j in range(i + 1, self.N):
                # checking if queens in same row or diagonal
                if self.board[i] == self.board[j] or abs(self.board[i] - self.board[j]) == abs(i - j):
                    value += 1
                    
        return value

    def make_move(self, move):
        # actually execute a move (change the board)
        i, j = move
        self.board[i] = j
        
    def best_move(self):
        # find the best move and the value function after making that move
        move = None
        value = self.value()
        
        # loooping through all possible moves
        for col in range(self.N):
            for row in range(self.N):
                if self.board[col] != row:
                    temp_val = self.board[col]
                    self.board[col] = row
                    new_val = self.value()
                    
                    if (temp_val < value):
                        move = (col, row)
                        value = new_val
                        
                    self.board[col] = temp_val
                    
        return move, value
            
def hill_climbing(pos):
    curr_value = pos.value()
    while True:
        move, new_value = pos.best_move()
        if new_value >= curr_value:
            # no improvement, give up
            return pos, curr_value
        else:
            # position improves, keep searching
            curr_value = new_value
            pos.make_move(move)


def print_board(pos):
    # loop trough all rows of the board
    for row in range(pos.N):
        line = ""
        for col in range(pos.N):
            if (pos.board[col] == row):
                line += "Q "
            else:
                line += ". "
                
        print(line)
        

def run_statistics(N, amount):
    solved = 0
    
    for i in range(amount):
        pos = NQPosition(N)
        best_pos, best_value = hill_climbing(pos)
        
        if (best_value == 0):
            solved += 1
    
    print(f"Board size of: {N}\nAmount of times ran: {amount}")
    print(f"Solved amount {solved}/{amount} -> {solved/amount * 100:.2f}%\n")
    
    
if __name__ == "__main__":
    
    pos = NQPosition(4)
    
    # if best_value is 0, we solved the problem
    print_board(pos)
    print("Initial position value", pos.value())
    best_pos, best_value = hill_climbing(pos)
    print("Final value", best_value)
    print_board(best_pos)
    
    if (best_value == 0):
        print("Solved!\n")
    else:
        print("No solution found!\n")
    
    for i in range(4, 9):
        run_statistics(i, 100000)
    