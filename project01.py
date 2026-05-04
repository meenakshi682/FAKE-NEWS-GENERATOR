#  FAKE NEWS HEADLINE GENERATOR
# USING  = LISTS , RANDOM .MODULE , PRINT() , INPUT(), WHILE LOOP , STRING CONCATENATION  OR F STRINGS ( TO CREATE A SENTENCE USING SELECTED WORDS) 
#  MAKE SPORTS , POLITICS , OR BY USER SUGGESTION ( UPADATED )
#PRESCODE 
# IMPORT THE RANDOM MODULE
import random
#CREATE A LIST OF INDIAN ACTIONS
#EXAPMLE : ["LAUNCHES" , "CANCELS ",  ]
#create subjects
subjects = [
    " shahrukh khan "
    "virat kholi"
    " man of the  words "
    "nirmala sithraman"
    " a group of monkey"
    " auto driver daughter won gold medal"
    "prime minister modi "
    
]
actions =[
    "launches "
    "cancels"
    "dances with"
    " yummy"
    " winner "
    " victory"
    " proud moments"
    " sad "
    " celebrate"
]
places_or_things =[
    "at red fort"
    " river cleaning"
    " 2026 world cup "
    " at ganga ghat"
    " during ipl match"
    " at vegatable market"
    " at india gat" 
]
# 3 start the headline generation loop 
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)

    headline = f"BREAKING NEWS: { subject} {action} { place_or_thing}" # f = forword string taki sub eak line mein aajaye 
    print("/n" + headline)
    

    user_input= input(" /n do you want another headline? ( yes /no )").strip()   # strip() = remove extra space
    if user_input == "no":
        break
    #print goodbye message
    print(" /n thanks for using the fake news headline generator. have a fun day")
