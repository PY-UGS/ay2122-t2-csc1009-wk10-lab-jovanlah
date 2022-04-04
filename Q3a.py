#Question 3a

def getModule(moduleCode):
    if moduleCode == "CSC1006":
        print("Mathematics 2")
    elif moduleCode == "CSC1007":
        print("Operating Systems")
    elif moduleCode == "CSC1008":
        print("Data Structures & Algorithms")
    elif moduleCode == "CSC1009":
        print("Object Oriented Programming")
    elif moduleCode == "CSC1010":
        print("Computer Networks")


moduleCode = input("Enter module code: ")
getModule(moduleCode.upper())

print()