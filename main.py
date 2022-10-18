from random import choice

# constants
MAX_LINES = 3
MIN_BET = 1
MAX_BET = 1000

ROWS = 3
COLS = 3

symbol_Count = {
    "💚" : 2,
    "💛" : 4,
    "🧡" : 6,
    "💖" : 8,
}

symbol_Vlaue = {
    "💚" : 5,
    "💛" : 4,
    "🧡" : 3,
    "💖" : 2,
}

def check_Winnings(columns, lines, bet, values):
    winnings = 0
    winning_Lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_To_Check = column[line]
            if symbol != symbol_To_Check:
                break
        else:
            winnings += values[symbol] * bet
            winning_Lines.append(line + 1)
        
    return winnings, winning_Lines
            
def get_Slot_Machine_Spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_Slot_Machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()
                
def get_Deposit():
    while True:
        amount = input("Amount to deposit> ")
        if amount.isdigit():
            break
        print("Please enter a valid positive amount")

    return int(amount)

def get_Lines():
    while True:
        lines = input(f"Number of lines 1-{MAX_LINES}> ")
        if lines.isdigit():
            if int(lines) in range(1, MAX_LINES+1):
                break
            else:
                print("Please enter a number between 1-3")
        else:
            print("Please enter a valid number")

    return int(lines)

def get_Bet():
    while True:
        bet = input(f"Bet {MIN_BET}-{MAX_BET}> ")
        if bet.isdigit():
            if int(bet) in range(MIN_BET, MAX_BET+1):
                break
            else:
                print(f"Bet must be between {MIN_BET}-{MAX_BET}")
        else:
            print("Please enter a valid bet")

    return int(bet)

def spin(balance):
    lines = get_Lines()

    # make sure total bet is less than balance
    while True:
        bet = get_Bet()
        total_Bet = lines * bet

        if total_Bet < balance:
            break
        else:
            print(f"Bet can't be more than your balance\nBALANCE: {balance}")

    print(f"\nBET: {bet}\nLINES: {lines}\nTOTAL BET: {total_Bet}")

    slots = get_Slot_Machine_Spin(ROWS, COLS, symbol_Count)
    print_Slot_Machine(slots)
    winnings, winning_Lines = check_Winnings(slots, lines, bet, symbol_Vlaue)
    print(f"You Won: {winnings}")
    print(f"You Won on lines:", *winning_Lines)
    
    return winnings - total_Bet

def main():
    balance = get_Deposit()
    while True:
        print(f"Current balance: {balance}")
        answer = input("Press enter to play (q to quit)")
        if answer == "q":
            break
        balance += spin(balance)
    
    print(f"You left with {balance}")
    
main()
