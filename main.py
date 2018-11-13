import random, time
from display import generate_grid

# TODO: export to own module
def magic_draw():
    return 'both magic cancelled each other out!'


def magic_stronger():
    return 'you overwhelmed your opponent!'


def magic_weaker():
    return 'your magic is weaker!'


def magic_simultanous_hit():
    return 'simultanous hit!'


MOVE_SET = ['fire', 'water', 'lightning', 'earth', 'wind']
MOVE_RESULTS = {
    ('fire', 'fire'): (magic_draw(), (0, 0)),
    ('fire', 'wind'): (magic_stronger(), (2, 0)),
    ('fire', 'water'): (magic_weaker(), (0, 2)),
    ('fire', 'lightning'): (magic_simultanous_hit(), (1, 1)),
    ('fire', 'earth'): (magic_simultanous_hit(), (1, 1)),

    ('water', 'water'): (magic_draw(), (0, 0)),
    ('water', 'fire'): (magic_stronger(), (2, 0)),
    ('water', 'lightning'): (magic_weaker(), (0, 2)),
    ('water', 'earth'): (magic_simultanous_hit(), (1, 1)),
    ('water', 'wind'): (magic_simultanous_hit(), (1, 1)),

    ('lightning', 'lightning'): (magic_draw(), (0, 0)),
    ('lightning', 'earth'): (magic_stronger(), (2, 0)),
    ('lightning', 'water'): (magic_weaker(), (0, 2)),
    ('lightning', 'wind'): (magic_simultanous_hit(), (1, 1)),
    ('lightning', 'fire'): (magic_simultanous_hit(), (1, 1)),

    ('earth', 'earth'): (magic_draw(), (0, 0)),
    ('earth', 'lightning'): (magic_stronger(), (2, 0)),
    ('earth', 'wind'): (magic_weaker(), (0, 2)),
    ('earth', 'fire'): (magic_simultanous_hit(), (1, 1)),
    ('earth', 'water'): (magic_simultanous_hit(), (1, 1)),

    ('wind', 'wind'): (magic_draw(), (0, 0)),
    ('wind', 'earth'): (magic_stronger(), (2, 0)),
    ('wind', 'fire'): (magic_weaker(), (0, 2)),
    ('wind', 'water'): (magic_simultanous_hit(), (1, 1)),
    ('wind', 'lightning'): (magic_simultanous_hit(), (1, 1)),
}


# TODO: catch errors outside y/yes or n/no
def application_continue():
    decision = input('continue playing? : ').lower()
    print(decision)
    if decision == 'y' or decision == 'yes':
        return True
    elif decision == 'n' or decision == 'no':
        return False
    else:
        print('not a valid choice')


def check_winner(player_health, opponent_health):    # results
    if player_health <= 0 or opponent_health <= 0:
        if player_health < opponent_health:
            print('opponent won!')
        elif player_health > opponent_health:
            print('player won!')
        else:
            print('draw!')
        return False
    else:
        return True


# TODO: uncouple function
def result_phase(player_move, opponent_move, player_health, opponent_health):
    message, (player_damage, opponent_damage) = MOVE_RESULTS[player_move, opponent_move]
    new_player_health, new_opponent_health = player_health - opponent_damage, opponent_health - player_damage
    return message, new_player_health, new_opponent_health


# TODO: error handling if outside the moveset
def action_phase():
    player_move = input().lower()
    opponent_move = random.choice(MOVE_SET)
    return player_move, opponent_move


def play_game():
    player_health, opponent_health = 5, 5
    no_winner = True
    while no_winner is True:
        stats = f'Player Health: {player_health} | Computer Health: {opponent_health}'
        generate_grid(f'invoke the spell you want to unlease to your feable foe.', stats)
        player_move, opponent_move = action_phase()

        message = f'you used [{player_move}] while your opponent used [{opponent_move}]'
        generate_grid(message, stats)
        time.sleep(2)

        message, player_health, opponent_health = result_phase(player_move, opponent_move, player_health, opponent_health)
        generate_grid(message, stats)
        no_winner = check_winner(player_health, opponent_health)
        time.sleep(1)


def run_application():
    # return player's information as a dict
    application_engine = True
    while application_engine is True:
        # Build Stage, welcome menu, stats
        play_game() # load player's information
        # save player's information
        application_engine = application_continue()
        

if __name__ == "__main__":
    run_application()
