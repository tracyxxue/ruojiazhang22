from load_map_ import load_map
import game_state
from game_state import map
from movement import *
from progressive_map import *
from blessed import Terminal
import time
from squirrel_battle_graphical_UI import *
from random_maze import generate_maze
check = None


def Starting_UI() -> None:
    print("""
          **************Welcome to ATTACK DAT SQUIRREL***************
          a zork-inspired game designed by Tracy Xue and Ruojia Zhang
          ############################################################
          Once upon a time...
          the villan of the world...
          Mr.KBLALA the Black Squirrel...
          appeared on our very own lovely Haverford College...
          You are tasked to reach the goal of the maze and chase off Mr.KBLALA
          """)
    while True:
        start = input("Choose a level (easy / medium / hard /random): ")
        if start == "easy":
            game_state.map[:] = load_map("map1.txt")  # This updates the list in place
            print("Good Choice")
            break
        elif start == "medium":
            game_state.map[:] = load_map("map2.txt")
            print("Good Choice")
            break
        elif start == "hard":
            game_state.map[:] = load_map("map3.txt")
            print("Good Choice")
            break
        elif start=="random":
            row=int(input("how many rows you want?"))
            col=int(input("how many column you want?"))
            game_state.map=generate_maze(row, col)
            print(game_state.map)
            print("A random map has been created!")
            break
        else:
            print("Invalid choice. Please try again.")
    print(""" I have a few more helpful tips for you before you pivot :)
          To teleport:
            type "teleport", then enter a coordinates that you want to travel to
          To move by grid:
            type "north?" or "south?" or "east?" or "west?" to test if you could move to your intended location
            type "go north" or "go south" or "go east" or "go west" to make your movement.
          To check where you have already traveled:
            type "map"
          GET READY FOR YOUR JOURNEY :)""")

    start = find_start_location(map)
    if start:
        row, col = start
        map[row-1][col-1] = 3
    print("your start location is: ", start)
    
    while True:
        user_command = input("Enter a command: \n")
        if goalReached()==True:
            break
        if user_command == "north?":
            answer = canGoNorth(map)
            if answer == True:
                print("yes. you may go north.")
            if answer == False:
                print("no. way to north is blocked")

        elif user_command == "south?":
            answer = canGoSouth(map)
            if answer == True:
                print("yes. you may go south")
            if answer == False:
                print("no. way to south is blocked")

        elif user_command == "east?":
            answer = canGoEast(map)
            if answer == True:
                print("yes. you may go east")
            if answer == False:
                print("no. way to east is blocked")

        elif user_command == "west?":
            answer = canGoWest(map)
            if answer == True:
                print("yes. you may go west")
            if answer == False:
                print("no. way to west is blocked")
        
        elif user_command == "go north":
            if goNorth():
                print("Moved north.")
                
            else:
                print("Cannot go north.")

        elif user_command == "go south":
            if goSouth():
                print("Moved south.")
               
            else:
                print("Cannot go south.")

        elif user_command == "go east":
            if goEast():
                print("Moved east.")
             
            else:
                print("Cannot go east.")

        elif user_command == "go west":
            if goWest():
                print("Moved west.")
             
            else:
                print("Cannot go west.")

        elif user_command == "teleport":
            draw_map()
            x_coord = input("Which x position would you like to go? ")
            y_coord = input("Which y position would you like to go? ")
            x = int(x_coord)
            y = int(y_coord)
            print(x,y)
            success = setLocation(x,y)
            if success:
                print("Teleportation successful.")
                for row in game_state.map:   
                    print(row)
            else:
                print("Teleportation failed. Invalid or blocked location.")
        
        elif user_command == "map":
            draw_map()
        
        else:
            print("Invalid input")
    squirrel_battle()

        
if __name__ == "__main__":
    Starting_UI()