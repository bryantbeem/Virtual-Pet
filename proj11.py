###############################################################################
#Computer Project 11
#   Pet Class
#       contains 13 functions
#   Cat class
#       inherits the pet class
#   Dog class
#       inherits the dog class
#   Main Function
#       Calls for the rest of the function
#       This is where the user interacts with the pet
#       User sees updated staus of pet
###############################################################################
from cse231_random import randint
from edible import *

MIN, MAX = 0, 10
dog_edible_items = [DogFood]
cat_edible_items = [CatFood]
dog_drinkable_items = [Water]
cat_drinkable_items = [Water]

class Pet(object):
    def __init__(self, name='fluffy', species='dog', gender='male',color='white'):
	# insert docstring
    
        self._name = name.capitalize()
        self._species = species.capitalize()
        self._gender = gender.capitalize()
        self._color = color.capitalize()
        self._edible_items = ''
        self._drinkable_items = ''

        self._hunger = randint(0,5)
        self._thirst = randint(0,5)
        self._smell = randint(0,5)
        self._loneliness = randint(0,5)
        self._energy = randint(5,10)

        self._reply_to_master('newborn')
        
    def _time_pass_by(self, t=1):
        '''
        This function asses how the pet status changes over time
        Returns the new value for each
        '''
        self._hunger = min(MAX, self._hunger + (0.2 * t))
        self._thirst = min(MAX, self._thirst + (0.2 * t))
        self._smell = min(MAX, self._smell + (0.1 * t))
        self._loneliness = min(MAX, self._loneliness + (0.1 * t))
        self._energy = max(MIN, self._energy - (0.2 * t))
        
    def get_hunger_level(self):
	# insert docstring
        return self._hunger
    
    def get_thirst_level(self):
        return self._thirst
    
    def get_energy_level(self):
        return self._energy #return energy
    
    def drink(self, liquid):
        
        if isinstance(liquid, tuple(self._drinkable_items)): #makes sure item is drinkable
            self._time_pass_by()
            liquid_quantity = liquid.get_quantity()
            if (self._thirst) < liquid_quantity:
                self._thirst = 0 #thirst value goes to 0 if liquid quanityt is larger
            else:
                self._thirst = (self._thirst) - liquid_quantity #makes new thirst qunatity
            self._reply_to_master('drink') #replies to master
        else:
            print("Not drinkable") #prints not drinakble
        self._update_status() #update status
        

    def feed(self, food):

        if isinstance(food, tuple(self._edible_items)): #makes sure item is edible
            self._time_pass_by() #pass time
            food_quantity = food.get_quantity() #gets food quantity
            if self._hunger < food_quantity: #hunger value goes to 0 if food quantity is greater
                self._hunger = 0
            else:
                self._hunger = self._hunger - food_quantity
            self._reply_to_master('feed') #replies to master
        else:
            print('Not edible') #prints not edible
        self._update_status() #update status


    def shower(self):
        time = 4 #set time to 2
        self._time_pass_by(time) #pass time

        self._smell = 0 #set smell to 0
        self._loneliness = max(MIN, self._loneliness - time) #increase loneliness level
        
        self._reply_to_master('shower') #reply to master
        self._update_status() #update status


    def sleep(self):

        time = 7 #sleep for 7
        self._time_pass_by(time) #pass time
        
        self._energy = min(MAX, self._energy + time) #increase energy level
        
        self._reply_to_master('sleep') #reply to master
        self._update_status() #update status
        
    def play_with(self):

        time = 4 #set time to 4
        self._time_pass_by(time)
        
        self._loneliness = max(MIN, self._loneliness - time) #Decrease loneliness level
        self._smell = min(MAX, self._smell + time) #increase smell level
        self._energy = max(MIN, self._energy - time) #decrease energy level
        
        self._reply_to_master('play')
        self._update_status() #update status
        
    def _reply_to_master(self, event='newborn'):

        faces = {}
        talks = {}
        faces['newborn'] = "(๑>◡<๑)"
        faces['feed'] = "(๑´ڡ`๑)"
        faces['drink'] = "(๑´ڡ`๑)"
        faces['play'] = "(ฅ^ω^ฅ)"
        faces['sleep'] = "୧(๑•̀⌄•́๑)૭✧"
        faces['shower'] = "( •̀ .̫ •́ )✧"

        talks['newborn'] = "Hi master, my name is {}.".format(self._name)
        talks['feed'] = "Yummy!"
        talks['drink'] = "Tasty drink ~"
        talks['play'] = "Happy to have your company ~"
        talks['sleep'] = "What a beautiful day!"
        talks['shower'] = "Thanks ~"

        s = "{} ".format(faces[event])  + ": " + talks[event] #string for face and reply
        print(s) #print reply
    def show_status(self):

        print("{:<12s}: [{:<20s}]".format('Energy','#'*2*int(round(self._energy))) + "{:5.2f}/{:2d}".format(self._energy,10))
        print("{:<12s}: [{:<20s}]".format('Hunger','#'*2*int(round(self._hunger))) + "{:5.2f}/{:2d}".format(self._hunger,10))
        print("{:<12s}: [{:<20s}]".format('Loneliness','#'*2*int(round(self._loneliness))) + "{:5.2f}/{:2d}".format(self._loneliness,10))
        print("{:<12s}: [{:<20s}]".format('Smell','#'*2*int(round(self._smell))) + "{:5.2f}/{:2d}".format(self._smell,10))
        print("{:<12s}: [{:<20s}]".format('Thirst','#'*2*int(round(self._thirst))) + "{:5.2f}/{:2d}".format(self._thirst,10))

    def _update_status(self):

        faces = {}
        talks = {}
        faces['default'] = "(à¹‘>â—¡<à¹‘)"
        faces['hunger'] = "(ï½¡>ï¹<ï½¡)"
        faces['thirst'] = "(ï½¡>ï¹<ï½¡)"
        faces['energy'] = "(ï½žï¹ƒï½ž)~zZ"
        faces['loneliness'] = "(à¹‘oÌ´Ì¶Ì·Ì¥á·…ï¹oÌ´Ì¶Ì·Ì¥á·…à¹‘)"
        faces['smell'] = "(à¹‘oÌ´Ì¶Ì·Ì¥á·…ï¹oÌ´Ì¶Ì·Ì¥á·…à¹‘)"

        talks['default'] = 'I feel good.'
        talks['hunger'] = 'I am so hungry ~'
        talks['thirst'] = 'Could you give me some drinks? Alcohol-free please ~'
        talks['energy'] = 'I really need to get some sleep.'
        talks['loneliness'] = 'Could you stay with me for a little while ?'
        talks['smell'] = 'I am sweaty'

