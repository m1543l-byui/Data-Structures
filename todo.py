# Press Enter after each chore
# use 'q' to quit when you are ready to begin 
# the list will tell you what chore to do first.
print('Please enter your chores: ')

chores = []

while True:
    todo = input()
    if str.lower(todo) == "q":
        break
    else:
        chores.append(todo)
    print(chores)

print()

print(chores.pop(0))

for item in chores:
    print("Chores left:", item)
