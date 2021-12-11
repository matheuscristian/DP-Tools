from pyautogui import typewrite, press
from threading import Thread
from os import system
from time import sleep

STOP = False
config = {}

PATH = "."


def readconfig():
    conf = open(f"{PATH}/.config", "r", encoding="utf8")
    conf = conf.readlines()

    for data in conf:
        try:
            values = data.split("=")
            config[values[0]] = values[1]
        except:
            pass


def title():
    system("clear")
    print(" ######   ######       #######                                 ")
    print(" #     #  #     #         #      ####    ####   #        ####  ")
    print(" #     #  #     #         #     #    #  #    #  #       #      ")
    print(" #     #  ######          #     #    #  #    #  #        ####  ")
    print(" #     #  #               #     #    #  #    #  #            # ")
    print(" #     #  #               #     #    #  #    #  #            # ")
    print(" ######   #               #      ####    ####   ######   ####  ")
    print("---------------------------------------------------------------")


def start_spam():
    txt = open(f"{PATH}/message.txt", "r")
    txt = txt.readlines()

    sleep(float(config["delay_to_init"]))
    while True:
        if STOP:
            break
        for word in txt:
            typewrite(word)
            press("enter")
            sleep(float(config["spam_delay"]))


readconfig()


def main():
    global config, STOP

    title()

    ans = input("What do you want?\n\t1) Start spammer\n\t2) Configure\n\t3) Change message\n\t4) Quit (Please quit using this)\nAnswer: ")
    if (ans.lower() == "1"):
        process = Thread(target=start_spam)
        process.start()
        input("Press enter key to stop...")
        STOP = True
    elif (ans.lower() == "2"):
        title()
        ans = input(
            "Configuration Screen\n\t1) delay_to_init\n\t2) spam_delay\n\t3) Back\nAnswer: ")

        if (ans.lower() == "1"):
            title()
            ans = input("Enter new value to delay_to_init: ")

            config["delay_to_init"] = ans
        elif (ans.lower() == "2"):
            title()
            ans = input("Enter new value to spam_delay: ")

            config["spam_delay"] = ans
        else:
            main()

        conf = open(f"{PATH}/.config", "w")
        txt = ""
        for item in config:
            txt += item + "=" + config[item] + "\n"
        conf.write(txt)
        conf.close()
        main()
    elif (ans.lower() == "3"):
        message = open(f"{PATH}/message.txt", "w", encoding="utf8")
        ans = input("Enter new message: ")
        message.write(ans)
        message.close()
        main()
    else:
        exit()


main()
