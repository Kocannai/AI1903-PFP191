def create_pupil(pupils, rollno, name, m1, m2, m3, m4, m5):
    if rollno not in pupils:
        pupils[rollno] = {"name": name, "m1": m1, "m2": m2, "m3": m3, "m4": m4, "m5": m5}
        x=input("wants to enter more record (y/n)?: ")
        if x == "y":
            rollno = int(input("Enter roll number: "))
            name = input("Enter name: ")
            m1 = int(input("Enter Marks in English: "))
            m2 = int(input("Enter Marks in Maths: "))
            m3 = int(input("Enter Marks in Physics: "))
            m4 = int(input("Enter Marks in Chemistry: "))
            m5 = int(input("Enter Marks in CS: "))
            create_pupil(pupils, rollno, name, m1, m2, m3, m4, m5)
        elif x == "n":
            admin_menu(pupils)
    else:
        print(f"Pupil with roll number '{rollno}' already exists.")

def display_all_pupils(pupils):
    print("PUPIL Details..")
    for rollno, pupil_info in pupils.items():
        print(f"Roll Number: {rollno}\nName: {pupil_info['name']}\nEnglish: {pupil_info['m1']}\nMaths: {pupil_info['m2']}\nPhysics: {pupil_info['m3']}\nChemistry: {pupil_info['m4']}\nCS: {pupil_info['m5']}")
    admin_menu(pupils)

def search_pupil(pupils, query):
    found = False
    for rollno, pupil_info in pupils.items():
        if str(rollno) == query.lower():
            print("PUPIL Details..")
            print(f"Roll Number: {rollno}\nName: {pupil_info['name']}\nEnglish: {pupil_info['m1']}\nMaths: {pupil_info['m2']}\nPhysics: {pupil_info['m3']}\nChemistry: {pupil_info['m4']}\nCS: {pupil_info['m5']}")
            found = True
    if not found:
        print(f"There is no roll number: '{query}'.")
    admin_menu(pupils)
    
def search_pupil1(pupils, query):
    found = False
    for rollno, pupil_info in pupils.items():
        if str(rollno) == query.lower():
            print("PUPIL Details..")
            print(f"Roll Number: {rollno}\nName: {pupil_info['name']}\nEnglish: {pupil_info['m1']}\nMaths: {pupil_info['m2']}\nPhysics: {pupil_info['m3']}\nChemistry: {pupil_info['m4']}\nCS: {pupil_info['m5']}")
            found = True
    if not found:
        print(f"There is no roll number: '{query}'.")
    report_menu(pupils)
    
def modify_pupil(pupils, query):
    query = int(query)
    if query in pupils:
        print(f"Name: {pupils[query]['name']}")
        new1 = input("wants to edit(y/n)? ")
        if new1 == "y":
            new_name = input("Enter the name: ")
            pupils[query]['name'] = str(new_name)
        
        print(f"English marks: {pupils[query]['m1']}")
        new2 = input("wants to edit(y/n)? ")
        if new2 == "y":
            new_m1 = input("Enter the mark: ")
            pupils[query]['m1'] = (new_m1)
        
        print(f"Maths marks: {pupils[query]['m2']}")
        new3 = input("wants to edit(y/n)? ")
        if new3 == "y":
            new_m2 = input("Enter the mark: ")
            pupils[query]['m2'] = (new_m2)
    
        print(f"Physics marks: {pupils[query]['m3']}")
        new4 = input("wants to edit(y/n)? ")
        if new4 == "y":
            new_m3 = input("Enter the mark: ")
            pupils[query]['m3'] = (new_m3)
                
        print(f"Chemistry marks: {pupils[query]['m4']}")
        new5 = input("wants to edit(y/n)? ")
        if new5 == "y":
            new_m4 = input("Enter the mark: ")
            pupils[query]['m4'] = (new_m4)
                        
        print(f"CS marks: {pupils[query]['m5']}")
        new6 = input("wants to edit(y/n)? ")
        if new6 == "y":
            new_m5 = input("Enter the mark: ")
            pupils[query]['m5'] = (new_m5)
        print("Record updated")
        print(f"Roll Number: {query}\nName: {pupils[query]['name']}\nEnglish: {pupils[query]['m1']}\nMaths: {pupils[query]['m2']}\nPhysics: {pupils[query]['m3']}\nChemistry: {pupils[query]['m4']}\nCS: {pupils[query]['m5']}")
    else:
        print(f"No record found for '{query}'. Cannot modify.")
    admin_menu(pupils)

