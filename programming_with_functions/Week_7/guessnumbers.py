import random

class guessnumber:

    def hard(self):
        
        self.LOWER = 1
        self.HIGHER = 1000

        number = random.randint(self.LOWER, self.HIGHER)
        return number

    def medium(self):
        
        self.LOWER = 1
        self.HIGHER  = 100
        
        number = random.randint(self.LOWER, self.HIGHER)
        return number

    def easy(self):

        self.LOWER = 1
        self.HIGHER = 10

        number = random.randint(self.LOWER, self.HIGHER)
        return number

    def main(self):
        play = ""
        
        while play != "no":
            easy = self.easy()
            medium = self.medium()
            hard = self.hard()
            number = -1
            level = input("Choose between easy medium or hard: ")

            if level == "easy":
                
                while number != easy:
                    
                    print()
                    number = int(input("What number do you think it is between 1-10? "))
                    
                    if number > easy:
                        print("Just a little bit lower.")
                    elif number < easy:
                        print("Just a little bit higher.")
                    else:
                        print()
                        print("YOU GOT IT!!")
            elif level == "medium":

                while number != medium:
                    
                    print()
                    number = int(input("What number do you think it is between 1-100? "))

                    if number > medium:
                        print("Just a little bit lower.")
                    elif number < medium:
                        print("Just a little bit higher.")
                    else:
                        print()
                        print("YOU GOT IT!!")
            elif level == "hard":

                while number != hard:
                    
                    print()
                    number = int(input("What number do you think it is between 1-100? "))

                    if number > hard:
                        print("Just a little bit lower.")
                    elif number < hard:
                        print("Just a little bit higher.")
                    else:
                        print()
                        print("YOU GOT IT!!")

                    
            play = input("Would you like to play again? ")
            print()


game = guessnumber()
game.main()
