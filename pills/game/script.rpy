# Pills script - draft copy from RenPy
# remember to put a "return" at the end of the last scene 
$ _game_menu_screen = None
$ renpy.register_sfont('new_sfont', 22, spacewidth=6)
# transition options: fade, pixelate, dissolve
# vpunch will shake the screen
# Declare a character that uses the sfont.
# Declare characters used by this game. 

$ esfont = Character(_("Eileen"), color="#c8ffc8", what_font="new_sfont")

# want slow text mode

# Alter Character text
# Weird-looking.
# add in an arrow to continue text : ctc=anim.Blink("#")
define j = Character(_(''), color="#c8ffc8", window_left_margin=400, window_yminimum=100)


# Declare images used by this game.
# Put all the videos here - one for each stress level.

image chapter1_0 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="chapter1_0", play="chapter1_0.webm")
image chapter1_1 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="chapter1_0", play="chapter1_0.webm")
image chapter1_2 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="chapter1_0", play="chapter1_0.webm")

image getup_0 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="getup_0", play="getup_0.webm")
# image bg getup1_1 = "getup1_1.webm"
# image bg getup1_2 = "getup1_2.webm"

image chapter2_0 movie = Movie(size=(1200, 600), xalign=0.5, yalign=0, channel="chapter2_0", play="chapter2_0.webm")
# image bg chapter2_1 = "chapter2_1.webm"
# image bg chapter2_2 = "chapter2_2.webm"

# image bg chapter3_0 = "chapter3_0.webm"
# image bg chapter3_1 = "chapter3_1.webm"
# image bg chapter3_2 = "chapter3_2.webm"

# image bg chapter4_0 = "chapter4_0.webm"
# image bg chapter4_1 = "chapter4_1.webm"
# image bg chapter4_2 = "chapter4_2.webm"

# image bg chapter5_0 = "chapter5_0.webm"
# image bg chapter5_1 = "chapter5_1.webm"
# image bg chapter5_2 = "chapter5_2.webm"

# image bg chapter6_0 = "chapter6_0.webm"
# image bg chapter6_1 = "chapter6_1.webm"
# image bg chapter6_2 = "chapter6_2.webm"

# image bg chapter7_0 = "chapter7_0.webm"
# image bg chapter7_1 = "chapter7_1.webm"
# image bg chapter7_2 = "chapter7_2.webm"

# image bg chapter8_0 = "chapter8_0.webm"
# image bg chapter8_1 = "chapter8_1.webm"
# image bg chapter8_2 = "chapter8_2.webm"

# image bg chapter9_0 = "chapter9_0.webm"
# image bg chapter9_1 = "chapter9_1.webm"
# image bg chapter9_2 = "chapter9_2.webm"





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

#    play music "illurock.ogg"
    scene black

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
    j "let loose of that tension and fall into the black."
    j "That moment..."
    j "that feeling..."
    j "that's what I wait for every single day."

    scene chapter1_0 movie
    with fade

    j "Already? Wow."
    j "I should probably get up."

# here is an example of a layered animation scene

#    scene bg uni
#    with fade

#    "When we came out of the university, I saw her."

#    show sylvie normal
#    with dissolve

#    "She was a wonderful person."
#    "And I decided..."

    menu:

        "Get up.":

            jump getup

        "Hit snooze.":
            
            jump snooze_1


label getup:

    #scene getup_%r movie % stress_count
    scene getup_0 movie
    with fade

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
         else :
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

    j "Holy crap I hit snooze 10 times?!"
    j "I overslept."
    j "I don't even have time to shower."
    j "I'm going to be so late."
    
    jump pills_scene
 
 
    
# this is the scene that the player gets
# every time a pill is taken
    
label pills_scene:

    scene black
    with dissolve

    j "That's it" # "What the hell is happening to me?", "I'm going to freak out."
    j "I can't handle this."
    j "I need escape."
    
    # play music "pillbottle.wav"
    # play music "exhale.wav"
    
    j "That's better."
    
    $ pills_count += 1
    $ stress_count = 0
    
    
    #jump scene_%r % scene_count + 1
    jump chapter2


screen chapter2_map:
    # imagemap:
        chapter2_0 movie 
        # Do I need to specify the base image?
        #hover "Hover.jpg" I don't want a hover change thing

        hotspot (8, 200, 78, 78) clicked Return("book")        #library book for bus/email
        hotspot (204, 50, 78, 78) clicked Return("bag")        #bag for bus pass
        hotspot (452, 79, 78, 78) clicked Return("calendar")   #calendar for meeting 
        hotspot (602, 316, 78, 78) clicked Return("door")      #door is leave
        
label chapter2:

    $ scene_count += 1
     
     #scene chapter2_%r movie % stress_count
     #scene chapter2_0 movie
     #with fade
     #weird imagemap call below - probably gonna break
    
    call screen chapter2_map movie
    with fade

    j "What am I forgetting?"
    j "I always forget something."
    
    $ result = _return
    
    if result == "book":
        $ book_check = 1
        j "Oh right I need to grab that library book."
        j "I think it's due already."
        j "I never have time to read finish anything."
        j "Whatever. One more bus ride made less awkward."
    elif result == "bag":
        $ bag_check = 1
        j "Did I pack everything for today?"
        j "Oh damn I almost forgot my bus pass."
        j "That would have been annoying."
    elif result == "calendar":
        $ calendar_check = 1
        j "Do I have anything at work today?"
        j "Sure doesn't look like it."
        j "Probably for the best."
    elif result == "door":
        j "Guess I should hit the road."
        j "Hope whatever it was isn't important."
        # play the outro cutscene where I leave or turn out light or something
        jump chapter3
        
label chapter3:

    $ scene_count += 1
    
    #consider using image map for easter eggs
    #look out the bus window
    #look into Joe's bag
    #maybe even look at other people staring at Joe? Would be really disconcerting.
    
    #scene chapter3_%r movie % stress_count
    scene chapter3_0 movie
    with fade

    j "Bus was only three minutes late today."
    j "That's a new record."
    j "Maybe today isn't all that bad."
    j "Probably never is."
    j "I'm kidding myself half the time."
    j "Look at me,"
    j "Preferring my own company to that of others."
    j "And you wonder why people go crazy."
    j "Doing this every single day."
    j "Look at this bus."
    j "Look at these ads lining the perimeter."
    j "Have you recently gone through a divorce?"
    j "Are you going through a fiscal dillema?"
    j "Have you lost your sexual potency?"
    j "Does your child have access to crystal meth?"
    j "Call here."
    j "Call there."
    j "Talk to someone, anyone."
    j "When has that crap ever helped anyone?"
    
    # work below
    
    
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