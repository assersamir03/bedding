Bedders = []
theMax = []

print("""
╔╗        ╔╗          
║║        ║║          
║╚═╗╔══╗╔═╝║╔╗╔═╗ ╔══╗
║╔╗║║╔╗║║╔╗║╠╣║╔╗╗║╔╗║
║╚╝║║║═╣║╚╝║║║║║║║║╚╝║
╚══╝╚══╝╚══╝╚╝╚╝╚╝╚═╗║
                  ╔═╝║
                  ╚══╝
""")


def bed():
    Name = input('enter your name: ')
    Bed = float(input('enter your bed: '))
    Bedders.append({'name': Name, 'bed': Bed})
    repeat = input('repeat y/n: ')
    if repeat == 'y':
        bed()
    else:
        print("calculating!")


def calc():
    for i in Bedders:
        theMax.append(i["bed"])
    newMax = max(theMax)
    for j in Bedders:
        if j["bed"] == newMax:
            print(f'the winner is {j["name"]}')


bed()
calc()
