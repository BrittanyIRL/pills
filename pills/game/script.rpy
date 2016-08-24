﻿# Pills script - draft copy from RenPy
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

image chapter1_0 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="chapter1_0", play="chapter1_0.webm")
image chapter1_1 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="chapter1_0", play="chapter1_0.webm")
image chapter1_2 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="chapter1_0", play="chapter1_0.webm")

image getup_0 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="getup_0", play="getup_0.webm")
image getup_1 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="getup_0", play="getup_0.webm")
image getup_2 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="getup_0", play="getup_0.webm")

image chapter2_0 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="chapter2_0", play="chapter2_0.webm")
image chapter2_1 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="chapter2_0", play="chapter2_0.webm")
image chapter2_2 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="chapter2_0", play="chapter2_0.webm")

image chapter3_0 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="chapter3_0", play="chapter3_0.webm")
image chapter3_1 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="chapter3_0", play="chapter3_0.webm")
image chapter3_2 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="chapter3_0", play="chapter3_0.webm")

image chapter4_0 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="chapter4_0", play="chapter4_0.webm")
image chapter4_1 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="chapter4_0", play="chapter4_0.webm")
image chapter4_2 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="chapter4_0", play="chapter4_0.webm")

image bag_0_0_1 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="bag_0_0_1", play="bag_0_0_1.webm")
image bag_1_0_1 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="bag_0_0_1", play="bag_0_0_1.webm")
image bag_2_0_1 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="bag_0_0_1", play="bag_0_0_1.webm")

image bag_0_1_1 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="bag_0_1_1", play="bag_0_1_1.webm")
image bag_1_1_1 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="bag_0_1_1", play="bag_0_1_1.webm")
image bag_2_1_1 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="bag_0_1_1", play="bag_0_1_1.webm")

image bag_0_1_0 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="bag_0_1_0", play="bag_0_1_0.webm")
image bag_1_1_0 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="bag_0_1_0", play="bag_0_1_0.webm")
image bag_2_1_0 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="bag_0_1_0", play="bag_0_1_0.webm")

image bag_0_0_0 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="bag_0_1_0", play="bag_0_0_0.webm")
image bag_1_0_0 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="bag_0_1_0", play="bag_0_0_0.webm")
image bag_2_0_0 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="bag_0_1_0", play="bag_0_0_0.webm")

image window_0 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="window_0", play="window_0.webm")
image window_1 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="window_0", play="window_0.webm")
image window_2 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="window_0", play="window_0.webm")

image rafters_0 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="rafters_0", play="rafters_0.webm")
image rafters_1 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="rafters_0", play="rafters_0.webm")
image rafters_2 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="rafters_0", play="rafters_0.webm")

image busppl_0 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="busppl_0", play="busppl_0.webm")
image busppl_1 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="busppl_0", play="busppl_0.webm")
image busppl_2 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="busppl_0", play="busppl_0.webm")

image chapter5_0 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="chapter5_0", play="chapter5_0.webm")
image chapter5_1 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="chapter5_0", play="chapter5_0.webm")
image chapter5_2 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="chapter5_0", play="chapter5_0.webm")

image stoplight_0 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="stoplight_0", play="stoplight_0.webm")
image stoplight_1 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="stoplight_0", play="stoplight_0.webm")
image stoplight_2 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="stoplight_0", play="stoplight_0.webm")

image chapter6_0 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="chapter6_0", play="chapter6_0.webm")
image chapter6_1 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="chapter6_0", play="chapter6_0.webm")
image chapter6_2 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="chapter6_0", play="chapter6_0.webm")

image mgmt_0 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="mgmt_0", play="mgmt_0.webm")
image mgmt_1 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="mgmt_0", play="mgmt_0.webm")
image mgmt_2 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="mgmt_0", play="mgmt_0.webm")

image clientmtg_0 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="clientmtg_0", play="clientmtg_0.webm")
image clientmtg_1 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="clientmtg_0", play="clientmtg_0.webm")
image clientmtg_2 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="clientmtg_0", play="clientmtg_0.webm")

image chapter7_0 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="chapter7_0", play="chapter7_0.webm")
image chapter7_1 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="chapter7_0", play="chapter7_0.webm")
image chapter7_2 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="chapter7_0", play="chapter7_0.webm")

# then we have the three montage videos, for chapter 8, which we want to treat as not clickable videos

# image chapter9_0 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="chapter9_0", play="chapter9_0.webm")
# image chapter9_1 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="chapter9_0", play="chapter9_0.webm")
# image chapter9_2 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="chapter9_0", play="chapter9_0.webm")

# image chapter10_0 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="chapter10_0", play="chapter10_0.webm")
# image chapter10_1 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="chapter10_0", play="chapter10_0.webm")
# image chapter10_2 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="chapter10_0", play="chapter10_0.webm")

# then we have the credits which we want to treat as not clickable videos, but still want to keep the car alarm

##############################################################
## Chapter 1 begins here                                    ##
## All counted dependents begin here                        ##
## Numbered chapters differ from other segments in that if  ##
## pills scene is triggered, player will skip to next       ##
## numbered chapter, missing all interim.                   ##
## Chapter 1 starts with getting out of bed                 ##
## Number of alarm snoozes is used numerous times later     ##
##############################################################


# The game starts here.
label start:
    
    $ scene_count = 1
    $ stress_count = 0
    $ pills_count = 0
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
    
    $ randmtg = renpy.random.choice(["plan", "projection", "marketing", "benefits"])
    $ randlng = renpy.random.choice(["french", "latin"])

    scene black
    show background solid at left

    j "There's this feeling..."
    j "right before I fall asleep,"
    j "right before I fade into oblivion,"
    j "where I actually feel like my mind is at peace."
    j "You can't sleep when you're stressed."
    j "Everyone knows that."
    j "You have to tell your brain to be quiet,"
    j "get it to stop ticking,"
    j "stop running through the endless loose ends of your day."
    j "Only after that can you let go,"
    j "let loose of that tension,"
    j "and fall into the nirvana of the darkness."
    j "That moment..."
    j "that feeling..."
    j "that's what I wait for every single day."

    scene chapter1_0 movie
    with fade
    show background solid at left
    show background solid at left

    
    play sound "sounds/alarm_clock.wav"

    $ randchp1 = renpy.random.choice(["Already? Wow.", "Please tell me it\'s Sunday.", "... How is it morning?"])

    j "[randchp1]"
    j "I should probably get up."

    menu:

        "Get up.":

            jump getup

        "Hit snooze.":
            
            jump snooze_1


