import csv
import pyautogui
import time
import webbrowser
import argparse
import os.path

parser = argparse.ArgumentParser(description='Whatsapp Automation by Mohlet')
parser.add_argument('-f', '--file', metavar='File',required=True , help='Example --> data.csv ')
parser.add_argument('-m', '--message', metavar='Message',required=True, help='Example --> "Hello {} ."')
args = parser.parse_args()

def readCSV(file):
    with open(file, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            str = ', '.join(row)
            num = str.split(",")[1]
            messageTempl = args.message
            msg = messageTempl.format(str.split(",")[0])
            sendMessage(num, msg)
        pyautogui.hotkey("alt", "f4")

def sendMessage(number, message):
    webUrl = "https://web.whatsapp.com/send?phone={}".format(number)
    webbrowser.open(webUrl)
    time.sleep(7)
    pyautogui.typewrite('{}\n'.format(message), interval=0.1)
    time.sleep(3)

def checkCredentials():
    if os.path.exists(args.file) == False:
        print("File not exists. Shutting Down...")
        exit()
    else:
        msg = str(args.message)
        if msg.count("{}") != 1:
            print("Wrong message type. Shutting Down...")
            exit()
        else:
            readCSV(args.file)

checkCredentials()