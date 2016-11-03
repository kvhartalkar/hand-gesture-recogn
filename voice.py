import pyttsx
engine = pyttsx.init()
a=['']
i=0
#while(i<5):
#a=raw_input('name')
#    i=i+1
#print a[1]
#engine.say(a)
engine.getProperty('rate')
engine.setProperty('rate',rate+100)
engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()