label getup:
    
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

    play music "sounds/pills_getting_ready_ost.wav" fadein 2.0

    j "Another day." # "Here we go again." "Alright, alright, I'm up."
    
    if snooze_count < 1:
         j "I should cook something."
         j "I kind of hate it though."
         j "I’m immediately going to have to do all the dishes."
         j "Are the dishes even clean? I can’t remember."
         j "At least I have coffee."
    elif snooze_count < 4:
         j "Do I have time to eat?"
         j "I guess I could grab something on my way in to work."
         j "I don’t know. Those coffees shops are getting so expensive."
         j "Plus everybody has headphones and isn’t paying attention."
         j "They don't look happy at all and it’s horrible."
         j "What the hell is happening to the world?"
    else:
         j "I can't believe I slept so much."
         j "There’s no way I have time to make something."
         j "I’m going to be lucky if I get anything at all."
    
    menu:

        "Cook something.":

            jump cook

        "Grab something on the way instead.":
        
            jump grab

label cook:

    if snooze_count < 1:
         j "Fine, I’ll cook something."
         j "Probably better for me anyways."
         j "Those scones are loaded with sugar."
         jump chapter2
    elif snooze_count < 4:
         j "Fine, I’ll cook something."
         j "But I won’t have much time. Might be late."
         $ stress_count += 1
         if stress_count > 2:
              jump pills_scene
         else:
              jump chapter2
    else:
         j "I should cook something..."
         j "I'm putting on weight, I know it."
         j "Who am I kidding? I don't have time for that!"
         j "Geez, what was I thinking?"
         $ Stress_count += 1
         $ coffee_choice = 1
         if stress_count > 2:
              jump pills_scene
         else:
              jump chapter2


label grab:

    $ coffee_choice = 1
    if snooze_count < 1:
         j "Screw cooking. It’s a free country."
         j "I’m gonna get one of those sugar scones."
         j "I don’t care how horrible they are for you."
         jump chapter2
    elif snooze_count < 4:
         j "Whatever. I don’t have time to cook."
         j "I’ll just grab something on the way."
         jump chapter2
    else :
         j "I can get something on the way."
         j "I have time."
         j "No need to freak out."
         j "Play it cool, man."
         j "Telling myself to be cool in a mirror."
         j "Just like in Reservoir Dogs."
         j "Guess it's not all bad."
         jump chapter2
         

label snooze_1:

    $ snooze_count += 1

    scene chapter1_0 movie
    with fade
    show background solid at left
    show background solid at left
    
    play sound "sounds/alarm_clock.wav"

    j "Was that already 10 minutes?"

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

    j "I hate that car."

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
    
    jump pills_scene
 

##############################################################
## Pills scene begins here                                  ##
## This is the scene that happens when stress count > 2     ##
## Stress count is reset after this                         ##
## Scene count is pushed forward 1                          ##
##############################################################
    
label pills_scene:
    #scene that happens when stress count > 2

    scene black
    with dissolve
    
    stop music fadeout 1.0

    if pills_count == 0:
        j "I don't need this right now."
        j "I'm just going to handle it."
        j "Put it out of mind, that's all."   
    elif pills_count == 1:
        j "I'm not doing this."
        j "I have too much to do and too much left to do today."
        j "I'm cutting this off before it starts."
    elif pills_count == 2:
        j "I'm not taking this."
        j "Maybe I have a real problem."
        j "Isn't this supposed to help me?"
        j "Yeah... of course it is."
        j "This is helping. This is the answer."
    elif pills_count == 3:
        j "I can't believe this."
        j "Why am I doing this?"
        j "Why can't I get a grip?"
        j "I'm not letting this get the best of me."
        j "I can't."
    else:
        j "That's it" # "What the hell is happening to me?", "I'm going to freak out."
        j "I can't handle this."
        j "I need escape."
        j "Now."
    
    play sound "sounds/pill_bottle.wav"
    # play sound "exhale.wav"
    
    j "That's better."
    
    $ pills_count += 1
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
    elif scene_count == 5 and coffee_choice > 0:
        jump coffeeshop
    elif scene_count == 5 and coffee_choice < 1:
        jump chapter6
    elif scene_count == 6 and go_to_meeting > 0:
        jump clientmeeting
    elif scene_count == 6 and go_to_meeting < 1:
        jump chapter7
    elif scene_count == 7:
        jump chapter8
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

        hotspot (22, 300, 314, 106) clicked Return("book")        #library book for bus/email
        hotspot (0, 93, 168, 80) clicked Return("bag")        #bag for bus pass
        hotspot (436, 406, 186, 92) clicked Return("calendar")   #calendar for meeting 
        hotspot (575, 133, 122, 167) clicked Return("door")      #door is leave
        
label chapter2:

    #getting out the door

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

    
    play music "sounds/pills_chp_2_ost.wav" fadein 2.0
    
    j "What am I forgetting?"
    j "I always forget something."

    jump chapter2_w_map

label chapter2_w_map:

    call screen chapter2_map
    
    $ result = _return
    
    if result == "book":
        $ book_check = 1
        j "Oh right I need to grab that library book."
        j "I think it's due already."
        j "I never have time to read finish anything."
        j "Whatever. One more bus ride made less awkward."
        jump chapter2_w_map
    elif result == "bag":
        $ bag_check = 1
        j "Did I pack everything for today?"
        j "Oh damn I almost forgot my bus pass."
        j "That would have been annoying."
        jump chapter2_w_map
    elif result == "calendar":
        $ calendar_check = 1
        j "Do I have anything at work today?"
        j "Sure doesn't look like it."
        j "Probably for the best."
        jump chapter2_w_map
    elif result == "door":
        j "Guess I should hit the road."
        j "Hope whatever it was isn't important."
        # play the outro cutscene where I leave or turn out light or something
        jump chapter3
        
##############################################################
## Chapter 3 begins here                                    ##
## Chapter 3 is a transition to see if you checked the bag  ##
## Getting on the bus before work                           ##
##############################################################

label chapter3:
    # bus stop

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

    
    play music "sounds/pills_chp_3_ost.wav" fadein 2.0

    j "Bus arrives in... zero minutes?"
    j "It's not even down the hill yet."
    j "I can see the damn hill - it's not there."
    j "I don't understand why they even make apps for bus times."
    j "Pure masochism is what it is."
    j "..."
    j "I wonder how much those small sanctions of every day life..."
    j "the plausibility of a missed bus..."
    j "the crosswalk you see in the distance that you might not catch..."
    j "the time you probably won't have to go to the gym..."
    j "How many are responsible for all the stress you feel?"
    
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
             j "I'll tell you."
             j "Nobody."
             $ stress_count += 1
             if stress_count > 2:
                 jump pills_scene
             else:
                 jump bus_time

         "All the sanctions.":
             j "Yeah. Probably the whole enchilada."
             j "Actually, admitting it like that kind of takes a load off."
             j "That way, a lot less to blame on myself."
             j "I can't possibly be the only one, right?"
             j "Maybe everybody else feels the same way."
             j "Or maybe not. Who knows?"
             j "I'm no genius."
             j "I'm just a guy trying catch his bus."
             j "On the way to another round of daily monotony."
             jump bus_time

         "Am I using that word correctly?":
             j "Ah, never mind."
             j "I swear, I can get on these tangents with myself"
             j "and get lost for days at a time."
             j "This one is hardly worth it."
             j "Boring conversation with myself anyway."
             j "Still... I'm deleting this app."
             j "It's horrible and pointless."
             j "There."
             j "I feel better already."
             jump bus_time
    
