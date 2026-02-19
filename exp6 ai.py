# Goal-Based Vacuum Cleaner Agent

def goal_based_vacuum(location, state):
    print("Starting Position:", location)
    print("Initial Room States:", state)

    goal = {'A': 0, 'B': 0}   # Goal: Both rooms clean
    cost = 0

    # While goal not achieved
    while state != goal:
        print("\nCurrent Location:", location)

        # If current location is dirty → clean
        if state[location] == 1:
            print(location, "is Dirty → Cleaning...")
            state[location] = 0
            cost += 1
        else:
            print(location, "is already clean.")

        # After cleaning or checking, move only if goal not reached
        if state != goal:
            # Move to the other room
            location = 'B' if location == 'A' else 'A'
            print("Moving to", location)
            cost += 1

    print("\n🎯 Goal Achieved: All rooms are clean!")
    print("Final Room States:", state)
    print("Total Cost:", cost)


# MAIN PROGRAM
start_location = 'A'
room_state = {'A': 1, 'B': 1}   # 1 = Dirty, 0 = Clean

goal_based_vacuum(start_location, room_state)
