import pyttsx3
engine = pyttsx3.init()
#rate = engine.getProperty('rate')
#print(rate)
#engine.setProperty('rate',300)
voices = engine.getProperty('voices')
#for voice in voices:
engine.setProperty('voice',voices[11].id)
engine.say('Good Evening Sir. I am Jarvis, Your Artificial Intelligent Agent. Sir, How can I Help You.')
engine.runAndWait()
engine.stop()
'''import pandas as pd
Location = "/home/desh/PycharmProjects/Test/dinfo.csv"
df = pd.read_csv(Location)
df.head()'''

