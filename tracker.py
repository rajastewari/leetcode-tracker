from problems import Problem
import storage

def add_problem(problems):
    # get user input for problem
    id = input("Enter problem ID: ")
    title = input("Title: ")
    difficulty = input("Difficulty (Easy/Medium/Hard): ")

    # create problem object and add to list
    problem = Problem(id, title, difficulty)
    problems.append(problem)

    # save updated list
    storage.save(problems)


def update_status(problems):
    # get user input for the ID
    id = int(input("Enter problem ID to update: "))

    # iterate through problems
    for p in problems:

        # check if the ID matches
        if p.id == id:
            # display current status and get new status
            print(f"Current status: {p.status}")
            new_status = input("Enter new status (todo/in_progress/done): ")
            p.update_status(new_status)

            # save updated list
            storage.save(problems)
            return
        
        print("Problem not found.")
            

def list_problems(problems):
    # if no problems
    if not problems:
        print("No problems added yet.")
        return
    
    # list all problems
    print("\nList of Problems:")
    for p in problems:
        print(p)


def mark_redo(problems):
    # get user input for problem ID
    id = int(input("Enter problem ID to mark for redo: "))

    # iterate through problems
    for p in problems:
        # check if the ID matches
        if p.id == id:
            # update redo flag and save
            p.redo = True
            storage.save(problems)
            return
        
        print("Problem not found.")


def main():
    problems = storage.load()

    # loop for menu
    while True:
        print("\n--- LeetCode Tracker ---")
        print("1. Add problem")
        print("2. Update status")
        print("3. List problems")
        print("4. Mark for redo")
        print("5. Quit")

        # get user input
        choice = input("\nChoose an option: ")

        if choice == "1":
            add_problem(problems)
        elif choice == "2":
            update_status(problems)
        elif choice == "3":
            list_problems(problems)
        elif choice == "4":
            mark_redo(problems)
        elif choice == "5":
            storage.save(problems)
            print("Progress saved. Bye!")
            break
        else:
            print("Invalid option, try again.")

main()