def delete_pupil(pupils, query):
    query = int(query)
    if query in pupils:
        print("PUPIL Details..")
        print(f"Roll Number: {query}\nName: {pupils[query]['name']}\nEnglish: {pupils[query]['m1']}\nMaths: {pupils[query]['m2']}\nPhysics: {pupils[query]['m3']}\nChemistry: {pupils[query]['m4']}\nCS: {pupils[query]['m5']}")
        del pupils[query]
        print("record found and deleted")
    else:
        print(f"No record found for '{query}'. Cannot delete.")
    admin_menu(pupils)

def main_menu(pupils):
    print("Main Menu:")
    print("1. Report")
    print("2. Admin")
    print("3. Exit")
    choice = input("Enter choice(1-3): ")
    if choice == "1":
        report_menu(pupils)
    elif choice == "2":
        admin_menu(pupils)
    elif choice == "3":
        print("Exit!")
        return False
    else:
        print("Invalid choice. Please try again.")
    return True

def admin_menu(pupils):
    print('ADMIN MENU')
    print('1. CREATE PUPIL RECORD')
    print('2. DISPLAY ALL PUPILS RECORD')
    print('3. SEARCH PUPIL RECORD')
    print('4. MODIFY PUPIL RECORD')
    print('5. DELETE PUPIL RECORD')
    print('6. BACK TO MAIN MENU')
    choice = input("Enter choice(1-6): ")
    if choice == "1":
        rollno = int(input("Enter roll number: "))
        name = input("Enter name: ")
        m1 = int(input("Enter Marks in English: "))
        m2 = int(input("Enter Marks in Maths: "))
        m3 = int(input("Enter Marks in Physics: "))
        m4 = int(input("Enter Marks in Chemistry: "))
        m5 = int(input("Enter Marks in CS: "))
        create_pupil(pupils, rollno, name, m1, m2, m3, m4, m5)
    elif choice == "2":
        display_all_pupils(pupils)
    elif choice == "3":
        query = str(input("Enter rollno you want to search: "))
        search_pupil(pupils, query)
    elif choice == "4":
        print('MODIFY RECORD')
        query = input("Enter roll number: ")
        modify_pupil(pupils, query)
    elif choice == "5":
        print('DELETE RECORD')
        query = input("Enter roll number: ")
        delete_pupil(pupils, query)
    elif choice == "6":
        return
    else:
        print("Invalid choice. Please try again.")
        admin_menu(pupils)
        
def report_menu(pupils):
    print("REPORT MENU:")
    print("1. CLASS RESULT")
    print("2. PUPIL RECORD CARD")
    print("3. BACK TO MAIN MENU")
    choice = input("Enter choice(1-3): ")
    if choice == "1":
        for rollno, pupil_info in pupils.items():
            print("Rollno    Name     English      Maths       Physics         Chemistry         CS")
            print(f"   {rollno}     {pupil_info['name']}    {pupil_info['m1']}     {pupil_info['m2']}     {pupil_info['m3']}     {pupil_info['m4']}    {pupil_info['m5']}")
            report_menu(pupils)
    elif choice == "2":
        query = str(input("Enter rollno you want to search: "))
        search_pupil1(pupils, query)
    elif choice == "3":
        return
    else:
        print("Invalid choice. Please try again.")
        admin_menu(pupils)
def main():
    pupils = {}

    while True:
        if not main_menu(pupils):
            break

if __name__ == "__main__":
    main()
