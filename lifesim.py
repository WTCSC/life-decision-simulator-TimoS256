path = []
print("Welcome to the life simulator! you are Ross Ronald, the day is may 23, 1997. You wake up to heat your alarm blaring and see the painfully bright red segmented LCD clock state the time, 8:00.")



def add_item(dec, opts):
    r = range(0,opts)
    if dec in r:
        path.append(int(dec))
    else:
        print(f"dec:{dec}")
        print(f"opts:{opts}")
        print(path)
        print('You feel as if something has gone very, very, wrong. You see objects vanish out of thin air, to be replaced with a vast darkness. The pebbles? Gone. The people? Gone. The cars? Gone. The buildings? Gone. The city? Gone. Slowly, more and more of this world is consumed. In time, all that remains is a string of words floating in the void, it reads: "Type error. process exited with error code -1"')
        quit()


def decision(fail, failmsg, opt, text):
    passing = False
    selection = int
    print(path)
    while passing == False:
        selection = int(input(text))
        if fail != selection:
            passing = True
            add_item(selection, opt)
        else:
            print(failmsg)
            retry = input("Would you like to retry? \n 1 : Yes. \n 2 : No \n > ")
            if retry == "2":
                quit()


def timeskip():
    print("After a while, you arrive back home. You notice that a tugnsten cube flew through your bedroom window and obliterated your alarm clock earlier today. You should have turned it off before you left.")
    if path[0] == 1:
        print("Even though you thought you turned your alarm off this morning, it happened to still be on for some reason.")
    


decision(None,None,4,"\n (Type the number of the option you would like to do.) \n 1 :Turn off your alarm clock. \n 2 : Get up. \n 3. Go back to sleep \n Answer: ")
if path[0] == 1:
#    decision(None, None, , "")
    print("tempfix yay")
elif path[0] == 2:
    decision(None, None, 2, "you get up, leave your bedroom, and think, What should I do today? \n 1 : Go for a walk outside \n 2 : Go rob a bank. \n Answer: ")
    if path[1] == 1:
        decision(2, "You continue down the path, and while caught up thinking about the bizarre events that have occurred, you trip over some moss. \n Game Over.", 2, "As you're walking down the sidewalk, a four-inch tungsten cube falls off the roof of the house next to you, smashing the paver below to pieces. What are you going to do? \n 1 :Throw the cube into the local swimming pool. \n 2 :Ignore the cube \n Answer: ")
        if path[2] == 1:
            decision(None, None, 2, "The cube is now in the local swimming pool, the lifeguard looks like he is being indecisive about what to do regarding the cube. Do you... \n 1 : Continue going about you day \n 2 : Go eat some moss \n >") 
            if path[3] == 1:
                timeskip()
            elif path[3] == 2:
                print("You find a patch of moss that fell off the roof of a nearby building. The moss is eaten and you feel like all is right in the world.")
                print("Your hp was mossed out.")
                timeskip()
    elif path[1] == 2:
        passing = False
        selection = str
        print(path)
        while passing == False:
            selection = input("At the bank, you wonder how you're going to break in. \n 1 : Shovel. \n 2 : Explosives \n 3 : Laser Drill. \n 4 : Wrecking ball \n 5 : Teleporter \n 6 : Disguise \n > ")
            if '1' == selection:
                print("You start digging downwards until your shovel hits something solid. Its too dark to see, so you pull out your lighter for some light. The flame illuminates the solid object, you see '-Gas Main-' written on the pipe, right above a uncture made by your shovel. \n Game Over.")
            elif '2' == selection:
                print("You set up a pile of all the explosives you had on you, but a small cartoonish bomb falls off the pile, triggering everything with it. \n Game over.")
            elif '5' == selection:
                print("you grab your Gadget Gabe™ approved Teleporter. Afrer pressing a few buttons, You disappear and reappear fused halfway into the wall that was just next to you. \n Game Over.")
            elif '4' == selection:
                print("As you start driving you crane towards the building, one of the guards yells at you. \n No construction scheduled for today. \n Game Over.")
            elif '3' == selection:
                print("Your laser drill cuts clean through the wall, the segment cut out falls on top of you. \n Game Over.")
            elif '6' == selection:
                print("Youve decided to shove yourself into a fake money bag on the side of the road. Once inside, an armored truck drives by and stops. The drivers hop out and say to each other 'How did we lose one?' 'Lets throw it in the back just to be safe?' Shortly, you make it into the bank vault. You leave your bag just to trip a laser sensor and get caught. A month later you arrive in prison and meet you cellmate, a four-inch tungsten cube")
                passing = True
                quit()
        retry = input("Would you like to retry? \n 1 : Yes. \n 2 : No \n > ")
        if retry == "2":
            quit()
elif path[0] == 3:
    awake = True
    while awake == True:
        g = input("You decide to get up. Nothing happened. \n 1: try again 2: go back to sleep \n >")
        if g == "2":
            awake = False
            path.append(int(g))
            print("While dreaming, you remeber that you had work today!")
            decision(1, "Why would you do such a thing??? How could you!? \n Game Over.", 3 , "Do you... \n 1 : Get up and go to work \n 2 : Keep sleeping \n >")
            if path[2] == 2:
                print("After a satisfying amount of sleeping in, you finally wake up, yawn, stretch your arms, and lean over to your still-beeping alarm clock. right before you turn it off you feel a dense metal cube slam into the back of your head. ")
                print("Next thing you know, you see a bright white light as you open your eyes to see the inside of an emergency room.")
                print(path)
                decision(2, "The lawsuit is not filed, you are now in an insurmountable amount of medical debt. \n Game Over.", 3, "Sue the cube for damages? \n 1: Yes \n 2: No \n >")
                print(path)
                if path[3] == 2:
                    print("\n September 17, 1997. District courthouse. Courtroom No. 4")
                    print("Judge: So. Your case states that Mister T. Cube here flew through you window somehow and hit you in the head? And for this you're asking for medical and property damage compensation. Is this correct?. Very good. Now how will you defend this claim?")
                    decision(2, "You reach into your back pocket for your moss, but you realize you ate it all. Without a solid legal defense you lose the case. \n Game Over.", 3, "What evidence do you present to support your claim? \n 1: Medical Examination \n 2: A pile of moss. \n 3: Security footage from the nearby pool.")
                    if path[4] == 1:
                        print("Prosecution: So this medical record lines up with your claim, but I fail to see how this tungsten cube became airborne. If you cannot explain that, you cannot defend your claim. I don't believe that it somehow launched itself through your window. Do you even know how dense tungsten is?")
                        print("The judge doesn't buy it, and your case is thrown out. Maybe representing yourself in a personal injury case wasn't the best idea")
                        quit()
                    elif path[4] == 3:
                        print("The jury is shocked to see the cctv footage of the tungsten cube inexplicably flying out of the pool and into your window, despite the best efforts of the local lifeguard. The judge rules in your favor. The cube has been sentenced to life in prison, and you have been awarded a large sum of money.")
                        print("Congradulations! You win! You are now Rich!")
                        quit()












