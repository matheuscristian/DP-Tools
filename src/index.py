from message import Message
from printer import Printer
from configuration import Config
from os import system
from time import sleep
from requests import post
from random import randint

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
    token = input("Enter token: ")
    channelID = input("Enter channel ID: ")
    nonce = randint(100000000000000000,999999999999999999)  # input("Enter nonce: ")
    msg = str(msg)
    while True:
        header = {
            "Authorization": token,
        }
        data = {
            "content": msg,
            "nonce": str(nonce),
            "tts": "false"
        }
        nonce += 1
        r = post(f"https://discord.com/api/v9/channels/{channelID}/messages",
                 headers=header, json=data)
        sleep(float(config.getValue("spam_delay")))

def configureMenu():
    title()
    print("""1) spam_delay
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
            print("CTRL + C to quit.")
            try:
                spammer(msg.read(), config)
            except:
                quit(0)
        elif (ans == "2"):
            configureMenu()
            ans = input("\nSelect option: ")
            if (ans == "1"):
                ans = inputCall()
                config.setValue("spam_delay", ans)
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