label bus_time:

    # play sound "busarrival.wav"
    j "There's the bus, finally."
    
    if bag_check > 0:
        j "Glad I remembered my pass."
        j "That would have been really annoying."
        j "Let alone stressful."
        j "I probably don't need any more stress than a normal day holds."
        j "Let's just try and keep it at a minimum today."
    else:
        j "Let me just grab my pass..."
        j "Wait... where is it?"
        j "Did I take it out of my bag?"
        j "I totally took it out of my bag."
        j "Last night, when I was rushing to catch the bus back from downtown."
        j "Dammit."
        j "I hate everything."
    $ stress_count += 2
    if stress_count > 2:
        jump pills_scene
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
    
    play music "sounds/pills_chp_4_ost.wav" fadein 2.0

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
    j "Look at me,"
    j "Preferring my own company to that of others."
    j "And you wonder why people go crazy."
    j "Doing this every single day."
    
    jump chapter4_w_map
    
    
# defining hotspots here, to be called later 
screen chapter4_map:
    imagemap:
        ground "blank.png"
        #we need to change these

        hotspot (163, 75, 332, 86) clicked Return("window")        #look out window
        hotspot (525, 132, 222, 204) clicked Return("openbag")        #look in yr bag
        hotspot (228, 268, 130, 84) clicked Return("ads")            #ads on bus 
        hotspot (0, 300, 163, 225) clicked Return("people")      #people on bus
        # hotspot (1, 1, 1, 1) clicked Return("nothingbus")          #NOTHINGNESS 
    
label chapter4_w_map:

    call screen chapter4_map
    
    $ result = _return
    
    if result == "window":
        if stress_count == 0:
            scene window_0 movie
            with fade
            show background solid at left
        elif stress_count == 1:
            scene window_1 movie
            with fade
            show background solid at left
        else:
            scene window_2 movie
            with fade
            show background solid at left
        j "I look out the window."
        j "I see a city unhappy with itself."
        j "Constantly changing."
        j "Wishing for something apart from monotony."
        j "Something to draw a crowd."
        j "Something to brag about."
        j "I wonder if it will ever find that."
        jump chapter4_w_map
    elif result == "openbag":
        if stress_count == 0 and calendar_check > 0 and book_check > 0:
            scene bag_0_1_1 movie
        elif stress_count == 1 and calendar_check > 0 and book_check > 0:
            scene bag_1_1_1 movie
        elif stress_count == 2 and calendar_check > 0 and book_check > 0:
            scene bag_2_1_1 movie
        elif stress_count == 0 and calendar_check < 1 and book_check > 0:
            scene bag_0_0_1 movie
        elif stress_count == 1 and calendar_check < 1 and book_check > 0:
            scene bag_1_0_1 movie
        elif stress_count == 2 and calendar_check < 1 and book_check > 0:
            scene bag_2_0_1 movie
        elif stress_count == 0 and calendar_check > 0 and book_check < 1:
            scene bag_0_1_0 movie
        elif stress_count == 1 and calendar_check > 0 and book_check < 1:
            scene bag_1_1_0 movie
        elif stress_count == 2 and calendar_check > 0 and book_check < 1:
            scene bag_2_1_0 movie
        elif stress_count == 0 and calendar_check < 1 and book_check < 1:
            scene bag_0_0_0 movie
        elif stress_count == 1 and calendar_check < 1 and book_check < 1:
            scene bag_1_0_0 movie
        elif stress_count == 2 and calendar_check < 1 and book_check < 1:
            scene bag_2_0_0 movie
        # really hard to notice the ellipsis, adding second one
        j "..."
        j "..."
        jump chapter4_w_map
    elif result == "ads":
        $ bus_check = 2
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
        j "Look at these ads."
        j "They line every page."
        j "Hell, they even line the rafters of the bus."
        j "Have you recently gone through a divorce?"
        j "Are you going through a fiscal dillema?"
        j "Have you lost your sexual potency?"
        j "Does your child have access to crystal meth?"
        j "Call here."
        j "Call there."
        j "Talk to someone, anyone."
        j "When has that kind of anonymous offer ever helped anyone?"
        jump chapter4_w_choice
    elif result == "people":
        $ bus_check = 1
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
        j "Look at these poor suckers."
        j "Just like me."
        j "Sucked into some false dream of stability."
        j "There's comfort in consistency, you know?"
        j "You don't have to think much about what's going on around you."
        j "But what do you really lose in the interim?"
        j "When do you stop being human,"
        j "and instead just become a monkey?"
        j "At least monkeys don't talk to themselves inside their heads."
        j "Or I don't know..."
        j "maybe they do."
        jump chapter4_w_choice
#    elif result == "nothingbus":
#        jump chapter4_w_choice
        
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
    
    if bus_check > 1:
        j "You can't really help but look away though can you?"
        j "Looking at all those problems,"
        j "imagining yourself in the thick of it all,"
        j "just to feel something."
        j "Kind of like Fight Club that way, I guess."
        j "And yet, I have a choice."
        j "To stare onwards..."
        j "or to turn and run."
    elif bus_check > 0:
        j "You can't really help but look away though can you?"
        j "Looking at all their boredom,"
        j "their utter apathy towards the problems of the world,"
        j "just imagining yourself in the thick of it all."
        j "Am I one of them?"
        j "Maybe I have to look closer."
        j "Maybe that's my choice..."
        j "To stare onwards,"
        j "or to turn and run."
    else:
        j "I just have this feeling."
        j "This indescribable itch."
        j "I guess you could call it a fear of missing out,"
        j "but I'm not really afraid of anything"
        j "and I don't really feel like going anywhere."
        j "It's more of an urge, I guess."
        j "An urge to find what it is that makes the world tick."
        j "What makes everyone else get out of bed in the morning?"
        j "God knows its hard enough finding a reason."
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
    j "Keep trying to find some meaning to all of it."
    if bus_check > 1:
        j "But geez, look at all I have left to deal with."
        j "There are so many people with so many problems."
        j "Who am I to think I'm any better than them?"
    elif bus_check > 0:
        j "But people, they keep staring."
        j "I feel like every step of the way I'm being watched."
        j "Like they are keeping tabs,"
        j "Making sure somehow I don't rise above the rest of them."
        j "Look at their eyes,"
        j "hungry for mutual suffering."
        j "It's terrifying."
    else:
        j "But what's the point?"
        j "There's so much change,"
        j "so much that no one has told me how to plan for or avoid."
        j "Who am I to think I'm going to win the Golden Ticket,"
        j "somehow figure all of this stuff out before the rest of them?"
        j "There's just no way."
        j "No way at all."
    $ stress_count += 2
    if stress_count > 2:
        jump pills_scene
    else:
        jump chapter5

