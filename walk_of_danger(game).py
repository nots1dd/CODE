print("""WALK OF DANGER""")
invalid = "You have typed an invalid input. Kindly re-rerun the game to play again!"
balance = 1000
death = "☠️ You died while walking on danger. You have lost the game. Kindly re-run the game if you wanna play again!"
bankrupt = "💵🚫 You have become bankrupt! You have lost the game. Kindly re-run the game if you wanna play again!"
imprisoned = "👮 You have become inprisoned!! You have lost all your money and are rotting in prison! Since you cannot earn any money now, you have lost the game! Kindly re-run the game if you want to play again!"
victory = "🎉 You have won the game!! A true warrior who has managed to survive the perils of life!! Hearty Congratulations! Kindly re-run the game if you wanna play again!"
name = input("Please enter your username to begin your walk of danger: ")[:11]


print("")
print("")

play = input(f"""Welcome {name} to WALK OF DANGER! A fun entralling game that will take you on an emotional rollercoaster. 
             
             Here are some rules of the game:
             
             1. You will start with $1000 of cash. Upon encountering some scenarios you may lose or gain cash.
             2. After each scene is described, a corresponding letter will indicate its action.
             3. Typing anything other than the given letters will result in you losing.
             4. If your balance should ever reach $0, you automatically lose the game.
             5. Some scenarios and options in the game can get you killed, meaning your entire walk of danger would end :(
             6. If you survive all the scenarios and have cash left, you win!
             
             
             PRESS (ok) to begin: """).lower()

print("")

if play == "ok":
    print(f"Alright {name}! Let us get started!!")
else:
    print("I suppose you did not want to walk through danger :(. Kindly re-run the program if you wish to play!")
    quit()

print("")
print('')

scene_1 = input("You enter a mansion with tons of cash. Do you take it or leave it? (Take/Leave) ").lower()

