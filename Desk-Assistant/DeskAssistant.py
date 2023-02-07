import pyttsx3
import datetime
import requests
import speech_recognition as v
import socket
import webbrowser
import os
import subprocess
import wikipedia
import pyjokes
import time
import wolframalpha
import json
from urllib.request import urlopen

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
voice_now = engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def Wishs():
    time = int(datetime.datetime.now().hour)
    t = datetime.datetime.now().strftime('%I:%M:%p')

    if time >= 0 and time < 12:
        wish = "Good Morning"
        speak(wish)
        print(wish)

    elif time == 12:
        wish1 = "Good noon"
        speak(wish1)
        print(wish1)

    elif time > 12 and time <= 15:
        wish2 = "Good Afternoon"
        speak(wish2)
        print(wish2)

    elif time > 15 and time <= 18:
        wish3 = "Good evening"
        speak(wish3)
        print(wish3)

    else:
        speak("good night")
        print("Good night")
        print(t)


def hear():
    r = v.Recognizer()
    with v.Microphone() as source:
        print("Listening...")
        speak("Listening...")
        r.pause_threshold = 1
        Audio = r.listen(source)

    try:
        print("Processing...")
        speak("processing...")
        query = r.recognize_google(Audio, language='en-in')
        print(f'USER SAID {query}\n')

    except Exception as ex:
        print(ex), speak(ex)
        print("Unable to recognize your voice")
        speak("Unable to recognize your voice")
        return "None"

    return query


def connectionCheck():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('www.google.com', 80))
        speak("you are online!")
        s.close()
    except Exception:
        print('Unable to Connect!')
        print("<!!!OFFLINE!!!>")
        speak('Unable to Connect!')


bot_name = "Alana"

