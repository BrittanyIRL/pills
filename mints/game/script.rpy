# mints script - draft copy from RenPy
# remember to put a "return" at the end of the last scene 
# init:
    # image main_menu = Movie(size=(1200, 600), xalign=0.5, yalign=0, play="mainmenu.webm")


$ _game_menu_screen = None
$ renpy.register_sfont('new_sfont', 22, spacewidth=6)
# transition options: fade, pixelate, dissolve
# vpunch will shake the screen
# Declare a character that uses the sfont.
# Declare characters used by this game. 


##############################################################
## Declare all the initial stuff                            ##
## Declare characters                                       ##
## All setup is up here                                     ##
## Dependent variables are defined below                    ##
##############################################################


# want slow text mode

# Alter Character text
# Weird-looking.
# add in an arrow to continue text : ctc=anim.Blink("#")
define j = Character(_(''), color="#c8ffc8", window_left_margin=400, window_yminimum=100)
# make o italics
define o = Character(_(''), color="#c8ffc8", window_left_margin=0, window_yminimum=100)

#image to use as a bottom border so that text doesn't pop in and out
image background solid = "black.png" 

# Put all the videos here - one for each stress level.
# For now, while we only have 1 video for each, set all webm videos to _0 version

image chapter1_0 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="backvid", play="chapter1_0.webm")
image chapter1_1 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="backvid", play="chapter1_0.webm")
image chapter1_2 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="backvid", play="chapter1_0.webm")

image getup_0 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="backvid", play="getup_0.webm")
image getup_1 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="backvid", play="getup_0.webm")
image getup_2 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="backvid", play="getup_0.webm")

image chapter2_0 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="backvid", play="chapter2_0.webm")
image chapter2_1 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="backvid", play="chapter2_0.webm")
image chapter2_2 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="backvid", play="chapter2_0.webm")

image chapter3_0 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="backvid", play="chapter3_0.webm")
image chapter3_1 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="backvid", play="chapter3_0.webm")
image chapter3_2 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="backvid", play="chapter3_0.webm")

image chapter4_0 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="backvid", play="chapter4_0.webm")
image chapter4_1 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="backvid", play="chapter4_0.webm")
image chapter4_2 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="backvid", play="chapter4_0.webm")

image bag_0_0_1 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="backvid", play="bag_0_0_1.webm")
image bag_1_0_1 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="backvid", play="bag_0_0_1.webm")
image bag_2_0_1 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="backvid", play="bag_0_0_1.webm")

image bag_0_1_1 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="backvid", play="bag_0_1_1.webm")
image bag_1_1_1 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="backvid", play="bag_0_1_1.webm")
image bag_2_1_1 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="backvid", play="bag_0_1_1.webm")

image bag_0_1_0 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="backvid", play="bag_0_1_0.webm")
image bag_1_1_0 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="backvid", play="bag_0_1_0.webm")
image bag_2_1_0 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="backvid", play="bag_0_1_0.webm")

image bag_0_0_0 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="backvid", play="bag_0_0_0.webm")
image bag_1_0_0 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="backvid", play="bag_0_0_0.webm")
image bag_2_0_0 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="backvid", play="bag_0_0_0.webm")

image window1_0 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="backvid", play="window1_0.webm")
image window1_1 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="backvid", play="window1_0.webm")
image window1_2 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="backvid", play="window1_0.webm")

image window2_0 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="backvid", play="window2_0.webm")
image window2_1 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="backvid", play="window2_0.webm")
image window2_2 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="backvid", play="window2_0.webm")

image rafters_0 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="backvid", play="rafters_0.webm")
image rafters_1 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="backvid", play="rafters_0.webm")
image rafters_2 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="backvid", play="rafters_0.webm")

image busppl_0 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="backvid", play="busppl_0.webm")
image busppl_1 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="backvid", play="busppl_0.webm")
image busppl_2 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="backvid", play="busppl_0.webm")

image chapter5_0 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="backvid", play="chapter5_0.webm")
image chapter5_1 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="backvid", play="chapter5_0.webm")
image chapter5_2 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="backvid", play="chapter5_0.webm")

image coffeeshop_0 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="backvid", play="coffeeshop_0.webm")

image stoplight_0 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="backvid", play="stoplight_0.webm")
image stoplight_1 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="backvid", play="stoplight_0.webm")
image stoplight_2 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="backvid", play="stoplight_0.webm")

image chapter6_0 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="backvid", play="chapter6_0.webm")
image chapter6_1 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="backvid", play="chapter6_0.webm")
image chapter6_2 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="backvid", play="chapter6_0.webm")

image mgmt_0 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="backvid", play="mgmt_0.webm")
image mgmt_1 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="backvid", play="mgmt_0.webm")
image mgmt_2 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="backvid", play="mgmt_0.webm")

image clientmtg_0 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="backvid", play="clientmtg_0.webm")
image clientmtg_1 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="backvid", play="clientmtg_0.webm")
image clientmtg_2 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="backvid", play="clientmtg_0.webm")

image chapter7_0 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="backvid", play="chapter7_0.webm")
image chapter7_1 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="backvid", play="chapter7_0.webm")
image chapter7_2 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="backvid", play="chapter7_0.webm")

image end_of_lunch_0 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="backvid", play="chapter7_1.webm")
image end_of_lunch_1 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="backvid", play="chapter7_1.webm")
image end_of_lunch_2 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="backvid", play="chapter7_1.webm")

# then we have the three montage videos, for chapter 8, which we want to treat as not clickable videos

image chapter9_0 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="backvid", play="chapter9_0.webm")
# image chapter9_1 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="backvid", play="chapter9_0.webm")
# image chapter9_2 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="backvid", play="chapter9_0.webm")

image TV_0 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="backvid", play="TV_0.webm")

image chapter10_0 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="backvid", play="chapter10_0.webm")
image chapter10_end movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="backvid", play="chapter10_nosound.webm")

# image chapter10_1 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="backvid", play="chapter10_0.webm")
# image chapter10_2 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="backvid", play="chapter10_0.webm")

# then we have the credits which we want to treat as not clickable videos, but still want to keep the car alarm
# image credit_playback movie = Movie(size=(1200,600), channel='credits', play="credits.webm")
##############################################################
## Chapter 1 begins here                                    ##
## All counted dependents begin here                        ##
## Numbered chapters differ from other segments in that if  ##
## mints scene is triggered, player will skip to next       ##
## numbered chapter, missing all interim.                   ##
## Chapter 1 starts with getting out of bed                 ##
## Number of alarm snoozes is used numerous times later     ##
##############################################################


# The game starts here.
label start:
    
    # ADJUST THIS ONCE WE GET THE IMAGE MAP CREATED
    # options are: "Easy 0", "Normal 1", "Hard 2"
    $ difficulty = 1
    
    $ scene_count = 1
    $ stress_count = 0
    $ mints_count = 0
    $ snooze_count = 0
    $ coffee_choice = 0
    $ calendar_check = 0
    $ book_check = 0
    $ bag_check = 0
    $ bus_check = 0
    $ guy_talk = 0
    $ phone_talk = 0
    $ go_to_meeting = 0
    $ check_email = 0
    $ meeting_panic = 0
    $ at_coffee = 0
    
    $ randmtg = renpy.random.randint(1,4)
    $ randlng = renpy.random.randint(1,2)
    $ randjoke = renpy.random.randint(1,7)
    $ randwind = renpy.random.randint(1,2)

    scene black
    show background solid at left

    $ renpy.pause(1)
    
    j "There's this feeling..."
    j "right before I fall asleep,"
    j "right before I fade into dreamland,"
    j "where I actually feel like my mind is at peace."
    j "You can't sleep when your mind wanders."
    j "Everyone knows that."
    j "You have to tell your brain to be quiet,"
    j "get it to stop ticking,"
    j "stop running through the endless loose ends of your day."
    j "Only after that can you let go,"
    j "let loose of that all the alternate possibilities,"
    j "and fall into nirvana,"
    j "that peaceful, still silence."
    j "That moment..."
    j "That feeling of completeness..."
    j "That's what I wait for every single day."
    
    $ renpy.pause(1)

    scene chapter1_0 movie
    with fade
    show background solid at left

    
    play sound "sounds/alarm_clock.wav"

    $ randchp1 = renpy.random.choice(["Already? Wow.", "Please tell me it\'s Sunday.", "... How is it morning already?"])

    j "[randchp1]"
    j "That alarm is the worst noise."
    j "Every single day."
    j "I should get a new one."
    j "Honestly, who needs that kind of heart attack every morning?"
    j "..."
    j "Ugh..."
    j "I should probably get up."

    menu:

        "Get up.":

            jump getup

        "Hit snooze.":
            
            jump snooze_1


label getup:
 
    scene black
    with dissolve
    
    stop music fadeout 2.0
    
    if difficulty < 2:
        $ stress_count = 0

    if stress_count == 0:
        scene getup_0 movie
        with fade
        show background solid at left

    elif stress_count == 1:
        scene getup_1 movie
        with fade
        show background solid at left

    else:
        scene getup_2 movie
        with fade
        show background solid at left

    play music "sounds/mints_getting_ready.wav" fadein 2.0

    j "Another day." # "Here we go again." "Alright, alright, I'm up."
    
    if snooze_count < 1:
         j "I should cook something."
         j "I kind of hate it though."
         j "I’m immediately going to have to do all the dishes."
         j "Are the dishes even clean? I can’t remember."
         j "I could also grab something on my way in to work."
         j "Either way, at least I have coffee."
    elif snooze_count < 4:
         j "Do I have time to eat?"
         j "I guess I could grab something on my way in to work."
         j "I don’t know. Those coffees shops are getting so expensive."
         j "But do I have time to cook?"
         j "Making omelettes takes me like... 30 minutes."
         j "Why doesn't anyone invent more time-sensitive delicious breakfasts?"
         j "Because who even knows what they put in cereal nowadays?"
         j "Ugh, I can't decide."
    else:
         j "I can't believe I slept so much."
         j "There’s no way I have time to make something."
         j "I’m going to be lucky if I get anything to eat at all."
    
    menu:

        "Cook something even though it sucks.":

            jump cook

        "Grab something on the way instead.":
        
            jump grab

label cook:

    if snooze_count < 1:
         j "Fine, fine."
         j "Probably better for me anyways."
         j "Those oat bars are loaded with sugar."
         j "And one time, those savory scones put me on the toilet all morning."
         j "Probably the safest bet just to chill here."
         jump chapter2
    elif snooze_count < 4:
         j "Fine, I’ll cook something."
         j "Probably better for me anyways."
         j "But I won’t have much time."
         j "Might be late to work."
         j "Again..."
         $ stress_count += 1
         if stress_count > 2:
              j "That would be the third time this month."
              j "Wouldn't people start to talk?"
              j "I can't even think about that."
              jump mints_scene
         else:
              jump chapter2
    else:
         j "I should cook something..."
         j "I'm putting on weight, I know it."
         j "Those scones are essentially just fried butter."
         j "Who am I kidding? I don't have time for that!"
         j "I have to get out the door and off to work."
         j "Geez, what was I thinking?"
         $ Stress_count += 1
         $ coffee_choice = 1
         if stress_count > 2:
              "Already stressing myself out this much..."
              "And it's just the beginning of the day..."
              jump mints_scene
         else:
              jump chapter2


label grab:

    $ coffee_choice = 1
    if snooze_count < 1:
         j "Screw cooking. It’s a free country."
         j "I’m gonna get one of those sugar scones."
         j "I don’t care how horrible they are for you."
         j "Or even pound cake or something."
         j "Go totally crazy."
         j "I'm an adult."
         j "Sort of..."
         jump chapter2
    elif snooze_count < 4:
         j "Whatever. I don’t have time to cook."
         j "I’ll just grab something on the way."
         j "No need to freak out."
         j "Play it cool, man."
         j "Telling myself to be cool in a mirror."
         j "Just like in that one movie..."
         j "With like the cops and the ear and the lime and the coconut..."
         j "What was that called again?"
         j "Anyways, guess it's not all bad."
         jump chapter2
    else :
         j "I can get something on the way."
         j "I have time."
         j "Just going to stress myself out otherwise."
         jump chapter2
         

label snooze_1:

    $ snooze_count += 1

    scene chapter1_0 movie
    with fade
    show background solid at left
    
    play sound "sounds/alarm_clock.wav"

    j "Was that already 10 minutes?"
    j "Probably just a misunderstanding."

    menu:

        "Get up.":

            jump getup

        "Choose the snooze.":
            
            jump snooze_2


label snooze_2:

    $ snooze_count += 1 

    scene chapter1_0 movie
    with fade
    show background solid at left
    
    play sound "sounds/alarm_clock.wav"

    j "Damn."
    j "Fooled again."

    menu:

        "Get up.":

            jump getup

        "Snooze it up.":
            
            jump snooze_3
            

label snooze_3:

    $ snooze_count += 1
    
    scene chapter1_0 movie
    with fade
    show background solid at left
    
    play sound "sounds/alarm_clock.wav"

    j "Now I really don't know."
    j "Which do I hate more?"
    j "The alarm clock?"
    j "Or that car outside?"

    menu:

        "Get up.":

            jump getup

        "You can't lose to snooze.":

            jump snooze_4
            
    
label snooze_4:

    $ snooze_count += 1
    
    scene chapter1_1 movie
    with fade
    show background solid at left
    
    play sound "sounds/alarm_clock.wav"
    
    $ stress_count += 1
    
    j "It never stops."

    menu:

        "Get up.":

            jump getup

        "Snoozefest.":

            jump snooze_5
            
            
label snooze_5:

    $ snooze_count += 1
    
    scene chapter1_1 movie
    with fade
    show background solid at left
    
    play sound "sounds/alarm_clock.wav"

    j "My head is going to explode."

    menu:

        "Get up.":

            jump getup

        "Snoozapalooza.":

            jump snooze_6
            

label snooze_6:

    $ snooze_count += 1
    
    scene chapter1_1 movie
    with fade
    show background solid at left
    
    play sound "sounds/alarm_clock.wav"
    
    j "Nope."

    menu:

        "Get up.":

            jump getup

        "Snoozaroo.":

            jump snooze_7



label snooze_7:

    $ snooze_count += 1
    
    scene chapter1_2 movie
    with fade
    show background solid at left
    
    play sound "sounds/alarm_clock.wav"
    
    $ stress_count += 1

    j "I'm going to murder that car."

    menu:

        "Get up.":

            jump getup

        "Snoozechella.":

            jump snooze_8
            
    
label snooze_8:

    $ snooze_count += 1
    
    scene chapter1_2 movie
    with fade
    show background solid at left
    
    play sound "sounds/alarm_clock.wav"

    j "Ok, this time maybe the snooze will do something else."

    menu:

        "Get up.":

            jump getup

        "Choose the snooze.":

            jump snooze_9
            
            
label snooze_9:

    $ snooze_count += 1
    
    scene chapter1_2 movie
    with fade
    show background solid at left
    
    play sound "sounds/alarm_clock.wav"

    j "Is today over yet?"

    menu:

        "Get up.":

            jump getup

        "Choose the snooze.":

            jump snooze_10
            
    
label snooze_10:

    $ snooze_count += 1
    
    scene chapter1_2 movie
    with fade
    show background solid at left
    
    play sound "sounds/alarm_clock.wav"

    j "Holy crap I hit snooze 10 times?!"
    j "I overslept."
    j "I don't even have time to shower."
    j "I'm going to be so late."
    
    jump mints_scene
 