if scene_1 == "take":
    print("")
    print("As you were grabbing your loot, the police arrived and arrested you, leading you to pay a $200 fine.")
    balance = balance - 200
    print(f"Your balance is now = ${balance}.")
    print("")

    scene_2 = input("After paying your hefty fine, you find yourself lost in an alley. You see a lady slumped on the ground. Do you help her? (Yes/No) ").lower()

    if scene_2 == "yes":
         print("")
         print("Your kindness was not appreciated as the lady stole $50 from your pocket.")
         balance = balance - 50
         print(f"Your balance is now = ${balance}.")
         print("")

         scene_4 = input("You have been tasked by the 420 gang with robbing a bank. Robbing it will get the police on your back. Will you choose to rob or not? (Rob/Not) ").lower()
         
         if scene_4 == "rob":
             print("")
             print("Upon robbing the bank, you get a $5000 payout!! But beware the police are behind you.")
             balance += 5000
             print(f"Your balance is now = ${balance}.")
             print("")
             
             scene_5 = input("As you visit your hometown, you spot some police tailing you. There is a diversion ahead. One leads to your hometown and other leads to an unknown location. Which one do you take? (Home/Unknown) ").lower()
             
             if scene_5 == "home":
                 print("")
                 print("Your stubborness caused you to be caught by the police and are sentenced to life imprisonment! Have fun in prison!!")
                 print("")
                 print("")
                 print(imprisoned)
                 quit() #imprisoned scenario

             elif scene_5 == "unknown":
                 print("")
                 print("You find yourself in a strange town with no person in sight. The police lose your trail.")
                 balance += 0
                 print(f"Your balance is now = ${balance}.")
                 print("")

                 scene_6 = input("As you wander the town, you find a person lying on the ground, presumed to be dead. Do you search the person for any items? (Yes/No) ").lower()
                 
                 if scene_6 == "yes":
                     print("")
                     print("You searched the person and found nothing.")
                     balance += 0
                     print(f"Your balance is now = ${balance}.")
                     print("") 

                     scene_7 = input("You escape the creepy town. On the way back to civilisation, you feel hungry and spot a rabbit on the way. Do you eat it or resort to surviving on unknown leaves till you get back? (Rabbit/Leaves) ").lower()
                     if scene_7 == "rabbit":
                         print("")
                         print("You ate the rabbit and my word it was delicious! You feel refreshed the next day and hitchhike on a bus back to society. However, on the way back you realize that your pocket is empty. All you money that you saved up is now in the forest.")
                         print(f"Well that was a rather anticlimatic ending {name}. I suggest you to figure out how to win at this game!!")
                         print("")
                         print(bankrupt)
                         quit() #bankrupt scenario
                     elif scene_7 == "leaves":
                         print("")
                         print("You tried to rely on eating random leaves but ended up ingesting a plumeria leaf! You end up dying in the forest with no one to help you.")
                         print("")
                         print("")
                         print(f"{death}")
                         quit() #death scenario
                     else:
                         print(invalid)
                     
                 elif scene_6 == "no":
                     print("")
                     print("You chose not to search the dead man and instead chose to search a nearby shed and miraculously found $300!")
                     balance += 300
                     print(f"Your balance is now = ${balance}.")
                     print("")


                     scene_15 = input("You run out of gas while driving on a highway. You spot a small mini-van parked on the side. Do you steal it or wait for help? (Steal/Wait) ").lower()
                     if scene_15 == "steal":
                         print("")
                         print("You stole the mini-van! However your sleek stealing skills don't pay off as the rusty vehicle blasts while driving and leaves you and your money up in flames.")
                         print("")
                         print(death)
                         quit() #death scenario
                     elif scene_15 == "wait":
                         print("")
                         print("After waiting for over half a day, you find a truck and the driver gets you back to your home for $500.")
                         balance = balance - 500
                         print(f"Your balance is now = ${balance}.")
                         print("")

                         scene_16 = input("A couple of boring months later, you enroll for a legal death battle competition! You have to pick a weapon before fighting. Do you pick a baseball bat or a rusty axe? (Bat/Axe) ").lower()

                         if scene_16 == "bat":
                             print("")
                             print("Your baseball bat turned out to be quite versatile and agile. You defeated your opponent with ease and earned $1250!! You head back home to rejoice and vow to never attempt anything risky again.")
                             balance += 1250
                             print(f"Your balance is now = {balance}.")
                             print("")
                             print(victory)
                             quit() #winning scenario
                         elif scene_16 == "axe":
                             print("")
                             print("Your rusty and heavy axe did not suit your fighting style. You were brutally killed by your opponent and there was no funeral for you :( .)")
                             print("")
                             print(death)
                             quit() #death scenario
                         else:
                             print(invalid)
                     else:
                         print(invalid)
             else:
                print(invalid)
            
         elif scene_4 == "not":
             print("")
             print("You chose not to rob the bank. Instead you give a tip to the police and are rewarded $1000 for the vital intel. But beware the 420 gang is now tracking you.")
             balance += 1000
             print(f"Your balance is now = ${balance}.")
             print("")
             
             scene_17 = input("As part of a challenge for $10,000, you are supposed to survive an entire month in the forest. All you have now is wood sticks and some water. You notice someone sleeping with their items beside them. Do you steal or not? (Yes/No) ").lower()
             if scene_17 == "yes":
                 print("")
                 print("You attempted to steal their items but it was a trap! Upon reaching for her items, she slit your throat and you drowned in your own blood.")
                 print("")
                 print(death)
                 quit() #death scenario
             elif scene_17 == "no":
                 print("")
                 print("You chose not to steal. Instead you kept a watch on her and aimed at looting her items. However, there were two 420 gang members observing you and at your most vulnerable moment, they struck an arrow to your leg which paralysed you. They soon robbed you clean and left you to nature. Clean payback as they put it ☠️.")
                 print("")
                 print(bankrupt)
                 quit() #bankrupt scenario

         else:
             print(invalid)


    elif scene_2 == "no":
         print("")
         print("You chose not to help the lady.")
         balance += 0
         print(f"Your balance is now = ${balance}.")
         print("")

         scene_18 = input("Bad omens strike you as you refused to help the lady. You are accused of robbing a store. You plead not guilty. The lawyers who are willing to help you are showed. Do you pick lawyer 1 or 2? (1/2) ")
         if scene_18 == "1":
             print("")
             print("The defense you picked was sensational. However through the course of the trial, he was bribed and soon enough, he did not provide any evidence to suggest that you were innocent. You were found guilty and had to pay everything you had as reparation.")
             print("")
             print(bankrupt)
             quit() #bankrupt scenario

         elif scene_18 == "2":
             print("")
             print("You managed to win the trial with ease as your lawyer was brilliant! However you had to pay $700 to become a free citizen.")
             balance = balance - 700
             print(f"Your balance is now = {balance}.")
             print("")

             scene_19 = input("You enter a weird shop full of witchcraft related items. The shop-keeper, a witch, asks you to purchase either a broken demonic looking vase for $20 or a cursed looking watch for $100. Do you take any one of these items or make a run for it? (Vase/Watch/Run) ").lower()
             if scene_19 == "vase":
                 print("")
                 print("The vase gave you incredible luck!! An amazing purchase after all!")
                 print("")
                 balance = balance - 20
                 if balance <= 0 :
                     print("")
                     print(f"Unfortunately, you cannot purchase the vase as your balance is now ${balance}. Since you tried to act greedy and buy, you are now broke.")
                     print("")
                     print(bankrupt)
                     quit() #bankrupt scenario
                 else:
                    print(f"Your balance is now = {balance}.")
                    print("")
                    print("EPILOGUE: YOUR LUCK NEVER RAN OUT!!! YOU ENDED UP BECOMING THE RICHEST PERSON ON EARTH! YOU SEEM UTTERLY UNTOUCHABLE!!")
                    print("")
                    print(victory)
                    quit() #winning scenario
             elif scene_19 == "watch":
                 print("")
                 print("The watch was deeply cursed. After taking it with you back home, many ghosts followed and haunted you till your last breath 24 hours later.")
                 print("")
                 print(death)
                 quit() #death scenario
             elif scene_19 == "run":
                 print("")
                 print("You ran away from the witch and she really wasn't happy. She inflicted a curse on you such that everytime you took a breath, your money would disappear into thin air. As you would have guessed by now, YA BROKE!")
                 print("")
                 print(bankrupt)
                 quit() #bankrupt scenario

    else:
         print(invalid)