label turn_and_burn:

    j "Probably best to avoid it."
    j "That conversation is terrifying anyways."
    if bus_check > 1:
        j "I don't want to know about all this stuff."
        j "The 18 things my loved ones don't know about depression."
        j "The 6 ways my pre-teen can find drugs before they reach high school."
        j "The 27 different ways I can die from an open wound on the street."
        j "I'm not interested."
        j "I'm not doing that to myself."
        j "I'd rather internalize."
    elif bus_check > 0:
        j "I don't want to know how other people cope."
        j "I don't want to have to dig into their messy lives to find a solution."
        j "Mine's messy enough as it is,"
        j "doing my best every day to try and play the wallflower,"
        j "stay out of people's way and out of their problems."
        j "I'm not opening up to that."
        j "I don't think I could handle it."
        j "I'd rather internalize."
    else:
        j "I mean, what's the point?"
        j "There's so much change,"
        j "so much that no one has told me how to plan for or avoid."
        j "Who am I to think I'm going to win the Golden Ticket,"
        j "somehow figure all of this stuff out before the rest of them?"
        j "There's just no way."
        j "No way at all."
    $ stress_count += 1
    if stress_count > 2:
        jump pills_scene
    else:
        jump chapter5
         
label book_instead:

    j "Wait..."
    j "Why am I doing this to myself?"
    j "I don't have to figure any of this stuff out."
    j "It won't get me anywhere, anyways."
    j "I don't have to read the ads."
    j "I don't have to talk to people."
    j "Hell, I don't really have to do anything at all."
    j "I can just read instead."
    j "I should have that book in my bag..."
    if book_check > 0:
        j "Yep, there it is."
        j "See? Nothing to worry about at all."
        j "Just the voice inside my head telling me everything is going to be alright."
        jump chapter5
    else:
        j "Wait, did I forget those library books?"
        j "Aren't they due today?"
        j "That's the third time this month."
        j "I can't do anything right, not even relax."
        $ stress_count += 2
        if stress_count > 2:
            jump pills_scene
        else:
            jump chapter5

##############################################################
## Chapter 5 begins here                                    ##
## Walking in to work                                       ##
## Short transition before coffee shop or get in            ##
##############################################################
         
label chapter5:

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
    
    play music "sounds/pills_chp_5_ost.wav" fadein 2.0

    j "I've been thinking..."
    j "Every day I take the same exact steps to work."
    j "Well, maybe not exact."
    j "I guess there's the deviation of a stoplight or two along the way."
    j "But other than that, nothing - no variation."
    j "And when I do try and mix it up, going this way or that,"
    j "going down a block or two to hit the better coffee shop,"
    j "or going to the ATM before work so I don't have to go after,"
    j "there's this tiny sting,"
    j "this simple twitch of a feeling,"
    j "that tells me something is wrong."
    j "All our studies on evolution and anthropology,"
    j "they tell us that humans have succeeded due to natural selection."
    j "The greater comprehension of survival within the hunter-gatherer,"
    j "that's what allowed him to persevere."
    j "I mean, sure, that was hundreds of thousands of years ago."
    j "But when I take the longer path to work and feel that twitch,"
    j "when I feel the hair standing up on the back of my neck"
    j "like someone is watching me,"
    j "waiting to tell me I'm out of line,"
    j "I wonder,"
    j "where are we now?"
    
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

    j "Hunter-gatherers worked in teams to survive."
    j "They'd take down giant wooly mammoths by overwhelming them."
    j "Larger nomadic villages meant greater security for everyone."
    j "Nowadays, it's the opposite."
    j "Half a dozen people all standing at a stoplight,"
    j "and none of us are rewarded for communicating."
    j "No one feels safer in the company of strangers."
    j "I could try and make smalltalk to alleviate the boredom,"
    j "but half the time I'm afraid I'll inadvertently offend someone."
    j "Like my greeting will be seen as a narcissistic cry for attention."
    j "Just another heterosexual cisgender white male"
    j "waltzing down the street, pretending the world is his."
    j "But I don't know..."
    j "How else am I supposed to engage with other people?"
    j "Do I keep on with my dissipating college friends and boring coworkers forever?"
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
                          jump pills_scene
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
                          jump pills_scene
                      elif coffee_choice > 0:
                          jump coffeeshop
                      else:
                          jump chapter6
                  "Nice weather today.":
                      j "Ok, a few token nods for the world's biggest elevator cliche."
                      j "Still, that wasn't the worst thing ever."
                      j "No lifelong friends, but no disgust either."
                      j "Maybe there's comfort in monotony after all."
                      if coffee_choice > 0:
                          jump coffeeshop
                      else:
                          jump chapter6
                  "How about them Hawks?":
                      j "Wait, now that guy is trying to follow up."
                      j "He's talking about the game last Sunday."
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
                          jump pills_scene
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
    
    if stress_count == 0:
        scene coffeeshop_0 movie
        with fade
        show background solid at left
    elif stress_count == 1:
        scene coffeeshop_1 movie
        with fade
        show background solid at left
    else:
        scene coffeeshop_2 movie
        with fade
        show background solid at left
    
    play music "sounds/pills_coffee_shop_ost.wav" fadein 2.0
    
    j "Always a line."
    j "I don't know why I ever think this is going to save time."
    j "Still, worth it..."
    j "I get exhausted so fast if I don't have anything in the morning."
    j "I'm not the only one, obviously."
    j "All these people here, like me."
    j "All waiting on the same ringer to kick off the day."
    j "One credit card at a time."
    
    # play sound "guyyelling.wav"
    
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

    j "No, no, forget it."
    j "He'll be gone in a second."
    j "It isn't my place."
    j "The baristas here are used to it..."
    j "She'll bounce back."
    
    # play sound "guyyelling2.wav"
    
    j "..."
    j "He's not stopping."
    j "What a complete jerk."
    j "I don't want to intrude, but wow, this is horrible."
    j "All these other people too, just like me..."
    j "Watching and waiting,"
    j "waiting for the discomfort to pass,"
    j "not her discomfort... ours."
    j "It's pathetic."
    j "It's wrong."
    j "I'm better than this, aren't I?"

    menu:

         "Stay staying quiet.":
             j "No..."
             j "I really shouldn't get involved."
             j "It's all ridiculous enough as it is."
             j "That guy will get what's coming to him."
             j "Still horrible to listen to."
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
    
    o "You are a complete asshole, you know that?"
    o "If I ever talk to me again, I swear I'll punch you in the face."
    o "And forget this stupid coffee shop."
    o "I always hated it here anyways."
    o "I'm out of here."
    
    j "..."
    j "Thank god he's gone."
    j "What a moron."
    j "But now everyone is staring at me, like I'm the one that did something wrong."
    j "Why are they doing that?"
    j "Did I burst their bubble of detachment?"
    j "Did I break the unspoken pact to stay out of the way?"
    j "Is that all the thanks I get for trying to be a good person?"
    j "Forget it."
    j "That wasn't worth it at all."

    $ stress_count += 2
    if stress_count > 2:
        jump pills_scene
    else:
        jump chapter6
         
