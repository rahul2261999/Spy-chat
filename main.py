from spy_detail import spy_name, spy_salutation, spy_age, spy_rating
print 'lets start'

question = "Do you want to continue as"+" "+ spy_salutation + " " + spy_name +" "+"(Y/N)?"
existing = input(question)

def start_chat(spy_name , spy_age, spy_rating):

    current_status_message = None

    spy_name = spy_salutation + " " + spy_name

    if spy_age > 18 and spy_age < 60:
        print "Authentication complete.... \n" + "welcome" + " " + spy_name + " " + "age" + " " + str(
            spy_age) + " " + "spy rating" + " " \
              + str(spy_rating) + " ""glad to see you active again"

        show_menu = True
    else:
        print "sorry you are not of a correct age for a spy"


if existing == "Y":
    start_chat(spy_name,spy_age,spy_rating)
else:
    spy_name = ''
    spy_salutation = ''
    spy_age = 0.0
    spy_rating = 0.0
    spy_is_online = False

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