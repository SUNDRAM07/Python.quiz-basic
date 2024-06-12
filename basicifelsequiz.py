print("Welcome to the Computer quiz")
x=input("Do you wanna play the quiz y or n? ")[0]

if x=="y" or "Y" :
    print("lets start the quiz")

else:
    print("You are a loser if you stop without even playing once")
    ask =input("Are you sure you want to quit? ")[0]
    if ask== "y" or "Y":
        print("YOU REALLY ARE A LOSER")
        quit()

    print("Okay lets play :)")
# print("HINT: THE QUIZ IS CASE SENSITIVE SO WRITE EVERYTHING IN SMALL")
score=0
ans1=input("What does CPU stand for? ")
if ans1.lower() == "central processing unit":
    print("YOU GOT IT CORRECT +1")
    score+=1
else:
    print("INCORRECT ANSWER TRY HARDER :(")
ans1=input("What does RAM stand for? ")
if ans1.lower() == "random access memory":
    print("YOU GOT IT CORRECT +1")
    score +=1
else:
    print("INCORRECT ANSWER TRY HARDER :(")
ans1=input("What does HDD stand for? ")
if ans1.lower() == "hard disk drive":
    print("YOU GOT IT CORRECT +1")
    score +=1
else:
    print("INCORRECT ANSWER TRY HARDER :(")
ans1=input("What does SSD stand for? ")
if ans1.lower() == "solid state drive":
    print("YOU GOT IT CORRECT +1")
    score +=1
else:
    print("INCORRECT ANSWER TRY HARDER :(")
ans1=input("What does ROM stand for? ")
if ans1.lower() == "read only memory":
    print("YOU GOT IT CORRECT +1")
    score +=1
else:
    print("INCORRECT ANSWER TRY HARDER :(")
ans1=input("What does USB stand for? ")
if ans1.lower() == "universal serial bus":
    print("YOU GOT IT CORRECT +1")
    score +=1
else:
    print("INCORRECT ANSWER TRY HARDER :(")
ans1=input("What does LAN stand for? ")
if ans1.lower() == "local area network":
    print("YOU GOT IT CORRECT +1")
    score +=1
else:
    print("INCORRECT ANSWER TRY HARDER :(")
ans1=input("What does WAN stand for? ")
if ans1.lower() == "wide area network":
    print("YOU GOT IT CORRECT +1")
    score +=1
else:
    print("INCORRECT ANSWER TRY HARDER :(")
ans1=input("What does ISP stand for? ")
if ans1.lower() == "internet service provider":
    print("YOU GOT IT CORRECT +1")
    score +=1
else:
    print("INCORRECT ANSWER TRY HARDER :(")
ans1=input("What does GPU stand for? ")
if ans1.lower() == "graphical processing unit":
    print("YOU GOT IT CORRECT +1")
    score +=1
else:
    print("INCORRECT ANSWER :(")
print("You got " + str(score) + " marks and your percentage is "+ str(score*10)+"%!!" )