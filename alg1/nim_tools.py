__author__ = 'hawker'
import urllib2


def nim_game_simulation(players):
    (moves1, moves2) = players
    if len(moves1) != len(moves2):
        raise ValueError
    else:
        stones = len(moves2)
        i = 0
        while stones > 0:
            player_turn = i%2
            move_value = int(players[player_turn][-stones]) + 1
            stones -= move_value
            #print move_value, stones, player_turn, i
            if stones == 1:
                return player_turn
            elif stones <= 0:
                return 1-player_turn
            else:
                i += 1
                continue

def send_nim_bot(name, bot):
    site_url = "http://178.62.87.35:8080/"
    fun = "addbot"
    get = site_url+fun+"?username="+name+"&botval="+bot
    urllib2.urlopen(get).read()