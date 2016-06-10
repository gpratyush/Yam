import record_audio
import search
import trending
import weather
import mailtest
import mailtest2
import bingsearch
from chatterbotapi import ChatterBotFactory, ChatterBotType

def listen():

    speech=record_audio.main(0)
    return speech


def do(speech):

     factory = ChatterBotFactory()

     bot1 = factory.create(ChatterBotType.CLEVERBOT)
     bot1session = bot1.create_session()

     bot2 = factory.create(ChatterBotType.PANDORABOTS, 'b0dafd24ee35a477')
     bot2session = bot2.create_session()

     while(speech!="bye bye"):

        if speech.find("search twitter for")!=-1:
             speech=speech.replace("search twitter for",'')
             search.main(speech)
        elif speech.find("show twitter trend")!=-1:
             trending.main()
        elif speech.find("tell the weather")!=-1:
             weather.main()
        elif speech.find('show my e-mail')!=-1:
             mailtest.main()
        elif speech.find('send email')!=-1:
             mailtest2.main()
        elif speech.find('search bing for')!=-1:
             speech=speech.replace('search bing for','')
             bingsearch.main(speech)
        else:
             s = bot2session.think(speech);
             print 'yam> ' + s

        speech=listen()
        speech=speech.lower()     



def main():
    
    speech=listen()
    speech=speech.lower()
    print speech
    do(speech)

main()





             