class Cat(Pet):

    def __init__(self, name='fluffy', gender='male',color='white'):

        Pet.__init__(self, name, "cat", gender, color) #initailizes pet class to a dog
        self._edible_items = [CatFood] #add catfood to edible items
        self._drinkable_items = [Water] #add water to drinkable items

    
class Dog(Pet):

    def __init__(self, name='fluffy', gender='male',color='white'):

        Pet.__init__(self, name, "dog", gender, color)  #initailizes pet class to a dog
        self._edible_items = [DogFood] #add dogfood to edible items
        self._drinkable_items = [Water]  #add water to drinkable items
    
def main():

    print("Welcome to this virtual pet game!") #introduction
    prompt = input("Please input the species (dog or cat), name, gender (male / female), fur color of your pet, seperated by space \n ---Example input:  [dog] [fluffy] [male] [white] \n (Hit Enter to use default settings): ")
    while True:
        prompt = prompt.split()
        if prompt == []:
            animal = Dog('fluffy', 'male', 'white') #this is the default for when user presses enter
            break
        if (prompt[0] == "dog" or prompt[0] == "cat") and (prompt[2] == "male" or prompt[2] == "female"):
            if prompt[0]== "dog":
                animal = Dog(prompt[1], prompt[2], prompt[3]) #user wants to use a dog
                break #break out of loop
            if prompt[0] == 'cat':
                animal = Cat(prompt[1], prompt[2], prompt[3]) #user wants to use a cat
                break #break out of loop
        if (prompt[0] != "dog" and prompt[0] != "cat") or (prompt[2] != "male" and prompt[2] != "female"):
            prompt = input("Please input the species (dog or cat), name, gender (male / female), fur color of your pet, seperated by space \n ---Example input:  [dog] [fluffy] [male] [white] \n (Hit Enter to use default settings): ")
            #user has invalid response

    intro = "\nYou can let your pet eat, drink, get a shower, get some sleep, or play with him or her by entering each of the following commands:\n --- [feed] [drink] [shower] [sleep] [play]\n You can also check the health status of your pet by entering:\n --- [status]."
    print(intro)
    #code to handle commands
    while True:
        prompt_1 = input("\n[feed] or [drink] or [shower] or [sleep] or [play] or [status] ? (q to quit): ")
        if prompt_1 != 'q': #user does not want to quit
            if prompt_1 == 'eat':
                print("Invalid command.") #command ins invalid
            if prompt_1 == 'feed':
                while True: #while loop to ask for food amount
                    food = input("How much food ? 1 - 10 scale: ") #ask for food amount
                    if food == 'drink': #invalid input
                        print("Invalid input.") #invalid command
                        continue
                    if (int(food) <= 10) and (int(food) >= 1): 
                        if int(food) <= 10 and int(food) > 1:
                            if prompt[0] == 'dog': #prompt is dog
                                eat_up = DogFood(int(food)) #dog eats food
                                animal.feed(eat_up)
                                break #break out of loop
                            if prompt[0] == 'cat':
                                eat_up = CatFood(int(food))
                                animal.feed(eat_up) #feed animals
                                break #break out of loops
                        if int(food) == 1:
                            print("Your pet is satisfied, no desire for sustenance now.") #pet doesnt want to eat
                            break
                    else:
                        print("Invalid input.") #invalid input
                        
            if prompt_1 == 'drink': #animal drinls
                while True:
                    liquid = input("How much drink ? 1 - 10 scale: ") #ask for scale
                    if liquid == 'play':
                        print("Invalid input.")
                        continue
                    if int(liquid) <= 10 and int(liquid) >= 1: #liquid if valid
                        bottoms_up = Water(int(liquid)) #animal drinks liquid
                        animal.drink(bottoms_up)
                        break
                    else:
                        print("Invalid input.") #input is invalid
                    
            if prompt_1 == 'shower':
                animal.shower() #animal shower
            if prompt_1 == 'sleep':
                animal.sleep() #animal sleeps
            if prompt_1 == 'play':
                animal.play_with() #play with animal
            if prompt_1 == 'status':
                animal.show_status() #show the status
        else:  
            print("Bye ~") #bye
            break #break out of loop

if __name__ == "__main__":
    main()