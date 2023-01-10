from datetime import datetime

#ჩანაწერების შემქმნელი კლასის შექმნა
class Todo:

    def __init__(self, text, deadline):
        self.text = text
        self.deadline = deadline
        self.date = datetime.now()

    def __str__(self):
        if self.deadline == None:
            return f'Create/edit Date: {self.date.strftime("%d/%m/%Y %H:%M")}\nDeadline: None\nTodo: {self.text}'

        else:
            return f'Create/edit Date: {self.date.strftime("%d/%m/%Y %H:%M")}\nDeadline: {self.deadline.strftime("%d/%m/%Y %H:%M")}\nTodo: {self.text}'

#უნდა შეიქმნას ბაზა (ფსევდო ბაზა) თუდუს ლისტის შესაქმნელად
class Database:
    #სია რომელიც შეინახავს ყველა დავალებას
    entries = []

    def add_db(self, todo):
        self.entries.append(todo)
        print("\nTask Added Successfully!")
        print("-"*50)

    def getALL(self):
        return self.entries

    def update_db(self, oldTodo, newTodo):
        self.entries[oldTodo] = newTodo
        print("\nTask Updated Successfully!")
        print("-"*50)
        print("\n")

    def check_db(self):
        return bool(self.entries)

    def delete_db(self, todoIndex):
        self.entries.pop(todoIndex)
        print("\nTask Deleted Successfully!")
        print("-"*50)
        print("\n")

#ბაზასთან ურთიერთობისთვის შუამავალი, უსმენს იუზერს, და არეგისტრირებს ბაზაში
class Manager:

    def __init__(self, db):
        self.db = db

    def add(self, todo):
        self.db.add_db(todo)

    def update(self, oldTodo, newTodo):
        self.db.update_db(oldTodo, newTodo)

    def len_data(self):
        return len(self.db.getALL())

    def showALL(self):
        data = self.db.getALL()

        for index, item in enumerate(data, 1):
            print("Task N:", str(index))
            print(item)
            print("-" * 50)

    def check_data(self):
        return self.db.check_db()

    def delete(self, todoIndex):
        return self.db.delete_db(todoIndex)


#დუბლირების თავიდან ასაცილებლად
def check_inputs(manager):
    if not manager.check_data():
        print("\n")
        print("XXXXX","Database is Empty!","XXXXX")

    else:
        while True:
            manager.showALL()

            print("\n")
            print("Type 'exit' to go back to main manu, or enter the task num to continue")
            index = input("Task N: ")

            if index == 'exit':
                return index

            if not index.isdigit():
                print("\n")
                print("Please enter the digit!")
                continue

            if int(index) > manager.len_data():
                print("XXXXX","Out of range!","XXXXX")
                print("\n")
                continue

            todoIndex = int(index) - 1

            return todoIndex

#კოდის დუბლირების შესამცირებლად
def date_format():
    date_input = input("Deadline date (ex. YYYY,MM,DD,HH,MM): ")
    date_components = date_input.split(",")
    deadline = datetime(int(date_components[0]),int(date_components[1]),int(date_components[2]),int(date_components[3]),int(date_components[4]),0)
    return deadline

def date_check():
    check = True
    while check:
        try:
            deadline = date_format()
            check = False
            return deadline
        except (ValueError, IndexError):
            print("Date value is invalid, please enter the relevant deadline date!")

#ძირითადი ოპერაციები რაც მომხმარებელმა უნდა აკეთოს
#add, edit, delete, show
def menu():
    choice = None

    db = Database()
    manager = Manager(db)

    #q ს აკრეფისას რომ გამოვიდეს პროგრამიდან
    while choice != "Q":
        print("\n")
        print("ToDo List Menu:")
        print("1. Create new task")
        print("2. Edit task")
        print("3. Delete task from list")
        print("4. Show all tasks")
        print("Type 'Q' for Exit")
        print("\n")

        choice = input("Action: ").upper()

        if choice == "1":
            print("Type 'exit' to go back to main manu, or enter the text for task")
            text = input("Text: ")
            if text == 'exit':
                continue

            has_deadline = input("If the task has a deadline, type 'Y'. Otherwise click just Enter/Return button.\nDeadline: --- ").upper()
            if has_deadline == 'Y':
                deadline = date_check()
            else:
                deadline = None

            todo = Todo(text, deadline)
            manager.add(todo)

        elif choice == "2":
            oldTodo = check_inputs(manager)

            if oldTodo == 'exit':
                continue
            else:
                text = input("Enter new text: ")

                has_deadline = input("If the task has a deadline, type 'Y'. Otherwise click just Enter/Return button.\nDeadline: --- ").upper()
                if has_deadline == 'Y':
                    deadline = date_check()
                else:
                    deadline = None

                newTodo = Todo(text, deadline)
                manager.update(oldTodo, newTodo)

        elif choice == "3":
            todoIndex = check_inputs(manager)

            if todoIndex == 'exit':
                continue
            else:
                manager.delete(todoIndex)

        elif choice == "4":

            if manager.check_data():
                manager.showALL()
            else:
                print("Database is Empty!")

        elif choice == "Q":
            print("Bye bye!")
            print("\n")

        else:
            print("-"*50)
            print("Wrong choice! please enter: 1/2/3/4 or Q!")

menu()
