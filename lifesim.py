path = []
print("Welcome to the life simulator! you are Ross Ronald, the day is may 23, 1997. You wake up to heat your alarm blaring and see the painfully bright red segmented LCD clock state the time, 8:00.")



decision(None,None,3,"\n (Type the number of the option you would like to do.) \n 1 :Turn off your alarm clock. \n 2 : Get up. \n 3. Go back to sleep \n Answer: ")
if path[0] == 1:
    decision(None, None, , "")
elif path[0] == 2:
    decision(None, None, 2, "you get up, leave your bedroom, and think, What should I do today? \n 1 : Go for a walk outside \n 2 : Go rob a bank. \n Answer: ")
    if path[1] = 1:
        decision(2, "You continue down the path, and while caught up thinking about the bizarre events that have occurred, you trip over some moss. \n Game Over.", 2, "As you're walking down the sidewalk, a four-inch tungsten cube falls off the roof of the house next to you, smashing the paver below to pieces. What are you going to do? \n 1 :Throw the cube into the local swimming pool. \n 2 :Ignore the cube \n Answer: ")
        if path[2] == 1:
            decision(None, None, 2, "The cube is now in the local swimming pool, the lifeguard looks like he is being indecisive about what to do regarding the cube. Do you... \n 1 : Continue going about you day \n 2 : Go eat some moss") 
        elif path[2] == 2:







def decision(fail, failmsg, opts, text):
    passing = False
    selection = str
    print(path)
    while passing == False:
        selection = input(text)
        if fail != selection:
            passing = True
            add_item(selection, opts)
        else:
            print(failmsg)
            retry = input("Would you like to retry? \n 1 : Yes. \n 2 : No \n > ")
            if retry == "2":
                quit()





def add_item(dec, opts):
    if dec in range(0, opts - 1):
        path.append(dec)
    else:
        print('You feel as if something has gone very, very, wrong. You see objects vanish out of thin air, to be replaced with a vast darkness. The pebbles? Gone. The people? Gone. The cars? Gone. The buildings? Gone. The city? Gone. Slowly, more and more of this world is consumed. In time, all that remains is a string of words floating in the void, it reads: "Type error. process exited with error code -1"')
        quit()

def 