label nada_coffee:

    j "Forget this, I'm leaving."
    j "That guy is way too much of a jerk to deal with today."
    j "Now I'm going to be hungry all morning."
    j "Ah, man..."
    j "That just makes me hate that guy even more."
    j "Forget it, I don't even care."
    j "I'm just going to get my ass to work."
    j "The only sane place anywhere outside the confines of my apartment."
    j "How demented is that?"
    j "One sick joke after another, today."

    $ stress_count += 1
    if stress_count > 2:
        jump pills_scene
    else:
        jump chapter6


##############################################################
## Chapter 6 begins here                                    ##
## Short chapter about getting in                           ##
## Small, immediate choices for meeting chapters            ##
## Phone will trigger mgmt meeting or not                   ##
##############################################################
         
label chapter6:

    $ scene_count += 1
    
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
    
    play music "sounds/pills_chp_6_ost.wav" fadein 2.0
    
    if bag_check > 0:
        j "Alright."
        j "I made it into work."
        j "The hard part is over."
        j "From here, the boredom is all well within the realm of reason."
        j "I just need to make it through without going nuts."
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
             
             if randmtg = "plan":
                 j "Something about a renewed business plan?"
                 j "Focus on big picture."
                 j "Moving the wheels of history..."
                 j "Wait, where have I heard that before?"
             elif randmtg = "projection":
                 j "Something about bad quarterly earnings?"
                 j "Yada yada yada..."
                 j "Trying to turn things around in the future..."
                 j "Well, yeah. Aren't we all?"
             elif randmtg = "marketing":
                 j "Something about globalized marketing outreach?"
                 j "Globally unified..."
                 j "Traditionally untraditional..."
                 j "Could there be any more hot words in here?"
                 j "This is bonkers."
             elif randmtg = "benefits":
                 j "Something about an updated benefits package?"
                 j "Wow, I wonder if I get acupuncture now..."
                 j "Oh wait, it's not for me. It's for someone else..."
                 j "Whatever."
             
             if calendar_check > 0:
                 "I don't have anything today - I checked my calendar."
                 "This can't be for me."
             else:
                 "Stil..."
                 "Am I supposed to go to this?"
                 "Is this on my calendar?"
                 "I have no idea."

             jump phonering

         "Do menial labor.":
             j "I got it."
             j "Desk cleaning time."
             j "That will put my mind at peace."
             j "You know, it really is disturbing how dirty your workspace gets"
             j "just under normal working conditions."
             j "Look how much dead skin there is just buried in my keyboard."
             j "If I shook that thing upside down it would look like a blizzard."
             j "And look at all these little hairs all over my papers and my mousepad!"
             j "Do I really stress myself out that much?"
             j "Or are we all really falling apart under these damn fluorescents?"
        
             jump phonering
         
         "Reread 7 Habits of Highly Effective People.":
             j "Right."
             j "I gotta focus up with some genius stuff."
             j "I need indepence..."
             j "I NEED SYNERGY"
             j "I have no idea how to get synergy, though."
             j "I barely have enough normal kind of energy, most days."
             if book_check > 0:
                 j "Oh, that reminds me."
                 j "I have to hit the library on my lunch to return those books."
             else:
                 j "Ah crap."
                 j "This just reminds me I forgot those damn library books again."
                 j "I hate books."
         
             jump phonering
         
         "Get hyped by watching Glengarry Glen Ross on Youtube.":
             j "I know what it is."
             j "I just need some fire under me."
             j "I'm gonna find that Youtube video."
             j "Where Alec Baldwin is a total dick,"
             j "but he's also like some kind of sales god."
             j "Is his name four words or three?"
             
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
             j "This morning was plain stupid."
             j "I deserve just a second to gather my thoughts."
             j "No noise."
             j "No commitments..."
             j "Just that fleeting daily moment of..."
         
             jump phonering

label phonering:
  
    # play sound "ringer.wav"
    
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
    
    o "I was just checking in before our big meeting today."
    o "Making sure you are all set to go for your presentation!"
    
    j "..."
    
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
                          
                          $ stress_count += 2
                          if stress_count > 2:
                              jump pills_scene
                          else:
                              jump clientmeeting           
                      
                      "No way, José.":
                      
                          o "..."
                          o "Wait a minute..."
                          o "Who is this?"
                          
                          j "Joseph... from sales."
                          
                          o "Oh."
                          o "Sorry about that, Joseph."
                          o "I meant to call Joe, from marketing."
                          o "Must have gotten the two of you mixed up."
                          o "All you kids look the same anyways."
                          o "Well, have a good one!"
                          
                          j "..."
                          j "Alright."
                          j "If anybody else has any curveballs to throw,"
                          j "now's your chance."
                          j "..."
                          j "None?"
                          j "Alright, I'm going to lunch."
                          
                          jump chapter7
  
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
        jump pills_scene
    else:
        jump mgmtmeeting  

label mgmtmeeting:
    
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
    
    play music "sounds/pills_mgmt_mtg_ost.wav" fadein 2.0
    
    o "Hey Joe how's it hanging?"
    
    j "Hi Tom..."
    j "It's Joseph, not Joe."
    j "I hate it when people call me Joe."
    
    o "Sure thing, Joe!"
    
    j "..."
    j "What do you need?"
    
    o "I was just checking in before our big meeting today."
    o "Making sure you are all set to go for your presentation!"
    
    j "..."
    
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
                          
                          $ stress_count += 2
                          if stress_count > 2:
                              jump pills_scene
                          else:
                              jump clientmeeting           
                      
                      "Don't think so.":
                      
                          o "..."
                          o "Wait a minute..."
                          o "You're not Joe."
                          
                          j "I'm not?"
                          
                          o "Like Joe from marketing."
                          
                          j "Oh."
                          j "No."
                          j "I'm Joseph... from sales."
                          
                          o "Damn."
                          o "Sorry about that, Joseph."
                          o "Must have gotten the two of you mixed up."
                          o "All you kids look the same nowadays."
                          o "Hard for us experience veterans to keep track."
                          o "Some mixup, eh?"
                          o "Well have a good one!"
                          
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
    