##############################################################
## mints scene begins here                                  ##
## This is the scene that happens when stress count > 2     ##
## Stress count is reset after this                         ##
## Scene count is pushed forward 1                          ##
##############################################################
    
label mints_scene:
    #scene that happens when stress count > 2

    scene black
    with dissolve
    
    if difficulty > 0:

        if mints_count == 0:
            j "I don't need this right now."
            j "I'm just going to handle it."
            j "Put it out of mind, that's all."
            j "Stay cool."   
        elif mints_count == 1:
            j "I'm not doing this."
            j "I have too much left to do today."
            j "I'm calling it, right here, right now."
            j "Gonna stay cool."
        elif mints_count == 2:
            j "I can't believe this."
            j "Why can't I get a grip today?"
            j "I'm not letting this get the best of me."
            j "I can't let this break my cool."
        elif mints_count == 3:
            j "What is going on today?"
            j "This isn't like me at all."
            j "I need to get a grip."
            j "And get on with my life."
            j "My cool, cool life."
        elif mints_count == 4:
            j "What the hell is happening?"
            j "I can't believe this."
            j "I am really struggling today."
            j "But nothing is going to stop me..."
            j "Nothing's going to break my cool."
        else:
            j "Alright."
            j "For the love of all that is holy..."
            j "Please let this be my last cool break today."
            j "How many calories are in these things anyways?"
    
        play sound "sounds/mint_bottle.wav"
        $ renpy.pause(2)
        play sound "sounds/exhale.wav"
    
        j "That's better."
        $ randmint = renpy.random.choice(["Nice and fresh.", "Hella fresh.", "So fresh."])
        j "[randmint]"
    
        $ mints_count += 1
        $ stress_count = 0
    
    #jump scene_%r % scene_count + 1
    if scene_count == 1:
        jump chapter2
    elif scene_count == 2:
        jump chapter3
    elif scene_count == 3:
        jump chapter4
    elif scene_count == 4:
        jump chapter5
    elif scene_count == 5 and coffee_choice > 0 and at_coffee < 1:
        jump coffeeshop
    elif scene_count == 5 and coffee_choice > 0 and at_coffee > 0:
        jump chapter6
    elif scene_count == 5 and coffee_choice < 1:
        jump chapter6
    elif scene_count == 6 and go_to_meeting > 0 and meeting_panic < 1:
        jump clientmeeting
    elif scene_count == 6 and go_to_meeting > 0 and meeting_panic > 0:
        jump chapter7
    elif scene_count == 6 and go_to_meeting < 1:
        jump chapter7
    elif scene_count == 7:
        jump end_of_lunch
    elif scene_count == 8:
        jump chapter9
    elif scene_count == 9:
        jump chapter10
    else:
        return

##############################################################
## Chapter 2 begins here                                    ##
## Chapter 2 involves an imagemap                           ##
## Collecting things before leaving for work                ##
##############################################################



# defining hotspots here, to be called later 
screen chapter2_map:
    imagemap:
        ground "blank.png"
        # Do I need to specify the base image?
        #hover "Hover.jpg" I don't want a hover change thing

        hotspot (22, 300, 314, 150) clicked Return("book")        #library book for bus/email
        hotspot (0, 0, 170, 205) clicked Return("bag")        #bag for bus pass
        hotspot (436, 406, 186, 194) clicked Return("calendar")   #calendar for meeting 
        hotspot (400, 50, 275, 300) clicked Return("door")      #door is leave

        
label chapter2:

    #getting out the door

    scene black
    with dissolve
    
    stop music fadeout 2.0
    
    $ scene_count += 1
    
    if stress_count == 0:
        scene chapter2_0 movie
        with fade
        show background solid at left

    elif stress_count == 1:
        scene chapter2_1 movie
        with fade
        show background solid at left

    else:
        scene chapter2_2 movie
        with fade
        show background solid at left

    
    play music "sounds/mints_chp2.wav"
    
    j "What am I forgetting?"
    j "I always forget something."
    j "And then I figure it out halfway through the day and it ruins everything."
    j "What do I need to grab before I head out the door?"

    jump chapter2_w_map

label chapter2_w_map:

    call screen chapter2_map
    
    $ result = _return
    
    if result == "book":
        $ book_check = 1
        j "Oh right I need to grab that library book."
        j "I think it's due already."
        j "And I just about to crack the secrets of the digital age..."
        j "Whatever. One more bus ride made less awkward."
        jump chapter2_w_map
    elif result == "bag":
        $ bag_check = 1
        j "Did I pack everything for today?"
        j "Oh wow, I almost forgot my bus pass."
        j "That would have been annoying."
        jump chapter2_w_map
    elif result == "calendar":
        $ calendar_check = 1
        j "Do I have anything at work today?"
        j "Sure doesn't look like it."
        j "Probably for the best."
        j "If anyone says anything to the contrary, I'm in full denial."
        jump chapter2_w_map
    elif result == "door":
        j "Guess I should hit the road."
        j "Hope whatever I forgot wasn't important."
        jump chapter3
        
##############################################################
## Chapter 3 begins here                                    ##
## Chapter 3 is a transition to see if you checked the bag  ##
## Getting on the bus before work                           ##
##############################################################

label chapter3:
    # bus stop

    scene black
    with dissolve
    
    stop music fadeout 2.0
    $ renpy.pause(1)
    
    if difficulty < 1:
        $ stress_count = 0

    $ scene_count += 1
    
    if stress_count == 0:
        scene chapter3_0 movie
        with fade
        show background solid at left

    elif stress_count == 1:
        scene chapter3_1 movie
        with fade
        show background solid at left

    else:
        scene chapter3_2 movie
        with fade
        show background solid at left

    
    play music "sounds/mints_chp3.wav"

    j "Bus arrives in... zero minutes?"
    j "It's not even down the hill yet."
    j "I can see the damn hill - it's not there."
    j "At least that gives me time to check email."
    j "Clear out another inbox full of spam alerts,"
    j "apologies for misdirected sensitive information,"
    j "countless newsletters I don't remember signing up for,"
    j "half of them for products that don't even apply to me."
    j "How berated with useless information are we, really?"
    j "Meanwhile, when you do try and use technology for good..."
    j "You look up the hill and question your sanity because there's no bus there."
    j "..."
    j "I wonder how much those small sanctions of every day life..."
    j "the plausibility of a missed bus..."
    j "the crosswalk you see in the distance that you might not catch..."
    j "the time you probably won't have left to go to the gym..."
    j "How many of those are responsible for all the stress you feel?"
    
    menu:
         "Some sanctions.":
             j "I mean, probably at least a couple."
             j "Other circumstances are probably a bit more universal."
             j "But which ones?"
             j "How the hell are you supposed to figure that out?"
             j "I'm not a genius or a social scientist."
             j "And yet somehow, we all need to learn how to deal."
             j "Well that's a hilarious gambit."
             j "Who's going to succeed at that?"
             $ stress_count += 1
             if stress_count > 2:
                 "And in the meantime..."
                 "It's just going to stress me out."
                 "So, so much..."
                 jump mints_scene
             else:
                 jump bus_time

         "All the sanctions.":
             j "Yeah. Probably the whole enchilada."
             j "Actually, admitting it like that kind of takes a load off."
             j "I can't possibly be the only one, right?"
             j "Maybe everybody else feels the same way."
             j "Or maybe not. Who knows?"
             j "I'm no genius."
             j "I'm just a guy trying catch his bus."
             j "On the way to another round of daily excitement."
             jump bus_time

         "Am I even using that word correctly?":
             j "Ah, never mind."
             j "I swear, I can get on these tangents with myself,"
             j "and get lost for days at a time."
             j "This one is hardly worth it."
             j "Boring conversation with myself anyway."
             j "Still... I'm deleting this app."
             j "The bus will show when it shows."
             j "There."
             j "I feel better already."
             jump bus_time
    
label bus_time:

    play sound "sounds/busarrival.wav"
    j "Here comes the bus, finally."
    
    if bag_check > 0:
        j "Glad I remembered my pass."
        j "That would have been really annoying."
        j "Let alone stressful."
        j "I'm gonna try and keep it at a minimum today."
        j "Stay cool."
    else:
        j "Let me just grab my pass..."
        j "Wait... where is it?"
        j "Did I take it out of my bag?"
        j "I totally took it out of my bag."
        j "Last night, when I was rushing to catch the bus back from downtown."
        j "Ugh."
        j "I hate everything."
        if difficulty > 0:
            $ stress_count += 2
            if stress_count > 2:
                jump mints_scene
            else:
                jump chapter4
        else:
            jump chapter4


##############################################################
## Chapter 4 begins here                                    ##
## On the bus headed to work                                ##
## Chapter 4 involves a hotspot for looking around the bus  ##
## The window should return a random choice of outside      ##
## This chapter also checks if in Chp2 you checked the book ##
##############################################################

label chapter4:
    # on the bus
    
    scene black
    with dissolve
    show background solid at left
    
    stop music fadeout 2.0
    
    if difficulty < 1:
        $ stress_count = 0
    
    $ scene_count += 1
    
    if stress_count == 0:
        scene chapter4_0 movie
        with fade
        show background solid at left
    elif stress_count == 1:
        scene chapter4_1 movie
        with fade
        show background solid at left
    else:
        scene chapter4_2 movie
        with fade
        show background solid at left
    
    play music "sounds/mints_chp4_p1.wav"

    if bag_check > 0:
        j "Only three minutes late today."
        j "That's a new record."
        j "Maybe today isn't all that bad."
        j "Probably never is."
        j "I'm kidding myself half the time."
    else:
        j "Late again."
        j "Absolutely figures - what a train wreck."
        j "I'm forming a pattern."
        j "Typical millennial, last one in, first one out."
        j "Begging for mercy from the shackles of the status quo."
    j "Look at me."
    j "Always choosing my own company to that of others."
    j "And you wonder why people go crazy."
    j "Doing this every single day."
    
    jump chapter4_w_map
    
    
# defining hotspots here, to be called later 
screen chapter4_map:
    imagemap:
        ground "blank.png"

        hotspot (163, 75, 332, 86) clicked Return("window")        #look out window
        hotspot (525, 132, 222, 204) clicked Return("openbag")        #look in yr bag
        hotspot (228, 268, 130, 84) clicked Return("ads")            #ads on bus 
        hotspot (0, 100, 163, 425) clicked Return("people")      #people on bus
        hotspot (429, 419, 297, 106) clicked Return("nothing")
    
label chapter4_w_map:
    
    if stress_count == 0:
        scene chapter4_0 movie
        show background solid at left
    elif stress_count == 1:
        scene chapter4_1 movie
        show background solid at left
    else:
        scene chapter4_2 movie
        show background solid at left
    
    call screen chapter4_map
    
    $ result = _return
    
    if result == "window":
        if randwind == 2:
            scene black
            with dissolve
            if stress_count == 0:
                scene window2_0 movie
                with fade
                show background solid at left
            elif stress_count == 1:
                scene window2_1 movie
                with fade
                show background solid at left
            else:
                scene window2_2 movie
                with fade
                show background solid at left
        else:
            scene black
            with dissolve
            if stress_count == 0:
                scene window1_0 movie
                with fade
                show background solid at left
            elif stress_count == 1:
                scene window1_1 movie
                with fade
                show background solid at left
            else:
                scene window1_2 movie
                with fade
                show background solid at left
        j "I look out the window."
        j "I see a city unsure of itself."
        j "Constantly wishing for change."
        j "Searching for something apart from the norm."
        j "Something to draw a crowd."
        j "Something new to be known by."
        j "I wonder if it will ever really find that."
        
        scene black
        with dissolve
        
        jump chapter4_w_map
    elif result == "openbag":
        if stress_count == 0 and calendar_check > 0 and book_check > 0:
            scene bag_0_1_1 movie
            show background solid at left
        elif stress_count == 1 and calendar_check > 0 and book_check > 0:
            scene bag_1_1_1 movie
            show background solid at left
        elif stress_count == 2 and calendar_check > 0 and book_check > 0:
            scene bag_2_1_1 movie
            show background solid at left
        elif stress_count == 0 and calendar_check < 1 and book_check > 0:
            scene bag_0_0_1 movie
            show background solid at left
        elif stress_count == 1 and calendar_check < 1 and book_check > 0:
            scene bag_1_0_1 movie
            show background solid at left
        elif stress_count == 2 and calendar_check < 1 and book_check > 0:
            scene bag_2_0_1 movie
            show background solid at left
        elif stress_count == 0 and calendar_check > 0 and book_check < 1:
            scene bag_0_1_0 movie
            show background solid at left
        elif stress_count == 1 and calendar_check > 0 and book_check < 1:
            scene bag_1_1_0 movie
            show background solid at left
        elif stress_count == 2 and calendar_check > 0 and book_check < 1:
            scene bag_2_1_0 movie
            show background solid at left
        elif stress_count == 0 and calendar_check < 1 and book_check < 1:
            scene bag_0_0_0 movie
            show background solid at left
        elif stress_count == 1 and calendar_check < 1 and book_check < 1:
            scene bag_1_0_0 movie
            show background solid at left
        elif stress_count == 2 and calendar_check < 1 and book_check < 1:
            scene bag_2_0_0 movie
            show background solid at left
        j "..."
        jump chapter4_w_map
    elif result == "ads":
        $ bus_check = 2
        scene black
        with dissolve
        if stress_count == 0:
            scene rafters_0 movie
            with fade
            show background solid at left
        elif stress_count == 1:
            scene rafters_1 movie
            with fade
            show background solid at left
        else:
            scene rafters_2 movie
            with fade
            show background solid at left
        j "Man alive."
        j "All I wanted to do was read the newspaper."
        j "But look at these ads."
        j "They line every page."
        j "Hell, they even line the rafters of the bus."
        j "Have you recently gone through a divorce?"
        j "Are you going through a fiscal dillema?"
        j "Have you lost your sexual potency?"
        j "Are you concerned your child is a sociopath?"
        j "Call here."
        j "Call there."
        j "Talk to someone, anyone."
        
        scene black
        with dissolve
        
        jump chapter4_w_choice
    elif result == "people":
        $ bus_check = 1
        scene black
        with dissolve
        if stress_count == 0:
            scene busppl_0 movie
            with fade
            show background solid at left
        elif stress_count == 1:
            scene busppl_1 movie
            with fade
            show background solid at left
        else:
            scene busppl_2 movie
            with fade
            show background solid at left
        j "Is everyone else on this bus just like me?"
        j "Aren't we all going through the motions,"
        j "lost in some dream of semi-fulfilling stability?"
        j "There's comfort in consistency, you know?"
        j "You don't have to think much about what's going on around you."
        j "But what do you really lose in the interim?"
        j "When do you stop being human,"
        j "and instead just become a robot?"
        j "At least robots don't talk to themselves inside their heads."
        j "Or I don't know..."
        j "maybe they do, too."
        
        scene black
        with dissolve
        
        jump chapter4_w_choice

    elif result == "nothing":
        j "Does that make me socially avoidant?"
        j "I guess I don't twice about it most days."
        j "But if I try and see it from someone else's point of view..."
        j "Here I am at the back of the bus, tuning out the world."
        j "Crumpled up in a ball, halfway in the fetal position."
        j "Maybe nothing's wrong with the world and all of its dealings."
        j "Maybe it's all just how I choose to respond to it."

        jump chapter4_w_choice
        
