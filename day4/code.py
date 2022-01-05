class number:
    def __init__(self, number):
        self.num = number
        self.marked = False

class bingo_board:
    def __init__(self, size):
        self.size = size
        self.board = []
        self.bingo = False
        for i in range(size):
            self.board.append([])
            for j in range(size):
                self.board[i].append(0)

    def print_board(self):
        for i in range(self.size):
            for j in range(self.size):
                second_digit = " " if self.board[i][j].num < 10 else ""
                end = "* " if self.board[i][j].marked else "  "
                print(f"{second_digit}{self.board[i][j].num}", end=end)

            print()

    def set_numbers_on_board(self, numbers):
        for i in range(self.size):
            for j in range(self.size):
                self.board[i][j] = number(int(numbers[i][j]))
        return self.board

    def sum_all_unmarked_numbers(self):
        sum = 0
        for i in range(self.size):
            for j in range(self.size):
                sum += self.board[i][j].num if not self.board[i][j].marked else 0
        return sum

    def check_number(self,num):
        #check if has the number in the board
        for i in range(self.size):
            num_list = [x.num for x in self.board[i]]
            if num in num_list:
                j = num_list.index(num)
                self.board[i][j].marked = True
                return True

    def check_bingo(self):
        #check if all numbers in the line are marked
        for i in range(self.size):
            marked = True
            for j in range(self.size):
                marked = marked and self.board[i][j].marked
            if marked:
                self.bingo = True

        #check if all the numbers in the column are marked
        for j in range(self.size):
            marked = True
            for i in range(self.size):
                marked = marked and self.board[i][j].marked
            if marked:
                self.bingo = True

        return self.bingo

def str_to_intlist(line):
    list_numbers = line.replace('  ', ' ').split(' ')
    list_numbers = [x for x in list_numbers if x != '']
    return list_numbers

def get_board_from_data(data):
    size = int(len(data))
    b = bingo_board(size)
    b.set_numbers_on_board(data)
    return b

def get_boards_from_data(data):
    boards = []
    board_numbers = []
    for i in range(len(data)):
        if data[i] == '':
            boards.append(get_board_from_data(board_numbers))
            board_numbers = []
        else:
            board_numbers.append(str_to_intlist(data[i]))
    return boards

# read from input.txt
with open('day4/input.txt', 'r') as f:
    data = f.read()

def part1(numbers,boards):
    for num in numbers:
        for i,board in enumerate(boards):
            if board.check_number(int(num)):
                board.check_bingo()
                if board.bingo:
                    print(f"\nbingo for {num} at board {i}")
                    board.print_board()
                    final_score = board.sum_all_unmarked_numbers() * int(num)
                    print(f'\nfinal score: {board.sum_all_unmarked_numbers()} * {num} = {final_score}')
                    return final_score

def part2(numbers,boards):
    num_of_boards = len(boards)-1
    num_of_winning_boards = 0
    for num in numbers:
        for i,board in enumerate(boards):
            if board.check_number(int(num)) and not board.bingo:
                board.check_bingo()
                if board.bingo:
                    if num_of_winning_boards == num_of_boards:
                        print(f"\nLast bingo for {num} at board {i}")
                        board.print_board()
                        final_score = board.sum_all_unmarked_numbers() * int(num)
                        print(f'\nfinal score: {board.sum_all_unmarked_numbers()} * {num} = {final_score}')
                        return final_score
                    else:
                        num_of_winning_boards += 1

data = data.split('\n')

numbers = data[0].split(',')
boards = get_boards_from_data(data[2:])
part1(numbers,boards)

numbers = data[0].split(',')
boards = get_boards_from_data(data[2:])
part2(numbers,boards)