__author__ = 'hawker'
import urllib2


def nim_game_simulation(players):
    pass
    
def send_nim_bot(name, bot):
    site_url = "http://178.62.87.35:8080/"
    fun = "addbot"
    get = site_url+fun+"?username="+name+"&botval="+bot
    urllib2.urlopen(get).read()