label chapter4_w_choice:

    if stress_count == 0:
        scene chapter4_0 movie
        with fade
        show background solid at left
    elif stress_count == 1:
        scene chapter4_1 movie
        with fade
        show background solid at left
    else:
        scene chapter4_2 movie
        with fade
        show background solid at left
    
    play music "sounds/mints_chp4_p2.wav"
    
    if bus_check > 1:
        j "You can't really help but think about it can you?"
        j "Seeing all those problems,"
        j "imagining yourself in the thick of it all,"
        j "even just to feel something."
        j "And yet, everyone has a choice."
        j "I have it, too."
        j "To stare onwards searching for feeling..."
        j "or to turn and run from it."
    elif bus_check > 0:
        j "You can't really help but think about it can you?"
        j "Seeing all the comfort in repetition,"
        j "maybe not so intentional so much as blissfully naive..."
        j "Am I one of them?"
        j "Maybe I have to look closer."
        j "Maybe we all do."
        j "That's our choice, really..."
        j "To stare onwards, searching for reason..."
        j "or to turn and run."
    else:
        j "I just have this feeling."
        j "This indescribable itch."
        j "I guess you could call it a fear of missing out,"
        j "but I don't know what I'm afraid of"
        j "and I'm not sure where I want to go..."
        j "It's more of an urge, I guess."
        j "An urge to find what it is that makes the world tick."
        j "What makes everyone else get out of bed in the morning?"
        j "Some days, it's pretty rough finding a reason."
        j "But it can't all be status quo, if you stare at it long enough."
        j "I guess that's my choice..."
        j "To stare onwards,"
        j "or to turn and run."

    menu:

         "Stare onwards.":

             jump onwards

         "Turn and run.":
        
             jump turn_and_burn

         "Read a book instead.":
        
             jump book_instead
            
label onwards:   
    
    j "Right... I need to keep staring."
    j "Keep trying to find some sense in all of it."
    if bus_check > 1:
        j "But geez, look at all there is to deal with."
        j "There are so many people in the world making ends meet..."
        j "Like I have any of the answers..."
        j "Who am I to think I'm any better than them?"
    elif bus_check > 0:
        j "But everyone else, they keep staring too."
        j "Every step of the way, we are all keeping tabs."
        j "Making sure no one rises above the rest."
        j "Who am I to think I'm any better than them?"
    else:
        j "But what's the point?"
        j "There's so much no one has told me how to plan for or avoid."
        j "Who am I to think I'm going to win the Golden Ticket,"
        j "somehow figure all of this stuff out before the rest of them?"
    $ stress_count += 2
    if stress_count > 2:
        jump mints_scene
    else:
        jump chapter5

label turn_and_burn:
    
    j "Probably best to avoid it."
    j "That conversation is terrifying anyways."
    if bus_check > 1:
        j "I don't want to know about all this stuff."
        j "The 18 things my loved ones don't know about erectile dysfunction."
        j "The 6 ways my pre-teen can find drugs before they reach high school."
        j "The 27 different ways I can die from an open wound on the street."
        j "I'm not interested."
        j "I'm not doing that to myself."
    elif bus_check > 0:
        j "I don't want to know how other people cope."
        j "My life is messy enough as it is."
        j "Doing my best every day to try and play the wallflower..."
        j "staying out of people's way."
        j "I don't need to add to the noise."
    else:
        j "I mean, what's the point?"
        j "I'm not doing too bad."
        j "Sitting here in my tiny comfort zone."
        j "Everyone else has their problems and I have mine."
        j "I don't need to add to the noise."
    $ stress_count += 1
    if stress_count > 2:
        jump mints_scene
    else:
        jump chapter5
         
label book_instead: 
    
    j "Wait..."
    j "Why am I doing this to myself?"
    j "I don't have to figure any of this stuff out."
    j "I don't have to read the ads."
    j "I don't have to talk to people."
    j "Hell, I don't really have to do anything at all."
    j "I can just read instead."
    j "I should have that book in my bag..."
    if book_check > 0:
        j "Yep, there it is."
        j "See? Nothing to worry about at all."
        j "Just the voice inside my head telling me everything is gonna be alright."
        jump chapter5
    else:
        j "Wait, did I forget those library books?"
        j "Aren't they due today?"
        j "That's the third time this month!"
        j "I can't do anything right, not even relax!"
        $ stress_count += 2
        if stress_count > 2:
            jump mints_scene
        else:
            jump chapter5

##############################################################
## Chapter 5 begins here                                    ##
## Walking in to work                                       ##
## Short transition before coffee shop or get in            ##
##############################################################
         
label chapter5:

    scene black
    with dissolve
    
    if difficulty < 2:
        $ stress_count = 0
    
    stop music fadeout 2.0
    $ renpy.pause(1)
    
    j "Once I leave the bus, the mood of the day changes."
    j "I feel a weight lift, though I'm not sure why."
    j "I no longer feel responsible for my own anxiety."
    j "Now, out in the wilds of a city in flux,"
    j "everything is a shared venture."
    j "And even though that in and of itself can be stressful,"
    j "somehow, there's something reassuring about it."
    j "When the unexpected strikes, we are all in it together."
    j "We all share the outcome."
    j "And we all get to find the humor in it, somehow."
    
    $ scene_count += 1
    
    if stress_count == 0:
        scene chapter5_0 movie
        with fade
        show background solid at left
    elif stress_count == 1:
        scene chapter5_1 movie
        with fade
        show background solid at left
    else:
        scene chapter5_2 movie
        with fade
        show background solid at left
    
    play music "sounds/mints_chp5_p1.wav"

    j "I've been thinking..."
    j "Every day I take the same exact steps to work."
    j "Well, maybe not exact."
    j "I guess I always deviate a stoplight or two along the way."
    j "But other than that, nothing - no variation."
    j "And when I do try and mix it up, breaking this way or that,"
    j "heading down a block or two to hit the better coffee shop,"
    j "or going to the ATM before work so I don't have to go after,"
    j "there's this tiny sting,"
    j "this simple twitch of a feeling,"
    j "that tells me something is wrong."
    j "All our studies on evolution and anthropology,"
    j "they tell us that humans have succeeded due to natural selection."
    j "The greater comprehension of survival and understanding of self,"
    j "that's what allowed humans to persevere."
    j "I mean, sure, that was hundreds of thousands of years ago."
    j "But when I take the longer path to work and feel that twitch,"
    j "when I feel the hair standing up on the back of my neck,"
    j "like someone is watching me,"
    j "waiting to tell me I'm out of line,"
    j "I wonder,"
    j "where are we now?"

    scene black
    with dissolve

    if stress_count == 0:
        scene stoplight_0 movie
        with fade
        show background solid at left
    elif stress_count == 1:
        scene stoplight_1 movie
        with fade
        show background solid at left
    else:
        scene stoplight_2 movie
        with fade
        show background solid at left

    play music "sounds/mints_chp5_p2.wav"
    
    j "Hunter-gatherers worked in teams to survive."
    j "They'd take down giant wooly mammoths by overwhelming them."
    j "Larger nomadic villages meant greater security for everyone."
    j "Nowadays, it's the opposite."
    j "Half a dozen people all standing at a stoplight,"
    j "and none of us feel rewarded for communicating."
    j "No one feels safety in numbers in the company of strangers."
    j "I could try and make smalltalk to alleviate the boredom,"
    j "but half the time I'm afraid I'll inadvertently offend someone."
    j "Like my greeting will be seen as a narcissistic cry for attention."
    j "Just another heterosexual cisgender white male,"
    j "waltzing down the street, pretending the world is his."
    j "But I don't know..."
    j "How else am I supposed to engage with other people?"
    j "Do I keep on with my dissipating college friends and coworkers forever?"
    j "Whose to say one casual interaction won't lead to a lifelong friend?"

    menu:
         "Try smalltalk.":
             menu:
                  "Hi?":
                      j "What was that?"
                      j "That was horrible."
                      j "No one even turned."
                      j "Who was I even talking to anyways?"
                      j "That was idiotic."
                      j "I'm just going to go to work."
                      $ stress_count += 1
                      if stress_count > 2:
                          jump mints_scene
                      elif coffee_choice > 0:
                          jump coffeeshop
                      else:
                          jump chapter6
                  "Hey there, stranger!":
                      j "Oh god, I have no idea why I did that."
                      j "The deafening silence is actually kind of a relief."
                      j "I might as well have offered to pay people to hang out with me."
                      j "Why am I so socially inept?" 
                      $ stress_count += 2
                      if stress_count > 2:
                          jump mints_scene
                      elif coffee_choice > 0:
                          jump coffeeshop
                      else:
                          jump chapter6
                  "Nice weather today.":
                      play sound "sounds/mints_xwalk_weather.wav"
                      $ renpy.pause(1)
                      j "Ok, a few token nods and mumbles for the world's best elevator cliche."
                      j "Still, it could have been worse."
                      j "No lifelong friends, but no disgust either."
                      j "Maybe there's comfort in monotony after all."
                      if coffee_choice > 0:
                          jump coffeeshop
                      else:
                          jump chapter6
                  "How about them Hawks?":
                      play sound "sounds/mints_xwalk_hawks.wav"
                      $ renpy.pause(2)      
                      j "Is he talking about the game last Sunday?"
                      j "I didn't watch that!"
                      j "I have no idea what he's talking about."
                      j "I could just nod, smile, look excited."
                      j "Wait, did he just ask me an actual question?"
                      j "That requires my response?"
                      j "I dont know, I wasn't paying attention."
                      j "I'm just going to fake a call and walk away."
                      j "I'm never doing that again."
                      $ stress_count += 2
                      if stress_count > 2:
                          jump mints_scene
                      elif coffee_choice > 0:
                          jump coffeeshop
                      else:
                          jump chapter6

         "Keep to yourself.":
             j "Nope. That never happens."
             j "Especially after you are out of college and into the world."
             j "Then you just become another potential freakshow."
             j "Walking down the street, whispering to no one."
             j "Debating the pros and cons of decisions to two voices in your head."
             j "I wouldn't want me to talk to me either."
             if coffee_choice > 0:
                 jump coffeeshop
             else:
                 jump chapter6
    
    
##############################################################
## Coffee shop begins here                                  ##
## Only triggered if user chose coffee before               ##
## This involves trigger with jerk at coffee shop           ##
## This will come back later in the office                  ##
##############################################################
         
label coffeeshop:
    
    scene black
    with dissolve
    
    stop music fadeout 2.0
    
    if difficulty < 1:
        $ stress_count = 0
    
    if stress_count == 0:
        scene coffeeshop_0 movie
        with fade
        show background solid at left
    elif stress_count == 1:
        scene coffeeshop_0 movie
        with fade
        show background solid at left
    else:
        scene coffeeshop_0 movie
        with fade
        show background solid at left
    
    play music "sounds/mints_coffee_shop.wav"
    
    $ at_coffee += 1

    j "I could do better."
    j "Always."
    j "I could get out of my head."
    j "Get far away from this daily ritual."
    j "And yet here I am..."
    j "In a room of people perusing and standing in lines."
    j "All waiting on the same buzz to kick off the day."
    j "One credit card at a time."
    j "All the people here, killing time like me."
    j "Waiting for something to happen."

    play sound "sounds/mints_coffee_shout.wav"
    $ renpy.pause(2)
    
    j "Damn, what is that guy up there yelling about?"
    j "He's already through the line."
    j "Waiting on his coffee for all of like... what, two minutes?"
    j "He's really chewing that barista out."
    j "He's being completely unfair..."
    j "This isn't right."
    j "I should say something..."
    
    menu:

         "Stay quiet.":

             jump quiet_coffee

         "Get involved.":
        
             jump loud_coffee

         "Leave without coffee.":
                 
             jump nada_coffee
            
label quiet_coffee:
    
    j "..."
    j "It isn't my place..."
    j "But he's not stopping."
    j "What a complete jerk."
    j "I don't want to intrude, but wow, this is horrible."
    j "All these other people too, just like me..."
    j "Watching and waiting,"
    j "waiting for the discomfort to pass,"
    j "not her discomfort... ours."
    j "It's wrong."
    j "I'm better than this, aren't I?"

    menu:

         "Stay staying quiet.":
             j "No..."
             j "I really shouldn't get involved."
             j "It's all ridiculous enough as it is."
             j "That guy will get what's coming to him."
             j "Still horrible to listen to."
             
             $ stress_count += 1
             if stress_count > 2:
                 jump mints_scene
             else:
                 jump chapter6

         "Get involved.":
        
             jump loud_coffee

label loud_coffee:

    $ guy_talk += 1
    
    j "Hey man, how about you quit hassling her?"
    o "Excuse me?"
    o "This is a whole milk latté."
    o "Every barista here knows I only drink nonfat milk."
    o "Every barista who actually wants to keep their job, that is."
    
    j "Come on, man."
    j "That's a ridiculous complaint."
    j "It's an honest mistake - just roll with it!"
    j "How bad can it be?"
    
    o "You are a complete ass, you know that?"
    o "If you ever talk to me again, I swear I'll punch you in the face."
    o "And forget this stupid coffee shop."
    o "I always hated it here anyways."
    o "I'm out of here."
    
    j "..."
    j "Thank god he's gone."
    j "What a moron."
    j "But now everyone is staring at me, like I'm the one that did something wrong."
    j "Why are they doing that?"
    j "Did I break the unspoken pact to stay out of the way?"
    j "Is that all the thanks I get for trying to be a good person?"
    j "Forget it."
    j "That wasn't worth it at all."

    $ stress_count += 2
    if stress_count > 2:
        jump mints_scene
    else:
        jump chapter6
         
label nada_coffee:

    j "Forget this, I'm leaving."
    j "That guy is way too much of a jerk to deal with today."
    j "Now I'm going to be hungry all morning."
    j "Ah, man..."
    j "That just makes me hate that guy even more!"
    j "Forget it, I don't even care."
    j "I'm just going to get my ass to work."
    j "The only sane place anywhere outside the confines of my apartment."
    j "How's that for irony?"

    $ stress_count += 1
    if stress_count > 2:
        jump mints_scene
    else:
        jump chapter6


##############################################################
## Chapter 6 begins here                                    ##
## Short chapter about getting in                           ##
## Small, immediate choices for meeting chapters            ##
## Phone will trigger mgmt meeting or not                   ##
##############################################################
         
