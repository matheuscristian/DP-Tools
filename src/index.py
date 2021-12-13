from message import Message
from printer import Printer
from configuration import Config
from os import system
from time import sleep
from pyautogui import typewrite, press
from threading import Thread

STOP = False
printer = Printer()

def title():
    system("clear")
    printer.print(" ######   ######       #######                                 ", "CYAN")
    printer.print(" #     #  #     #         #      ####    ####   #        ####  ", "CYAN")
    printer.print(" #     #  #     #         #     #    #  #    #  #       #      ", "CYAN")
    printer.print(" #     #  ######          #     #    #  #    #  #        ####  ", "CYAN")
    printer.print(" #     #  #               #     #    #  #    #  #            # ", "CYAN")
    printer.print(" #     #  #               #     #    #  #    #  #            # ", "CYAN")
    printer.print(" ######   #               #      ####    ####   ######   ####  ", "CYAN")
    printer.print("---------------------------------------------------------------", "RED")

def spammer(msg: str, config: Config):
    sleep(float(config.getValue("start_delay")))
    while True:
        global STOP
        if STOP:
            break
        for word in msg:
            typewrite(word)
            press("enter")
            sleep(float(config.getValue("spam_delay")))

def configureMenu():
    title()
    print("""1) spam_delay
2) start_delay
3) Back""")

def mainMenu():
    print("""1) Start spammer
2) Configure
3) Change message
4) Quit""")

def inputCall():
    title()
    ans = input("Enter new value: ")
    return ans

def main():
    config = Config("./dp.config")
    msg = Message("./message.txt")
    while True:
        global STOP
        title()
        mainMenu()
        ans = input("\nSelect option: ")
        if (ans == "1"):
            process = Thread(target=spammer, args=(msg.read(), config,))
            process.start()
            input("Press enter key to stop...")
            STOP = True
            quit(0)
        elif (ans == "2"):
            configureMenu()
            ans = input("\nSelect option: ")
            if (ans == "1"):
                ans = inputCall()
                config.setValue("spam_delay", ans)
            elif (ans == "2"):
                ans = inputCall()
                config.setValue("start_delay", ans)
            else:
                continue
            config.writeConfig()
        elif (ans == "3"):
            ans = inputCall()
            msg.write(ans)
        elif (ans == "4"):
            quit(0)
        else:
            continue

if __name__ == "__main__":
    main()