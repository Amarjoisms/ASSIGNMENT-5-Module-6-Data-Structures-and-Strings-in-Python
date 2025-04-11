try:
    dir = {'Amar':98,'Alice':85,'AJ':86}
    name = input("Enter the student's name: ")
    print(dir[name])
except KeyError:
    print('Student not found')

