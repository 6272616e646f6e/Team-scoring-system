x = 1
while x > 0:

    individuals = [] # creates the arrays
    iscores = []
    teams = []
    tscores = []
    number1 = 1
    number2 = 1

    y = 1
    while y > 0: # this loop is here for the restart option and the x loop prevents the program from stopping

        ########## sets individuals tables ##########
        q = 1
        while q > 0: # this loop is for error trapping because its stops the program from progressing if there is an error
            try: 
                noi = int(input("How many individuals are competing? ")) # noi = number of individuals
            except ValueError:
                print("Please enter a number ")
                q = q + 1 # this adds 1 to q so the loops stays active because it has to take away 1 after so that the loop stops if there is no error
            q = q - 1
        while noi > 0: # this loop controls how many times a string is added to the array
            ip1 = "individual " #ip1 = individual part 1. this is creating a string of text that will be added to the array
            ip2 = str(number1)
            i = ip1 + ip2 
            individuals.append(i) # this is adding the string
            number1 = number1 + 1
            noi = noi - 1 # reducing the number of strings that need to be added to the array
        nois = len(individuals) # gets the legnth of the array
        while nois > 0: # nois = number of individuals' scores
            iscores.append(0) # adding a 0 for each person
            nois = nois - 1
        #############################################

        ########## sets teams tables ################
        q = 1
        while q > 0: # the same thing but for teams
            try:
                noteam = int(input("How many teams are competing? ")) 
            except ValueError:
                print("Please enter a number ")
                q = q + 1
            q = q - 1
        while noteam > 0:
            tp1 = "team "
            tp2 = str(number2)
            t = tp1 + tp2 
            teams.append(t) 
            number2 = number2 + 1
            noteam = noteam - 1
        nots = len(teams)
        while nots > 0:
            tscores.append(0)
            nots = nots - 1
        #############################################

        ########## user input #######################
        z = 1
        while z > 0:
            ti = input("Would you like to score a team or an individual competitor? (enter t - team/i - individual/r - restart) ") # ti = team/individual
            if ti == "r":
                ays = input("Are you sure you want to restart? (enter y - yes/ n - no) ") # ays = are you sure
                if ays == "y":
                    print("You have restarted") 
                    z = 0
                else:
                    print("You did not restart") 
            elif ti == "t" or ti == "team":
                w = 1
                while w > 0:
                    try:
                        tno = int(input("Which team would you like to score? (team number) ")) # tno = team number
                    except ValueError:
                        print("Please enter a team number ")
                        w = w + 1
                    w = w - 1 
                tno2 = str(tno) # tno 2 = team number 2. This is converted to a string so it can be added to a line of text
                tno = tno - 1 # because arrays start from 0, not 1
                if tno > (len(teams) - 1): # checks if the user has entered a team number bigger than the number of teams available. the -1 is because arrays start from 0, not 1
                    tlen = str(len(teams)) 
                    print("There are only " + tlen + " teams. If you want to restart, (enter r - restart). ") 
                else:
                    tnos = int(input("What did team " + tno2 + " score? ")) # tnos = team number score. this is to add the the array
                    tscores[tno] = tscores[tno] + tnos
                    print(tscores)
            elif ti == "i" or ti == "individual":
                w = 1
                while w > 0:
                    try:
                        ino = int(input("Which individual competitor would you like to score? (enter competitor number) "))
                    except ValueError:
                        print("Please enter a competitor number ")
                        w = w + 1
                    w = w - 1
                ino2 = str(ino) 
                ino = ino - 1
                if ino > (len(individuals) - 1):
                    ilen = str(len(individuals))
                    print("There are only " + ilen + " individual competitors. If you want to restart, (enter r - restart). ") 
                else:
                    inos = int(input("What did competitor " + ino2 + " score? ")) 
                    iscores[ino] = iscores[ino] + inos
                    print(iscores)
            else:
                print("Please enter t to score a team, or i to score an individual competitor. ")
        y = 0 # this is for restarting
        #############################################
