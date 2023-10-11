print("This is an adventure game. Depending on what you choose vastly helps with your survival. ")
print()

luck = int(input("Please enter the amount of luck you wish to have. 10 is your max: "))
if luck > 10:
    print("Incorrect response!")
    luck = 0
    print("Loading in avatar with no luck points...")
else:
    print("Input saved: Loading avatar...")

print()
option = input("You are walking through a dark forest and find two items: a MATCH and a FLASHLIGHT. Which one will you choose? ")
print()

if option.lower() == "match":
    run_hide = input("You pick up the match and strike it, and for an instant, the forest around you is illuminated. You see a large grizzly bear, and then the match burns out. Do you want to RUN, or HIDE behind a tree? ")
    print()
    if run_hide.lower() == "run":
        print("You started running but the bear is much faster than any human. The bear catches you; Game Ended")
    elif run_hide.lower() == "hide":
        print("You notice that you are standing on top of a pocket made from a tree falling in the forest, You hide in said pocket promptly, holding your breath. The bear finds you but runs off thinking you aren't alive.")
        increase = luck + 5
        print(f"Your luck has increased by 5; your new total luck points are: {increase}")
        print()
        option2 = input("The bear has gone off and for now you seem safe, but again you hear something and notice that this time it isn't the bear but something much more terrifying. You look behind you as the eyes glow from behind a tree. Do you TALK to it, try to WALK calmly away from it, try to FIGHT it, or RUN? ")
        if option2.lower() == "walk":
            print()
            option3 = input("You see it but try to pretend it isn't there, when you hid you lost where you were supposed to go until you come back to where the flashlight was, do you pick up the FLASHLIGHT or do you continue to WALK? ")
            more = increase + 10
            print(f"Your luck has increased by 10; your new total luck points are: {more}")
            print()
            if option3.lower() == "walk":
                print("You keep walking but as you do so you get lost; Game Ended")
            elif option3.lower() == "flashlight":
                option4 = input("You pick up the flashlight with your left hand, then you turn it on as you continue to walk the noise from the creature you hear behind you goes away. You come to a path and start walking up it until you come to a five way split in the road each with signs. One named MOON, one named GOLD, one named SUN, one named FREEDOM, one named LAND. Whats your choice? Note that two of these pathes will lead you to freedom... The other three will get you into situations that only can be found in imagination. ")
                print()
                if option4.lower() == "moon":
                    print("Moon has been chosen: You go down the path and as you do the forest splits once more but into the look of that land. You are now free")
                    win = more + 20
                    print(f"Your luck has increased by 20; your new total luck points are: {win}")
                    print()
                    if win >= 40:
                        print("You win")
                    else:
                        print("The vains of the trees drag you back in never to see the light of day again; Game Ended")
                elif option4.lower() == "gold":
                    print("Gold has been chosen: You take this path but as you do you kind it getting darker and increasingly more quiet, then a branch hits you, thinking nothing of it you disregard it, but suddenly the branch wraps around you picking you up as the trees eyes open locking eyes with it, it opens it's mouth to swallow you whole; Game Ended")
                elif option4.lower() == "sun":
                    print("Sun has been chosen: You take this path but you notice that as you keep going it starts to get hotter and hotter. You keep trying to wipe the sweat away as your vision becomes blurry. You end up passing out from the heat as it just keeps getting hotter; Game Ended")
                elif option4.lower() == "freedom":
                    print("Freedom has been chosen: This path is taken and you just keep walking the leaves from the tree rustling, not a care in the world. You come out to see beautiful land all of a sudden hearing muttering and the dragging of chains behind you, as you dart off the chains catch you slowly creeping you back into the forest as the grunting voice of a man says 'You may be free, but that doesn't mean you've won, haha'; Game Ended")
                elif option4.lower() == "land":
                    print("Land has been chosen: You run down the path but as you do notice it gets harder and harder to move you lets as everything around you seems to get taller but no, you are sinking into the path. It thus swallows you whole; Game Ended")
                else:
                    print("No path was chosen, the bear comes back finding you and knocking you into a tree; Game Ended")
            else:
                print("The noises of the creature get louder and louder as you stand there doing nothing. The beast then takes you away; Game Ended")
        elif option2.lower() == "talk":
            print("You turn around trying to talk to it but in the blink of an eye its already right next to you; Game Ended")
        elif option2.lower() == "fight":
            print("You turn around trying to be rave and boldly face the creature, you slowly grab a stick and yell for it to come down but as soon as you say that you are face to face with it's golden eyes and it's sharp teeth. You lose composure and as you to it knocks you out; Game Ended")
        elif option2.lower() == "run":
            print("You try to run but as you bolt he catches your attention and flies toward you in a leaping motion catching you; Game Ended")
        else:
            print("You stood still in fear as the creature then went away. You are still lost though and never find your way out; Game Ended")
    else:
        print("The bear catches you right as the light goes out; Game Ended")
elif option.lower() == "flashlight":
    follow_look = input("You pick up the flashlight and turn it on. You see the pathway lit up in front of you, but you thought you also heard something off to the side. Do you want to FOLLOW the path or LOOK in the trees for the thing that made the noise? ")
    print()
    if follow_look.lower() == "look":
        print("You try to follow the path but you get too curious as the noises get louder so you decide to go searching for the noise, you go off the path and a few trees in you run into the noise. It's the bear, you you fall trying to run away, he catches you; Gamed Ended")
    elif follow_look.lower() == "follow":
        print("You follow the path ignoring the noises, but the noises continue to get louder and louder until finally a bear runs at you on the path.")
        run_hide = input("Do you RUN, HIDE or CLIMB the tree next to you? ")
        if run_hide.lower() == "run":
            print("You start darting down the path but the bear is much faster than humans. The bear catches you; Game Ended")
        elif run_hide.lower() == "hide":
            print()
            print("You start running and hide quickly behind a tree off to the side of the path turning off your flashlight abruptly.")
            print("The bear runs passed you not seeing you and continues to run on the path ahead of you.")
            increase = luck + 5
            print(f"Your luck has increased by 5; your new total luck points are: {increase}")
            print()
            option5 = input("You walk back onto the path and see yellow eyes off in the distance. Do you scream and RUN or do you decide its your IMAGINATION? ")
            print()
            if option5.lower() == "imagination":
                print("A veil of black goes over your field of vision as you are then hit and pass out")
                if increase == 15:
                    print("You wake up in your bed, it was simply all a bad dream")
                else:
                    print("Game Ended")
            elif option5.lower() == "run":
                print("You are swallowed by the forest instantly; Game Ended")
            else:
                print("You have not decided correctly; Game Ended")
        elif run_hide.lower() == "climb":
            print("You run into the tree behind you and start trying to climb up the tree, He sees the light and heads toward it and before you even make it half way up the tree he knocks you down; Game Ended")
        else:
            print("The bear catches you; Game Ended")
    else:
        print("The bear catches you after turning on your flashlight; Game Ended")
else:
    print("You get hit with something knocking you cold; Game Ended")
    