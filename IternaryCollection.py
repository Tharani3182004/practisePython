totalItem = 1000

def AddtoIter(item):
    global totalItem
    totalItem = item + totalItem

def SubToIter(item):
    global totalItem
    totalItem = totalItem - item

while True:
    print("Please tell the options: it is either add or sub or stop")

    option = input()

    if option == "add":
        print("Please provide item count for add")
    elif option == "stop":
        print("logging off")
        break
    else:
        print("Please provide item count for sub")

    itemCount = int(input())

    if option == "add":
        AddtoIter(itemCount)
    else:
        SubToIter(itemCount)

    print(f"number of item: {totalItem}")
