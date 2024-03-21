from Modules import *
from FAQ import faq
from snake import start_game


remb_lis=[]

with open('Remember file.dat', 'rb') as remb:
    try:
        while True:
            remb_lis.append(pickle.load(remb))
    except EOFError:
        pass

with open('jokes.txt') as joker:
    joke_lines=joker.readlines()


botname =("Metrobot")     
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    print(audio)
    
    engine.say(audio)
    engine.runAndWait()

def listen():
    '''
    r = sr.Recognizer()
     
    with sr.Microphone() as source:
         
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
  
    try:
        print("Recognizing...")   
        query = r.recognize_google(audio, language ='en-in')
        
        print(f"User said: {query}\n")
  
    except Exception as e:
        print(e)   
        print("Unable to Recognize your voice.") 
        return "None"
    return query
    '''
    
    return input()
    
def wishMe():
    pass
    
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning")
  
    elif hour>= 12 and hour<18:
        speak("Good Afternoon")  
  
    else:
        speak("Good Evening") 
    
    speak("I am your Voice Assistant")
    speak(botname)
    
    speak("I will be there to answer all your common questions along with metro related any kind of queries")


def username():
    global uname
    speak("What should i call you")
    
    user_resp_name = listen()
    uname=''
    
    for i in user_resp_name.split(' '):
        if i[0].isupper:
            uname+=' '+i
    uname=uname[1:]
    
    speak("Welcome Mister "+uname)
    speak("How can i Help you")

def joke_func():
    rand_line=random.randrange(0,586,3)
    return joke_lines[rand_line]+joke_lines[rand_line+1]

def flush():
    with open('Remember file.dat', 'wb') as remb:
        for i in remb_lis:
            pickle.dump(i,remb)

def sendEmail(to, content):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        
        # Enable low security in gmail
        server.login('your email id', 'your email password')
        server.sendmail('your email id', to, content)
        server.close()
    except:
        speak('Some Error Occured, Please try asking \'send whatsapp message\'')