elif scene_1 == "leave":
    print("")
    print("The owner of the mansion saw you leaving emptyhanded and as a gesture of kindness gave you $1000.")
    balance += 1000
    print(f"Your balance is now = ${balance}.")
    print("")

    scene_3 = input("You managed to strand yourself on an idle boat. The water appears to be shallow. Do you risk swimming to shore which is 200 metres away or wait for help? (Swim/Wait) ").lower()

    if scene_3 == "swim":
        print("")
        print("Some killer fish chased you as you swam, however you barely make it to the shore. However, $100 of cash gets completely as a result.")
        balance = balance - 100
        print(f"Your balance is now = ${balance}.")
        print("")

        scene_8 = input("You venture out in the desert to find a lost city. You are lost and find a traveller and seek his guidance. Do you trust him or not? (Yes/No) ").lower()
        if scene_8 == "yes":
            print("")
            print("You placed your trust in a random person and shocker....he tricked you. You were caught in a sandstorm in the middle of nowhere and wake up nauseated.")
            balance += 0
            print(f"Your balance is now = ${balance}.")
            print("")

            scene_9 = input("On your way to find the lost city, you come across a Gambling hub and wish to bet on it. But there is a twist. You must bet everything you have or else you cannot participate. Do you bet it all or not? (Yes/No) ").lower()
            if scene_9 == "yes":
                print("")
                print(f"You bet everything you had ({balance}) and lost it all!!")
                print("")
                print(bankrupt)
                quit() #death scenario
            elif scene_9 == "no":
                print("")
                print("You chose not to gamble your earnings away. However as you were exiting the hub, you overhear a woman talking about the lost city. You now possess valuable INTEL!!")

                intel_sell = input("You have acquired INTEL!!! Should you choose to do so, you can sell it for an undisclosed amount to a traveller, or keep it and hope for it to be of use to you. (Sell/Keep) ").lower()
                if intel_sell == "sell":
                    print("")
                    print("You have sold your precious intel for an astounding $100! You should have kept it to yourself.")
                    balance += 100
                    print(f"Your balance is now = ${balance}.")

                    scene_20 = input("After giving away the vital INTEL, you were knocked unconcious by an intelligence agency. They interrogate you into giving away the identity of the buyer of INTEL. Do you give it or not? (Yes/No) ").lower()
                    if scene_20 == "yes":
                        print("")
                        print("In exchange for the buyers identity you sought for asylum and you got it! You are now safeguarded by the government and have no more risks of endangering yourself!!")
                        print("")
                        print(victory)
                        quit() #winning scenario
                    elif scene_20 == "no":
                        print("")
                        print("You were mentally and physically tortured for the identity of the buyer as well the location of the lost city. Eventually, you were thrown into a supermax prison on account of aiding a terrorist organisation! You now rot in prison till your last breath!!")
                        print("")
                        print(imprisoned)
                        quit() #imprisoned scenario
                    else:
                        print(invalid)
                        
                elif intel_sell == "keep":
                    print("")
                    print("At the risk of making many enemies, you chose to keep the intel to yourself. Beware, you ought to sleep with one eye from now on...")
                    balance += 0
                    print(f"Your balance is now = {balance}.")
                    print("")

                    scene_10 = input("You have travelled for several days in the desert with no pursuers in sight. You spot an oasis quite far away. Do you go there to rest or continue your journey to the lost city? (Rest/Continue) ").lower()
                    if scene_10 == "rest":
                        print("")
                        print("You desperately tried to find the oasis but it was no where to be seen. You died due to starvation a couple of days later with your precious intel and money all gone to waste!")
                        print("")
                        print(death)
                        quit() #death scenario
                    elif scene_10 ==  "continue":
                        print("")
                        print("You enthusiastically continued on your journey to the lost city but your enemies caught up with you and slaughtered and disfigured you for the intel you possessed.")
                        print("")
                        print(death)
                        quit() #death scenatio.

                else:
                    print(invalid)

        elif scene_8 == "no":
            print("")
            print("You chose not to listen to the traveller. You tried your best but you did not manage to fine the lost city. However you managed to find an AMULET in the sand!")
            print("")
            print("You have unlocked AMULET!! Should you choose, you can sell it for an undisclosed amount!!")
            print("")
        
            AMULET = 5000
            amulet_sell = input("Do you want to sell the amulet for XXXX amount?  (Yes/No) ").lower()
            if amulet_sell == "yes":
                print("")
                print("You have sold your AMULET for a whopping $5000!!")
                balance += 5000
                print(f"Your balance is now = {balance}.")
                print("")

                scene_11 = input("After making the deal of your life, you head to a bar to celebrate. You get drunk and spend the night there. In the morning, you find that $2000 was stolen from you last night. The bartender says that a man named AJ pickpocketed you and left. You possess a detailed sketch of 'AJ' and are able to find him. Do you go after him or not? (Yes/No) ").lower()
                if scene_11 == "yes":
                    print("")
                    print("You attempted to go after 'AJ' but the bartender lied to you and instead you end up being kidnapped by a drug smuggling ring. They steal all your money and leave you destitute.")
                    print("")
                    print(bankrupt)
                    quit() #bankrupt scenario
                elif scene_11 == "no":
                    print("")
                    print("Although cowardly, you chose not to chase AJ and instead head to a safe house and spend the rest of your life there.")
                    print("")
                    print(victory)
                    print(f"Good Game {name}!! You have walked the path of danger and made it out alive! Your final balance is = ${balance}.")
                    quit() #winning scenario

            elif amulet_sell == "no":
                print("")
                print("You chose to keep the AMULET. People are fucking pissed at you.")
                balance += 0
                print(f"Your balance is now = {balance}.")
                print("")

                scene_12 = input("You find yourself a bit sad so you treat yourself by going golfing. On the way, you find some people are tailing your vehicle. Do you worry about it and change course or just head for golf? (Worry/Golf) ").lower()
                if scene_12 == "worry":
                    print("")
                    print("You attempted to get rid of the tailing car but due to reckless driving, you crash and get fatally wounded. In your final moments, you see some suits taking your AMULET and fleeing the scene.")
                    print("")
                    print(death)
                    quit() #death scenario
         

    elif scene_3 == "wait":
        print("")
        print("You waited for an entire day before a random fisherman offered you to go back to the shore for a scandalous amount of $250.")
        balance = balance - 250
        print(f"Your balance is now = ${balance}.")
        print("")

        scene_13 = input("Upon reaching the shore, you find out about an NFT that piqued your interest. However, the NFT costs your entire balance. Do you risk it all for a digital art? (Yes/No) ").lower()
        if scene_13 == "yes":
            print("")
            print("You risked it all for a NFT and it drained your balance completely. Just a few days after purchasing it, the NFT was worthless and so is your life.")
            print("")
            print(bankrupt)
            quit() #bankrupt scenario
        elif scene_13 == "no":
            print("")
            print("You could have possibly missed out on a lot of money, but your balance is safe. You chose not to invest in the NFT.")
            balance += 0
            print(f"Your balance is now = {balance}.")

            scene_14 = input("Due to your past crimes, a bounty is placed on you. Eventually, you are cornered and have nowhere to run. Do you attempt to bribe the bounty hunter or make a last attempt at saving your life? (Bribe/Run) ").lower()
            if scene_14 == "bribe":
                print("")
                print("The bounty hunter accepted your bribe. But as you were leaving the house, he shot you dead. Both your money and soul ended up in hell.")
                print("")
                print(death)
                quit() #death scenario
            elif scene_14 == "run":
                print("")
                print("You ran like The Flash and somehow managed to escape! However, it was raining outside and as a result, you slipped and fell on a big pond. Therefore LOSING ALL YOUR MONEY TO THE RAIN!!")
                print("")
                print(bankrupt)
                quit() #bankrupt scenario
            else:
                print(invalid)


    else:
        print(invalid)
else:
    print(invalid)

print("")
print('')

#to debug the program and make optimisations.
#code running smoothly so far no errors.
#to set username limits(min and max)







