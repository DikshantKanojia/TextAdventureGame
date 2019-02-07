#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sunday Oct 14 15:00:00 2018

@author: Dikshant.Kanojia
Working Directory: ~/Desktop/Game/
"""

"""
    DocString:

    A) Introduction:
    This is a text based adventure game. It’s story is the original creation of the author.
    In this game, Natsu(you), the Protagonist,22 have to save the Kingdom of Kanto by defeating
    the Acnologia,  a ruthless & bloodthirsty dragon slayer, and bring peace to
    the world where dragons and humans co-exist. It consists of three stages,
    and has defined functions for start,for different stages of games, and for losing. This game requires basic
    of knowledge natural elements ( fire, water, etc), attention to detail
    while playing game to solve basic puzzle, some common sense  and
    some luck factor(random function included) to win.

    Stage 1: Decide the strategy to fight the enemies
    Stage 2: Overcome the illness
    Stage 3: Defeat the Acnologia

    B) Known Bugs and/or Errors:
    None.

"""
#import the necessary funtions
from sys import exit
import random

#List of comrades with the user
comrades = ['1. Natsu(You) - Fire Dragon Slayer', '2. Minato - Wind Dragon Slayer', '3. Hiruzen - Earth Dragon Slayer', \
            '4. Juvia - Water Dragon Slayer', '5. Laxus - Lightning Dragon Slayer', '6. Gray - Ice Dragon Slayer' ]

#List of enemies that that user and his comrade has to face
six_demons = ['1. Karaka - Fire Dragon', '2. Evanhell - Ice Dragon', '3. Rak - Lightning Dragon', \
'4. Wraithraiser - Water Dragon', '5. Boro - Wind Dragon', '6. Sachi - Earth Dragon']



def start():
    """ This function displays the context of the game and asks users what they want to do"""

    print("\n\n\n")
    print("#"*100)
    print("""\t\t\tKING OF DRAGONS WAR - A Text Based Adventure Game""")
    print("#"*100)
    print("\n\n")
    print("\t\t\t\t\tINTRODUCTION")
    print("""\n\n
        Over 400 years ago, in the kingdom of Kanto, the Dragons were considered
        to be the rulers of the world. The humans were food to the Dragons who
        flew the skies, freely dominating the lands and seas.
        However, an unknown Dragon questioned their reign and fought many battles
        to create the world we live today, where Dragons and humans coexist.

        Now, Acnologia, Self Proclaimed King of Dragons, a ruthless &
        bloodthirsty dragon slayer, who has killed any and all humans & dragons he could,
        ignoring the fact that many were his comrades,
        believes he is the rightful ruler of this world and has gathered
        followers with similar mindset to set out on the journey to kill the King
        of Kanto and re-built the world under his evil guidance.

        Your job is to stop Acnologia from reaching the King’s Palace and
        defeat him to bring peace back to the world.
        Do you have what it takes to defeat the King of the Dragons ??
    """)
    print("\n")

    print("""
        1. START GAME
        2. MORE INFO
        3. EXIT GAME
    """)

    print("What do you want to do?")

    counter = 0 # Iterable for while loop for introductory game choice
    force_exit = 0 # iterable variable for force exit if user does not enter a valid response 3 times in a row

    #This loop checks the condition of userput and takes appropriate action accordingly.
    while(counter == 0):
        user_input = input("> ")
        if user_input == "1" or user_input.lower() == 'START GAME'.lower():
            counter = 1 # Set counter to 1 to exit the while loop and start the game
            stage_1() #This function begins the game

        elif user_input == "2" or user_input.lower() == 'MORE INFO'.lower():
            more_info()

        elif user_input == "3" or user_input.lower() == 'EXIT GAME'.lower():
            quit_game()

        else:
            force_exit += 1 #increase the force_exit varible by 1
            if force_exit != 4:
                print("Please enter appropriate response from the following")
                print("""
                \t 1. START GAME
                \t 2. MORE INFO
                \t 3. EXIT GAME
                """)

            else:
                print("#"*100)
                print("Invalid Response. GAME OVER!!!!")
                quit_game()



#the following function is used in the main menu of the game
def more_info():
    """ This function diplays more information about the helpful tips for the game."""

    print("\n\n\n")
    print("#"*100)
    print("""\t\t\t\t\tMORE INFORMATION""")
    print("#"*100)
    print("\n\n")
    print("\t\t\t\t\tPLEASE READ CAREFULLY")
    print("""\n\n
        This is a text based adventure game. It’s story is the original creation of the author.

        In this game, Natsu(you) have to save the Kingdom of Kanto by defeating
        Acnologia,  a ruthless & bloodthirsty dragon slayer, and bring peace to
        the world where dragons and humans co-exist. The Game consists of three stages.

        You need to use the following to win:

        * your basic nature elements(fire, water,etc) knowledge
        * read attentively for clues
        * your wit and intelligence
        * and you need a bit of luck factor too :) !!!!

        The following information will be useful:

        Dragon are very powerful beings in the Kingdom of Kanto. They terrorized
        the World 400 years ago. Humans were food to the dragons. But an Unknown
        Dragon, realized this as wrong doing and taught some humans magic to defeat dragons.
        Each of those humans were implanted with a special elemental(such as fire, water, etc) seed
        which made those humans Dragon Slayers.

        Each Dragon Slayer is of different type. For eg: If some one is a Shadow Dragon Slayer, He can
        slay a Shadow Dragon with relative ease as compared to other type of Dragon. Alternatively, a Shadow Dragon
        Slayer will be weak against a Light Dragon.

    """)
    print("\n")
    input("<Press enter to return to the Main Screen>")
    start() #This will return the game to the starting point

#the following function is used in the main menu of the game
def quit_game():
    """ This function quits the game without playing it"""

    print("\n")
    print("*"*100)
    print("\n")
    print("\t\t\t\t\t!!!!! BYE BYE !!!!!") # #Change Statement
    print("\n")
    print("*"*100)
    print("\n\n")
    exit() #Exits the game


###############################################################################
# Stage 1: Defeat the enemies and Pass the forest of illusions
###############################################################################
def stage_1():
    """ This function starts the game and begins the first stage of the game"""
    print("Game started")
    print("\n\n")
    print("#"*100)
    print("""\t\t\t\t\t\tSTAGE-1""")
    print("#"*100)
    print("\n\n")
    #Describe the current situation to the user
    print("\t\t\t\t\t\tSCENARIO")
    print("""
        Acnologia has made his move. He has waged war on the Kingdom of Kanto. His army of Dragons
        have started destroying the kingdom. Acnologia along with his strongest dragons is
        heading towards the King's Palace to kill the King.

        Natsu(You) and your comrades are along with the King in his palace. But wait something is
        happening........
    """)
    print("\t\t\t\t****FLASH OF BRIGHT LIGHT****")
    print("\n\n")
    input("<Press enter to continue>")
    print("\n")
    print("#"*100)
    print("#"*100)
    print("\n")
    #Describe the current situation to the User and what user has to do:
    print("\t\t\t\t\tCURRENT SCENARIO")
    print("""
        You are seperated from the king and are on the edge of the kingdom. How did this happen????

        Acnologia has used his space displacement magic to seperate you and your comrades
        from the king.

        If you have to stop Acnologia in time from killing the king,
        you have to go through TOTO LAND - the forest of illusions.

        Acnologia's Six Strongest Dragons are guarding the entrance of TOTO LAND
        and one of them has the map to cross the TOTO LAND successfully.

        They challenge you and your comrades to a one on one fight.
        As the leader of the group, you have to decide who will fight whom.
        REMEMBER YOUR STRENGTHS OHH WISE FIRE DRAGON SLAYER
        AND ALSO REMEMBER THAT FIRE IS WEAK AGAINST WATER.
        """)

    print("Look below at the abilities of your comrades and enemies and decide who will fight whom")

    #Print comrades name and abilities
    print("\n\tYou & Your Comrades")
    for friends in comrades:

        print(friends)

    print("\n")
    #Print Enemies name and abilities
    print("\n\tENEMIES")
    for enemies in six_demons:

        print(enemies)

    print("\n\n")

    input("<Press enter to continue>")
    print("\n")
    print("**** NOTE: ENTER THE NUMBER THAT REPRESENTS YOU & YOUR COMRADES ****")
    print("**** NOTE: YOU HAVE TO ENTER A NUMBER ONLY ONCE. NO DUPLICATE ENTRIES ****")
    #the following code asks user for their decisions and store them in a variable.
    print("Who will fight Karaka - the Fire Dragon?")
    fight1 = input("> ")
    print("Who will fight Evanhell - the Ice Dragon?")
    fight2 = input("> ")
    print("Who will fight Rak - the Lightning Dragon?")
    fight3 = input("> ")
    print("Who will fight Wraithraiser - the Water Dragon?")
    fight4 = input("> ")
    print("Who will fight Boro - the Wind Dragon?")
    fight5 = input("> ")
    print("Who will fight Sachi - the Earth Dragon?")
    fight6 = input("> ")

    #Following code to checks user input and decides whether you win or lose for stage 1
    #It is also displayed in the Game Map
    if (fight1 == '1' and fight2 == '6' and fight3 == '5' and fight4 == '4' and fight5 == '2' and fight6 == '3'):
        print("\n")
        print("#"*100)
        print("#"*100)
        print("\n")
        print("""
            \t\t\t\t!!!!!! Congrats !!!!!!!

            You have Defeated the enemies and acquired the map of the Forest of Illusions

            Now hurry up you need to stop Acnologia!!!!
        \n""")
        print("""\t\t\t\t\t***** STAGE-1 CLEARED *****""")
        print("\n")
        print("#"*100)
        print("#"*100)
        print("\n")
        input("<Press enter to cross the Forest of Illusions>")
        stage_2() #Starts the second stage

    else:
        print("\n")
        print("#"*100)
        print("#"*100)
        print("\n")
        print("""
            \t\t\t\t!!!!!! DEFEAT !!!!!!!

            You're strategy has failed!!!! You and your comrades are defeated.
            Acnologia has killed the King!!!! This is World is Doomed !!!!
        \n""")
        print("""\t\t\t\t\t***** STAGE-1 FAILED *****""")
        print("\n")
        print("#"*100)
        print("#"*100)
        print("\n")
        fail()   #Activates the fail function

"""
Answer: Strategy of who will fight whom
Fire Dragon Slayer can defeat Fire Dragon with relative ease
Therefore, the following will fight each other:

