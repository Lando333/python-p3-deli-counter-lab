# import ipdb

katz_deli = []

def line(current_line):
    if current_line == []:
        print("The line is currently empty.")
    else:
        katz_deli = [f"{current_line.index(person) + 1}" + ". " + person for person in current_line]
        print("The line is currently: " + " ".join(katz_deli))

def take_a_number(katz_deli, new_person):
    katz_deli.append(new_person)
    print(f"Welcome, {new_person}. You are number {len(katz_deli)} in line.")


def now_serving(katz_deli):
    if katz_deli == []:
        print("There is nobody waiting to be served!")
    else:
        print(f"Currently serving {katz_deli[0]}.")
        katz_deli.pop(0)