##############################################################
## Client meeting begins here                               ##
## Dependent on coffee, email, snooze, etc                  ##
## Pretty much geared towards a meltdown                    ##
##############################################################
         
label clientmeeting:
    
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
    
    play music "sounds/pills_client_mtg_ost.wav" fadein 2.0
    
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
    
    j "Of course he picks the chair furthest from me..."
    
    if coffee_choice > 0:
        j "Wait a second..."
        j "Oh my god."
        j "That's the guy from the coffee shop."
        
        if guy_talk > 0:
            o "Well what are the odds?"
            o "Joe, did you say it was?"
            
            j "Um... Joseph, actually."
            
            o "Alright, Joe."
            
            j "Let's see what brilliant stuff you have for me."
            
            $ stress_count += 2
            
            if stress_count > 2:
                j "Oh no."
                j "I think I'm having a panic attack."
                
                o "Please."
                o "You are totally faking it, you scumbag."
                
                j "No, really."
                j "I need my pills."
                j "They are at my desk."
                
                o "This is ridiculous."
                
                j "This is..."
                j "I need to get out of here..."
                
                $ meeting_panic += 1
                
                jump pills_scene
            else:
                jump meeting_prompt
                
        else:
            j "That guy was a complete jerk to that barista."
            j "What the hell is going to do to me?"
            
            o "Go ahead whenever you feel like it, Joe."
            o "I don't have all day here, you know."
            
            $ stress_count += 1
            
            if stress_count > 2:
                j "Oh no."
                j "I think I'm having a panic attack."
                
                o "What?"
                o "What's going on?"
                
                j "Please."
                j "I need my pills."
                j "They are at my desk."
                j "I need to go get them."
                
                o "This is utterly bizarre."
                o "We aren't selling a Life Alert, here, you know..."
                
                j "I know that..."
                j "It's just..."
                j "Really..."
                j "I need to get out of here..."
                
                $ meeting_panic += 1
                
                jump pills_scene
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
            if randmtg = "plan":
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
                o "Tom, who the hell is this asshat?"
            
                $ stress_count += 2
            
                if stress_count > 2:
                    j "Oh no."
                    j "I think I'm having a panic attack."
                
                    o "You'd better have a panic attack."
                    o "I don't see any way this is going to end any better."
                
                    j "No, really."
                    j "I need my pills."
                    j "They are at my desk."
                
                    o "Well I'm not going to carry you if that's what you're asking."
                
                    j "This is..."
                    j "I need to get out of here..."
                
                    $ meeting_panic += 1
                
                    jump pills_scene
                else:
                    jump meeting_w_map

             
        "So about your quarterly projections...":
            if randmtg = "projection":
                o "Not the best opening line I've ever heard..."
                o "But I'll take it."
                o "Let's see what you plan on doing about them."
                 
                jump meeting_w_map
            
            else:
                o "Quarterly projections?"
                o "You don't even know what this meeting is for, do you?"
                o "Tom, who are these monkeys that do your dirty work nowadays?"
            
                $ stress_count += 2
            
                if stress_count > 2:
                    j "Oh no."
                    j "I think I'm having a panic attack."
                
                    o "I've got a quarterly projection for you."
                    o "It's called a quarter life crisis."
                
                    j "No, really."
                    j "I need my pills."
                    j "They are at my desk."
                
                    o "Get a job."
                
                    j "This is..."
                    j "I need to get out of here..."
                
                    $ meeting_panic += 1
                
                    jump pills_scene
                else:
                    jump meeting_w_map
             
        "So about your marketing campaign...":
            if randmtg = "marketing":
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
            
                $ stress_count += 2
            
                if stress_count > 2:
                    j "Oh no."
                    j "I think I'm having a panic attack."
                
                    o "Not a good brand image, Joe."
                
                    j "No, really."
                    j "I need my pills."
                    j "They are at my desk."
                
                    o "Survey says..."
                    o "Whoops, sorry Joe."
                    o "Just not a very popular response."
                
                    j "This is..."
                    j "I need to get out of here..."
                
                    $ meeting_panic += 1
                
                    jump pills_scene
                else:
                    jump meeting_w_map
        
        "So about your employee benefits policy...":
            if randmtg = "benefits":
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
            
                $ stress_count += 2
            
                if stress_count > 2:
                    j "Oh no."
                    j "I think I'm having a panic attack."
                
                    o "Still not covered under our policy, sorry."
                
                    j "No, really."
                    j "I need my pills."
                    j "They are at my desk."
                
                    o "I sure hope I didn't pay for those."
                    o "What's your copay here, anyways?"
                    o "Swanky lookin' office like this, probably pretty low."
                    o "Damn socialists."
                
                    j "This is..."
                    j "I need to get out of here..."
                
                    $ meeting_panic += 1
                
                    jump pills_scene
                else:
                    jump meeting_w_map

# defining hotspots here, to be called later 
screen meeting_map:
    imagemap:
        ground "blank.png"
        #we need to change these

        hotspot (8, 200, 100, 100) clicked Return("phone")        #use the phone
        hotspot (204, 50, 78, 78) clicked Return("easel")         #use the easel
        hotspot (452, 79, 78, 78) clicked Return("tv")            #use the tv 
        hotspot (602, 316, 300, 300) clicked Return("papers")     #use the papers
        hotspot (1, 1, 1, 1) clicked Return("desk")               #use the desk 
    
