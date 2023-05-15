# Instructions for CIS110 FINAL projext(Undercover_Professor)
print("This is a story about a young pup who is forced with the choice of going undercover to save his owners grades")
print("or runaway to a world he has never seen.")
print("Listed is a series of questions, when you have your chosen input please press enter for each one.")
print("Continue? Please press the ENTER key")
print(f"\nWould you like to continue? Please type yes or no:       ")
keepPlaying = "yes"
while (len(keepPlaying)) == "no":
 input("GAME OVER")
#STORY START POINT
print("Welcome to Mr. Woofles super secret undercover mission adventure. I am going to ask some questions i need answered so we can help him on his journey and get the paper turned in.")
userName = input("\nWhat is your name?           ")
while userName == "0":
 print("Please enter a valid user name!      ")
else:
 print(f"\nWelcome {userName} Lets get started!")
 print("Our paper got rejected for being too similar to our teachers, so we need to go deep undercover to get it turned in for our owner")
 underDog = input("First we need a super cool undercover name for Mr Woofles, Please enter a code name for the young pup:        ")
while underDog == "":
 print("Please enter a code name!        ")
else:
 print(f"Thats great! Mr Woofington will love the name, {underDog}")  
 #storyline2
 print("We are in charge of the descicion but I will leave it to you, as I can only see two options")
 pathA = "pathA -Continue with the mission and risk being torn apart by that guy that turns into a cheetah every football game"
 pathB = "pathB -Set out for parts unknown and abandon our owner and forget about the paper"
 print({pathA})
 print({pathB})
 chosenPath = ["'pathA' or 'pathB'"]
 chosenPath = input(f"\nPlease type your choice, 'pathA', for continue or 'pathB' to run away:       ")
while chosenPath not in ["pathA" , "pathB"]:
 print("Please make a selection")
while chosenPath == "pathB":
 pathB == input(f"\nWhere you gonna get your kibbles at now Mr Woofles, He never abandoned us! GAME OVER")
if chosenPath == "pathA":
 pathA == input(f"\nNext we got to infiltrate the web to get this paper submitted, press any key to continue")

keepGoing = "y"
print("There are many tools , I would use the one tool known to defeat evil teachers, Microsoft Word, but the choice is yours")
superTool = input("We have a wide variety of tools to accomplish this task, Please pick a tool to use:          ")
while superTool == "":
 print("Please select a tool ")
if superTool.lower() == "Microsoft Word":
 print("A puppy and a copy cat too, never the less good choice")
 
