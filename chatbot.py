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

print("It was nice chatting with you",name)