if True:
    clear = lambda: os.system('cls')
    #clean any command before execution of this python file
    clear()


    wishMe()
    username()
    
    while True:
         
        query = listen().lower().replace('metrobot','')

        if 'what' in query and 'remember' in query:
                if 'last' not in query:
                    if len(remb_lis)==0:
                        speak('I was not told to remember anything till now')
                    elif len(remb_lis)==1:
                        speak('I was told to remember this')
                        speak(remb_lis[0])
                    else:
                        speak('I was told to remember these')
                        for i in range(len(remb_lis)):
                            ordinal=num2words(i+1,True)
                            speak(ordinal)
                            speak(remb_lis[i])
                else:
                    if len(remb_lis)==0:
                        speak('I was not told to remember anything till now')
                    else:
                        speak('I was told to remember this last time')
                        speak(remb_lis[-1])

        elif 'forget' in query and 'last' in query and ('told' in query or 'said' in query or 'conveyed' in query or 'ordered' in query):
            remb_lis.pop()
            speak('Ok Done')
            flush()

        elif 'remember' in query:
            if ('remember that' or 'remember this') in query:
                remb_line=query[14:]
            else:
                remb_line=query[9:]
            
            def remb_func(remb_st): # Function Here for recursion
                speak('You said to remember \''+remb_st+'\'')
                speak('Is that Correct')

                ch=listen().lower().split(' ')
                if 'not' in ch or 'incorrect' in ch or 'wrong' in ch or 'nope' in ch or 'no' in ch or 'inaccurate' in ch or ch==['n']:
                    speak('Speak the line again so that I can remember it or you may quit')
                    remb_listen=listen()
                    if remb_listen=="None" or remb_listen=="quit":
                        speak('Unable to remember/quiting performed')
                        speak('How can I help you by the way')
                    else:
                        remb_func(remb_listen)
                else:
                    speak('Ok I will remember that')
                    remb_lis.append(remb_st)
                    flush()

            remb_func(remb_line)

        elif 'forget' in query:
            if ('forget that' or 'forget this') in query:
                remb_line=query[12:]
            else:
                remb_line=query[7:]
            
            def remb_func(remb_st): # Function Here for recursion
                speak('You said to forget \''+remb_st+'\'')
                speak('Is that Correct')

                ch=listen().lower().split(' ')
                if 'not' in ch or 'incorrect' in ch or 'wrong' in ch or 'nope' in ch or 'no' in ch or 'inaccurate' in ch or ch==['n']:
                    speak('Speak the line again so that I can forget it or you may quit')
                    remb_listen=listen()
                    if remb_listen=="None" or remb_listen=="quit":
                        speak('Unable to forget/quiting performed')
                        speak('How can I help you by the way')
                    else:
                        remb_func(remb_listen)
                else:
                    remb_lis.remove(remb_st)
                    speak('Ok Done')
                    flush()

            remb_func(remb_line)

        elif 'salwan' in query and 'school' in query:
            speak('''Salwan Public School is a public school in New Delhi, India.
This school has 10 branches: Salwan Boys Sr. Sec. School, Rajendra Nagar(1949),
Salwan Girls Sr. Sec. School, Rajendra Nagar (1950), Salwan Public School, Rajendra Nagar(1953),
Gyan Devi Salwan Public School, Rajendra Nagar(1990), Salwan Public School (Afternoon), Rajendra Nagar (1991),
Salwan Junior School, Naraina (1993), Salwan Public School, Mayur Vihar, Phase III (1996),
Salwan Public School, Sector 15(II), Gurugram (1996), Salwan Montessori School, Sector 5, Gurugram(1999)
and Salwan Public School, Trans-Delhi Signature City, Ghaziabad (2005).
The Old Rajendra Nagar branch was the first branch that was launched, and is an important landmark in
the Rajendra Nagar and Karol Bagh localities. The Mayur Vihar branch was listed as second among the top ten schools in East Delhi, in 2012.
The school is registered under Delhi administration.

To increase awareness about Delhi Metro, Delhi Metro Rail Corporation dedicated a pillar
on Pusa Road to this school and for its children to do decoration work.

Try Asking More about creators

''')

        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences = 5)
            except Exception as e:
                results=e
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open ' in query:
            open_this=query.split(' ')[query.split(' ').index('open')+1]
            if open_this=='file':
                if query.split(' ')[query.split(' ').index('open')+2]=='explorer':
                    open_this='explorer'
            speak('Attempting to open '+ open_this)
            if False:
                pass
            else:
                os.system('start '+open_this)
                os.system('start ms-'+open_this+':')

        elif 'play'==query:
            speak('Try Asking to play a song with its name or play game')

        elif 'play ' in query and 'game' in query:
            speak('Which game you would like to try snake or flappy bird')
            if 'snake' in listen().lower():
                speak('enjoy your game')
                while start_game()!=True:
                    pass
            else:
                os.startfile('flappy_bird.py')
                speak('enjoy your game')
 
        elif 'play ' in query and ('music' in query or 'song' in query):
            speak("Here you go with your song")
            song=query.replace('play ','')
            try:
                song=song.replace('song','')
            except:
                song=song.replace('music','')

            pywhatkit.playonyt(song)
    
        elif faq(query)!='':
            speak(faq(query))
 
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("% H:% M:% S")   
            speak(f"the time is {strTime}")
 
        elif 'email to arnav' in query:
            speak("What should I say?")
            content = listen()
            to = "Receiver email address"   
            sendEmail(to, content)
            speak("Email has been sent !")
 
        elif 'send a mail' in query:
            speak("What should I say?")
            content = listen()
            speak("whom should i send")
            to = input()   
            sendEmail(to, content)
            speak("Email has been sent !")

        elif 'send' in query and 'whatsapp' in query:
            speak('What is the message')
            message=listen()
            speak('Please Confirm the Indian reciptant number (Indian country Code by default(+91))')
            phone_num=listen()
            pywhatkit.sendwhatmsg('+91'+str(phone_num))
 
        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you")
 
        elif ('fine' in query or "good" in query) and 'I am' in query:
            speak("It's good to know that your fine")
 
        elif "change my name to" in query:
            query = query.replace("change my name to", "")
            uname = query
 
        elif "change name" in query:
            speak("What would you like to call me ")
            botname = listen()
            speak("Thanks for naming me")
 
        elif "what's your name" in query or "what is your name" in query:
            speak('My name is '+botname)
 
        elif 'exit' in query or 'quit' in query:
            speak("Thanks for giving me your time")
            os._exit(True)
 
        elif "who made you" in query or "who created you" in query:
            speak("I have been created by Arnav one of the member 3 students group of Salwan School MV-3 under an investigatory project of Computer Science")
            speak("Try asking 'know more about creators'")
             
        elif 'joke' in query:
            speak(random.choice((joke_func(),pyjokes.get_joke())))
 
        elif 'search' in query:
             
            query = query.replace("search", "")
            query = query.replace("play", "")         
            webbrowser.open(query)
 
        elif "who i am" in query:
            speak("If you talk then definitely your human.")
 
        elif "more about creators" in query:
            speak("Thanks to Arnav, Anirudh and Vipul - three students of Salwan Public School Mayur Vihar.")
            speak("You may try asking \'about salwan public school\'")
            speak("or you may ask \'What can you do\'")
 
        elif 'document' in query or 'report file' in query:
            speak("opening document")
            doc= r'CS Investigatory project report.pdf'
            os.startfile(doc)

        elif 'who are you' in query:
            speak("I am your virtual assistant")
            speak("I was created under a project for Metro Administration as a chatbot")
            speak('To know my abilities or know more about creators try asking \'what can you do\'')
            speak('or \'know more about creators\'')

        elif 'what can you do' in query or 'abilities' in query or 'reason for you' in query:
            speak("I am your virtual assistant")
            speak("I was created under a project for Metro Administration as a chatbot")
            speak('I was initially made to resolve any queries related to metro for the project based on metro but as the time passed I was made better with some special abilities that I am gonna describe')
            speak('Any doubts related to tokens, smart cards or any other metro related queries, I am here')
            speak('I have multiple other abilities like information of weather report, news on particular category or even you may ask me to crack a joke for detailed information about my abilites check documentations provided')
            #####################

        elif 'news' in query or 'headline' in query:
            news_api_key='fda31ec791fe47c582d82562758018b0'
            categories=('war', 'government', 'politic', 'education', 'health', \
                        'environment', 'economy', 'business', 'fashion', 'entertainment', \
                        'sport', 'international', 'india', 'tech', 'food', 'agriculture' \
                        'finance', 'defense', 'home', 'current affairs', 'today', 'space' \
                        'research', 'astrolog')

            category=False
            for i in categories:
                if i in query:
                    category=i
            
            if not category:
                speak('I wasnt told any news category during the call So therefore please tell any topic so that I can bring news for you')
                topic=listen()
                speak('Showing top headlines on topic '+topic)

                url='https://newsapi.org/v2/top-headlines?q='+topic+'&sortBy=publishedAt&apiKey='+news_api_key
            else:
                speak('Showing top headlines on category '+category)
                speak('If you want news in specific topic then just ask me for \'news\'')
                
                url='https://newsapi.org/v2/top-headlines?country=in&category='+category+'&apiKey='+news_api_key

            data=requests.get(url).json()

            try:
                status=data['status']
                totalResults=data['totalResults']
            except:
                status=totalResults=0

            if data['status']=='ok' and data['totalResults']!=0:
                speak(str(totalResults)+' results found')
                speak('5 news headlines will be announced in one go')
                articles=data['articles']
                
                for i in range(len(articles)):
                    speak('Headline '+str(i+1))
                    if articles[i]['author']!=None:
                        speak('by '+articles[i]['author'])
                    speak(articles[i]['title'])
                    speak('\n')
                    if (i+1)%5==0 and i!=len(articles)-1:
                        speak('Wanna continue??')
                        ch=listen()
                        if 'yes' in ch or 'why not' in ch or 'sure' in ch:
                            speak('Ok')
                        else:
                            speak('Ok, exiting news')
                            break
            else:
                speak('Didnt find any news, please try again with different parameters')

        elif 'lock window' in query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()
 
        elif 'shutdown' in query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')
 
        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop jarvis from listening commands")
            a = int(listen())
            time.sleep(a)
            print(a)
 
        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl / maps / place/" + location + "")
 
        elif "camera" in query or "take a photo" in query:
            ec.capture(0, "Jarvis Camera ", "img.jpg")
 
        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])
             
        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")
 
        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

        elif "fact" in query:
            fact=randfacts.get_fact()
            speak('Here you go with a fun fact')
            speak(fact)
 
        elif "weather" in query or 'temperature' in query:
            api_key = "3fd08ccaff1741cd47f312b378a4a3b6"
            base_url = "http://api.openweathermap.org/data/2.5/weather?"
            speak(" City name ")
            print("City name : ")
            city_name = listen()
            complete_url = base_url + "q=" + city_name + "&appid=" + api_key
            response = requests.get(complete_url)
            x = response.json()
             
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = round(y["temp"]-273.15,3)
                current_pressure = y["pressure"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature = " +str(current_temperature)+"Celsius"+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description))
             
            else:
                speak(" City Not Found ")
 
        elif "good morning" in query or "good evening" in query or "good afternoon" in query:
            speak("A warm" +query)
            speak("How are you")

        elif botname in query:
            wishMe()
            speak("On your service")
 
        # elif "" in query:
            # Command go here
            # For adding more commands
