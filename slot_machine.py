import random

MAX_LINES = 3

MAX_BET = 1000
MIN_BET = 1

ROWS = 3
COLS = 3

symbols_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
}

symbols_values = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
}
def deposit():
    while True:
        deposit = input("Enter the amount to be deposited: ")
        if deposit.isdigit():
            deposit = int(deposit)
            if deposit <= 0:
                print("Deposit unsuccessful. Enter the number > 0")
            else:
                break
        else:
            print("Deposit unsuccessful. Enter the number")
    return deposit

def get_lines():
    while True:
        lines = input("Enter the number of lines: ")
        if lines.isdigit():
            lines = int(lines)
            if MAX_LINES >= lines > 0 :
                break
            else:
                print("Enter the number of lines between 1 and ", MAX_LINES)

        else:
            print("Enter the number")
    return lines

def get_bet():
    while True:
        bet = input("What would you like to bet? $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print("Bet unsuccessful. Enter the number between ", MIN_BET, " and ", MAX_BET)

        else:
            print("Enter the number")
    return bet

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, value in symbols.items():
        for i in range(value):
            all_symbols.append(symbol)

    columns = []       
    for _ in range(cols):
        column = []
        symbols = all_symbols[:]
        for _ in range(rows):
            new_symbol = random.choice(symbols)
            column.append(new_symbol)
            symbols.remove(new_symbol)

        columns.append(column)
    return columns

# maybe wrong
def print_slot_machine(columns, rows, cols):
    for row in range(rows):
        for i, column in enumerate(columns) :
            if i<cols-1:
                print(column[row], end=" | ")
            else:
                print(column[row], end=" ")
        print()
        
        
def check_winnings(columns, rows, cols, symbols_values, bet):
    result = 0
    for row in range(rows):
        symb = columns[0][row]

        for col in range(cols):
            if columns[col][row] != symb:
                break
        else:
            result += symbols_values[symb] * bet
    return result

def spin(balance):
    lines = get_lines()

    while True:
        bet = get_bet()
        total_bet = lines * bet
        if total_bet > balance:
            print("You don't have enough money to bet")
        else:
            break

    columns = get_slot_machine_spin(ROWS, COLS, symbols_count)
    print_slot_machine(columns, ROWS, COLS)
    result = check_winnings(columns, lines, COLS, symbols_values, bet)
    print("You won: $", result)

    return result-total_bet


def main():
    balance = deposit()
    while True:
        answer = input("Press enter to play (q to quit) ")
        if answer=="q"  or answer=="Q":
            break
        result = spin(balance)        
        balance += result
        if balance <= 0:
            print("You lost all your money")
            break
            
        print("Your balance: $", balance)
    print("Thank you for playing")
            
main()