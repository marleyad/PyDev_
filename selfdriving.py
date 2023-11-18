
def move_forward():
    print("moving forward")

def turn(direction):
    print(f"turning {direction}")

def start_engine():
    print("starting engine")

def stop_engine():
    print("stopping engine")

def follow_roundabout(exit_number):
    print(f"taking exit number {exit_number} from the roundabout")

start_engine()

destination = input("Where do you want to go?\n")

if destination == "library":
    move_forward()
    turn("left")
    print(f"You have arrived at the {destination}")
elif destination == "tech park":
    move_forward()
    turn("right")
    print(f"You have arrived at the {destination}")
elif destination == "hospital" or "mall" or "airport" or "university" or "stadium":
    move_forward()
    if destination == "hospital":
        follow_roundabout(1)
        print(f"You have arrived at the {destination}")
    elif destination == "mall":
        follow_roundabout(2)
        print(f"You have arrived at the {destination}")
    elif destination == "airport":
        follow_roundabout(3)
        print(f"You have arrived at the {destination}")
    else:
        follow_roundabout(4)
        move_forward()
        if destination == "university":
            turn("left")
            print(f"You have arrived at the {destination}")
        else:
            turn("right")
            print(f"You have arrived at the {destination}")
else:
    print("Invalid destination. Please try again")

stop_engine()

