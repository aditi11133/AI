print("Hello, I am AI bot, Whats your name:")
name=input()
print("Nice to meet you", name)
print ("How are you feeling today? (good/bad):")
mood= input().lower()
if mood=="good":
    print("I'm glad to hear that")
elif mood=="bad":
    print("I'm sorry to hear that. Hope things get better")
else:
    print("I see. Sometimes its hard to put feelings into words")
print("What are you doing?")
work=input().lower()
if work=="eating":
    print("What are you eating?:")
    food=input()
    print("sounds YUMMY")
elif work=="listening to music" or "I am listening to music" or "i am listening to music" or "music" or "songs":
    print("What is your favourite genre?(rock/pop/hip hop/indie)")
    genre=input().lower()
    if genre=="rock":
      print("What is your favourite band?:")
      band=input()
      print ("I love",band)
    elif genre=="pop":
        print("Who is your favourite artist?:")
        artist=input()
        print("I love",artist)
        
    elif genre=="hip hop":
        print("Who is your favourite artist?:")
        artist=input()
        print("I love",artist)
    elif genre=="indie":
        print("Who is your favourite artist?:")
        artist=input()
        print("I love",artist)
    else:
        print("Thats some great taste")
elif work=="Watching match" or "watching match" or "Cricket" or "cricket" or "watching cricket":
    print("Who do you support?:")
    support=input()
    print("Thats a great team")

    
else:
  print("Sounds interesting")



