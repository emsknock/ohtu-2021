from rps import RPS

def main():
    while True:
        
        print(
            "Valitse pelataanko \n"
            "(a) Ihmistä vastaan \n"
            "(b) Tekoälyä vastaan \n"
            "(c) Parannettua tekoälyä vastaan \n"
            "Muilla valinnoilla lopetetaan"
        )

        mode = input().lower()

        modes = {
            "a": RPS.player_vs_player(),
            "b": RPS.player_vs_simple_ai(),
            "c": RPS.player_vs_better_ai(),
        }

        if mode in modes:
            modes[mode].play()
        else:
            break


if __name__ == "__main__":
    main()