def Assistant():
    Wishs()

    while True:
            query = hear().lower()

            if 'wiki' in query or 'wikipedia' in query:
                try:
                    speak('Searching Wikipedia')
                    query = query.replace("wikipedia", "")
                    query = query.replace("wiki", "")
                    wikiResults = wikipedia.summary(query, sentences=4)
                    print(f"\n\tAccording to Wikipedia:\t {wikiResults}")
                    speak('According to Wikipedia: ' + wikiResults)
                except Exception as e:
                    print("<!!!OFFLINE!!!>")
                    print('\n\tUnable to Get Results!')
                    print("Please check your Internet connection")
                    speak("Couldn't Get Results!")


            # Searches With Google.
            elif "search" in query:
                query = query.replace("search", "")
                query = query.replace(" for ", "")
                query = query.replace("about", "")
                webbrowser.open(f'https://alana-shrisanjiv-ave.com/search?q={query}')
                print(f'\n\tSearching For "{query}"')
                speak(f"Searching for {query}")

                # Fetches Youtube Results
            elif "youtube" in query:
                speak("Ok! Fetching Results")
                query = query.replace("youtube ", "")
                query = query.replace(" youtube", "")
                webbrowser.open(f'https://www.youtube.com/results?search_query={query}')
                print('\n\tCheckout YouTube Results!')
                speak("Checkout Youtube Results!")

            # Copies User's Command.
            elif 'say ' in query or 'speak' in query:
                copy = query.replace("say ", "")
                print(f'\n\t{copy.title()}')
                speak(copy)
                time.sleep(1)

            # Tells The Time.
            elif 'time' in query:
                strTime = datetime.datetime.now().strftime("%I:%M %p")
                print(f"\n\tIt is {strTime}")
                speak(f"It's {strTime}")
                time.sleep(1)

            # Tells The Date.
            elif 'date' in query or "today's date" in query:
                strDate = datetime.datetime.now().strftime("%m/%d/%y")
                print(f"\n\tToday is {strDate}")
                speak(f"Today is, {strDate}")
                time.sleep(1)

            # Greets the User.
            elif 'greet me' in query or 'wish me' in query:
                Wishs()

            # Greets User When User Greets.
            elif 'good morning' in query or 'good afternoon' in query or 'good evening' in query:
                Wishs()

            # Plays Music.
            elif 'play music' in query or "play song" in query:
                import random
                speak("Here you go with music")
                music = 'C:\\Users\\Shrivanth\\PycharmProjects\\ALANA ASSISTANT\\Music'
                list = os.listdir(music)
                print(f'[{list}]')
                song = os.startfile(os.path.join(music, list[random.randint(0, 46)]))
                print(song)

            # Plays Any Music Online.
            elif 'play ' in query:
                query = query.replace('play ', '')
                musicSearch = f'https://music.youtube.com/search?q={query}'
                print(f"\n\tPlaying {query} Online.")
                speak(f'Playing {query} Online!')
                webbrowser.open(musicSearch)

            # Opens Notepad.
            elif 'notepad' in query:
                print('\n\tOpening NOTEPAD!')
                speak('Opening Notepad')
                os.startfile('C:\\Windows\\notepad')

            elif 'news' in query:

                try:
                    jsonObj = urlopen(
                        '''https://newsapi.org/v2/top-headlines?country=in&apiKey=17f9124eaa174ff1a965dce8ffde2f5c''')
                    data = json.load(jsonObj)
                    i = 1

                    speak('here are some top news from the times of india')
                    print('''=============== TIMES OF INDIA ============''' + '\n')

                    for item in data['articles']:
                        print(str(i) + '. ' + item['title'] + '\n')
                        print(item['description'] + '\n')
                        speak(str(i) + '. ' + item['title'] + '\n')
                        i += 1
                except Exception as e:

                    print(str(e))

            elif "find my phone" in query:
                speak("Finding your phone!")
                print("Finding your phone!")
                webbrowser.open('https://www.google.com/android/find')

            elif "alana site" in query:
                speak("Here you go with my home site!")
                print("Here you go with my home site!")
                webbrowser.open('home.alana-shrisanjiv-ave.com')

            elif 'this pc' in query:
                print(f'\n\tOpening "This PC"')
                os.startfile('C:\\Users\\Shrivanth\\Desktop\\This PC.lnk')

            # Opens Task Manager.
            elif 'task manager' in query or 'task-manager' in query:
                print('\n\tOpening Task Manager!')
                speak('Opening Task Manager')
                os.startfile('%windir%\\system32\\taskmgr.exe /7')

            elif "calculate" in query:

                app_id = "ATW37H-AELJWVLLE3"
                client = wolframalpha.Client(app_id)
                indx = query.lower().split().index('calculate')
                query = query.split()[indx + 1:]
                res = client.query(' '.join(query))
                answer = next(res.results).text
                print("The answer is " + answer)
                speak("The answer is " + answer)
            elif "what is" in query or "who is" in query:
                # Use the same API key
                # that we have generated earlier
                client = wolframalpha.Client("ATW37H-AELJWVLLE3")
                res = client.query(query)

            # Opens CMD.
            elif 'cmd' in query or 'command prompt' in query:
                print('\n\tOpening COMMAND PROMPT!')
                speak('Opening Command Promt')
                os.startfile('%windir%\system32\cmd.exe')

            elif "coder" in query or "pycharm" in query:
                print("Opening Pycharm!")
                speak("Opening Pycharm!")
                os.startfile("C:\\Program Files\\JetBrains\\PyCharm 2022.3.2\\bin\\pycharm64.exe")

            elif "webstrom" in query:
                print("Opening Webstrom!")
                speak("Opening Webstrom!")
                os.startfile("C:\\Program Files\\JetBrains\\WebStorm 2022.3.1\\bin\\webstorm64.exe")

            elif "chrome" in query:
                print("Opening Google Chrome!")
                speak("Opening Google Chrome!")
                os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

            elif "power point presentation" in query or "power point" in query:
                print("Opening PPT!")
                speak("Opening PPT!")
                os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE")

            elif "exel" in query or "xl" in query:
                print("Opening EXEL!")
                speak("Opening EXEL")
                os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE")

            elif "word" in query or "microsoft word" in query:
                print("Opening Microsoft Word!")
                speak("Opening Microsoft Word!")
                os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE")

            elif "outlook" in query or "microsoft outlook" == query:
                print("Opening Outlook!")
                speak("Opening Outlook!")
                os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\OUTLOOK.EXE")

            elif "one note" in query:
                print("Opening Onenote!")
                speak("Opening Onenote!")
                os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\ONENOTE.EXE")

            elif "opera gx" in query or "opera" in query:
                print("Opening Opera GX!")
                speak("Opening your gaming browser")
                os.startfile("C:\\Users\\Shrivanth\\AppData\\Local\\Programs\\Opera GX\\launcher.exe")

            elif "edge" in query:
                print("Opening Microsoft Edge!")
                speak("Opening Microsoft Edge")
                os.startfile("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

            elif "quick heal" in query or "antivirus" in query or "anti virus" in query or "anti-virus" in query:
                print("Opening Quick Heal!")
                speak("Opening Quick Heal!")
                os.startfile("C:\\Program Files\\Quick Heal\\Quick Heal IS Essentials\\SCANNER.EXE")

            elif 'calculator' in query:
                print('\n\tOpening CALCULATOR')
                speak('Opening Calculator!')
                os.startfile('C:\\Windows\\System32\\calc.exe')

            # Shows Connected Wifi Details.
            elif "wi-fi details" in query or 'wifi details' in query:
                try:
                    speak("Trying to Show Details")
                    print("Trying Show Details...")
                    subprocess.call('netsh wlan show profiles')
                    time.sleep(3)
                except Exception as e:
                    print("\n\tUnable to Show Details!")
                    speak("Unable to ShoW Details! Sorry")

            # Shows IP Details
            elif 'ip details' in query or 'my ip' in query:
                print('\n\tShowing!')
                speak("Showing Ip Details")
                subprocess.call("ipconfig")
                time.sleep(1)

            elif "dns details" in query or "my dns" in query:
                print("Showing DNS!")
                speak("Showing DNS!")
                subprocess.call('ipconfig /displaydns')
                speak("Done!")
                time.sleep(2)

            elif "don't listen" in query or "do not listen" in query or "stop listening" in query:
                speak("How much time should I stop listening!")
                print("How much time should I stop listening!")
                v = int(hear())
                time.sleep(v)

            elif "blue stacks" in query or "bluestacks" in query:
                speak("Opening Blue Stacks!")
                print("Opening Blue Stacks!")
                os.startfile("C:\\Program Files (x86)\\BlueStacks X\\BlueStacks X.exe")

            elif "flash dns" in query or "flush dns" in query:
                print("Erasing all data!")
                speak("Erasing all data!")
                subprocess.call('ipconfig /flushdns')
                speak("Done!")
                time.sleep(5)

            # Shows System Information in CMD.
            elif 'systeminfo' in query or 'system info' in query:
                print('\n\tShowing System Information!\n')
                speak("Ok, Showing Your System Information. Please Wait")
                subprocess.call('systeminfo')
                speak('Done!')
                time.sleep(5)

            # Shows All Running Tasks.
            elif 'task list' in query or 'tasklist' in query:
                print('\n\tShowing All Running Tasks!')
                speak('Showing All Running Tasks!')
                subprocess.call('tasklist')
                time.sleep(10)

            # Clears the Console.
            elif 'clear' in query or 'clean' in query or 'clear console' in query:
                os.system('cls')
                speak('Current Console Cleared')

            elif "where is" in query or "route to" in query:
                query = query.replace("where is", "")
                query = query.replace("route to", "")
                speak(f"user asked to locate{query}")
                webbrowser.open(r'https://www.google.com/maps/place/')

            # Shuts Down the PC.
            elif 'shutdown' in query or 'power off' in query:
                speak("Shutting down your PC!")
                print("Shutting down your PC!")
                os.system('shutdown -s')

            elif "restart" in query:
                speak("Restarting your PC!")
                print("Restarting your PC!")
                os.system('shutdown -r')

            elif "sleep" in query or "hibernate" in query:
                speak("Hibernating your PC!")
                print("Hibernating your PC!")
                os.system('shutdown -h')

            elif "weather" in query:
                speak("wait a second")
                print("Wait a second")
                webbrowser.open(f'https://www.google.com/search?q=weather')
                time.sleep(5)

            elif "notes for 1st grade" in query:
                speak("yeah wait a sec!")
                print("Yeah wait a sec!")
                webbrowser.open('https://www.studyadda.com/notes/1st-class/32')

            elif "log off" in query or "sign out" in query:
                print("Loging off PC!")
                speak("Loging off PC!")
                subprocess.call('shutdown /l')
            # Answers Your Hello.
            elif f'hello' in query or f'hi {bot_name}' in query or "hai" in query or "hay" in query:
                import random
                hello_ans = [
                    f'Hi ',
                    f'Hey ',
                    f'Hello ',
                    f'Hi There ',
                    f'Hey There ',
                    f'Hello There '
                ]
                hello_ans = random.choice(hello_ans)
                print(f'\n\t{hello_ans}! How Can I Help You?')
                speak(f'{hello_ans}! How Can I Help You?')

            # If Only It's Name in Query.
            elif "bot" in query:
                import random
                toReply = [
                    'Ready to Help You!',
                    'How Can I Help You?',
                    'I am Here'
                ]
                toReply = random.choice(toReply)
                print(f"\n\t{toReply}")
                speak(toReply)

            # Reacts If User Says Hey.
            elif "hey" in query or "hi" == query:
                import random
                hey_ans = [
                    'Ready to Help You!',
                    'How Can I Help You?',
                    'I am Here to Help You!'
                ]
                hey_ans = random.choice(hey_ans)
                print(f'\n\t{hey_ans}')
                speak(hey_ans)

            # Says It's Condition.
            elif 'how are you' in query or 'how do you do' in query:
                import random
                as_i_am = [
                    'I am Fine,',
                    'I am Doing Well,',
                    'I am Great,'
                ]
                as_i_am = random.choice(as_i_am)
                print(f'\n\t{as_i_am} Thanks For Asking!')
                speak(as_i_am + ' Thanks For Asking!')

            # Replies Thank You!
            elif 'thanks' in query or 'thank you' in query:
                import random
                thanksGiving = [
                    'Never mind!',
                    'You are Always Welcome!',
                    'Mention Not!',
                    "That's My Duty!"
                ]
                thanksGiving = random.choice(thanksGiving)
                print(f'\n\t{thanksGiving}')
                speak(thanksGiving)

            elif "notes for 2nd grade" in query:
                speak("yeah wait a second")
                print("yeah wait a second")
                webbrowser.open('https://www.studyadda.com/notes/2nd-class/33')

            elif "notes for 3rd" in query:
                speak("yeah wait for a second")
                print("yeah wait a second")
                webbrowser.open('https://www.studyadda.com/notes/3rd-class/34/science/5')

            elif "notes for 4th grade" in query:
                speak("yeah wait for a second")
                print("yeah wait for a second")
                webbrowser.open('https://byjus.com/cbse/class-4/')

            elif "notes for 5th grade" in query:
                speak("yeah wait for a second")
                print("yeah wait for a second")
                webbrowser.open("https://byjus.com/cbse/class-5/")

            elif "notes for 6th grade" in query:
                speak("yeah wait a second")
                print("yeah wait for a second")
                webbrowser.open('"http://byjus.com/cbse-notes/class-6-science-notes/')

            elif "notes for 7th grade" in query:
                speak("yeah wait for a second")
                print("yeah wait for a second")
                webbrowser.open('https://byjus.com/cbse/class-7/')

            elif "notes for 8th grade" in query:
                speak("Yeah wait for a second")
                print("yeah wait for a second")
                webbrowser.open('https://byjus.com/cbse/class-8/')

            elif "notes for 9th grade" in query:
                speak("yeah wait a second")
                webbrowser.open('https://byjus.com/cbse/class-9/')

            elif "notes for 10th grade" in query:
                speak("yeah wait a second")
                webbrowser.open('https://byjus.com/cbse/class-10/')

            elif "notes for 11th grade" in query:
                speak("yeah wait a second")
                webbrowser.open('https://byjus.com/cbse/class-11/')

            elif "notes for 12th grade" in query:
                speak("yeah wait for a second")
                webbrowser.open('https://byjus.com/cbse/class-12/')

            # Replies Welcome.
            elif 'welcome' in query:
                print('\n\tI Feel Honored!')
                speak('I Feel Honored!')

            # Replies Sorry.
            elif 'sorry' in query or 'my fault' in query or 'my mistake' in query:
                print('\n\tHey! Never Repeat This.')
                speak('Hey! Please Never Repeat This.')

            # It's Creator.
            elif 'who made you' in query or 'who created you' in query:
                print('\n\tI Was Made by Shrivanth and Rahul sanjiv.')
                speak("I Was Made By Shrivanth and Rahul sanjiv.")

            # Tells It's Identity.
            elif 'who are you' in query or 'your name' in query:
                print(f'I am {bot_name.title()}, Your Virtual Assistant!')
                speak(f"I am {bot_name}, Your Virtual Assistant.")

            # Exit or Quit.
            elif 'exit' in query or 'quit' in query:
                exit(0)

            # Replies Okay
            elif 'ok' in query or 'okay' in query:
                print("\n\tThat's It")
                speak("That's It.")

            elif "open google" in query:
                webbrowser.open('https://www.google.com')
                speak("opening google")

            if "joke" in query:

                jokes = pyjokes.get_joke()
                speak(jokes)
                print(jokes)

            elif "open gmail" in query:
                webbrowser.open('https://mail.google.com')
                speak("opening gmail")

            elif "open translator" in query:
                webbrowser.open('https://translate.google.com')
                speak("opening google translator")

            elif "open drive" in query or "open google drive" in query:
                webbrowser.open('https://drive.google.com')
                speak("opening google drive")

            elif "open google pay" in query:
                webbrowser.open('https://pay.google.com')
                speak("opening google pay")

            elif "open paypal" in query:
                webbrowser.open('https://www.paypal.com')
                speak("opening google")

            elif "open google meet" in query or "open meet" in query:
                webbrowser.open('https://meet.google.com')
                speak("opening google meet")

            elif "open outlook" in query:
                webbrowser.open('https://outlook.live.com/')
                speak("opening microsoft outlook")

            elif "web office" in query:
                webbrowser.open('https://www.office.com/')
                speak("opening microsoft office")

            elif "open netflix" in query:
                webbrowser.open('https://www.netflix.com/in/')
                speak("opening netflix")

            elif "open website assistant" in query or "open alana web voice bot" in query or "open alana web voice bot" in query:
                webbrowser.open('web.alana-shrisanjiv-ave.com/')
                speak("opening my web version")

            elif "open amazon" in query:
                webbrowser.open('https://www.amazon.in/')
                speak("opening amazon")

            elif "amrita" in query or "about your school" in query:
                speak("opening amrita site")
                webbrowser.open('https://avettimadai.edu.in')

            elif "open amazon prime" in query or "open prime video" in query or "open amazon prime video" in query:
                webbrowser.open('https://www.primevideo.com/')
                speak("opening prime video")

            elif "open godaddy" in query:
                webbrowser.open('https://www.godaddy.com/')
                speak("opening godaddy")

            elif "open flipkart" in query:
                webbrowser.open('www.flipkart.com')
                speak("opening flipkart")

            elif "open hot star" in query or "open hotstar" in query or "disney plus hotstar" in query or "disney + hotstar" in query or "disney+hotstar" == query:
                webbrowser.open('www.hotstar.com')
                speak("opening disney + hotstar")

            elif "open youtube" in query or "open yt" in query:
                webbrowser.open('youtube.com')
                speak("opening yt")

            elif "open facebook" in query:
                webbrowser.open('https://www.facebook.com/')
                speak("opening facebook")

            elif "open instagram" in query or "open insta" in query:
                webbrowser.open('https://www.instagram.com/')
                speak("opening insta")

            elif "open snapchat" in query:
                webbrowser.open('https://www.snapchat.com/')
                speak("opening snapchat")

            elif "open twitter" in query:
                webbrowser.open('https://twitter.com/')
                speak("opening twitter")

            elif "open whatsapp" in query:
                webbrowser.open('https://web.whatsapp.com/')
                speak("opening whatsapp web")

            elif "open wikipedia" in query:
                webbrowser.open('https://www.wikipedia.org/')
                speak("opening wiki")

            elif "open bing" in query or "open microsoft bing" in query:
                webbrowser.open('https://www.bing.com/')
                speak("opening bing")

            elif "open discord" in query:
                webbrowser.open('https://discord.com/')
                speak("opening discord")

            elif "open github" in query:
                webbrowser.open('https://github.com/')
                speak("opening github")

            elif "open microsoft site" in query:
                webbrowser.open('https://www.microsoft.com/')
                speak("opening microsoft site")

            elif "open ebay" in query:
                webbrowser.open('https://www.ebay.com/')
                speak("opening ebay")

            elif "open skype" in query:
                webbrowser.open('https://www.skype.com/')
                speak("opening skype")

            elif "open classroom" in query:
                webbrowser.open('https://classroom.google.com/')
                speak("opening classroom")

            elif "open duck duck go" in query:
                webbrowser.open('https://duckduckgo.com/')
                speak("opening duck duck go")

            elif "open seraxng" in query:
                webbrowser.open('https://alana-shrisanjiv-ave.com')
                speak("opening opening my search engine")

            elif "open yahoo" in query:
                webbrowser.open('https://in.search.yahoo.com/')
                speak("opening yahoo")

            elif "open stackoverflow" in query:
                speak("Here you go to Stack Over flow.Happy coding")
                webbrowser.open("stackoverflow.com")

            elif "open spotify" in query or "open Spotify" in query:
                webbrowser.open("https://open.spotify.com/artist/0e86yPdC41PGRkLp2Q1Bph")
                speak("opening spotify")

            elif "open gaana" in query or "open Gaana" in query:
                webbrowser.open("https://gaana.com")
                speak("opening gaana")

            elif "open telegram" in query or "open Telegram" in query:
                webbrowser.open("https://telegram.org/")
                speak("opening telegram")

            elif "open google photo" in query or "open Google Photo " in query or "open Google photos" in query:
                webbrowser.open("https://photos.google.com")
                speak("opening google photo")

            elif "open phonepe" in query or "open phone pay" in query:
                webbrowser.open("https://www.phonepe.com")
                speak("opening phonepay")

            elif "open olx" in query or "open OLX" in query or "open Olx" in query:
                webbrowser.open("https://www.olx.in")
                speak("opening olx")


            elif "open meesho" in query or "open Meesho" in query:
                webbrowser.open("https://www.meesho.com")
                speak("opening meesho")

            elif "amazon" in query:
                speak("searching in amazon")
                print("Searching in Amazon!")
                webbrowser.open('https://www.amazon.in/s?k=laptop&crid=2Z28S0KZ33INE&sprefix=laptop%2Caps%2C653&ref=')

            elif "flipkart" in query or "flip cart" in query or "flipcart" in query:
                speak("Searching in Flipkart!")
                print("Searching in Flipkart!")
                webbrowser.open('https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=')

            elif "open myntra" in query or "open Myntra" in query:
                webbrowser.open("https://www.myntra.com")
                speak("opening myntra")

            elif "open python site" in query:
                webbrowser.open('https://www.python.org/')
                speak("install one of the popular coding language")

            elif "internet speed test" in query or "Internet Speed Test" in query:
                webbrowser.open("https://www.speedtest.net")
                speak("opening internet speed test")

            elif "youtube video saver" in query:
                webbrowser.open('https://savefrom.net')
                speak("opening save from . net")

            elif "search" in query or 'about' in query or 'search for' in query:
                query = query.replace('for', '')
                query = query.replace('search', ' ')
                query = query.replace('about', '')
                webbrowser.open(f'https://alana-shrisanjiv-ave.com/search?q={query}')
                print(f'\n\tSearching For "{query}"')
                speak(f"Searching for {query}")

            else:
                pass

# Run the app
if __name__ == '__main__':
    Assistant()