import colorama
from colorama import Fore, Style
from textblob import TextBlob
colorama.init()
print(Fore.CYAN+"Welcome to sentiment spy"+Style.RESET_ALL)
username=input(Fore.MAGENTA+"Please enter your naeme:"+Style.RESET_ALL).strip()
if not username:
    username="Mystery Agent"
conversation_history=[]
print(Fore.CYAN,"Hello agent",username)
print("Type a sentence and i will analyze your sentence and show you the sentiment")
print(Fore.YELLOW+"reset"+Fore.CYAN+Fore.YELLOW+"history"+Fore.CYAN,Fore.YELLOW+"exit"+Fore.CYAN+"to quit"+Style.RESET_ALL)
while True:
    userinput=input(Fore.GREEN+Style.RESET_ALL).strip()
    if not userinput:
        print(Fore.RED+"Please enter some text or a valid command"+Style.RESET_ALL)
        continue
    if userinput.lower()=="exit":
        print(Fore.BLUE+"Exiting sentiment spy, Farewell, Agent"+username,Style.RESET_ALL)
        break
    elif userinput.lower()=="reset":
        conversation_history.clear()
        print(Fore.CYAN+"All conversation history cleared"+Style.RESET_ALL)
        continue
    elif userinput.lower()=="history":
        if not conversation_history:
            print(Fore.YELLOW+"No conversation history yet."+Style.RESET_ALL)
        else:
            print(Fore.CYAN+"Conversation history:"+Style.RESET_ALL)
            for idx,(text,polarity,sentiment_type) in enumerate(conversation_history,start=1):
                if sentiment_type=="positive":
                    color= Fore.GREEN
                elif sentiment_type=="negative":
                    color=Fore.RED
                else:
                    color=Fore.YELLOW
                print(f"{idx}.{color} {text}"
                      f"(Polarity:{polarity:2f},{sentiment_type}){Style.RESET_ALL}")
                continue
            polarity=TextBlob(userinput).sentiment.polarity
            if polarity>0.25:
                sentiment_type="Positive"
                color=Fore.GREEN
            elif polarity<0.25:
                sentiment_type="Negative"
                color=Fore.RED
            else:
                sentiment_type="Neutral"
                color=Fore.YELLOW

            conversation_history.append((userinput, polarity, sentiment_type))

            print(color,sentiment_type,"sentiment detected"
                  "Polarity:",polarity,Style.RESET_ALL)

