
import random
print(""" Name of Game:- Rock Paper Scissors """)
l=['rock','paper','scissors']
while True:
    ccount=0
    ucount=0
    uc=int(input('''Enter your choice to start the game:-
1- Yes  
2- No|Exit            
            
            '''))
    if uc==1:
        for i  in range(1,6):
            uchoice=int(input('''Enter your choice from below option:-
1-rock                  
2-paper                  
3-scissors
0-back        
                              '''))
            if uchoice==1:
                userInput="rock"
            elif uchoice==2:
                userInput="paper"
            elif uchoice==3:
                userInput="scissors"
            elif uchoice==0:
                break
            Cchoice=random.choice(l)
            
            if Cchoice==userInput:

                print("Computer Choice: "+Cchoice)
                print("Your Choice: "+userInput)
                print("Game Draw")
                ucount=ucount+1
                ccount=ccount+1
            elif Cchoice=="rock" and userInput=="scissors" or Cchoice=="scissors" and userInput=="paper" or Cchoice=="paper" and userInput=="rock":
                
                print("Computer Choice: "+Cchoice)
                print("Your Choice: "+userInput)
                print("Computer win")
                ccount=ccount+1
            else:
                
                print("Computer Choice: "+Cchoice)
                print("Your Choice: "+userInput)
                print("You win")
                ucount=ucount+1
        
        print("User score:- ",ucount)
        print("Compter score:- ",ccount)
        
        if ccount==ucount:
            print("Final Game is Draw")
           
        elif ucount>ccount:
            print("Final You won the Game")
            
        else:
            print("Final Computer won the Game")
        1
                    
                
    else:
        break