label chapter6:

    scene black
    with dissolve
    
    stop music fadeout 2.0
    $ renpy.pause(1)
    
    if difficulty < 2:
        $ stress_count = 0
    
    $ scene_count += 1
    
    j "Once I exit the streets..."
    j "That semblance of control fades completely."
    j "I am no longer the arbiter of my own anxiety."
    j "Now, roaming the halls, strolling by the coffee maker..."
    j "I have plenty of volunteers, waiting to jump in."
    j "There's humor in that, right?"
    j "At least a little bit..."
    j "Maybe?"
    
    if stress_count == 0:
        scene chapter6_0 movie
        with fade
        show background solid at left
    elif stress_count == 1:
        scene chapter6_1 movie
        with fade
        show background solid at left
    else:
        scene chapter6_2 movie
        with fade
        show background solid at left
    
    play music "sounds/mints_chp6_begin_ost.wav"
    
    if bag_check > 0:
        j "Alright."
        j "I made it into work."
        j "The hard part is over."
        j "From here, the boredom is all well within the realm of reason."
        j "I just need to make it through without losing my cool."
        j "Let's see..."
        j "What to do..."
        
    else:
        j "What a morning."
        j "Look at me."
        j "I feel like I need a break even before my day has started."
        j "Alright, alright, I can cool down..."
        j "I just need to take a moment..."
        
    menu:

         "Check nonexistent email.":
             
             $ check_email += 1
             j "Guess I should sift through my inbox..."
             j "Wait..."
             j "What is this email about a meeting?"
             
             if randmtg == 1:
                 j "Something about a renewed business plan?"
                 j "Focus on big picture."
                 j "Moving the wheels of history..."
                 j "Wait, where have I heard that before?"
                 if calendar_check > 0:
                     j "I don't have anything today - I checked my calendar."
                     j "This can't be for me."
                 else:
                     j "Still..."
                     j "Am I supposed to go to this?"
                     j "Is this on my calendar?"
                     j "I have no idea."
                     
             elif randmtg == 2:
                 j "Something about bad quarterly earnings?"
                 j "Yada yada yada..."
                 j "Trying to turn things around in the future..."
                 j "Well, yeah. Aren't we all?"
                 if calendar_check > 0:
                     j "I don't have anything today - I checked my calendar."
                     j "This can't be for me."
                 else:
                     j "Still..."
                     j "Am I supposed to go to this?"
                     j "Is this on my calendar?"
                     j "I have no idea."

             elif randmtg == 3:
                 j "Something about globalized marketing outreach?"
                 j "Globally unified..."
                 j "Traditionally untraditional..."
                 j "Could there be any more hot words in here?"
                 j "This is bonkers."
                 if calendar_check > 0:
                     j "I don't have anything today - I checked my calendar."
                     j "This can't be for me."
                 else:
                     j "Still..."
                     j "Am I supposed to go to this?"
                     j "Is this on my calendar?"
                     j "I have no idea."

             elif randmtg == 4:
                 j "Something about an updated benefits package?"
                 j "Wow, I wonder if I get acupuncture now..."
                 j "Oh wait, it's not for me. It's for someone else..."
                 j "Whatever."
                 if calendar_check > 0:
                     j "I don't have anything today - I checked my calendar."
                     j "This can't be for me."
                 else:
                     j "Still..."
                     j "Am I supposed to go to this?"
                     j "Is this on my calendar?"
                     j "I have no idea."

             jump phonering

         "Do menial labor.":
             j "I got it."
             j "Desk cleaning time."
             j "That will put my mind at peace."
             j "You know, it really is disturbing how dirty your workspace gets."
             j "Look how much dead skin there is just buried in my keyboard."
             j "If I shook that thing upside down it would look like a blizzard."
             j "And look at all these little hairs all over my papers and my mousepad!"
             j "Do I really stress myself out that much?"
             j "Or are we all really falling apart under these damn fluorescents?"
        
             jump phonering
         
         "Reread 7 Habits of Highly Effective People.":
             j "Right."
             j "I gotta focus up with some genius stuff."
             j "I need independence..."
             j "I NEED SYNERGY."
             j "I have no idea how to get synergy, though."
             j "I barely have enough normal kind of energy, most days."
             if book_check > 0:
                 j "Oh, that reminds me."
                 j "I have to hit the library on my lunch to return those books."
             else:
                 j "Ah crap."
                 j "This just reminds me I forgot those damn library books again."
                 j "I hate books."
                 $ stress_count += 1
                 if stress_count > 2:
                     jump mints_scene
                 else:
                     jump phonering
         
         "Get hyped by watching inspirational movie clips.":
             j "I know what it is."
             j "I just need some fire under me."
             j "I'm gonna find that 90s movie."
             j "Where Alec Baldwin is that total jerk sales god."
             j "Only closers get oxygen!"
             j "Something like that."
             j "Is the title four words or three?"
             
             jump phonering
         
         "Make sure to get the memo.":
             j "I sure try and take the initiative to..."
             j "Wait, do we even do memos anymore?"
             j "Why do I feel this sudden need to make sure I got the memo?"
             j "I swear, they put something in the air conditioning here."
             j "Makes us all crazy."
             
             jump phonering
         
         "Sit and wait for something to happen.":
             j "Yeah..."
             j "I'm not doing anything."
             j "I deserve just a second to gather my thoughts."
             j "No noise."
             j "No commitments..."
             j "Just that fleeting daily moment of..."
         
             jump phonering

label phonering:
  
    play sound "sounds/ringer.wav"
    $ renpy.pause(1)
    
    j "Oh crap."
    j "Who is that?"
    j "I don't recognize the number."
    j "Probably a telemarketer..."
    j "But what if it's someone important?"
    j "I don't know..."
    j "Haven't I already done enough this morning?"
    
    menu:

         "Answer phone.":
             jump phonecall

         "Don't answer phone.":
             jump nocall

##############################################################
## Phone call w/ mgmt begins here                           ##
## Talk with manager about client meeting                   ##
## Menu option dependent on if you check calendar earlier   ##
## will trigger client meeting                              ##
##############################################################
         
label phonecall:
    
    j "Hello?"
    
    o "Joe."
    o "It's Tom."
    o "From across the hall."
    
    j "Hi Tom..."
    j "It's Joseph, not Joe."
    j "I hate it when people call me Joe."
    
    o "Alright, then!"
    
    j "..."
    j "What do you need?"
    
    stop music fadeout 4.0
    
    o "I was just checking in before our big meeting today."
    o "Making sure you are all set to go for your presentation!"
    
    j "..."
    
    play music "sounds/mints_mgmt_talk.wav"
    
    if calendar_check > 0:
    
        menu:
        
             "What presentation?":
                 o "Hah! Good one, Joe."
                 o "With that kind of confidence, I know you're fine."
                 o "No need to micromanage."
                 o "I'll see you in the conference room at 10."
                 o "Later!"
                 
                 j "..."
                 j "What the hell just happened?"
                 
                 $ go_to_meeting += 1
             
                 jump clientmeeting
             
             "Oh right, the presentation!":
             
                 o "Come on now, Joe."
                 o "Don't give me a heart attack like that."
                 o "You didn't forget to write it down on your calendar did you?"
                 
                 j "Hah."
                 j "No."
                 j "Of course, not."
                 
                 o "There! That's right."
                 o "That's the Joe I know."
                 o "See you at 10."
                 
                 j "..."
                 j "What the hell just happened?"
                 
                 $ go_to_meeting += 1
                 
                 jump clientmeeting
             
             "I don't have anything on my calendar...":
             
                 o "What?"
                 o "You don't?"
                 o "Well you must have forgotten it!"
                 
                 menu:
                      "Maybe I did...":
                      
                          j "It's possible..."
                          
                          o "Well I hope you come up with something quick, Joe."
                          o "We have a big client in there with a lot on the line."
                          o "You better whip something up in a hurry."
                          o "See you at 10, god willing."
                          
                          j "..."
                          j "What did I just get myself into?"
                          j "I am so screwed."
                          
                          $ go_to_meeting += 1
                          
                          if difficulty > 0:
                              $ stress_count += 2
                              if stress_count > 2:
                                  jump mints_scene
                              else:
                                  jump clientmeeting
                          else:
                              jump clientmeeting      
                      
                      "No way, José.":
                      
                          jump more_deliberating
  
    else:
    
        menu:
        
             "What presentation?":
                 o "Hah! Good one, Joe."
                 o "With that kind of confidence, I know you're fine."
                 o "No need to micromanage."
                 o "I'll see you in the conference room at 10."
                 o "Later!"
                 
                 j "..."
                 j "What the hell just happened?"
                 
                 $ go_to_meeting += 1
             
                 jump clientmeeting
             
             "Oh right, the presentation!":
             
                 o "Come on now, Joe."
                 o "Don't give me a heart attack like that."
                 o "You didn't forget to write it down on your calendar did you?"
                 
                 j "Hah."
                 j "No."
                 j "Of course, not."
                 
                 o "There! That's right."
                 o "That's the Joe I know."
                 o "See you at 10."
                 
                 j "..."
                 j "What the hell just happened?"
                 
                 $ go_to_meeting += 1
                 
                 jump clientmeeting

label more_deliberating:

    o "Joe, I'm in my office right now."
    o "I'm standing at my window, looking out at the world."
    o "And I'm not seeing you."
    o "Where are you, son?"
    o "This meeting is serious business."

    menu:
    
        "Wherever you want me to be, Tom.":
            if randjoke == 1:
                o "Joe, that's just the kind of dedication this team really needs."
                o "And you are an inspiration to us all."
                o "Forget the meeting."
                
                j "Wait... what?"
                
                o "That's right."
                o "I'll handle it all."
                o "You just keep walking that extra mile around the office today."
                o "I'm proud of you, son."
                o "Talk to you later."
                
                j "..."
                j "Alright."
                j "If anybody else has any curveballs to throw,"
                j "now's your chance."
                j "..."
                j "None?"
                j "Alright, I'm going to lunch."

                jump chapter7
            else:
                o "Joe, while I admire your sincere dedication to the company..."
                o "I won't pretend that doesn't come off a bit creepy."
                o "I'll see you in the meeting at 10."
                o "But let's try to keep it professional in there."
                o "Talk to you then."
                
                j "This is not good."
                
                jump clientmeeting
        
        "I'm right behind you, Tom.":
            if randjoke == 2:
                o "Holy smokes."
                o "Joe, you scared me there."
                
                j "Sorry about that."
                
                o "No, don't apologize."
                o "I get it. It's figurative, or something like that."
                o "This kind of job takes initiative,"
                o "and you are right behind me, every step of the way."
                o "I appreciate the daylights out of that, son."
                
                j "Thank you?"
                
                o "Don't worry about the meeting."
                o "I'm pretty sure I can handle it."
                o "But I know who's right behind me if I get into trouble."
                o "I'll talk to you later, Joe."
                
                j "..."
                j "Alright."
                j "If anybody else has any curveballs to throw,"
                j "now's your chance."
                j "..."
                j "None?"
                j "Alright, I'm going to lunch."

                jump chapter7
            else:
                o "Holy smokes."
                o "Joe, don't scare me like that."
                o "I know all about your work as a magician on nights and weekends."
                o "But here in the office, let's try and keep it civil."
                o "I'll see you in the meeting at 10."
                o "Later."
                
                j "This is not good."
                
                jump clientmeeting
        
        "In my same old cubicle, watching the years fly by.":
            if randjoke == 3:
                o "I have to hand it to you, Joe."
                o "You're right."
                o "How many years have we all been here?"
                o "In these tiny prisons, like lambs to the slaughter?"
                
                j "I have no idea, Tom."
                
                o "You know what?"
                o "You've inspired me."
                o "Change needs to start happening around here."
                o "And it needs to start right now."
                o "I'm putting off this meeting until we get things moving."
                o "There's no time to wait!"
                o "We need to seize the day!"
                o "Talk to you later."
                
                j "..."
                j "Alright."
                j "If anybody else has any curveballs to throw,"
                j "now's your chance."
                j "..."
                j "None?"
                j "Alright, I'm going to lunch."

                jump chapter7
            else:
                o "Well apparently they moved you sometime recently."
                o "Because I don't see you anywhere."
                o "Better get to that meeting at 10, though."
                o "It's in the conference room."
                o "Which is still in the same place it's been for years."
                o "Just for the record."
                o "Talk to you then."
                
                j "This is not good."
                
                jump clientmeeting
        
        "Far, far away, Tom.":
            if randjoke == 4:
                o "Wait... really?"
                o "That's..."
                o "Actually, that's quite respectable, son."
                
                j "Wait... what?"
                
                o "That's right."
                o "I respect that kind of ability to remove yourself from your job."
                o "What kind of automated wind up toys are we if we never escape the rat race?"
                o "I like your style, Joe."
                o "Don't worry about the meeting."
                o "I'll handle it with newfound inspiration."
                o "Talk to you later."
                
                j "..."
                j "Alright."
                j "If anybody else has any curveballs to throw,"
                j "now's your chance."
                j "..."
                j "None?"
                j "Alright, I'm going to lunch."

                jump chapter7
            else:
                o "Well wherever that is Joe..."
                o "I highly suggest you geographically relocate."
                o "So that you end up in the conference room at 10."
                o "No problem with traveling as long as you are punctual."
                o "Talk to you then."
                
                j "This is not good."
                
                jump clientmeeting
        
        "I'm all the way up, Tom.":
            if randjoke == 5:
                o "Like hell you are, Joe."
                o "And you know what?"
                o "Nothing can stop you."
                
                j "That's absolutely right, Tom."
                
                o "Forget the presentation."
                o "I'll handle it all."
                o "You just keep doing you today, son."
                o "I'm proud of you."
                o "Talk to you later."
                
                j "..."
                j "Alright."
                j "If anybody else has any curveballs to throw,"
                j "now's your chance."
                j "..."
                j "None?"
                j "Alright, I'm going to lunch."

                jump chapter7
            else:
                o "Like hell you are, Joe."
                o "And you know what?"
                o "Nothing can stop you."
                
                j "That's absolutely right, Tom."
                
                o "Specifically..."
                o "Nothing can stop you from being in the conference room at 10."
                o "For your presentation."
                o "I'll talk to you then."
                
                j "This is not good."
                
                jump clientmeeting
        
        "I'm your worst nightmare, Tom.":
            if randjoke == 6:
                o "Hold on a hot minute, Joe."
                o "Nobody ever said anything like that."
                o "Wherever you are, sit down and second and hear me out."
                
                j "Wait... what?"
                
                o "I may be a bit stressed by this presentation."
                o "But in no way does this make you a nightmare to work with."
                o "We all have our up days and down days."
                o "You just have to take the rose with the thorns."
                o "I had my fair share of parental disagreements as well."
                o "But you can't let it get to your self esteem."
                o "You are nobody's worst nightmare."
                o "No need to worry about the presentation."
                o "Just take the morning to get that self esteem back up where it should be."
                o "I'll check in later."
                
                j "..."
                j "Well that was surprisingly heartwarming."
                j "If anybody else has any curveballs to throw,"
                j "now's your chance."
                j "..."
                j "None?"
                j "Alright, I'm going to lunch."

                jump chapter7
            else:
                o "Joe, in all honesty."
                o "My worst fear is surviving the Armageddon."
                o "And finding myself utterly alone in the aftermath."
                o "But that's not really relevant right now."
                o "My second biggest fear is that you screw up this presentation."
                o "I'll see you in the conference room at 10."
                o "Bring your A-game."
                
                j "This is not good."
                
                jump clientmeeting
        
        "I don't have money, Tom, but what I do have is a very particular set of skills.":
            if randjoke == 7:
                o "Joe, why do you think we hired you in the first place?"
                o "We know you have... some type of skills."
                o "And stay here long enough, you won't have to worry about the money."
                o "If you are really concerned about it in the meantime..."
                o "Maybe you should cut down on your coffee budget or something."
                
                j "Wait... what?"
                
                o "I get it."
                o "This presentation is stressing you out, isn't it?"
                o "You know what?"
                o "Forget it."
                o "I know the client."
                o "I can handle the whole thing."
                o "Take the rest of the morning and chill out."
                o "Remember the skills that got you here, and visualize the money."
                o "None of it's taken for granted here."
                o "I'll talk to you later."
                
                j "..."
                j "Alright."
                j "If anybody else has any curveballs to throw,"
                j "now's your chance."
                j "..."
                j "None?"
                j "Alright, I'm going to lunch."

                jump chapter7
            else:
                o "Alright, jokester."
                o "I'll let you go and dial in on that presentation."
                o "Before I've TAKEN any more of your time."
                o "...Get it?"
                o "Good one, right?"
                o "Talk to you then."
                
                j "This is not good."
                
                jump clientmeeting

  
##############################################################
## Manager meeting begins here                              ##
## Talk with manager about client meeting                   ##
## Menu option dependent on if you check calendar earlier   ##
## will trigger client meeting                              ##
##############################################################
         
