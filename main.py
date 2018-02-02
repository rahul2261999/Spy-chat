print 'hello'
print 'lets start'

# spy details
spy_name = raw_input("welcome to spy chat tell your name first\t")

# checking spy eligibility
if len(spy_name) > 0:
   print "welcome"+" " + spy_name + " " + "Glad to see you here "
   spy_salutation = raw_input("Should I call you Mr. or Miss?")
   spy_name = spy_salutation + " " + spy_name
   print "alright" + " " + spy_name + '' + " I'd like to know a little bit more about you."

   spy_age = 0
   spy_rating = 0
   spy_is_online = False

   spy_age = input("enter you age")

   spy_age = int(spy_age)

#checking spy age

if 12 < spy_age < 60:
    spy_rating=input("what is you rating")
    if spy_rating > 4.5:
        print "great ace"
    elif spy_rating > 4 and spy_rating < 4.5:
        print "you are good spy"
    elif spy_rating > 3 and spy_rating < 4:
        print "you can do better"+" "+ spy_name
    else:
        print "we can also use somebody to help in office"

    spy_is_online = True
    #printing the details of spy
    print "Authentication complete.... \n" + "welcome"+" "+ spy_name + " "+"age" + " "+ str(spy_age) +" "+ "spy rating"+ " "\
          +str(spy_rating)+" ""glad to see you active"

else:
     print "sorry you are not of a correct age to be a spy"