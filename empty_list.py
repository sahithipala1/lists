my_agenda = []


def print_list():
    print()
    for item in my_agenda:
        print(item)
    print()


while True:
    item = input("What's next on the Agenda? :")
    my_agenda.append(item)
    print_list()
else:
    print("are you done")