label nocall:
    
    j "Great."
    j "The phone stopped."
    j "One less thing to worry about."
    j "I swear."
    j "Today has it out for me."
    j "But you know what?"
    j "That's never stopped me from..."
    j "..."
    j "Wait..."
    j "Who is that coming over here?"
    j "Is that Tom from down the hall?"
    j "Oh no."
    j "That guy is awful."
    $ stress_count += 1
    if stress_count > 2:
        
        scene black
        with dissolve
    
        if stress_count == 0:
            scene mgmt_0 movie
            with fade
            show background solid at left
        elif stress_count == 1:
            scene mgmt_1 movie
            with fade
            show background solid at left
        else:
            scene mgmt_2 movie
            with fade
            show background solid at left
    
        play sound "sounds/mints_mgmt_words.wav"
        
        o "Hey Joe."
        o "Woah, what's going on?"
    
        j "Hi Tom..."
        j "I'm losing my cool."

        o "Bummer. That's no good, Joe."
        o "We have a client presentation at 10."
        o "How about you get that all wrapped up before then?"
        
        j "..."
        j "Alright."
        
        $ go_to_meeting += 1
        
        jump mints_scene
    else:
        jump mgmtmeeting  

label mgmtmeeting:
    
    scene black
    with dissolve
    
    if stress_count == 0:
        scene mgmt_0 movie
        with fade
        show background solid at left
    elif stress_count == 1:
        scene mgmt_1 movie
        with fade
        show background solid at left
    else:
        scene mgmt_2 movie
        with fade
        show background solid at left
    
    play sound "sounds/mints_mgmt_words.wav"
    $ renpy.pause(2)
    
    o "Hey Joe, how's it hanging?"
    
    j "Hi Tom..."
    j "It's Joseph, not Joe."
    j "I hate it when people call me Joe."
    
    o "Sure thing, Joe!"
    
    j "..."
    j "What do you need?"
    
    stop music fadeout 4.0
    
    o "I was just checking in before our big meeting today."
    o "Making sure you are all set to go for your presentation!"
    
    j "..."
    
    play music "sounds/mints_mgmt_talk.wav"
    
    if calendar_check > 0:
    
        menu:
        
             "What presentation?":
                 o "Classic you, Joe."
                 o "With that kind of confidence, I know you're fine."
                 o "I'll get out of here."
                 o "See you in the conference room at 10."
                 
                 j "..."
                 j "Sounds good?"
                 
                 $ go_to_meeting += 1
             
                 jump clientmeeting
             
             "Oh right, the presentation!":
             
                 o "Come on now, Joe."
                 o "Don't give me a heart attack like that."
                 o "You didn't forget to write it down on your calendar did you?"
                 
                 j "Hah."
                 j "No."
                 j "Of course, not."
                 
                 o "There! That's right."
                 o "That's the Joe I know."
                 o "See you at 10."
                 
                 j "..."
                 j "I'll be there?"
                 
                 $ go_to_meeting += 1
                 
                 jump clientmeeting
             
             "I don't have anything on my calendar...":
             
                 o "What?"
                 o "You don't?"
                 o "Well you must have forgotten it!"
                 
                 menu:
                      "I probably did.":
                      
                          j "It's possible..."
                          
                          o "Well I hope you come up with something quick, Joe."
                          o "We have a big client in there with a lot on the line."
                          o "If you don't come through on this..."
                          o "I don't know what to tell you."
                          o "..."
                          o "See you at 10."
                          o "Godspeed."
                          
                          scene black
                          with dissolve
                          
                          if stress_count == 0:
                              scene chapter6_0 movie
                              with fade
                              show background solid at left
                          elif stress_count == 1:
                              scene chapter6_1 movie
                              with fade
                              show background solid at left
                          else:
                              scene chapter6_2 movie
                              with fade
                              show background solid at left
                          
                          j "..."
                          j "What did I just get myself into?"
                          j "I am so screwed."
                          
                          $ go_to_meeting += 1
                          
                          if difficulty > 0:                          
                              $ stress_count += 2
                              if stress_count > 2:
                                  jump mints_scene
                              else:
                                  jump clientmeeting
                          else:
                              jump clientmeeting
                      
                      "Don't think so.":
                      
                          jump more_deliberating_mgmt
  
    else:
    
        menu:
        
             "What presentation?":
                 o "Hah! Good one, Joe."
                 o "With that kind of confidence, I know you're fine."
                 o "No need to micromanage."
                 o "I'll see you in the conference room at 10."
                 
                 j "..."
                 j "Sounds good?"
                 
                 $ go_to_meeting += 1
             
                 jump clientmeeting
             
             "Oh right, the presentation!":
             
                 o "Come on now, Joe."
                 o "Don't give me a heart attack like that."
                 o "You didn't forget to write it down on your calendar did you?"
                 
                 j "Hah."
                 j "No."
                 j "Of course, not."
                 
                 o "There! That's right."
                 o "That's the Joe I know."
                 o "See you at 10."
                 
                 j "..."
                 j "You sure will?"
                 
                 $ go_to_meeting += 1
                 
                 jump clientmeeting


label more_deliberating_mgmt:

    o "Joe, I really don't have time for this kind of tizzy."
    o "We have a client coming here and I think you have a presentation."
    o "Furthermore, I'm your boss, and I'm not putting up with any nonsense."
    o "All I really need to know from you is this."
    o "Where are you going to be at 10 today?"

    menu:
    
        "Wherever you want me to be, Tom.":
            if randjoke == 1:
                o "Joe, that's just the kind of dedication this team really needs."
                o "And you are an inspiration to us all."
                o "Forget the meeting."
                
                j "Wait... what?"
                
                o "That's right."
                o "I'll handle it all."
                o "You just keep walking that extra mile around the office today."
                o "I'm proud of you, son."
                o "Talk to you later."
                
                scene black
                with dissolve
                
                if stress_count == 0:
                  scene chapter6_0 movie
                  with fade
                  show background solid at left
                elif stress_count == 1:
                  scene chapter6_1 movie
                  with fade
                  show background solid at left
                else:
                  scene chapter6_2 movie
                  with fade
                  show background solid at left

                j "..."
                j "Holy crap."
                j "That was horrible."
                j "I'm going to need a second to calm the hell down."
                j "..."
                j "Actually."
                j "Nah."
                j "I'm just going to go to lunch."

                jump chapter7
            else:
                o "Joe, while I admire your sincere dedication to the company..."
                o "I won't pretend that doesn't come off a bit creepy."
                o "I'll see you in the meeting at 10."
                o "But let's try to keep it professional in there."
                o "Talk to you then."
                
                scene black
                with dissolve
                
                if stress_count == 0:
                  scene chapter6_0 movie
                  with fade
                  show background solid at left
                elif stress_count == 1:
                  scene chapter6_1 movie
                  with fade
                  show background solid at left
                else:
                  scene chapter6_2 movie
                  with fade
                  show background solid at left
                
                j "This is not good."
                
                jump clientmeeting
        
        "Right behind you, Tom.":
            if randjoke == 2:
                o "Wait, what's behind me?!"
                o "Holy smokes."
                o "Joe, you scared me there."
                
                j "Sorry about that."
                
                o "No, don't apologize."
                o "I get it. It's figurative, or something like that."
                o "This kind of job takes initiative,"
                o "and you are right behind me, every step of the way."
                o "I appreciate the daylights out of that, son."
                
                j "Thank you?"
                
                o "Don't worry about the meeting."
                o "I'm pretty sure I can handle it."
                o "But I know who's right behind me if I get into trouble."
                o "I'll talk to you later, Joe."
                
                scene black
                with dissolve
                
                if stress_count == 0:
                  scene chapter6_0 movie
                  with fade
                  show background solid at left
                elif stress_count == 1:
                  scene chapter6_1 movie
                  with fade
                  show background solid at left
                else:
                  scene chapter6_2 movie
                  with fade
                  show background solid at left

                j "..."
                j "Holy crap."
                j "That was horrible."
                j "I'm going to need a second to calm the hell down."
                j "..."
                j "Actually."
                j "Nah."
                j "I'm just going to go to lunch."

                jump chapter7
            else:
                o "Wait, what's behind me?!"
                o "Holy smokes."
                o "Joe, don't scare me like that."
                o "I know all about your work as a magician on nights and weekends."
                o "But here in the office, let's try and keep it civil."
                o "I'll see you in the meeting at 10."
                o "Later."
                
                scene black
                with dissolve
                
                if stress_count == 0:
                  scene chapter6_0 movie
                  with fade
                  show background solid at left
                elif stress_count == 1:
                  scene chapter6_1 movie
                  with fade
                  show background solid at left
                else:
                  scene chapter6_2 movie
                  with fade
                  show background solid at left
                
                j "This is not good."
                
                jump clientmeeting
        
        "In my same old cubicle, watching the years fly by.":
            if randjoke == 3:
                o "I have to hand it to you, Joe."
                o "You're right."
                o "How many years have we all been here?"
                o "In these tiny prisons, like lambs to the slaughter?"
                
                j "I have no idea, Tom."
                
                o "You know what?"
                o "You've inspired me."
                o "Change needs to start happening around here."
                o "And it needs to start right now."
                o "I'm putting off this meeting until we get things moving."
                o "There's no time to wait!"
                o "We need to seize the day!"
                o "Talk to you later."
                
                scene black
                with dissolve
                
                if stress_count == 0:
                  scene chapter6_0 movie
                  with fade
                  show background solid at left
                elif stress_count == 1:
                  scene chapter6_1 movie
                  with fade
                  show background solid at left
                else:
                  scene chapter6_2 movie
                  with fade
                  show background solid at left

                j "..."
                j "Holy crap."
                j "That was horrible."
                j "I'm going to need a second to calm the hell down."
                j "..."
                j "Actually."
                j "Nah."
                j "I'm just going to go to lunch."

                jump chapter7
            else:
                o "Well how about you put those years on hold for a couple hours."
                o "I need you in the conference room at 10."
                o "Talk to you then."
                
                scene black
                with dissolve
                
                if stress_count == 0:
                  scene chapter6_0 movie
                  with fade
                  show background solid at left
                elif stress_count == 1:
                  scene chapter6_1 movie
                  with fade
                  show background solid at left
                else:
                  scene chapter6_2 movie
                  with fade
                  show background solid at left
                
                j "This is not good."
                
                jump clientmeeting
        
        "Far, far away, Tom.":
            if randjoke == 4:
                o "Wait... really?"
                o "That's..."
                o "Actually, that's quite respectable, son."
                
                j "Wait... what?"
                
                o "That's right."
                o "I respect that kind of ability to remove yourself from your job."
                o "What kind of automated wind up toys are we if we never escape the rat race?"
                o "I like your style, Joe."
                o "Don't worry about the meeting."
                o "I'll handle it with newfound inspiration."
                o "Talk to you later."

                scene black
                with dissolve

                if stress_count == 0:
                  scene chapter6_0 movie
                  with fade
                  show background solid at left
                elif stress_count == 1:
                  scene chapter6_1 movie
                  with fade
                  show background solid at left
                else:
                  scene chapter6_2 movie
                  with fade
                  show background solid at left

                j "..."
                j "Holy crap."
                j "That was horrible."
                j "I'm going to need a second to calm the hell down."
                j "..."
                j "Actually."
                j "Nah."
                j "I'm just going to go to lunch."

                jump chapter7
            else:
                o "Well wherever that is Joe..."
                o "I highly suggest you find your way back quickly."
                o "So that you end up in the conference room at 10."
                o "No problem with traveling as long as you are punctual."
                o "Talk to you then."
                
                scene black
                with dissolve
                
                if stress_count == 0:
                  scene chapter6_0 movie
                  with fade
                  show background solid at left
                elif stress_count == 1:
                  scene chapter6_1 movie
                  with fade
                  show background solid at left
                else:
                  scene chapter6_2 movie
                  with fade
                  show background solid at left
                
                j "This is not good."
                
                jump clientmeeting
        
        "All the way up, Tom.":
            if randjoke == 5:
                o "Like hell you will be, Joe."
                o "And you know what?"
                o "Nothing can stop you."
                
                j "That's absolutely right, Tom."
                
                o "Forget the presentation."
                o "I'll handle it all."
                o "You just keep doing you today, son."
                o "I'm proud of you."
                o "Talk to you later."
                
                scene black
                with dissolve
                
                if stress_count == 0:
                  scene chapter6_0 movie
                  with fade
                  show background solid at left
                elif stress_count == 1:
                  scene chapter6_1 movie
                  with fade
                  show background solid at left
                else:
                  scene chapter6_2 movie
                  with fade
                  show background solid at left

                j "..."
                j "Holy crap."
                j "That was horrible."
                j "I'm going to need a second to calm the hell down."
                j "..."
                j "Actually."
                j "Nah."
                j "I'm just going to go to lunch."

                jump chapter7
            else:
                o "Like hell you will be, Joe."
                o "And you know what?"
                o "Nothing can stop you."
                
                j "That's absolutely right, Tom."
                
                o "Specifically..."
                o "Nothing can stop you from being in the conference room at 10."
                o "For your presentation."
                o "I'll talk to you then."
                
                scene black
                with dissolve
                
                if stress_count == 0:
                  scene chapter6_0 movie
                  with fade
                  show background solid at left
                elif stress_count == 1:
                  scene chapter6_1 movie
                  with fade
                  show background solid at left
                else:
                  scene chapter6_2 movie
                  with fade
                  show background solid at left
                
                j "This is not good."
                
                jump clientmeeting
        
        "In your worst nightmare, Tom.":
            if randjoke == 6:
                o "Hold on a hot minute, Joe."
                o "Nobody ever said anything like that."
                o "Wherever you are, sit down and second and hear me out."
                
                j "Wait... what?"
                
                o "I may be a bit stressed by this presentation."
                o "But in no way does this make you a nightmare to work with."
                o "We all have our up days and down days."
                o "You just have to take the rose with the thorns."
                o "I had my fair share of parental disagreements as well."
                o "But you can't let it get to your self esteem."
                o "You are nobody's worst nightmare."
                o "No need to worry about the presentation."
                o "Just take the morning to get that self esteem back up where it should be."
                o "I'll check in later."
                
                scene black
                with dissolve
                
                if stress_count == 0:
                  scene chapter6_0 movie
                  with fade
                  show background solid at left
                elif stress_count == 1:
                  scene chapter6_1 movie
                  with fade
                  show background solid at left
                else:
                  scene chapter6_2 movie
                  with fade
                  show background solid at left

                j "..."
                j "Well that was unexpectedly sentimental."
                j "..."
                j "On that note."
                j "I'm just going to go to lunch."

                jump chapter7
            else:
                o "Joe, in all honesty."
                o "My worst fear is surviving the Armageddon."
                o "And finding myself utterly alone in the aftermath."
                o "But that's not really relevant right now."
                o "My second biggest fear is that you screw up this presentation."
                o "I'll see you in the conference room at 10."
                o "Bring your A-game."
                
                scene black
                with dissolve
                
                if stress_count == 0:
                  scene chapter6_0 movie
                  with fade
                  show background solid at left
                elif stress_count == 1:
                  scene chapter6_1 movie
                  with fade
                  show background solid at left
                else:
                  scene chapter6_2 movie
                  with fade
                  show background solid at left
                
                j "This is not good."
                
                jump clientmeeting
        
        "I don't have money, Tom, but what I do have is a very particular set of skills.":
            if randjoke == 7:
                o "Joe, why do you think we hired you in the first place?"
                o "We know you have... some type of skills."
                o "And stay here long enough, you won't have to worry about the money."
                o "If you are really concerned about it in the meantime..."
                o "Maybe you should cut down on your coffee budget or something."
                
                j "Wait... what?"
                
                o "I get it."
                o "This presentation is stressing you out, isn't it?"
                o "You know what?"
                o "Forget it."
                o "I know the client."
                o "I can handle the whole thing."
                o "Take the rest of the morning and chill out."
                o "Remember the skills that got you here, and visualize the money."
                o "None of it's taken for granted here."
                o "I'll talk to you later."
                
                scene black
                with dissolve
                
                if stress_count == 0:
                  scene chapter6_0 movie
                  with fade
                  show background solid at left
                elif stress_count == 1:
                  scene chapter6_1 movie
                  with fade
                  show background solid at left
                else:
                  scene chapter6_2 movie
                  with fade
                  show background solid at left

                j "..."
                j "Holy crap."
                j "That was horrible."
                j "I'm going to need a second to calm the hell down."
                j "..."
                j "Actually."
                j "Nah."
                j "I'm just going to go to lunch."

                jump chapter7
            else:
                o "Alright, jokester."
                o "I'll let you go and dial in on that presentation."
                o "Before I've TAKEN any more of your time."
                o "...Get it?"
                o "Good one, right?"
                o "Talk to you then."
                
                scene black
                with dissolve
                
                if stress_count == 0:
                  scene chapter6_0 movie
                  with fade
                  show background solid at left
                elif stress_count == 1:
                  scene chapter6_1 movie
                  with fade
                  show background solid at left
                else:
                  scene chapter6_2 movie
                  with fade
                  show background solid at left
                
                j "This is not good."
                
                jump clientmeeting
    
