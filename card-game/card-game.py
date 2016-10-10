import random
poke = {
    'cs': [],       # cards
    'c': [],        # clubs
    'd': [],        # diamonds
    'h': [],        # hearts
    's': [],        # spades
    'j': []         # joker
}
player = {}
for i in range(1, 14):
    for ii in poke:
        if ii == 'cs':
            continue
        elif ii == 'j' and i > 2:
            continue
        else:
            poke[ii].append(ii + str(i))
            poke['cs'].append(ii + str(i))
# print (len(poke['cs']))
# begin the game
while True:
    random.shuffle(poke['cs'])
    player['a'] = (poke['cs'][0:17])
    player['b'] = (poke['cs'][17:34])
    player['c'] = (poke['cs'][34:51])
    r = (poke['cs'][51:54])
    for i in player:
        print ('player %s ' % i + 'get cars as: ' + str(player[i]))
    print ('we still remain: ' + str(r))
    go = raw_input('press "Y" to go on: ')
    if go == 'Y':
        print ('\nnew game')
        continue
    else:
        break
