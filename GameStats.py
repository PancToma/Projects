import matplotlib.pyplot as plt

print("Game list: COD, CS:GO, Fortnite")
userinput = input("select which game you want to see the stats of: ")



def fortniteGame():
    y = [2022, 2023, 2024, 2025]
    x = [10217, 11476, 16543, 18719]
    plt.title("Fortnite game player statistics over the years")
    plt.xlabel("Players")
    plt.ylabel("Years")
    plt.plot(y,x)
    plt.show()


def CodGame():
    y = [2022, 2023, 2024, 2025]
    x = [24112, 24512, 42712, 57231]
    plt.title("COD game player statistics over the years")
    plt.xlabel("Players")
    plt.ylabel("Years")
    plt.plot(y,x)
    plt.show()

def CsGame():
    y = [2022, 2023, 2024, 2025]
    x = [46212, 46521, 57123, 59122]
    plt.title("CS:GO game player statistics over the years")
    plt.xlabel("Players")
    plt.ylabel("Years")
    plt.plot(y,x)
    plt.show()


if userinput == "Fortnite" or userinput == "fortnite" or userinput == "FORTNITE":
    fortniteGame()
elif userinput == "COD" or userinput == "cod" or userinput == "Cod":
    CodGame()
elif userinput == "CSGO" or userinput == "CsGo" or userinput == "csgo":
    CsGame()
else:
    print("Selected game not found. Make sure to choose a game from the list")



