define pov = Character("Dr. [povname]")
define nurse = Character("Nurse")
define shilpa = Character("Shilpa")
define patient = Character("Patient")
define madhav = Character("Madhav")
define riya = Character("Riya")
define kabir = Character("Kabir")
image bg bedroom = "bedroom.jpg"
image bg hospital = "hospital.jpg"
image shilpa = "shilpa.jpg"

label start:

    show bg bedroom

    "Hey, you. You’re finally awake. "
    "Its almost time for your shift, Dr. <name>"
    $ povname = renpy.input("What is your name?", length=32)
    $ povname = povname.strip()

    if not povname:
        $ povname = "Pat Smith"
    pov "Good Morning"

    "It’s a sunny April morning. You see the sun’s silhouette through your bedroom’s curtains."
     
    "*You draw the curtains and begin your morning routine.*"

    "After breakfast, you begin to change into your doctor’s attire, when you realise that it’s a Sunday. It is optional to go to the hospital on Sundays."
    
    menu:
        "Go to the hospital regardless.(start the hospital storyline directly)":
            jump choice_a
        
        "Head outside for a leisurely stroll around the city.":
            jump choice_b

    label choice_a:
        "You put on your Doctor's attire and head outside in your car."
        
        "On the way to the hospital, you look outside at Central Park and the City Lake."
    
        show bg hospital

        "Upon reaching the hospital, you're greeted by the nurse."

        nurse "Good Morning, [pov]"
    
    menu:
        "Morning Jeane, how was your day so far?":
            jump choice_a1
        
        "Morning darling, hearing from you always brightens my day.":
            jump choice_a1
        
    label choice_a1:
        nurse "Going great, your first patient is waiting for you OR *blushes* That's what all the patients say. Anyways your first patient is in your office."

        "You enter your office with the nurse. A young woman, probably in her 20s, is already there."

        pov "Good morning, what's your name?"

        show shilpa

        shilpa "Hello Doctor, It's Shilpa"

        pov "How old are you, Shilpa?"

        shilpa "I am twenty one years old."

        pov "Oh, great, so you must be in University?"

        shilpa "Yeah, Doctor, I am studying at Panacea University"

    menu:
        "That's great! So tell me Shilpa, what's troubling you?":
            jump choice_a2
        
        "That's a great university! Tell me, what brings you here?":
            jump choice_a2

    label choice_a2:
        shilpa "I feel a slight ache in the pelvic region, and an unusual burning sensation while urinating for a few days."

    menu:
        "Hmm, are you sexually active?":
            jump choice_a3
        
        "That’s very common with girls your age, you will be okay in a couple days. Nurse! Next!":
            jump gameover
    
    label choice_a3:
        shilpa "*nervously* Nooo, I am not even married how could I be."

        pov "Sorry to say this Shilpa, but there’s only two ways you might be suffering. Either you have had a very careless sexual partner, or you are suffering through a rare incurable disease called lyingitis."

        shilpa "Sorry doctor, it’s true. I have a boyfriend, and we do engage in you know what"

    menu:
        "It’s sex! Don’t be ashamed to use the word.":
            jump choice_a4
        
        "What?! Sex? Cultured girls do not even dare to think about that before marriage! Aren’t you an engineer ":
            jump gameover
        
    label choice_a4:
        shilpa "Yes Doctor. I am sorry. Please don’t tell my parents. They will disown me otherwise."

        pov "Don’t worry. My job is to treat you, nothing else. We’ll get you tested first to know whether you have any STD or not."

    menu:
        "*Prescribes an STD Test":
            jump choice_a5
        
        "Mein toh batoonga hehe":
            jump gameover        
        
        "As they should!":
            jump gameover
        
    label choice_a5:
        shilpa "Thanks Doctor. But we have always used protection, how could have this happened?"

        pov "Shilpa, while using protection like condoms reduces the risk of STDs, it cannot be an absolute protection against STDs."

        shilpa "Oh god! But, will it get cured or not?"

    menu:
        "Some STDs get cured quickly, while others might last longer, depends, on which one you have. So, first let’s get you tested":
            jump choice_a6
        
        "How can I tell that now, stop asking so many questions!":
            jump gameover

    label choice_a6:
        shilpa "Can I take this right now, at the hospital?"

        pov "Yes, you can. Nurse!"

        nurse "Yes Doctor?"

        pov "Can you please take Shilpa and get this test done."

        shilpa " Doctor, also, Should I ask my partner to get tested as well? "

    menu:
        "I would highly encourage that, Shilpa":
            jump choice_a7
        
        "Yes, get that person also, who’s most probably the reason why you ended up here in the first place.":
            jump gameover
        
    label choice_a7:
        shilpa "Thank you so much Doctor!"

        pov "Here, don't forget your painkiller prescription."

        "Doctor: Lucky for you, we’re not in America, so you won’t go bankrupt from this five minute conversation"

        shilpa "Oh yeah, sure, thanks."

        "Shilpa leaves."

        nurse "Doctor, your next patient is here."

        pov "Send him in."

        "A middle aged man enters."

        pov "Good morning sir, How are you doing?"

        patient "Morning Doctor, nothing new, just the usual routine, hope all’s well for you?"

        pov "Oh yeah, everything is fine. So, tell me sir, what trouble brings you here today?"

        patient " I was previously prescribed 20mg tablets of Oxycontin and Morphine for the severe pain I was suffering from a traffic accident. The pain has subsided now, but I still consume the tablets regularly."
    
    menu:
        "Okay, go ahead, I am listening":
            jump choice_a8
        
        "Can you be a bit quick, I have other patients waiting out there. I don’t have all day!":
            jump gameover

    label choice_a8:
        patient "So, I ran out of tablets two days ago, and ever since, my anxiety has been spiking and I am unable to focus at work either. I assumed this had to do with the painkillers since I am not on any other medication at the moment."

    menu:
        "Oh you don’t need to worry. This is a very common side effect of prescription opioids. You just have a mild addiction to the medication.":
            jump choice_a9
        
        "Tch-tch-tch….. You are clearly addicted to these drugs. I will have to report you to the cops and get you into rehab ASAP":
            jump gameover

    label choice_a9:
        patient "Wait what?! Addiction? No doctor! How can it be? "

        pov "You seem to have a mild addiction to Oxycontin, which occurs if the usage isn't carefully monitored. I will prescribe two tablets of 5mg of Oxycontin for the next two days. This should be an effective step down for the addiction."

        patient "Oh Doctor, will I be alright? I have seen those people before and after pictures of drug addicts and it’s very scary."

        pov "Trust me, as long as you listen to my instructions you will have no issues whatsoever. Just walk outside more and stay hydrated. You will be fine in no time."

        patient "Thank you, Doctor. I will return two days later with the updates."

        "THE END"

        return



    label choice_b:
        "You change into some casual clothing, and head outside in your car."

        "At this time of the year, Central Park is quite beautiful, with its colourful flowers and serene skies."

        "Another good spot to leisurely waste away a fine Sunday is the  City Lake, which is home to over three thousand bird and fish species. The City Lake is bound to be less crowded and make for a more cozy, peaceful Sunday."
    
    menu: 
        "Enjoy the Sunday vibe and colourful surroundings of Central Park.":
            jump choice_c
        
        "Head to the City Lake for its placid ambience and lush wildlife":
            jump choice_d
        
    label choice_c:
        "Within 15 minutes, you reach your destination. You park your car and enter Central Park. It’s spring and the flowers are at their peak, this definitely beats working at the hospital. The trees have their strong moist fragrance, providing a rejuvenating ambience."

        "You lazily stroll across the brick walk path, watching the children play in the playground area under the late morning sun. You see one child hunkered over their knee in the sand pit, crying his heart out."

    menu:
        "Go to check on the child’s knee.":
            jump choice_c1
        
        "Just carry on with your leisurely park stroll, anyways it’s the kid’s parents who are responsible, not you":
            jump gameover
    
    label choice_c1:
        "You are genuinely concerned, so you make your way into the messy sandpit."

    menu:
        "Hey kid what’s wrong? Are you okay?":
            jump choice_c2
        
        "Hey kid, stop crying, you’re disrupting the ambience of the park!":
            jump gameover
    
    label choice_c2:
        madhav "*breathlessly* Hi, I am Madhav. I am alright, please goaway."

    menu:
        "You do not look alright, tell me what the trouble is, I can help you":
            jump choice_c3
        
        "Fine then, if you’re alright, I’ll go. Got better things to do anyways.":
            jump gameover

    label choice_c3:
        madhav "It's nothing, I just fell from the swing. Happens all the time"

        "Madhav moves his hand off of his knee revealing a deep gash running right across the knee. You know that this is a serious injury, requiring multiple stitches."

    menu:
        "Oh, shucks, let’s get your wound cleaned with water first":
            jump choice_c4
        
        "OR Happens all the time, right? Shouldn’t be a problem then, off you go!":
            jump gameover
    
    label choice_c4:
        "Madhav limps out of the sand pit and towards a nearby fountain. You return with the first aid kit just as Madhav has finished rinsing the bruise under the fountain’s cold water."

    menu:
        "Hey don't worry, this is just Dettol. It will help you prevent nasty infections":
            jump choice_c5
        
        "Oh yeah, you careless kid, you fall and now you scream when I am helping you.":
            jump gameover

    label choice_c5:
        pov "Ok now tell me do you remember your mummy or daddy’s phone number?"

        madhav "Yeah, it’s 123456XXXX"

        "You call Madhav’s parents, informing them about the injury and suggesting that they take Madhav to the hospital immediately. They arrive in about five minutes, and you continue on your walk."

        "You walk right past the sand pit, turning your head far left, away from the child, so as to avoid as much eye contact as possible. Your neck even aches a little from turning your head so far left, but that’s okay, walking with trees and plants does have healing capabilities. Thus, you resume your leisurely stroll."

        "A little ahead you see a large antique lamp post. You notice a slight commotion beside the lamp post, as if someone is lying on the floor."

    menu:
        "Move aside, I’m a Doctor!":
            jump choice_c6
        
        "Why bother, another drunkard probably!":
            jump gameover

    label choice_c6:
        "You recognise the victim here, it's your neighbour Riya. She’s lying on the floor sobbing bitterly, and is grasping her calf tightly."

    menu:
        "Riya! Riya! What happened?!":
            jump choice_c7
        
        "Always getting into trouble, aren’t you? Let me call your parents":
            jump gameover

    label choice_c7:
        riya "Oh thank god [pov] you’re here. A crazy monkey bit me and it hurts so bad!"

        pov "Show me the injury"

        "She twists her leg clumsily to reveal the back of her bloody calf. Laying there, among the soggy blood stains on her jeans, are 4 deep teeth impressions that seem to have hit the saphenous vein."
    
    menu:
        "Riya this is a very serious bite and you need medical attention immediately, I’ll call the ambulance":
            jump choice_c8
        
        "Oh, come on, grow up girl. Be an adult and just walk it off.":
            jump gameover

    label choice_c8:
        riya "Thank you doctor. Could you inform my parents, they will be worried."

    menu:
        "Yeah, I’ll call up your parents, they need to be informed":
            jump choice_c9
        
        "Let your parents be worried, after all they allowed you to saunter off all alone":
            jump gameover
        
        "No need to get them involved":
            jump gameover
        
    label choice_c9:
    menu:
        "Meanwhile, let’s get your wound to avoid infection, contamination of any sort":
            jump choice_c10
        
        "Meanwhile, let me tell you a story to divert your attention, there’s nothing we can do about your wound till ambulance comes":
            jump gameover

    label choice_c10:
        "Goes to fetch his first aid kit and water bottle"

    menu:
        "Let’s clean your wound using water, dettol and cotton":
            jump choice_c11

        "Let’s apply band aid over your wound, no need to clean, band aid will avoid exposure":
            jump gameover

        "Let’s apply soil over it, it has organic healing qualities":
            jump gameover

    label choice_c11:
        "Within 10 minutes, the ambulance arrives and Riya thanks you for your assistance."

        "You have seen enough blood for a day, so you choose to 	instead sit at a bench nearby and continue reading your digital copy of Animal Farm."

        "THE END"

        return 


    
    label choice_d:
        "You make your way to the City Lake. It isn't too crowded, less so than most other Sundays even. You park your car and make your way to the large footpath that encircles the lake. Beside the entrance gate, you see a family that you recognise to be your neighbors. THey seem to be arguing and fighting. The perfect family, or atleast what you thought so. The parents seem to be pouring their hearts out about how much they love the son, but he is just crying and yelling back at them. His name is Kabir, you realise since he is a patient of yours. He runs off from his parents towards the benches."

        "Begin leisurely stroll."

        "You start your brisk walk around the lake. You stop at a couple of spots to observe the occasional swan that ventures to the edge of the lake. Most trees are filled with massive flocks of sparrows and doves."

        "About two kilometers into your brisk walk, you see a boy sitting on a bench, staring forlornly at the lake. It’s Kabir. You’ve treated him a few times and he’s always carried a melancholy aura about it, which is especially apparent now. He seems really spaced out and unaware of his surroundings."

    menu:
        "Observing for a bit, you notice he probably needs to talk to someone":
            jump choice_d1
        
        "maybe you should let him learn the lesson the hard way, the universe really doesn’t care.":
            jump gameover

    label choice_d1:
    menu:
        "Hey buddy, you good there?’ you softly ask him ":
            jump choice_d2
        
        "Hey punk, why aren’t you at school? you say, cuffing the side of his head":
            jump gameover

    label choice_d2:
        "Jumping, he turns to face you"

        kabir "Y-yeah. I didn’t know anybody was here."

        pov "I mean it's a public park, are you surprised to see said public here?"

        "He doesn't even crack a smile. Yikes, either your jokes have gotten that bad or he really is that sad. You’re willing to hazard a bet that it's the latter. "

        pov "What's on your mind?"

        kabir "A lot."

        "You pause for him to go on but it seems like that's all he had to say."

        pov "How are things at home and at school?"

        kabir "Everything is awful. My parents don’t understand me and yell at me for being difficult. People at school don’t understand me and bully me because I, apparently, talk about stupid and weird things. My brain always feels so loud and there’s so much that I feel so overwhelmed all the time."

        pov "Well, that's tough Kabir and I’m sorry to hear that."

    menu:
        "I’m glad you trusted me with that. Do you think telling me more would help?":
            jump choice_d3
        "I bet you don’t wake up early, go for jogs or eat healthy, no wonder your parents are always yelling at you.":
            jump gameover
        
    label choice_d3:
        kabir "Yeah, maybe. I just thought today would be a good day. I, even, forced a smile to be on my face for as long as I could, but those guys bullied me again. It sucks and nothing will ever change."

        pov "I know it may seem that way to you now but I promise things will take a turn for the better soon-"

        kabir "No, they won’t. Just like this lake. The teacher had asked if this lake would be cleaned and I said yes, what with trying to be positive today. The bullies said no and they’re right, just like they’re right about every mean thing they say about me."

    menu:
        "Haven’t your parents told you to believe your elders?":
            jump choice_d4
        "Talking to the right people can surprisingly solve a lot of problems. Want me to show you how?":
            jump choice_d4
        
    label choice_d4:
        "It's a long shot but it seems to pay off with the boy perking up just the least bit. He still tries to feign nonchalance and shrugs."

        kabir "Okay"

        pov "We can draft a mail to the municipal commissioner to arrange the distillation of the lake. Then organise a garbage clean up drive to ensure the chemicals from it dont seep in and foam up the lake again"

        kabir "Woah, and that will work?"

        pov "Sure will. See how talking to the right person helps solve things? Similarly, I think it would be great if you’d be willing to talk to a psychologist along with your parents to help you will feel better."

        kabir "If it works out like the lake, yeah! I’ll do it. You’ll have to talk to my parents about it though."

        pov "Sure thing, Kabir. I’ll drop by after my shift at the hospital, which I should be leaving for now."

        kabir "Okay! Bye, doctor!"

        pov "Bye, Kabir!"

        "THE END"

        return 

    

    label gameover:
        "you picked the wrong choice"
        return


    # This ends the game.

    return
