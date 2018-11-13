# TODO: add a mechanism to detech the height / width of a terminal instance


def display_stats(stats, width):
    stats_length = int(len(stats))
    print('* ' + stats + (' ' * (width - stats_length - 3)) + '*')

def display_prompt(message, width):
    message_length = int(len(message))
    print('* ' + message + (' ' * (width - message_length - 3)) + '*')


def generate_grid(message, stats):    
    width = 80
    row = '*' * width
    whitespace = ' ' * (width - 2)
    
    print(row)
    for height in range(1, 18):
        print('*' + whitespace + '*')
    print(row)
    display_stats(stats, width)
    display_prompt(message, width)
    print(row)


if __name__ == "__main__":
    message = 'adobo flakes'
    stats = 'human: 1 | computer: 1'
    generate_grid(message, stats)
    # stats, prompt
