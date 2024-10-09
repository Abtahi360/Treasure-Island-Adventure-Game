print("Welcome to Treasure Island.")
print("Your mission is to find the Treasure.")
print("You are at a cross road. Where do you want to go..?")
ch1 = input('Type "Left" or "Right"\n ==')
if ch1.lower() == "left":
    ch1_1 = input("You've come to a lake. There is an island in the middle of the lake.\n --> Type \"wait\" to wait for a boat. Type \"swim\" to swim across.\n ==")
    if ch1_1.lower() == "wait":
        ch1_2 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n ==")
        if ch1_2.lower() == "red":
            print("It's a room full of fire. GAME OVER..!")
        elif ch1_2.lower() == "yellow":
            print("You found the treasure! YOU WIN..!")
        elif ch1_2.lower() == "blue":
            print("You enter a room of beasts. GAME OVER..!")
        else:
            print("Invalid choice..! Please choose a valid door: Red, Yellow or Blue")
    else:
        print("You get attacked by an angry trout. Game Over..!")
else:
    print("You fell into a hole. Game Over..!")