Karaka - Natsu(You)
Evanhell - Gray
Rak - Laxus
Wraithraiser - Juvia
Boro - Hiruzen
Sachi - Minato
"""
###############################################################################
# Stage 2: Overcome your illness
###############################################################################
def stage_2():
    """Function for the second stage of the Game"""
    print("\n\n")
    print("#"*100)
    print("""\t\t\t\t\t\tSTAGE-2""")
    print("#"*100)
    print("\n\n")
    #Describe the current situation to the user
    print("\t\t\t\t\t\tSCENARIO")

    #Story Line of 2nd Stage
    print("""
        As you exit the Forest of Illusions, you and your comrades are exhausted from the battle.
        But at the sight of Kingdoms Destruction and Acnologia heading towards
        the King's Palaces,  you and your comrades are filled with determination to
        defeat Acnologia even at the expense of your own lives.

        Suddenly, you hold your chest and collapse. The pain is unbearable. Is this the
        moment you will die?

        Your comrades are worried about you and they try to heal you with
        their powers. But their efforts are in Vain.

        The Markarov, the wizard, sees this sight from his tower and instantenously appears
        before you and your comrades.
    """)

    input("<Press enter to continue>")
    print("\n")
    print("#"*100)
    print("#"*100)
    print("""
    Markarov(the wizard): Natsu, you have been fightning your illness for a very long time.
                          This illness arise because you were born as a human so you
                          have a human soul. You were killed as an infant by Acnologia.
                          But Your family loved you very much and so they used dark
                          dragon magic to bring you back from the dead
                          at the expense of their own lives.

                          The dark magic your family used implanted a demon seed in you. Soon, after that
                          a Fire Dragon named Draco found you and raised you as his child. To turn you
                          into a Fire Dragon Slayer he implanted a Dragon Seed in you.

                          The cause of your illness is the fusion between the Dragon Seed and
                          the Demon Seed. It is disturbing your life force as a human.
                          You should stop the fusion between them and choose only one.
    """)

    #User makes a choice which leads to win or lose in the second stage
    while_loop_iterator = 0
    while(while_loop_iterator == 0):
        print("""
        \nSTRENGTHEN YOUR WILL. DECIDE YOUR SELF
        \nAre you Dragon Or Are you Demon?
            1. Dragon
            2. Demon
            3. Neither
            """)
        answer = input("> ")

        if answer == '1':
            print("#"*100)
            print("\n")
            print("""
                                     !!!!!! FAILURE !!!!!!

            You chose to be a Dragon. You body can't withstand the transformation into
            a Dragon and you die painfully.

            Your comrades are defeated by Acnologia. Acnologia has killed the King!!!!
            This is World is DOOMED!!!!!!
                            ***** STAGE-2 FAILED *****

            """)
            print("#"*100)
            while_loop_iterator += 1
            fail()

        elif answer == '2':
            print("#"*100)
            print("\n")
            print("""
                                       !!!!!! FAILURE !!!!!!

            You chose to be a Demon. Acnologia has powers to control demons. ACNOLOGIA
            controls you and orders you to kill your comrades.

            You kill your comrades and then kill the King for Acnologia. Acnologia is the
            new king of the world and he uses you as his puppet to carry out his evil
            deeds. This World is DOOMED!!!!!!

                                    ***** STAGE-2 FAILED *****
            """)
            print("#"*100)
            while_loop_iterator += 1
            fail()


        elif answer == '3':
            print("""
            Makarov(The Wizard): If you are neither a Dragon nor a Demon, Then who are you?
            """)
            answer2 = input("> ")
            if answer2.lower() == 'Human'.lower():
                print("\n")
                print("#"*100)
                print("#"*100)
                print("\n")
                print("""
                                    !!!!!! CONGRATS !!!!!!

                Makarov(The Wizard): Wise choice my son. You know your roots.
                Now you will be able to control both the Dragon and Demon powers.
                You are more stronger now and are ready to face Acnologia.
                With my powers, I'll transport you instantenously to where Acnologia is.
                Go now, May Victory be yours !!!!


                !!!!! SHUNKAIDō NO MAHō !!!!! (CASTS THE SPELL)

                """)
                print("""\t\t\t\t\t***** STAGE-2 CLEARED *****""")
                print("#"*100)
                print("#"*100)
                print("\n")
                input("<Press Enter to Continue>")
                stage_3() #Connect to stage 3
                while_loop_iterator += 1

            else:
                print("#"*100)
                print("""
                                      !!!!!! FAILURE !!!!!!

                You don't know who you are???

                You run out of time and die painfully

                Your comrades are defeated by Acnologia. Acnologia has killed the King!!!!
                This is World is DOOMED!!!!!!

                                  ***** STAGE-2 FAILED *****

                """)
                print("#"*100)
                while_loop_iterator += 1
                fail()

        else:
            print("Invalid Response Young Man. Please choose a option number")


"""
Answer for the puzzle is Human because the protagonist has human soul to begin with.
"""


###############################################################################
# Stage 3: Defeat Acnologia
###############################################################################
def stage_3():
    """This function starts the third stage of the game"""
    print("\n\n")
    print("#"*100)
    print("""\t\t\t\t\t\tSTAGE-3""")
    print("#"*100)
    print("\n\n")
    #Describe the current situation to the user
    print("\t\t\t\t\t\tSCENARIO")

    print("""
    The Wizard has teleported you in front of the King's Palace. Acnologia appears
    before you and your comrades. His army is destroying the places nearby and killing
    innocent people. You order your comrades to help the King's army fight Acnologia's
    army and protect the citizens. You Decide to face Acnologia one on one. You are the
    last line of Defense. If you lose, the world will be ruled by the EVIL ACNOLOGIA!!!!
    """)

    input("<Press enter to continue>")

    print("""
    Natsu(You): Acnologiaaaaa!!!! You have taken your last life.

    Acnologia: NO. YOU HAVE LIVED YOUR LAST DAY

    You charge to attack Acnologia Head-On
    """)


    # Life of the final boss
    Acnologia = 100

    #attack of the final boss
    boss_attacks = [['Eternal flair',25] ,['Black Dragon Soul Technique',30], ['Ankhseram Black Magic',30], \
    ['Black Dragon Flame of Hell',35], ['Black Dragon\'s Roar',25], ['Black Eternal Susanoo',40], ['Black Fire Storm',50]]


    # Life of the user
    user_life = 100

    #attacks of the user
    your_attacks = [['Fire Dragon Slayer\'s Iron Fist', 25],['Crimson Lotus: Fire Dragon\'s Flame of Death', 40], \
    ['Fire Dragon\'s Roar',30]]

    #The following code runs until the user either wins the game or loses it
    loop_iterator = 0
    while(loop_iterator == 0):

        print(f"""
        Choose one move to attack Acnologia with:
        \t1. {your_attacks[0][0]}
        \t2. {your_attacks[1][0]}
        \t3. {your_attacks[2][0]}
        """)
        print("**** NOTE: ENTER THE NUMBER THAT REPRESENTS THE ATTACK ****")
        attack = int(input(">  "))

        if attack == 1:
            Acnologia = Acnologia - your_attacks[attack - 1][1]
            ran_choice = random.choice([0,1,2,3,4,5,6])
            user_life = user_life - boss_attacks[ran_choice][1]
            print('*'*100)
            print('*'*100)
            print(f"""
            You attacked Acnologia with {your_attacks[attack-1][0]} and did {your_attacks[attack-1][1]} damage.

            Acnologia attacked you with {boss_attacks[ran_choice][0]} and did {boss_attacks[ran_choice][1]} damage.
            """)


        elif attack == 2:
             Acnologia = Acnologia - your_attacks[attack - 1][1]
             ran_choice = random.choice([0,1,2,3,4,5,6])
             user_life = user_life - boss_attacks[ran_choice][1]
             print('*'*100)
             print('*'*100)
             print(f"""
             You attacked Acnologia with {your_attacks[attack-1][0]} and did {your_attacks[attack-1][1]} damage.

             Acnologia attacked you with {boss_attacks[ran_choice][0]} and did {boss_attacks[ran_choice][1]} damage.
             """)

        elif attack == 3:
             Acnologia = Acnologia - your_attacks[attack - 1][1]
             ran_choice = random.choice([0,1,2,3,4,5,6])
             user_life = user_life - boss_attacks[ran_choice][1]
             print('*'*100)
             print('*'*100)
             print(f"""
             You attacked Acnologia with {your_attacks[attack-1][0]} and did {your_attacks[attack-1][1]} damage.

             Acnologia attacked you with {boss_attacks[ran_choice][0]} and did {boss_attacks[ran_choice][1]} damage.
             """)
        else:
            print('*'*100)
            print("\nPlease Enter an appropriate response")

        if Acnologia <= 0:
            print("#"*100)
            print("#"*100)
            print("\n")
            print("""
                                !!!!!! You Win !!!!!!

            Acnologia in his dying breath declares you As THE KING OF DRAGONS

            You have successfully defeated Acnologia and saved the King.

            You have restored peace back to this world.



            """)
            print("""\t\t\t\t\t***** STAGE-3 CLEARED *****""")
            print("#"*100)
            print("#"*100)
            print("\n")
            loop_iterator = 1
            input("<Press enter to return to the main menu>")
            start()

        elif user_life <= 0:
            print("#"*100)
            print("#"*100)
            print("\n")
            print("""
                                     !!!!!! DEFEAT !!!!!!!

                You've failed!!!! Acnologia rips your heart out of the Chest.
                Acnologia Kills your comrades
                Acnologia Kills the King!!!!
                He is the new ruler of this world.
                This is World is now Doomed !!!!
            \n""")
            print("""\t\t\t\t\t***** STAGE-3 FAILED *****""")
            print("\n")
            print("#"*100)
            print("#"*100)
            loop_iterator = 1
            fail()

        else:
             print(f"""
             Your current life {user_life}%

             Acnologia's current life {Acnologia}%
             """)




def fail():
    """This functions activates when user loses the game and exits them to the start point."""

    print("\n")
    print("#"*100)
    print("""

        \t\t\t********** GAME OVER **********

    """)
    print("#"*100)
    print("\n\n")
    print("""

    Do you want to play again?
    1. Yes
    2. No

    *** NOTE: Enter the number ***
    """)
    print('\n')
    user_in = input("> ")
    if user_in == '1':
        start()
    else:
        print("\n\n")
        print("\t\t\t !!!!! BYE BYE !!!!!")
        print("\n\n")
        exit()

#Starts the game
start()