label meeting_w_map:

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
                
                $ stress_count += 1
            
                if stress_count > 2:
                    j "Oh no."
                    j "I think I'm having a panic attack."
                
                    o "Wow, sure a shame Jim isn't here."
                    o "Sounds like it was more his presentation than yours."
                
                    j "No, really."
                    j "I need my pills."
                    j "They are at my desk."
                
                    o "I don't have time for this."
                
                    j "I need to get out of here..."
                
                    $ meeting_panic += 1
                
                    jump pills_scene
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
                
                $ stress_count += 1
            
                if stress_count > 2:
                    j "Oh no."
                    j "I think I'm having a panic attack."
                
                    o "You should visualize some serenity."
                
                    j "No, really."
                    j "I need my pills."
                    j "They are at my desk."
                
                    o "No really. It's worth my time and yours."
                    o "Take all you need."
                
                    j "I need to get out of here..."
                
                    $ meeting_panic += 1
                
                    jump pills_scene
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
                
                $ stress_count += 1
            
                if stress_count > 2:
                    j "Oh no."
                    j "I think I'm having a panic attack."
                
                    o "Is this part of your art piece, or..."
                
                    j "No, really."
                    j "I need my pills."
                    j "They are at my desk."
                
                    o "I don't have time for this."
                
                    j "I need to get out of here..."
                
                    $ meeting_panic += 1
                
                    jump pills_scene
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
                        
                        j "I don't have any problems!"
                        
                        o "What do you call your lack of a presentation then?"
                        o "Right... not problems."
                        o "Just failure."
                        
                        $ meeting_panic += 1
                
                        jump pills_scene   
                    
                    "At my desk, actually.":
                    
                        o "Is it on a..."
                        o "Flash drive or something?"
                        
                        j "That's exactly where it is."
                        j "I forgot to grab it."
                        j "Sorry about that."
                        
                        o "Well go and grab it, Joe."
                        o "Don't want to waste Mr. Mills' time."
                        o "Any more than necessary that is..."
                        
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
                        j "Let me just get it up and running..."
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
                        
                        $ stress_count += 2
            
                        if stress_count > 2:
                            j "Oh no."
                            j "I think I'm having a panic attack."
                
                            o "You better be."
                            o "It can't be worse than this."
                
                            j "No, really."
                            j "I need my pills."
                            j "They are at my desk."
                
                            o "Great, fine with me."
                            o "I'm getting out of here."
                
                            $ meeting_panic += 1
                
                            jump pills_scene
                        else:
                            jump meeting_w_map
                    
                    "In my mind...":
                        o "Joe, I'm going to be honest..."
                        o "That doesn't sound incredibly helpful right now."
                        
                        o "Tom, this is Mills."
                        o "Is there any way we can crack this bozo's head open?"
                        o "I might be able to see the presentation better that way."
                
                        $ stress_count += 1
            
                        if stress_count > 2:
                            j "Oh no."
                            j "I think I'm having a panic attack."
                
                            o "Wow, sure a shame Jim isn't here."
                            o "Sounds like it was more his presentation than yours."
                
                            j "No, really."
                            j "I need my pills."
                            j "They are at my desk."
                
                            o "I don't have time for this."
                
                            j "I need to get out of here..."
                 
                            $ meeting_panic += 1
                
                            jump pills_scene
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
                        if randlng = "french":
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
                            
                            $ stress_count += 2
            
                            if stress_count > 2:
                                j "Oh no."
                                j "I think I'm having a panic attack."
                
                                o "Probably better this way, son."
                                o "You don't have to be here when Tom comes over."
                
                                j "No, really."
                                j "I need my pills."
                                j "They are at my desk."
                
                                o "Well, good luck."
                                o "I'll be seein' ya."
                
                                j "I need to get out of here..."
                 
                                $ meeting_panic += 1
                
                                jump pills_scene
                            else:
                                jump meeting_w_map
                    
                    "C'est la vie, Tom.":
                        if randlng = "french":
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
                            
                            $ stress_count += 2
            
                            if stress_count > 2:
                                j "Oh no."
                                j "I think I'm having a panic attack."
                
                                o "Probably better this way, son."
                                o "You don't have to be here when Tom comes over."
                
                                j "No, really."
                                j "I need my pills."
                                j "They are at my desk."
                
                                o "Well, good luck."
                                o "I'll be seein' ya."
                
                                j "I need to get out of here..."
                 
                                $ meeting_panic += 1
                
                                jump pills_scene
                            else:
                                jump meeting_w_map
                    
                    "Carpe diem, Tom.":
                        if randlng = "latin":
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
                            
                            $ stress_count += 2
            
                            if stress_count > 2:
                                j "Oh no."
                                j "I think I'm having a panic attack."
                
                                o "Probably better this way, son."
                                o "You don't have to be here when Tom comes over."
                
                                j "No, really."
                                j "I need my pills."
                                j "They are at my desk."
                
                                o "Well, good luck."
                                o "I'll be seein' ya."
                
                                j "I need to get out of here..."
                 
                                $ meeting_panic += 1
                
                                jump pills_scene
                            else:
                                jump meeting_w_map

                    
                    "Quid pro quo, Tom.":
                        if randlng = "latin":
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
                            
                            $ stress_count += 2
            
                            if stress_count > 2:
                                j "Oh no."
                                j "I think I'm having a panic attack."
                
                                o "Probably better this way, son."
                                o "You don't have to be here when Tom comes over."
                
                                j "No, really."
                                j "I need my pills."
                                j "They are at my desk."
                
                                o "Well, good luck."
                                o "I'll be seein' ya."
                
                                j "I need to get out of here..."
                 
                                $ meeting_panic += 1
                
                                jump pills_scene
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
                
                $ stress_count += 1
            
                if stress_count > 2:
                    j "Oh no."
                    j "I think I'm having a panic attack."
                
                    o "Kind of depends on your point of view."
                
                    j "No, really."
                    j "I need my pills."
                    j "They are at my desk."
                
                    o "Tom, I think your employees might have a drug problem."
                
                    j "I need to get out of here..."
                
                    $ meeting_panic += 1
                
                    jump pills_scene
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
                
        $ stress_count += 1
            
        if stress_count > 2:
            j "Oh no."
            j "I think I'm having a panic attack."
                
            o "From the desk?"
            o "Wow."
            o "You are a complete basket case."
                
            j "No, really."
            j "I need my pills."
            j "They are at my desk."
                
            o "I think you need a lot more than pills, buddy."
                
            j "I need to get out of here..."
                
            $ meeting_panic += 1
                
            jump pills_scene
        else:
            jump meeting_w_map


##############################################################
## Chapter 7 starts here                                    ##
## Lunch on the balcony begins here                         ##
## This is a reprieve chapter from the last couple          ##
## Lots of thoughts about the morning                       ##
##############################################################
         
label chapter7:
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
    
    play music "sounds/pills_chp_7_ost.wav" fadein 2.0

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
    j "I find myself in these inescapable, ridiculous situations."
    j "And no matter how ridiculous they are,"
    j "they still manage to be impossibly stressful."
    j "Is it really that bad?"
    j "Does everyone go through this stuff?"
    j "And if so, how am I this dumb that I let it all happen to me every day?"
    j "Or maybe, it's really not that bad, and I'm the one making it worse."
    j "Maybe I perpetuate the stress where there's no need to."
    j "Maybe I just work myself up to the anxiety."
    j "It has to be one or the other, right?"

    menu:
         "Everybody goes through it.":
             j "It can't just be me."
             j "Maybe other people are just better at hiding it."
             j "Or maybe not - maybe that's why it seems to hard every day."
             j "All of us, trying to live into this fake well-adjusted routine."
             j "But all of us suffering equally by not saying anything about it."
             j "And sure, I mean, I guess the opposite would be worse..."
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
                 jump pills_scene
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
             jump pills_scene

         "What the hell do I know?":
             j "I guess if you could figure that kind of thing out,"
             j "There would be a lot less sadness and confusion in the world."
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
                 jump pills_scene
             else:
                 jump end_of_lunch
    
