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
chooseTool = ["'superTool' , 'superToolA' , superToolB' "]
superTool = "office"
superToolA = "coloring pencils and scrap paper"
superToolB = "ink and paw prints"
print("We have a wide variety of tools to accomplish this task, Please pick a tool to use please input an option")
print(f"superTool = {superTool}")
print(f"superToolA = {superToolA}")
print(f"superToolB = {superToolB}")
chooseTool == input(f"Please input one tool :superTool,superToolA,supertoolB:         ")
if chooseTool == "":
 chooseTool == input("Please select a tool ")
if chooseTool =="superToolA":
         chooseTool == input(f"\nWe draft the paper with the coloring pencils and our scrap paper had some takeout menu printed on the back,")
         chooseTool == input(f"needless to say our paper was failed on site, GAME OVER")
if chooseTool == "superToolB":
          chooseTool == input(f"Turns out the head of the college cant read puppy print, Who knew? GAME OVER")
if chooseTool == "superTool":
  chooseTool == input(f"\nGood choice , {userName}, Lets begin the paper!")
print("We spend hours writing the paper, then find our way to the head of college's main office ahead of the teacher. We turn the paper in and get caught because the paper smells of pure kibbles and bits. We tried! GAME OVER")
print("The good news is Mr Woofles is no longer undercover and at home safe. Bad news is i failed this class but had a brave puppy to atleast try to save me")
print("The End")

