from playerReader import PlayerReader

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    reader = PlayerReader(url)

if __name__ == "__main__":
    main()