##############################################################
## Client meeting begins here                               ##
## Dependent on coffee, email, snooze, etc                  ##
## Pretty much geared towards a meltdown                    ##
##############################################################
         
label clientmeeting:
    
    scene black
    with dissolve
    
    stop music fadeout 2.0
    $ renpy.pause(1)
    
    if difficulty < 2:
        $ stress_count = 0
    
    if stress_count == 0:
        scene clientmtg_0 movie
        with fade
        show background solid at left
    elif stress_count == 1:
        scene clientmtg_1 movie
        with fade
        show background solid at left
    else:
        scene clientmtg_2 movie
        with fade
        show background solid at left
    
    play music "sounds/mints_client_mtg_p1_ost.wav"
    
    j "Oh my god."
    j "How is this happening?"
    j "I'm going to die."
    j "No, worse..."
    j "I'm going to get fired."
    j "What am I going to do?"
    
    o "Alright, Joe. This is Tom on the speakerphone here."
    o "Did you catch the email I sent this morning?"
    
    if check_email > 0:
        j "I sure did."
        o "Great! Excellent work, as always."
    else:
        j "I... didn't quite get to it, yet."
        o "Well, good thing you've been prepping for this for weeks!"
    
    o "Mr. Mills is there with you in the conference room now."
    if randlng == 1:
        o "Mr. Mills is the client's COO."
        o "Plus, former Ivy League professor of... what was it?"
        o "French language? Parisian art? Something fancy like that?"
        o "Anyways, he's there with you now. Proceed as planned."
    else:
        o "Mr. Mills is the client's COO."
        o "Plus, former Ivy League professor of... what was it?"
        o "Dead languages? Latin? Ancient runes?"
        o "Anyways, he's there with you now. Proceed as planned."
    
    play sound "sounds/mints_client_grumble.wav"
    $ renpy.pause(2)
    
    j "Of course he picks the chair furthest from me..."
    
    play music "sounds/mints_client_mtg_p2_ost.wav"
    
    if coffee_choice > 0:
        j "Wait a second..."
        j "Oh, crap."
        j "That's the guy from the coffee shop."
        
        if guy_talk > 0:
            o "Well what are the odds?"
            o "Joe, did you say it was?"
            
            j "Um... Joseph, actually."
            
            o "Alright, Joe."
            o "Let's see what brilliant stuff you have for me."
            
            if difficulty > 1:
                $ stress_count += 2
            elif difficulty > 0:
                $ stress_count += 1
            else:
                $ stress_count = 0
            
            if stress_count > 2:
                j "Oh no."
                j "I think I'm losing my cool."
                
                o "Please."
                o "You are totally faking it, you scumbag."
                
                j "No, really."
                j "I need my mints."
                j "They are at my desk."
                
                o "This is ridiculous."
                
                j "This is..."
                j "I need to get out of here..."
                
                $ meeting_panic += 1
                
                jump mints_scene
            else:
                jump meeting_prompt
                
        else:
            j "That guy was a complete jerk to that barista."
            j "What if he finds out I don't have a presentation?"
            j "I can only imagine what he'll do to me."
            
            o "Go ahead whenever you feel like it, Joe."
            o "I don't have all day here, you know."
            
            $ stress_count += 1
            
            if stress_count > 2:
                j "Oh no."
                j "I think I'm losing my cool."
                
                o "What?"
                o "What's going on?"
                
                j "Please."
                j "I need my mints."
                j "They are at my desk."
                j "I need to go get them."
                
                o "This is utterly bizarre."
                
                j "I know that..."
                j "It's just..."
                j "Really..."
                j "I need to get out of here..."
                
                $ meeting_panic += 1
                
                jump mints_scene
            else:
                jump meeting_prompt
    
    else:
    
        o "Get on with it whenever you're ready."
        o "I don't really mean that, by the way."
        o "Whenever you're ready..."
        o "I mean get on with it as soon as possible."
        
        j "Geez, what a jerk..."
        j "Still, I have to think of something..."
        
        jump meeting_prompt            

label meeting_prompt:
    
    menu:
        
        "So about your business plan...":
            if randmtg == 1:
                o "I know full well about our business plan."
                o "What I want to hear about is how you are going to fix it."
                o "You are a consultant, aren't you?"
            
                j "Well, actually I'm..."
                j "Yeah, I'm definitely a consultant."
            
                o "Well then, get on with it."
            
                jump meeting_w_map
            
            else:
                o "Business plan?"
                o "You don't even know what this meeting is for, do you?"
                o "Tom, who the hell is this clown?"
            
                if difficulty > 1:
                    $ stress_count += 2
                elif difficulty > 0:
                    $ stress_count += 1
                else:
                    $ stress_count = 0
            
                if stress_count > 2:
                    j "Oh no."
                    j "I think I'm losing my cool."
                
                    o "Then I suggest you go find it."
                    o "I don't see any way this is going to end any better."
                
                    j "No, really."
                    j "I need my mints."
                    j "They are at my desk."
                
                    o "Well I'm not going to carry you if that's what you're asking."
                
                    j "This is..."
                    j "I need to get out of here..."
                
                    $ meeting_panic += 1
                
                    jump mints_scene
                else:
                    jump meeting_w_map

             
        "So about your quarterly projections...":
            if randmtg == 2:
                o "Not the best opening line I've ever heard..."
                o "But I'll take it."
                o "Let's see what you plan on doing about them."
                 
                jump meeting_w_map
            
            else:
                o "Quarterly projections?"
                o "You don't even know what this meeting is for, do you?"
                o "Tom, who are these monkeys that do your work nowadays?"
            
                if difficulty > 1:
                    $ stress_count += 2
                elif difficulty > 0:
                    $ stress_count += 1
                else:
                    $ stress_count = 0
            
                if stress_count > 2:
                    j "Oh no."
                    j "I think I'm losing my cool."
                
                    o "I've got a quarterly projection for you."
                    o "It's called a quarter life crisis."
                
                    j "No, really."
                    j "I need my mints."
                    j "They are at my desk."
                
                    o "Get a job."
                
                    j "This is..."
                    j "I need to get out of here..."
                
                    $ meeting_panic += 1
                
                    jump mints_scene
                else:
                    jump meeting_w_map
             
        "So about your marketing campaign...":
            if randmtg == 3:
                o "I know."
                o "Currently, it sucks."
                o "Which is why we are paying you people way more than you deserve."
                o "You like getting paid more than you deserve, Joe?"
        
                j "I... no..."
                j "I mean, yes?"
        
                o "Sure you do."
                o "Let's get on with it."
        
                jump meeting_w_map
        
            else:
                o "Marketing campaign?"
                o "You don't even know what this meeting is for, do you?"
                o "You want to talk marketing?"
                o "How about you try marketing yourself to a new client?"
            
                if difficulty > 1:
                    $ stress_count += 2
                elif difficulty > 0:
                    $ stress_count += 1
                else:
                    $ stress_count = 0
            
                if stress_count > 2:
                    j "Oh no."
                    j "I think I'm losing my cool."
                
                    o "Not a good brand image, Joe."
                
                    j "No, really."
                    j "I need my mints."
                    j "They are at my desk."
                
                    o "Survey says..."
                    o "Whoops, sorry Joe."
                    o "Just not a very popular response."
                
                    j "This is..."
                    j "I need to get out of here..."
                
                    $ meeting_panic += 1
                
                    jump mints_scene
                else:
                    jump meeting_w_map
        
        "So about your employee benefits policy...":
            if randmtg == 4:
                o "It's absolutely..."
                o "Wait..."
                o "You're not one of my employees, are you?"
            
                j "I... don't think I am..."
            
                o "Right."
                o "It's the legal bottom of the barrel."
                o "Uncle Sam is making us raise it a bit."
                o "That's all there is to this."
                o "So let's hurry up and get it over with."
        
                jump meeting_w_map
            
            else:
                o "Employee benefits?"
                o "You don't even know what this meeting is for, do you?"
                o "You trying to ask for a job or something?"
                o "Because buddy, this is about the worst way to go about it."
            
                if difficulty > 1:
                    $ stress_count += 2
                elif difficulty > 0:
                    $ stress_count += 1
                else:
                    $ stress_count = 0
            
                if stress_count > 2:
                    j "Oh no."
                    j "I think I'm losing my cool."
                
                    o "Loss of cool is not covered under our policy, Joe."
                    o "Unless you just mean getting old and irrelevant."
                
                    j "No, really."
                    j "I need my mints."
                    j "They are at my desk."
                
                    o "I sure hope I didn't pay for those."
                    o "What's your copay here, anyways?"
                    o "Swanky lookin' office like this, probably pretty low."
                    o "Damn socialists."
                
                    j "This is..."
                    j "I need to get out of here..."
                
                    $ meeting_panic += 1
                
                    jump mints_scene
                else:
                    jump meeting_w_map

# defining hotspots here, to be called later 
screen meeting_map:
    imagemap:
        ground "blank.png"

        hotspot (0, 188, 91, 80) clicked Return("phone")         #use the phone
        hotspot (400, 120, 126, 148) clicked Return("easel")     #use the easel
        hotspot (696, 75, 104, 178) clicked Return("tv")         #use the tv 
        hotspot (449, 318, 101, 45) clicked Return("papers")     #use the papers
        hotspot (56, 300, 328, 169) clicked Return("desk")       #use the desk 
    
