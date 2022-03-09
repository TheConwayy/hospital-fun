from colorama import Fore, Style

# Make the class that holds all activities
class Class:

    def __init__(self, name, activities, hospital):
        self.name = name
        self.activities = activities
        self.hospital = hospital

    def printResults(self):

        def hasHospital():
            if (hospitalI == 'N/A'):
                return 'Hostpital not provided.'
            else:
                return hospitalI

        print(Style.RESET_ALL + Fore.BLUE + Style.BRIGHT + f"""


You, {self.name}, like to do the following:

1. {self.activities[0]}
2. {self.activities[1]}
3. {self.activities[2]}

In the "{hasHospital()}" hospital.\n\n""" + Style.RESET_ALL)

# Empty array for activities
activitiesA = []

#Print the intro
print(Fore.CYAN + r"""

██╗░░██╗░█████╗░░██████╗██████╗░██╗████████╗░█████╗░██╗░░░░░  ███████╗██╗░░░██╗███╗░░██╗
██║░░██║██╔══██╗██╔════╝██╔══██╗██║╚══██╔══╝██╔══██╗██║░░░░░  ██╔════╝██║░░░██║████╗░██║
███████║██║░░██║╚█████╗░██████╔╝██║░░░██║░░░███████║██║░░░░░  █████╗░░██║░░░██║██╔██╗██║
██╔══██║██║░░██║░╚═══██╗██╔═══╝░██║░░░██║░░░██╔══██║██║░░░░░  ██╔══╝░░██║░░░██║██║╚████║
██║░░██║╚█████╔╝██████╔╝██║░░░░░██║░░░██║░░░██║░░██║███████╗  ██║░░░░░╚██████╔╝██║░╚███║
╚═╝░░╚═╝░╚════╝░╚═════╝░╚═╝░░░░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚══════╝  ╚═╝░░░░░░╚═════╝░╚═╝░░╚══╝     

""" + Style.RESET_ALL)

print("""
Now. We all know that sitting in a hospital is no fun. Hell, I'm sitting here in one coding this right now bored out of my mind.

So, I decided that I would create this so that I could help some people have some fun and organize what is fun for them.
""" + Fore.YELLOW + """
The instructions are simple, just answer the questions and following any special instructions they may have
""" + Style.RESET_ALL)


# Questions
nameI = input(Fore.CYAN + 'What is your name?' + Fore.BLUE + ' -> ' + Style.RESET_ALL + Style.DIM)
activitiesI = input(Style.RESET_ALL + Fore.CYAN + 'List THREE activities you like to do in the hospital (sperate them with a comma and space)' + Fore.BLUE + ' -> ' + Style.RESET_ALL + Style.DIM)
hospitalI = input(Style.RESET_ALL + Fore.CYAN + 'What hospital did you go to? (Put "N/A" if you don\'t wanna say)' + Fore.BLUE + ' -> ' + Style.RESET_ALL + Style.DIM)

# Cool stuff
activitiesNS = activitiesI.split(', ')

for i in activitiesNS:
    activitiesA.append(i)

finishedClass = Class(nameI, activitiesA, hospitalI)
finishedClass.printResults()