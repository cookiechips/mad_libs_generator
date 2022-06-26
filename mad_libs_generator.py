print("LET'S PLAY!!!!")

while True:

    color = input("Choose a color: ")

    p_noun = input("Choose a plural noun: ")

    noun = input("Choose a noun: ")

    adjective = input("Choose an adjective (Describing word): ")


    print('==================================================================')

    print(f'Roses are {color.capitalize()},')
    print(f'{p_noun.capitalize()} are blue,')
    print(f'{noun.capitalize()} is {adjective.capitalize()},  ')
    print('and so are you.')

    print('==================================================================')

    game_on = input("Do you want to play again? 'y' or 'n' ")
    if game_on[0].lower() == 'y':
        continue
    else:
        break
