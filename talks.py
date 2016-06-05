import pyttsx

def main(speech):
    
    engine=pyttsx.init()
    engine.setProperty('rate',150)
    engine.setProperty('voice','en-wims')
    engine.say(speech)
    engine.runAndWait()
    