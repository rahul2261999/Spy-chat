from spy_detail import spy_name, spy_salutation, spy_age, spy_rating
print 'lets start'

  # STATUS


def add_status(current_status_message):
    update_status_message = None


    if current_status_message != None:
        print "your current status message is %s"%(current_status_message)

    else:
        print "you do not have any status message currently"

    default = input("do you want to select older status(Y/N)")

    if default.upper == "N":
        new_status_message = raw_input("enter your status message")

        if len(new_status_message) > 0:

            STATUS_MESSAGE.append(new_status_message)
            update_status_message = new_status_message

        elif default.upper == "Y":
            item_position = 1

            for message in STATUS_MESSAGE:

                print item_position + " " + message
                item_position = item_position + 1
                message_selection = input("enetr your choice")

            if len(STATUS_MESSAGE) >= message_selection:
                update_status_message = STATUS_MESSAGE(message_selection - 1)
            else: print "option is invalid"

    return update_status_message

    # FUNCTION FOR ADDING  NEW FRIEND
def add_friend():
    pass

     # FUNCTION FOR CHAT

def start_chat(spy_name , spy_age, spy_rating):

    current_status_message = None

    spy_name = spy_salutation + " " + spy_name

    if spy_age > 18 and spy_age < 60:

        print "Authentication complete.... \n" + "welcome" + " " + spy_name + " " + "age" + " " + str(
            spy_age) + " " + "spy rating" + " " \
              + str(spy_rating) + " ""glad to see you active again"

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



      # LIST

STATUS_MESSAGE = {"HELLO","AVAILABLE"}   #STATUS LIST

friends_name = []

friends_age = []

friends_rating = []

friends_is_online = []



question = "Do you want to continue as"+" "+ spy_salutation + " " + spy_name +" "+"(Y/N)?"
existing = input(question)

if existing == "Y":

    start_chat(spy_name,spy_age,spy_rating)   # FUNCTION CALLING

else:


    spy_name = ''
    spy_salutation = ''
    spy_age = 0.0
    spy_rating = 0.0
    spy_is_online = False

    # NEW SPY DETAILS

    spy_name = raw_input("enter your name first")

    if len(spy_name) > 0:

       print "welcome"+" " + spy_name + " " + "Glad to see you here "

       spy_salutation = raw_input("Should I call you Mr. or Miss?")

       spy_name = spy_salutation + " " + spy_name

       print "alright" + " " + spy_name + '' + " I'd like to know a little bit more about you."

       spy_age = input("enter you age")

       spy_is_online = True

       start_chat(spy_name,spy_age,spy_rating)


    else:

         print "sorry you are not of a correct age to be a spy"