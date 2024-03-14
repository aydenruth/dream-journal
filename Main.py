from datetime import date


Entries = []
tempEntry = ""
today = "0/0"
newEntry = 0

print(f"{'D R E A M    J O U R N A L':-^100}")
newEntry = input(f'{"1 to start a new entry, 2 to browse...": ^100}\n')

if newEntry == "1":
    print(f"{'Write Your Entry Below...': ^100}")
    tempEntry = input()
    today = str(date.today())
    Entries.append([today, tempEntry])
    print(Entries)
    
newEntry = False