label meeting_w_map:

    play music "sounds/mints_client_mtg_p3_ost.wav"
    
    call screen meeting_map
    
    $ result = _return
    
    if result == "phone":
        j "Tom, can we dial in Jim over in... um... Operations?"
        
        o "Who the hell is Jim?"
        
        j "He's my main contact for..."
        j "Pretty much everything..."
        
        o "Joe, this is Tom on the speakerphone again."
        o "Looks like Jim is out today."
        o "Did he have something crucial to your presentation?"
        
        menu:
            "He sure did.":
                j "Can't believe he backed out on me like that."
                j "Guess we'll have to... you know..."
                
                o "Well you know what they say in the biz."
                o "Show must go on!"
                
                if difficulty > 0:
                    $ stress_count += 1
                else:
                    $ stress_count = 0
            
                if stress_count > 2:
                    j "Oh no."
                    j "I think I'm losing my cool."
                
                    o "Wow, sure a shame Jim isn't here."
                    o "Sounds like it was more his presentation than yours."
                
                    j "No, really."
                    j "I need my mints."
                    j "They are at my desk."
                
                    o "I don't have time for this."
                
                    j "I need to get out of here..."
                
                    $ meeting_panic += 1
                
                    jump mints_scene
                else:
                    jump meeting_w_map
                    
            "Not really.":
                j "I just felt like getting his input on this."
                j "You know... all hands on deck."
                
                o "I didn't realize we were in that sort of a situation."
                o "But alright... whatever you think is best."
                o "As long as this doesn't take much longer."
                
                jump meeting_w_map
                
    elif result == "easel":

        j "Tom, do you have a pen on you?"
        j "I think I'll draw up a diagram for all of our findings."
        
        o "Still just on the speakerphone here, Joe."
        o "But it's great to know this thing has such a lifelike quality!"
        
        o "Tom, this is Mills."
        o "Why the hell do we need a diagram?"
        o "This is a waste of my time."
        
        menu:
            "Visualize the profits cycle.":
                j "Gotta see that money, Mr. Mills!"
                j "How else do you stay hungry?"
                
                o "What a load of baloney!"
                o "Tom, is this really the best you have to offer me?"
                
                if difficulty > 0:
                    $ stress_count += 1
                else:
                    $ stress_count = 0
            
                if stress_count > 2:
                    j "Oh no."
                    j "I think I'm losing my cool."
                
                    o "You should visualize some icebergs."
                
                    j "No, really."
                    j "I need my mints."
                    j "They are at my desk."
                
                    o "No really. It's worth my time and yours."
                    o "Take all you need."
                
                    j "I need to get out of here..."
                
                    $ meeting_panic += 1
                
                    jump mints_scene
                else:
                    jump meeting_w_map

            "Business is art.":
                j "If you really think about it..."
                j "You try so hard and get so far..."
                j "But in the end..."
                
                o "Cripes."
                o "Tom, you've really outdone yourself this time."
                o "Am I being filmed or something?"
                o "Please get this idiot out of my face."
                
                if difficulty > 0:
                    $ stress_count += 1
                else:
                    $ stress_count = 0
            
                if stress_count > 2:
                    j "Oh no."
                    j "I think I'm losing my cool."
                
                    o "Is this part of your art piece, or..."
                
                    j "No, really."
                    j "I need my mints."
                    j "They are at my desk."
                
                    o "I don't have time for this."
                
                    j "I need to get out of here..."
                
                    $ meeting_panic += 1
                
                    jump mints_scene
                else:
                    jump meeting_w_map
                    
            "You are right - we probably don't.":
                j "Just felt like it would help."
                
                o "Well stop helping."
                o "I mean..."
                o "Help in more expedient ways."
                
                jump meeting_w_map  

    elif result == "tv":
        j "Tom, can we get this screen going?"
        
        o "Sure, Joe. Do you have a presentation ready to go?"
        
        menu:
            "You betcha.":
                j "Got it right here."
                
                o "..."
                o "Where?"
                
                menu:
                
                    "Right the hell here, Tom!":
                        o "Alright, Joe, I think you need to calm down, son."
                        
                        o "Tom, this is Mills. Who is this psycho?"
                        o "Because if he's not going to tell me what I need to know..."
                        o "I'm not interested in his problems."
                        
                        if difficulty > 0:
                            j "I don't have any problems!"
                        
                            o "What do you call your lack of a presentation then?"
                            o "Right... not problems."
                            o "Just failure."
                        
                            $ meeting_panic += 1
                
                            jump mints_scene
                        else:
                            jump meeting_w_map
                    
                    "At my desk, actually.":
                    
                        o "Is it on a..."
                        o "Laptop or something?"
                        
                        j "That's exactly where it is."
                        j "I forgot to email it to myself."
                        j "Sorry about that."
                        
                        o "Well just go and grab your laptop, Joe."
                        o "Don't want to waste Mr. Mills' time."
                        o "Any more than necessary that is..."
                        
                        scene black
                        with dissolve
                        
                        if stress_count == 0:
                            scene clientmtg_0 movie
                            with fade
                            show background solid at left
                        elif stress_count == 1:
                            scene clientmtg_1 movie
                            with fade
                            show background solid at left
                        else:
                            scene clientmtg_2 movie
                            with fade
                            show background solid at left
                            
                        o "Alright, now that that colossal waste of time is over."
                        o "Let's see this presentation you have for me."
                        
                        j "Right."
                        j "Let me just get this up and running..."
                        j "Oh wait..."
                        j "Looks like it's not here anymore."
                        
                        o "What is that folder that says Presentation?"
                        
                        j "..."
                        j "I don't think that's the same presentation."
                        
                        o "Come on, let's break it open and see what's in there."
                        
                        j "..."
                        j "Alright."
                        
                        o "..."
                        o "This is just a slideshow of photos from your..."
                        o "Family trip to Greece?"
                        o "Good lord, is that your grandfather in a speedo?"
                        
                        o "Joe, this is Tom, still on the speakerphone."
                        o "What the hell kind of presentation is this?"
                        o "This is utterly unacceptable."
                        
                        if difficulty > 0:
                            $ stress_count += 2
                        else:
                            $ stress_count = 0
            
                        if stress_count > 2:
                            j "Oh no."
                            j "I think I'm losing my cool."
                
                            o "You better be."
                            o "I can never unsee that, you know."
                
                            j "No, really."
                            j "I need my mints."
                            j "They are at my desk."
                
                            o "Great, fine with me."
                            o "I'm getting out of here."
                
                            $ meeting_panic += 1
                
                            jump mints_scene
                        else:
                            jump meeting_w_map
                    
                    "In my mind...":
                        o "Joe, I'm going to be honest..."
                        o "That doesn't sound incredibly helpful right now."
                        
                        o "Tom, this is Mills."
                        o "Is there any way we can crack this bozo's head open?"
                        o "I might be able to see the presentation better that way."
                
                        if difficulty > 0:
                            $ stress_count += 1
                        else:
                            $ stress_count = 0
            
                        if stress_count > 2:
                            j "Oh no."
                            j "I think I'm losing my cool."
                
                            o "Wow, sure a shame Jim isn't here."
                            o "Sounds like a much cooler guy than you."
                
                            j "No, really."
                            j "I need my mints."
                            j "They are at my desk."
                
                            o "I don't have time for this."
                
                            j "I need to get out of here..."
                 
                            $ meeting_panic += 1
                
                            jump mints_scene
                        else:
                            jump meeting_w_map
                    
            "Not really.":
                j "My mistake."
                j "You can leave it off."
                
                o "Damn screens."
                o "We are addicted to them, I swear."
                o "It's like everywhere you turn, you can't be away from them."
                
                o "Alright, enough banter."
                o "Well let's keep it right along, then."
                
                jump meeting_w_map
                
    elif result == "papers":

        j "Printed a few things off."
        
        o "Joe, this is Tom on the speakerphone."
        o "I can't see the printouts."
        o "Are they relevant to the presentation?"
        
        menu:
            "You bet your ass.":
                j "In fact, I'd say they are important enough"
                j "that you should come sit in on the rest of the meeting."
                
                o "..."
                o "You really think so?"
                o "I have another meeting in 15..."
                o "Mills, can you look at those papers?"
                o "What do you make of it?"
                
                o "Tom, looks like some kind of graph."
                o "Hell if I know."
                
                o "You sure about this, Joe?"
                
                menu:
                
                    "Lassez-faire, Tom.":
                        if randlng == 1:
                            o "Wow, French?"
                            o "You run a sophisticated crowd around here, Tom."
                            o "Forget the presentation."
                            o "I'm sold."
                            o "Let's go with whatever you have."
                            
                            j "Wow, just like that?"
                            
                            o "Just like that."
                            o "Art of the deal, son."
                            o "You've got it."
                        else:
                            o "Wow, French?"
                            o "What a bunch of snobs."
                            o "Forget it, I don't want want to see the damn presentation."
                            o "I'm calling this off."
                            
                            if difficulty > 0:
                                $ stress_count += 2
                            else:
                                $ stress_count = 0
            
                            if stress_count > 2:
                                j "Oh no."
                                j "I think I'm losing my cool."
                
                                o "Probably better this way, son."
                                o "French stuff fell out of fashion a while ago."
                
                                j "No, really."
                                j "I need my mints."
                                j "They are at my desk."
                
                                o "Well, good luck."
                                o "I'll be seein' ya."
                
                                j "I need to get out of here..."
                 
                                $ meeting_panic += 1
                
                                jump mints_scene
                            else:
                                jump meeting_w_map
                    
                    "C'est la vie, Tom.":
                        if randlng == 1:
                            o "Wow, French?"
                            o "You run a sophisticated crowd around here, Tom."
                            o "Forget the presentation."
                            o "I'm sold."
                            o "Let's go with whatever you have."
                            
                            j "Wow, just like that?"
                            
                            o "Just like that."
                            o "Art of the deal, son."
                            o "You've got it."
                        else:
                            o "Wow, French?"
                            o "What a bunch of snobs."
                            o "Forget it, I don't want want to see the damn presentation."
                            o "I'm calling this off."
                            
                            if difficulty > 0:
                                $ stress_count += 2
                            else:
                                $ stress_count = 0
            
                            if stress_count > 2:
                                j "Oh no."
                                j "I think I'm losing my cool."
                
                                o "Probably better this way, son."
                                o "French stuff fell out of fashion a while ago."
                
                                j "No, really."
                                j "I need my mints."
                                j "They are at my desk."
                
                                o "Well, good luck."
                                o "I'll be seein' ya."
                
                                j "I need to get out of here..."
                 
                                $ meeting_panic += 1
                
                                jump mints_scene
                            else:
                                jump meeting_w_map
                    
                    "Carpe diem, Tom.":
                        if randlng == 2:
                            o "Wow, Latin?"
                            o "You run a sophisticated crowd around here, Tom."
                            o "Forget the presentation."
                            o "I'm sold."
                            o "Let's go with whatever you have."
                            
                            j "Wow, just like that?"
                            
                            o "Just like that."
                            o "Art of the deal, son."
                            o "You've got it."
                        else:
                            o "Wow, Latin?"
                            o "What a bunch of snobs."
                            o "Forget it, I don't want want to see the damn presentation."
                            o "I'm calling this off."
                            
                            if difficulty > 0:
                                $ stress_count += 2
                            else:
                                $ stress_count = 0
            
                            if stress_count > 2:
                                j "Oh no."
                                j "I think I'm losing my cool."
                
                                o "Probably better this way, son."
                                o "Latin is pretty irrelevant today anyways."
                
                                j "No, really."
                                j "I need my mints."
                                j "They are at my desk."
                
                                o "Well, good luck."
                                o "I'll be seein' ya."
                
                                j "I need to get out of here..."
                 
                                $ meeting_panic += 1
                
                                jump mints_scene
                            else:
                                jump meeting_w_map

                    
                    "Quid pro quo, Tom.":
                        if randlng == 2:
                            o "Wow, Latin?"
                            o "You run a sophisticated crowd around here, Tom."
                            o "Forget the presentation."
                            o "I'm sold."
                            o "Let's go with whatever you have."
                            
                            j "Wow, just like that?"
                            
                            o "Just like that."
                            o "Art of the deal, son."
                            o "You've got it."
                        else:
                            o "Wow, Latin?"
                            o "What a bunch of snobs."
                            o "Forget it, I don't want want to see the damn presentation."
                            o "I'm calling this off."
                            
                            if difficulty > 0:
                                $ stress_count += 2
                            else:
                                $ stress_count = 0
            
                            if stress_count > 2:
                                j "Oh no."
                                j "I think I'm losing my cool."
                
                                o "Probably better this way, son."
                                o "Latin is pretty irrelevant today anyways."
                
                                j "No, really."
                                j "I need my mints."
                                j "They are at my desk."
                
                                o "Well, good luck."
                                o "I'll be seein' ya."
                
                                j "I need to get out of here..."
                 
                                $ meeting_panic += 1
                
                                jump mints_scene
                            else:
                                jump meeting_w_map
                    
            "Matter of perspective, really.":
                j "I mean, who can really say?"
                j "Isn't everything subjective at some level?"
                
                o "Tom on the speakerphone again."
                o "I'm gonna have to disagree with you there, Joe."
                o "I'd say when it's a professional opinion for sale..."
                o "We try to limit the subjectivity."
                o "Try to stay off the bud for the rest of the presentation."
                
                if difficulty > 0:
                    $ stress_count += 1
                else:
                    $ stress_count = 0
            
                if stress_count > 2:
                    j "Oh no."
                    j "I think I'm losing my cool."
                
                    o "Kind of depends on your point of view."
                
                    j "No, really."
                    j "I need my mints."
                    j "They are at my desk."
                
                    o "Do they make hemp ones nowadays?"
                
                    j "I need to get out of here..."
                
                    $ meeting_panic += 1
                
                    jump mints_scene
                else:
                    jump meeting_w_map
                                
            
            "Nah.":
                j "I just needed something to take notes on."
                j "Never come unprepared, that's what I always say."
                j "You want me to write anything down, Mr. Mills?"
                
                o "Um..."
                o "Not particularly at the moment, no."
                o "Continue with your presentation."
                
                jump meeting_w_map
                
    elif result == "desk":

        j "I haven't really taken the time to think about it before."
        j "But isn't this a great desk?"
        
        o "Why are we talking about the damn desk?"
        
        o "Joe, this is Tom on the speakerphone."
        o "Let's avoid talking about the desk as much as possible, please."
        o "Unless it plays a very key role in your presentation."
                
        if difficulty > 0:
            $ stress_count += 1
        else:
            $ stress_count = 0
            
        if stress_count > 2:
            j "Oh no."
            j "I think I'm losing my cool."
                
            o "Desk pissed you off that much?"
            o "Wow."
            o "You are a complete basket case."
                
            j "No, really."
            j "I need my mints."
            j "They are at my desk."
                
            o "I think you need a lot more than mints, buddy."
                
            j "I need to get out of here..."
                
            $ meeting_panic += 1
                
            jump mints_scene
        else:
            jump meeting_w_map


##############################################################
## Chapter 7 starts here                                    ##
## Lunch on the balcony begins here                         ##
## This is a reprieve chapter from the last couple          ##
## Lots of thoughts about the morning                       ##
##############################################################
         
label chapter7:
    
    scene black
    with dissolve
    
    stop music fadeout 2.0
    $ renpy.pause(1)
    
    if difficulty < 2:
        $ stress_count = 0
    
    $ scene_count += 1
    
    if stress_count == 0:
        scene chapter7_0 movie
        with fade
        show background solid at left
    elif stress_count == 1:
        scene chapter7_1 movie
        with fade
        show background solid at left
    else:
        scene chapter7_2 movie
        with fade
        show background solid at left
    
    play music "sounds/mints_chp7_nobass_ost.wav"

    if go_to_meeting > 0 and meeting_panic > 0:
        j "That sure was good of Tom to take over that meeting for me."
        j "Maybe I underestimated that guy."
        j "Still..."
    elif go_to_meeting > 0 and meeting_panic < 1:
        j "I can't believe I got through that meeting."
        j "I don't even think I was supposed to be there."
        j "That was a miracle!"
        j "Still..."
    else:
        j "That business with Tom was ridiculous."
        
    j "How does this happen every day?"
    j "Here I am, taking my lunchtime escape from the madness,"
    j "And already, just this morning, I've been through the ringer."
    
    # play music "sounds/mints_chp7_begin_ost.wav"
    
    j "I find myself in these inescapable, ridiculous situations."
    j "And no matter how ridiculous they are,"
    j "they still manage to be impossibly stressful."
    j "How come I can never keep cool?"
    j "Is it really that bad?"
    j "Does everyone go through this stuff?"
    j "And if so, how am I this dumb that I let it all happen to me every day?"
    j "Or maybe, it's really not that bad, and I'm the one making it worse."
    j "Maybe I perpetuate the stress where there's no need to."
    j "Maybe I just work myself up to the anxiety."
    j "It has to be one or the other, right?"
    
    play music "sounds/mints_chp7_wguitar_ost.wav"

    menu:
         "Everybody goes through it.":
             j "It can't just be me."
             j "Maybe other people are just better at hiding it."
             j "Or maybe not - maybe that's why it seems too hard every day."
             j "All of us, trying to live into this fake well-adjusted routine."
             j "But all of us suffering equally by not saying anything about it."
             j "And sure, I guess the opposite would be worse..."
             j "Not having a job to go to at all, driving myself nuts in my apartment."
             j "But isn't there some other alternative?"
             j "Isn't there a way where we don't just default to the norm?"
             j "Even those fancy tech companies with their biospheres and nap pods,"
             j "there's still that pressure to abandon your culture for theirs."
             j "I guess that's the way people have been doing it for decades."
             j "But it just seems so... anticlimactic."
             j "Is that really all I have to look forward to?"
             $ stress_count += 2
             if stress_count > 2:
                 jump mints_scene
             else:
                 jump end_of_lunch

         "It's just me.":
             j "It can't be that bad."
             j "If it was, everybody would be crazy."
             j "I'd get on the bus every morning, surrounded by people just like me."
             j "People paralyzed to meet each other in the eye."
             j "People at crosswalks who fight themselves over making smalltalk."
             j "People who can't ride an elevator without all facing the same direction."
             j "Wait..."
             j "Oh my god..."
             j "It isn't just me."
             j "This happens every single day."
             j "Everyone is crazy."
             j "Everyone is like me, constantly stuck inside their own mind,"
             j "weighing the decisions of every single strand of chaos theory madness."
             j "I'm surrounded by psychos,"
             j "a bunch of them probably here in this park."
             j "What the hell am I supposed to do?"
             if difficulty > 0:
                 jump mints_scene
             else:
                 jump end_of_lunch

         "What the hell do I know?":
             j "I guess if you could figure that kind of thing out,"
             j "there would be a lot less sadness and confusion in the world."
             j "I don't know."
             j "Maybe it's a little bit of both."
             j "And maybe it's a sliding scale,"
             j "tilting heavier on one side or the other depending on the day." 
             j "It has to be, right?"
             j "What other sane way is there to look at it?"
             j "All the ridiculousness of every day..."
             j "Doesn't everyone just have to take it all with a grain of salt?"
             $ stress_count += 1
             if stress_count > 2:
                 jump mints_scene
             else:
                 jump end_of_lunch
    
