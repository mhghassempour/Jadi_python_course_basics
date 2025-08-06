import random


def welcome():
    print('---------------------------------------')
    print('Welcome to "Geuss my numbe" game')
    print('i have a number in my mind. you have to try and guess it.')
    print('Good Luck!!!')
    print('---------------------------------------')


def win (computer_random, guess):
    return computer_random == guess


def get_guess():
    guess = input("guess a number: ")
    return int(guess)


def answer(computer, guess):
    if computer > guess:
        return 'my number is larger'
    if computer < guess:
        return 'my number is smaller'
    return '---------------------------------------\nWOW! CONGRATULATIONS!! you won'


def finish(computer, count, best):
    print(f'my number was {computer} and you guessed it in {count} tries')
    print(f'so far best result was {best} tries')
    print('---------------------------------------')
    ans = input('Do you want to play again? (Y/N)')
    print('---------------------------------------')
    if ans.upper() in ['Y', 'YES', '', 'ARE', 'BALE']:
        return True
    else:
        return False


welcome()
best_score = None
continue_playing = True
while continue_playing:

    computer_random = random.randint(1, 20)
    guess = 0 
    count = 0

    while not win(computer_random, guess):
        guess = get_guess()
        count +=1
        print(answer(computer_random, guess))

    if best_score is None or count < best_score:
        best_score = count

    continue_playing = finish (computer_random, count, best_score)