from spy_detail import spy

from spy_detail import spy
print 'lets start'
STATUS_MESSAGE = ["HELLO","Available"]
  # STATUS
def add_status(current_status_message):
    update_status_message = None


    if current_status_message != None:
        print "your current status message is %s"%(current_status_message)

    else:
        print "you do not have any status message currently"

    default = input("do you want to select older status(Y/N)")

    if default.upper() == "N":
        new_status_message = raw_input("enter your status message")

        if len(new_status_message) > 0:

             update_status_message = new_status_message
             STATUS_MESSAGE.append(update_status_message)

    elif default.upper() == "Y":
            item_position = 1

            for message in STATUS_MESSAGE:

                print str(item_position) + ". " + message
                item_position = item_position + 1
                message_selection = input("enetr your choice")

            if len(STATUS_MESSAGE) >= message_selection:
                update_status_message = STATUS_MESSAGE[message_selection - 1]
            else: print "option is invalid"


    return update_status_message

    # FUNCTION FOR ADDING  NEW FRIEND

friends = []
def add_friend():
    new_friend = {
        'name': '',
        'salutation': '',
        'age': 0,
        'rating': 0.0
    }
    new_friend['name'] = input("Please add your friend's name: ")
    new_friend['salutation'] = raw_input'("Are they Mr. or Ms.:")

    new_friend['name'] = new_friend['salutation'] + " " + new_friend['name']

    new_friend['age'] = input("Age?")

    new_friend['rating'] = input("Spy rating?")

    if len(new_friend['name']) > 0 and new_friend['age'] > 12 and new_friend['rating'] >= spy['rating']:
        friends.append(new_friend)
        print 'Friend Added!'
    else:
        print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'


    return len(friends)

def select_friend():
    item_num = 0
    for friend in friends:
        print "str(item_num+1)"+ friends['name']
        item_num = item_num + 1
    s = input("select friend index ")

    friend_choice_position = int(s)-1

    return friend_choice_position






     # FUNCTION FOR CHAT

def start_chat(spy):

    current_status_message = None

    spy_name = spy['salutation'] + " " + spy['name']

    if spy['age'] > 18 and spy['age'] < 60:

        print "Authentication complete.... \n" + "welcome" + " " + spy['name'] + " " + "age" + " " + str(
            spy['age']) + " " + "spy rating" + " " \
              + str(spy['rating']) + " ""glad to see you active again"

        show_menu = True

        while show_menu:
            menu_choices = "What do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Close Application \n"
            menu_choice = input(menu_choices)

            if menu_choice == 1:
                current_status_message = add_status(current_status_message)

            elif menu_choice == 2:
                number_of_friends = add_friend()

                print 'You have %d friends' % (number_of_friends)

    else:

        print "sorry you are not of a correct age for a spy"


                    # new friend details

friends_name = []

friends_age = []

friends_rating = []

friends_is_online = []



question = "Do you want to continue as"+" "+ spy['salutation'] + " " + spy['name'] +" "+"(Y/N)?"
existing = input(question)

if existing .upper()== "Y":

    start_chat(spy)   # FUNCTION CALLING

else:


    spy_name = ''
    spy_salutation = ''
    spy_age = 0.0
    spy_rating = 0.0
    spy_is_online = False

    # NEW SPY DETAILS

    spy_name = raw_input("enter your name first")

    if len(spy['name']) > 0:

       spy['salutation'] = raw_input("Should I call you Mr. or Miss?")

       spy['name'] = spy['salutation']+" "+spy['name']

       print "alright" + " " + spy['name'] + '' + " I'd like to know a little bit more about you."

       spy['age']= input("enter you age")

       spy['is_online'] = True

       start_chat(spy)


    else:

         print "sorry you are not of a correct age to be a spy"