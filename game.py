import sys
import time
class Character:
    def __init__(self,name="Eric",sword=None,shield=None,backpack=None):
        self.name = name
        self.sword = sword
        self.shield = shield
        self.backpack = backpack
    def attack(self):
        if self.sword:
            return self.sword.power
        else:
            return 1
    def defend(self):
        if self.shield:
            return self.shield.defense
        else:
            return None
    def items(self):
        if self.backpack:
            return self.backpack.items
        else:
            return None

class Sword:
    def __init__(self,power=2,name="basic"):
        self.power = power
        self.name = name
    
class Shield:
    def __init__(self,defense=1,name="basic"):
        self.defense = defense
        self.name = name

if __name__ == '__main__':
    name = str(raw_input("what's your name?"))
    Me = Character(name)
    time.sleep(2)
    print "Hello, "+ Me.name +",here you are in the world.  Oh look you found a sword, what do you do?"
    time.sleep(2)
    print "1.Pick it up"
    time.sleep(2)
    print "2.Do nothing"
    time.sleep(2)
    print "3.Why is there a sword here?"
    time.sleep(2)
    print "4.exit"
    time.sleep(2)
    action = int(raw_input("> "))
    if action == 1:
        Me.sword = Sword(4,"flame sword")
        time.sleep(2)
        print "congradulations, you got " + Me.sword.name
    elif action == 2:
        print "what's wrong with you?  Are you dead?  Not again!"
        sys.exit()
    elif action == 3:
        print "Why is there a sword here?!"
        time.sleep(2)
        print "Seriously?! That's what you say to a sweet sword?!?!  You are taking it and liking it."
        time.sleep(2)
        Me.sword = Sword(50,"Rage sword")
        print "congradulations, you got " + Me.sword.name
    elif action == 4:
        sys.exit()
    else:
        print "I didn't understand, clearly you don't know english, which is fine.  But I still have to say, you should have been able to understand me..."
        sys.exit()
