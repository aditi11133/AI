from textblob import TextBlob
print("Welcome to the Mood Detector")
name= input("What's your name")
print("Nice to meet you",name)
print("Type exit to quit")
while True:
    sentence= input("Your sentence:")
    if sentence.lower() == 'exit':
        print("Goodbye")
        break
    blob= TextBlob(sentence)
    sentence=blob.sentiment.polarity
    if sentiment>0:
        print("Positive sentiment detected")
    elif sentiment<0:
        print("Negative sentiment detected")
    else: 
        print("Neutral sentiment detected")
