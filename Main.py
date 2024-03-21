from datetime import date


Entries = ["googoo", "gaga"]
tempEntry = ""
today = "0/0"
newEntry = 0
whichToVeiw = 0
isQuit = "No"
cont = ""


print(f"{'D R E A M    J O U R N A L':-^100}")
while isQuit == "No":
    newEntry = input(f'{"1 to start a new entry, 2 to browse, 3 to quit...": ^100}\n')

    if newEntry == "1":
        print(f"{'Write Your Entry Below...': ^100}")
        tempEntry = input()
        #today = str(date.today()) not using this yet
        Entries.append(tempEntry)
        print("Entry Added...")
        newEntry = input(f'{"1 to start another entry, 2 to browse, 3 to quit...": ^100}\n')
        
    if newEntry == "2":
        while newEntry == "2":
            print(f"{'Select an entry to view': ^100}\n")
            for i in enumerate(Entries):
                print(i)
            whichToVeiw = input()
            for i in range(len(Entries)):
                if i == int(whichToVeiw):
                    print(f"{Entries[i]: ^100}")
            
            cont = input(f'{"View another? (1 for yes, 2 for no)": ^100}\n')
            if cont == "1":
                newEntry = "2"
            else:
                newEntry = "1"

    else:
        isQuit = input(f"{'Quit? Yes or No...': ^100}")
