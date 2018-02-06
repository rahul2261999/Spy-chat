from spy_detail import spy, friends
from steganography.steganography import Steganography
from datetime import datetime
print 'lets start'
STATUS_MESSAGE = ["HELLO", "Available"]
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

def add_friend():
    new_friend = {
        'name': '',
        'salutation': '',
        'age': 0,
        'rating': 0.0
    }
    new_friend['name'] = input("Please add your friend's name: ")
    new_friend['salutation'] = raw_input("Are they Mr. or Ms.:")

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
        print '%d. %s'%(item_num +1), friend['name']
        item_num = item_num + 1
    s = input("select friend index ")

    friend_choice_position = int(s)-1

    return friend_choice_position

                # MESSAGE SENDING

def send_message():

    friend_choice = select_friend()  # CALLING FUNCTION select_friend

    original_image = raw_input("What is the name of the image?") # enter input path of image

    output_path = raw_input('enter')                   # enter output path of image

    text = raw_input("What do you want to say? ")

    Steganography.encode(original_image, output_path, text)

    new_chat = {
        "message": text,
        "time": datetime.now(),
        "sent_by_me": True
    }

    friends[friend_choice]['chats'].append(new_chat)

    print "Your secret message image is ready!"

def read_message():

    sender = select_friend() #calling function select_friend

    output_path = input("What is the name of the file?")

    secret_text = Steganography.decode(output_path)

    new_chat = {
        "message": secret_text,
        "time": datetime.now(),
        "sent_by_me": False
    }

    friends[sender]['chats'].append(new_chat)

    print "Your secret message has been saved!"





def start_chat(spy):

    current_status_message = None

    spy_name = spy['salutation'] + " " + spy['name']

    if spy['age'] > 12 and spy['age'] < 60:

        print "Authentication complete.... \n" + "welcome" + " " + spy['name'] + " " + "age" + " " + str(
            spy['age']) + " " + "spy rating" + " " \
              + str(spy['rating']) + " ""glad to see you active again"

        show_menu = True

        while show_menu:
            menu_choices = "What do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n " \
                           "5. store user data \n 6. Read Chats from a user \n 7. Exit \n Enter your Choice"

            menu_choice = input(menu_choices)

            if menu_choice == 1:
                current_status_message = add_status(current_status_message)

            elif menu_choice == 2:
                number_of_friends = add_friend()

                print 'You have %d friends' % (number_of_friends)

            elif menu_choice == 3 :

                send_message()

            elif menu_choice == 4:

                read_message()

            elif menu_choice == 5:

                pass

            elif menu_choice == 6:

                pass

            elif menu_choice == 7:

                pass
            else: show_menu == False
    else:

        print "sorry you are not of a correct age for a spy"


                    # new friend details

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