numbers = [1, 2, 3, 4, 5, 6, 7, 8]

names = ["Jane", "Anna", "Reni", "July", "Adriana", "Stephany"]

if __name__ == "__main__":
    print(list(map(lambda num: num * 2, numbers)))

    # Връща True ili False като обхожда списъка и пак го връща като списък
    print(list(map(lambda name: name.startswith('A'), names)))