label end_of_lunch:
    
    scene black
    with dissolve
    
    stop music fadeout 2.0
    
    if stress_count == 0:
        scene end_of_lunch_0 movie
        with fade
        show background solid at left

    elif stress_count == 1:
        scene end_of_lunch_1 movie
        with fade
        show background solid at left

    else:
        scene end_of_lunch_2 movie
        with fade
        show background solid at left
    
    play music "sounds/mints_chp7_begin_ost.wav"
    
    j "Then again..."
    j "I am the one sitting in a park on his lunch break,"
    j "quietly weighing the decisions of every moment of my waking life."
    j "Taking it out on my mint budget."
    
    j "And how many have I already taken today?"
    if mints_count == 0:
        j "Wait..."
        j "None? ...Really?"
        j "Wow."
        if difficulty < 1:        
            j "Maybe I'm better at staying cool than I thought."
            j "Or, maybe I put my life on an easy setting or something today."
        else:
            j "Maybe I'm better at staying cool than I thought."
        
        play music "sounds/mints_client_mtg_p3_ost.wav"
        
        j "I just get so caught up in keeping track of it all."
        j "Like there's some kind of score board at the end."
        j "I don't want my life to be a never ending set of choices, good and bad."
        j "I don't want to stress about the score, whatever it might be."
        j "No..."
        j "I want the reward to be something more tangible."
        j "Is that asking too much?"
        j "..."
        j "No..."
        j "I'm not asking for all that."
        j "Just enough to get by."        
    
    elif mints_count == 1:
        j "Only 1?"
        j "That's not too bad."
        
        play music "sounds/mints_client_mtg_p3_ost.wav"
        
        j "Still, I don't know how I do it..."
        j "But I find a way to make everything into some kind of an ultimatum."
        j "Like every little thing could be the big one..."
        j "The one thing that pushes me over the edge into some kind of nuthouse."
        j "I can't treat every experience like that."
        j "I don't want my life to be a never ending set of choices, good and bad,"
        j "where I get a score at the end that I don't even know how to interpret."
        j "I don't want to stress about the score."
        j "I want the reward to be something more tangible."
        j "Maybe I'm asking for too much..."        
        j "..."
        j "Or,"
        j "maybe I'm asking for just enough to get by."
    
    else:
        j "[mints_count] mints?"
        j "Maybe I shouldn't take everything so seriously."
        j "Those things can get expensive."
        j "All that wintergreen technology doesn't come cheap."
        
        play music "sounds/mints_client_mtg_p3_ost.wav"
        
        j "Won't I become one of those people that just stumbles through life?"
        j "Those people who somehow thrive off their own flippancy,"
        j "who make every decision with as much focused thought as a labrador."
        j "But there has to be some alternative..."
        j "Somewhere between riding the wave without a care in the world,"
        j "and letting it crash over me every time I'm determined to swim further."
        j "I don't know."
        j "I don't want my life to be a never ending set of choices, good and bad,"
        j "where I get a score at the end that I don't even know how to interpret."
        j "I don't want to stress about the score."
        j "I want the reward to be something more tangible."
        j "Maybe I'm asking for too much..."
        j "..."
        j "Or,"
        j "maybe I'm asking for just enough to get by."

    jump chapter8
    
    
##############################################################
## Chapter 8 starts here (montage video)                    ##
## Montage video triggered here                             ##
## Cleans up the afternoon, depending on mints count        ##
## Video is slightly different                              ##
## This is the only time player hears the full mints music  ##
##############################################################
         
label chapter8:
    scene black
    with dissolve
    
    stop music fadeout 3.0
    $ renpy.pause(3)
    
    $ scene_count += 1
    
    play movie "chapter8_lp.webm"
    $ renpy.pause(71.0, hard=True)
    
    jump chapter9
    
    
##############################################################
## Chapter 9 starts here                                    ##
## Last opportunity to stress Joseph out                    ##
## With a completely ridiculous choice of what to watch     ##
## This is supposed to bring out the humor in the satire    ##
## It's here that you're supposed to see the ridiculousness ##
##############################################################
         
label chapter9:
    
    scene black
    with dissolve
    
    stop music fadeout 2.0
    
    play sound "sounds/mints_chp9_intro_ost.wav"
    $ renpy.pause(3.15)

    if difficulty < 2:
        $ stress_count = 0

    $ scene_count += 1

    #scene chapter9_%r movie % stress_count
    # scene chapter9_1 movie
    # with fade
    # show background solid at left
    
    if stress_count == 0:
        scene chapter9_0 movie
        with fade
        show background solid at left
    elif stress_count == 1:
        scene chapter9_0 movie
        with fade
        show background solid at left
    else:
        scene chapter9_0 movie
        with fade
        show background solid at left
    
    play music "sounds/mints_chp9_p1_ost.wav"

    j "What a day."
    j "I feel like I survived a hurricane or something."
    j "Whatever it was that happened, I'm done with it."
    j "I'm calling it a day."
    j "I'm getting a glass of water,"
    j "brushing my teeth,"
    j "putting my PJs on,"
    j "chilling out,"
    j "and watching some binge-worthy streaming television entertainment."
    j "I refuse to do anything to the contrary."
    
    scene black
    with dissolve    

    #scene TV_%r movie % stress_count
    scene TV_0 movie
    with fade
    show background solid at left
    
    j "Hmmm..."
    j "How are there always like ten thousand shows recommended just for me?"
    j "And they expect you to pick just one without freaking out?"
    j "I'm not gonna read all the descriptions."
    j "Who has that kind of time?"
    j "No, I'd rather just pick something."
    j "Feel a bit of that well earned American freedom at the end of a long day."
    j "So what'll it be..."
    
    menu:
        "What did I watch yesterday?":
            j "I could just watch whatever I played last."
            j "Yeah."
            j "I don't have the mental energy to pick anything else."
            j "That sounds great."
            j "Another fine episode of derivative 90s sitcoms, coming right up."
            jump chapter10
        "What's recommended just for me?":

            j "I should check out some new stuff."
            j "That does involve more reading..."
            j "Ah, how bad can it be?"
            
            jump tv_options

label tv_options:

    menu:
        "Franz Season 4":
            j "Man, that Franz gets himself into some real hijinks!"
            j "But will he ever tie the knot with Melissa?"
            jump tv_options
        "Park n Wreck Season 2":
            j "The underbelly of the monster truck rally scene."
            j "Who knew the mockumentary directorial style would be so conducive?"
            jump tv_options
        "Grazed Anatomy Season 4":
            j "Best free-roaming farm animal veterinarian drama on television."
            jump tv_options
        "House of Cords Season 3":
            j "Who knew there was so much corruption in the IT industry?"
            jump tv_options
        "30 Rocks Season 4":
            j "Four season later, and somehow,"
            j "a show about a funny guy's rock collection is still pretty solid."
            jump tv_options
        "Howie Met Your Mother Season 5":
            j "I feel like Howie is wearing on me a bit."
            j "He was cool at first but now he's really encroaching on Susan's space."
            jump tv_options
        "Sax and the City Season 3":
            j "The dialogue is a little coarse at times, but still,"
            j "every scene, I feel so engrossed in the jazz scene, I can't help it."
            jump tv_options
        "American Hoarder Story Season 2":
            j "They can sure paint a vivid picture of some real world horrors."
            j "But I can't help but feel that it's too kitschy at times."
            jump tv_options
        "The Bing Bong Theory Season 3":
            j "Onomatopoeic chaos theory staged in a sitcom environment."
            j "It's ambitious, I'll give them that."
            jump tv_options
        "The Walking Dads Season 5":
            j "Season 5, I'm still hooked."
            j "I can't get over how much these real life dads walk every day."
            jump tv_options
        "Fear The Walking Dads Season 2":
            j "The spinoff isn't as good."
            j "A bit of unnecessary ambulophobia, not to mention ageism."
            jump tv_options
        "Awl That Season 1":
            j "It may have only lasted one season."
            j "But a leathercraft-themed sketch comedy show was a one in a million."
            jump tv_options
        "Hey Arnette Season 2":
            j "Things got really weird when they changed the main character."
            j "Didn't really say anything about it either."
            jump tv_options
        "Rickets Powder Season 3":
            j "Extreme sports and experimental medicine"
            j "Together and better than ever."
            jump tv_options
        "Sew Weird Season 2":
            j "There was a real art to the subtlety on this one."
            j "There will never be another paranormal seamstress show like it."
            jump tv_options
        "Forget it... this is impossible.":
            j "Holy crap."
            j "How am I this many seasons behind on everything I watch?"
            j "When did they even make these seasons between the other ones?"
            j "I am so behind."
            j "Look at me."
            j "I can't even relax without stressing myself out."
            j "I need a new hobby."
            j "One that requires no thought, attention span, or time commitment."
            j "But..."
            j "Somehow isn't sleep?"
            j "..."
            j "There is nothing for me here."
            j "Nothing but a void."
            if difficulty > 0:
                jump mints_scene
            else:
                jump chapter10
        "Forget it... these all look like garbage.":
            j "This isn't worth it."
            j "I don't spend all day doing menial tasks in a holding pen,"
            j "to come home and waste my time on endless, pandering cliches."
            j "Does this stuff even qualify as entertainment?"
            j "What even is entertainment anymore?"
            j "Even video games are all starting to get so serious and somber."
            j "And then TV is all this type of moronic hogwash."
            j "Forget it."
            j "I'm going to bed."
            j "Maybe I'll have the patience tomorrow."
            $ stress_count += 2
            if stress_count > 2:
                jump mints_scene
            else:
                jump chapter10

##############################################################
## Chapter 10 starts here                                   ##
## Closing moment, back to bed the same way he woke up      ##
## Tie back to the intro dialogue of falling asleep         ##
## Then car alarm hits again                                ##
##############################################################
    
label chapter10:
    
    scene black
    with dissolve
    
    stop music fadeout 2.0
    $ renpy.pause(1)
    
    if stress_count == 0:
        scene chapter10_0 movie
        with fade
        show background solid at left
    elif stress_count == 1:
        scene chapter10_0 movie
        with fade
        show background solid at left
    else:
        scene chapter10_0 movie
        with fade
        show background solid at left
    
    play music "sounds/mints_chp9_p1_wdrums_ost.wav"

    j "Finally."
    j "I made it."
    j "Yet another day, finally coming to an end."
    j "All of the ridiculousness of the day,"
    j "all of it begins to melt away."
    if snooze_count > 3:
        j "Waking up late..."
    if bag_check < 1:
        j "Forgetting my stupid bus pass..."
    if book_check < 1:
        j "Those stupid library books..."
    if coffee_choice > 0 and go_to_meeting > 0:
        j "That crazy guy from the coffee shop..."
        j "And that insane meeting..."
    elif coffee_choice > 0:
        j "That crazy guy from the coffee shop..."
    elif coffee_choice < 1 and go_to_meeting > 0:
        j "That insane client meeting I wasn't even supposed to be at..."
    j "Everything that came of it..."
    j "All of it fades away."
    j "And I get to let it float on into the ether."
    j "Out into the darkness where I can't find it anymore."
    j "It's lovely."
    j "Lovely quiet."
    j "Quiet."
    
    stop music fadeout 3.0
    
    j "Nothingness."
    j "..."
    j "......."
    
    scene black
    with dissolve
    
    play music "sounds/mints_chp9_p2_loop_ost.wav"
    
    o "Joseph."
    o "This is the voice inside your head."
    o "I'm just checking in..."
    o "Because, sometimes, you know..."
    o "You can really benefit from some outside opinion..."
    if mints_count > 3:
        o "Holy smokes, you downed [mints_count] mints today!"
        o "Wow!"
        o "Sheesh, those are 12 hour mints!"
        o "You gotta try and keep cool, man!"
        o "You should go to sleep. It seems like you need it."
        o "Tomorrow, try to not stress yourself out that much."
        o "Life isn't all that bad."
        o "You have to see the humor in it."
        o "Otherwise, what's the point?"
        o "Here's a great example..."
    elif mints_count > 1:
        o "You downed [mints_count] mints today."
        o "You should try for less tomorrow."
        o "I'm sure you'll do great."
        o "Sleep tight."
        o "Oh, wait,"
        o "one more thing..."
    elif mints_count > 0:
        o "You downed 1 mint today."
        o "You should try for less tomorrow."
        o "I'm sure you'll do great."
        o "Sleep tight."
        o "Oh, wait,"
        o "one more thing..."
    else:
        if difficulty < 1:
            o "Wow, you didn't need any mints today!"
            o "Hold on a hot second..."
            o "Did you use the easy setting?"
            o "Ok, well..."
            o "Big golf clap for you. Really."
            o "How about tomorrow you try to up the ante a little?"
            o "How else do you expect to learn anything from these lil' pep talks?"
            o "Anyways..."
            o "Today's not over yet..."        
        else:
            o "Wow, you didn't need any mints today!"
            o "Isn't it crazy how you can keep your cool like that?"
            o "I mean, it's kind of a bummer that there's only one way to do it..."
            o "Stay on schedule,"
            o "keep a tight, check-listed routine,"
            o "limit your interaction with others,"
            o "keep yourself distracted from your own thoughts where you can..."
            o "But hey!"
            o "Still pretty neat!"
            o "Sleep tight. You deserve it."
            o "Well..."
            o "I mean..."
            o "You deserve it..."
            o "But still..."
        
    $ renpy.pause(1)

    scene chapter10_end movie
    with fade
    show background solid at left
    
    play music "sounds/car_alarm.wav"
    
    j "..."
    j "Are you serious?"
    j "..."
    j "No."
    j "Nope."
    j "Not letting this get to me."
    j "It could be worse."
    j "It could always be worse."
    j "..."
    
    stop music fadeout 3.0
    
    j "See?"
    j "There."
    j "There it is."
    j "Night after night, but only a moment..."
    j "Nirvana."
    j "..."

    scene black
    with dissolve
    
    j "Just have to wait for it."
    
    $ renpy.pause(2)    
    
    play music "sounds/mints_credits_ost.wav"
    
    jump credits 

label credits:
    # scene credit_playback
    # with fade
    # image splash = Text("{size=90}Company Name", text_align=0.5, ypos=0.5) #Placeholder code if you don't have anything to use as a splash image or are just pure lazy.
    # image cred = Text(credits_s, text_align=0.5) #use this if you want to use special fonts
    # image cred = Text(credits_s, text_align=0.5)
    image title = Text("{size=20}Mints", text_align=0.5)
    image writing = Text("{size=20}Story and Logic by \nGerrit Feenstra")
    image music = Text("{size=20}Score and Sound by \nGerrit Feenstra")
    image video = Text("{size=20}Video by \nBrittany and Gerrit Feenstra")
    image gui = Text("{size=20}GUI by \nBrittany Feenstra")
    image programming = Text("{size=20}Developed in Python by \nGerrit and Brittany")
    image renpy = Text("{size=20}Built on Ren'Py", text_align=0.5)
    image location = Text("{size=20}Filmed in Seattle, WA August 2016", text_align=0.5)
    image copyright = Text("{size=20}Made For Fun \n Copyright 2016", text_align=0.5)
    image thanks = Text("{size=20}Thanks for Playing.", text_align=0.5)
    # $ credits_speed = 5 #scrolling speed in seconds
    
    scene black #replace this with a fancy background
    # show cred at Move((0.5, 5.0), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    show title:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(2)
    hide title
    with dissolve
    with Pause(2)
    show writing:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(2)
    hide writing
    with dissolve
    with Pause(2)
    show music:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(2)
    hide music
    with dissolve
    with Pause(2)
    show video:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(2)
    hide video
    with dissolve
    with Pause(2)
    show gui:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(2)
    hide gui
    with dissolve
    with Pause(2)
    show programming:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(2)
    hide programming
    with dissolve
    with Pause(2)
    show renpy:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(2)
    hide renpy
    with dissolve
    with Pause(2)
    show location:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(2)
    hide location
    with dissolve
    with Pause(2)

    show copyright:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(2)
    hide copyright
    with dissolve
    with Pause(2)
    show thanks:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(2)
    hide thanks
    with dissolve
    with Pause(2)
    
    return