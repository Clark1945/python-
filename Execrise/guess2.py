from guess import figure_guess
def run():
    computer=figure_guess()
    my=input("輸入選擇")
    if my == "A":
        print("A wins")

if __name__ == '__main__':
    for i in range(10):
        run()
