def minion_game(string):
    
    players = {
        "Kevin": 0,
        "Stuart": 0,
    }

    max_len = len(string)
    iter = 0
    vogal = False
    consoante = False
    
    # for i in range(len(string)):
    #     if string[i] == ('A' or 'E' or 'I' or 'O' or 'U'):
    #         vogal = True
    #         for next in range(i+1, len(string)):
    #             if string[i] == ('A' or 'E' or 'I' or 'O' or 'U'):

    for i in range(len(string)):
        if string[i] == 'A' or string[i] == 'E' or string[i] =='I' or string[i] =='O' or string[i] =='U':
            while max_len != i:
                players['Kevin'] += 1
                max_len -= 1
        else:
            while max_len != i:
                players['Stuart'] += 1
                max_len -= 1
        max_len = len(string)

    if players['Stuart'] == players['Kevin']:
        print('Draw')
    else:
        winner = max(players, key=players.get)
        print(f"{winner} {players[winner]}")
    print(f" Kevin: {players['Kevin']}, Stuart: {players['Stuart']}")

if __name__ == '__main__':
    s = 'AEIOU'
    minion_game(s)