label end_of_lunch:

    j "Then again..."
    j "I am the one sitting in a park on his lunch break,"
    j "quietly weighing the decisions of every moment of my waking life."
    j "Maybe I shouldn't take everything so seriously."
    j "Won't I become one of those people that just stumbles through their life?"
    j "Those people that I hate,"
    j "who somehow thrive off their own flippancy,"
    j "who make every decision with about as much focused thought as a labrador."
    j "I have no desire to become one of those people."
    j "But there has to be some middle ground, right?"
    j "Somewhere between riding the wave without a care in the world,"
    j "and letting it crash over me every time I'm determined to swim out further."
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
## Cleans up the afternoon, depending on pills count        ##
## Video is slightly different                              ##
## This is the only time player hears the full Pills music  ##
##############################################################
         
label chapter8:
    $ scene_count += 1
    #if pills_count > 2:
    #    play movie "chapter8_sad.webm"
    #    play music "sounds/pills_chp_8_ost_sad.wav" fadein 2.0
    #elif pills_count > 0:
    #    play movie "chapter8_meh.webm"
    #    play music "sounds/pills_chp_8_ost_sad.wav" fadein 2.0
    #else:
    #    play movie "chapter8_spiffy.webm"
    #    play music "sounds/pills_chp_8_ost_happy.wav" fadein 2.0
    
    stop music fadeout 1.0
    
    jump chapter9
    
    
##############################################################
## Chapter 9 starts here                                    ##
## Last opportunity to stress Joseph out                    ##
## With a completely ridiculous choice of what to watch     ##
## This is supposed to bring out the humor in the satire    ##
## It's here that you're supposed to see the ridiculousness ##
##############################################################
         
label chapter9:
    $ scene_count += 1

    #scene chapter9_%r movie % stress_count
    scene chapter9_0 movie
    with fade
    show background solid at left
    
    if stress_count == 0:
        scene chapter9_0 movie
        with fade
        show background solid at left
    elif stress_count == 1:
        scene chapter9_1 movie
        with fade
        show background solid at left
    else:
        scene chapter9_2 movie
        with fade
        show background solid at left
    
    play music "sounds/pills_chp_9_ost.wav" fadein 2.0

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
    
    #scene TV_%r movie % stress_count
    scene TV_0 movie
    
    j "Hmmm..."
    j "There are always ten thousand things to watch on this crap."
    j "How are you ever supposed to pick just one?"
    j "I'm not gonna read all the descriptions."
    j "Who does that?"
    j "No, I'd rather just pick one."
    j "Feel a bit of that well earned American freedom at the end of a long day."
    j "So what'll it be..."
    
    menu:
        "What did I watch yesterday?":
            j "I could just watch whatever I played last."
            j "Yeah."
            j "I don't have the mental energy to pick anything else."
            j "That sounds great."
            j "Another fine episode of derivative cop shows, coming right up."
            jump chapter10
        "What's on New Releases?":

            j "I should check out some new stuff."
            j "That does involve more reading..."
            j "Ah, how bad can it be?"
            
            jump tv_options

label tv_options:

    #scene TV_%r movie % stress_count
    scene TV_0 movie

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
            jump tv_shows
        "Forget it... these all look like garbage.":
            j "This isn't worth it."
            j "I'm going to bed."
            j "Maybe I'll have the patience tomorrow."
            $ stress_count += 1
            if stress_count > 2:
                jump pills_scene
            else:
                jump chapter10

label tv_shows:

    #scene TV_%r movie % stress_count
    scene TV_0 movie

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
    $ stress_count += 2
    if stress_count > 2:
        jump pills_scene
    else:
        jump chapter10

##############################################################
## Chapter 10 starts here                                   ##
## Closing moment, back to bed the same way he woke up      ##
## Tie back to the intro dialogue of falling asleep         ##
## Then car alarm hits again                                ##
##############################################################
    
label chapter10:
    
    if stress_count == 0:
        scene chapter10_0 movie
        with fade
        show background solid at left
    elif stress_count == 1:
        scene chapter10_1 movie
        with fade
        show background solid at left
    else:
        scene chapter10_2 movie
        with fade
        show background solid at left
    
    play music "sounds/pills_chp_10_ost_p1.wav" fadein 2.0

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
    j "Nothingness."
    j "..."
    j "......."
    
    scene black
    with dissolve
    
    play music "sounds/pills_chp_10_ost_p2.wav"
    
    o "Joseph"
    o "This is the voice inside your head"
    o "I'm just checking in..."
    o "Because, sometimes, you know..."
    o "You can really benefit from some outside opinion..."
    if pills_count > 3:
        o "Holy smokes, you downed [pills_count] anti-anxiety pills today!"
        o "Wow!"
        o "Sheesh, those are 12 hour pills!"
        o "You gotta try and keep cool, man!"
        o "You should go to sleep. It seems like you need it."
        o "Tomorrow, try to not stress yourself out that much."
        o "Life isn't all that bad."
        o "You have to see the humor in it."
        o "Otherwise, what's the point?"
        o "Here's a great example..."
    elif pills_count > 1:
        o "You downed [pills_count] anti-anxiety pills today."
        o "You should try for less tomorrow."
        o "I'm sure you'll do great."
        o "Sleep tight."
        o "Oh, wait,"
        o "one more thing..."
    elif pills_count > 0:
        o "You downed 1 anti-anxiety pill today."
        o "You should try for less tomorrow."
        o "I'm sure you'll do great."
        o "Sleep tight."
        o "Oh, wait,"
        o "one more thing..."
    else:
        o "Wow, you didn't need to take any pills today!"
        o "Isn't it crazy how you can control your anxiety like that?"
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
        
    stop music fadeout 1.0
    
    #scene chapter10_%r movie % stress_count
    scene chapter10 movie
    
    # play sound "<loop 300>car_alarm.wav"
    
    j "..."
    j "Are you serious?"
    j "..."
    j "No"
    j "Nope"
    j "Not letting this get to me."
    j "It could be worse."
    j "It could always be worse."
    j "..."
    j "See?"
    j "There."
    j "There it is."
    j "Night after night, but only a moment..."
    j "Nirvana."
    j "..."
    j "Just have to wait for it."
    
    # make sure that car alarm is still going
    # play movie "Credits.webm"

    return