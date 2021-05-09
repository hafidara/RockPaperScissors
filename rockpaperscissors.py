import random

N_GAMES = 3

def main():
    print_welcome()
    score = 0
    for i in range(N_GAMES):
        ai_move = get_ai_move()
        human_move = get_human_move()
        winner = get_winner(ai_move, human_move)
        score += get_score(winner)
        print('')
        print('the winner is', winner)
    print('The score is', score)

def get_ai_move():
    value = random.randint(1, 3)
    if value == 1:
        return 'rock'
    if value == 2:
        return 'paper'
    return 'scissors'


def get_score(winner):
    if winner == 'human':
        return +1
    if winner == 'ai':
        return -1
    if winner == 'tie':
        return 0

def get_human_move():
    while True:
        move = input('What is your move? ')
        if is_valid_move(move):
            return move
        return 'invalid.'

def is_valid_move(human_move):
    if human_move == 'paper':
        return True
    if human_move == 'rock':
        return True
    if human_move == 'scissors':
        return True
    return False

def get_winner(ai_move, human_move):
    if ai_move == 'rock':
        if human_move == 'paper':
            return 'human'
        return 'ai'
    if ai_move == 'paper':
        if human_move == 'scissors':
            return 'human'
        return 'ai'
    if ai_move == 'scissors':
        if human_move == 'rock':
            return 'human'
        return 'ai'
    return 'tie'

        

def print_welcome():
    print('Welcome to Rock Paper Scissors')
    print('You will play '+str(N_GAMES)+' games against the AI')
    print('rock beats scissors')
    print('scissors beats paper')
    print('paper beats rock')
    print('----------------------------------------------')
    print('')

if __name__ == '__main__':
    main()
