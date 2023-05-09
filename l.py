import pyautogui as pag
import tkinter as tk
import time
import webbrowser

def open_notepad():
    # Open the Run dialog
    pag.hotkey('win', 'r')
    time.sleep(1)

    # Type "notepad" into the Run dialog and hit enter
    pag.typewrite('notepad')
    pag.press('enter')
    time.sleep(1)

    # Type "Hello World" into Notepad
    pag.typewrite('Hello World')

def spam():
    #Goto messenger text box
    pag.moveTo(752, 699)
    pag.click()
    time.sleep(1)
    pag.typewrite('Hello World, This is from my own spammer , i tried to make it myself (Devs > Me & ChatGPT)')
    pag.press('enter')

def spam2():
    # Ask for the text to spam
    try:
        spam_text = input("Enter the text to spam: ")
        if not spam_text:
            return
    except Exception as e:
        print(e)
        return

    # Ask for the number of times to spam the text
    try:
        num_spam = int(input("Enter the number of times to spam the text: "))
        if num_spam < 1:
            return
    except ValueError:
        print("Invalid input. Please enter a positive integer.")
        return

    #Goto messenger text box and spam
    try:
        pag.moveTo(752, 699)
        pag.click()
        time.sleep(1)
        for i in range(num_spam):
            pag.typewrite(spam_text)
            pag.press('enter')
    except Exception as e:
        print(e)

def open_messenger():
    # Open Messenger.com in Google Chrome
    webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s").open("https://messenger.com")
    
def exit_program():
    root.destroy()
    
    
    
def test():
    print('Hello. .... . .. .. ... ... . .. . . .. . .. . .. . . .. .. . . .. . .. ..')
    print(' ')
    print('Hello. .... . .. .. ... ... . .. . . .. . .. . .. . . .. .. . . .. . .. ..')
    print(' ')
    print('Hello. .... . .. .. ... ... . .. . . .. . .. . .. . . .. .. . . .. . .. ..')
    print(' ')
    print('Hello. .... . .. .. ... ... . .. . . .. . .. . .. . . .. .. . . .. . .. ..')
    print(' ')
    print('Hello. .... . .. .. ... ... . .. . . .. . .. . .. . . .. .. . . .. . .. ..')
    print(' ')
    print('Hello. .... . .. .. ... ... . .. . . .. . .. . .. . . .. .. . . .. . .. ..')
    print(' ')
    print('Hello. .... . .. .. ... ... . .. . . .. . .. . .. . . .. .. . . .. . .. ..')
    print(' ')
    print('Hello. .... . .. .. ... ... . .. . . .. . .. . .. . . .. .. . . .. . .. ..')
    print(' ')
    print('Hello. .... . .. .. ... ... . .. . . .. . .. . .. . . .. .. . . .. . .. ..')
    print(' ')
    print('Hello. .... . .. .. ... ... . .. . . .. . .. . .. . . .. .. . . .. . .. ..')
    print(' ')
    print('Hello. .... . .. .. ... ... . .. . . .. . .. . .. . . .. .. . . .. . .. ..')
    print(' ')
    print('Hello. .... . .. .. ... ... . .. . . .. . .. . .. . . .. .. . . .. . .. ..')
    print(' ')
    

# Create a simple Tkinter GUI with buttons to open Notepad and spam
root = tk.Tk()
root.geometry("350x200")
root.title('Kuy Spammer')
btn_open_notepad = tk.Button(root, text="Open Notepad", command=open_notepad)
btn_open_notepad.pack()
btn_spam = tk.Button(root, text="Spam on Messenger", command=spam)
btn_spam.pack()
btn_spam2 = tk.Button(root, text="Spam on Messenger (Custom Text)", command=spam2)
btn_spam2.pack()
btn_open_messenger = tk.Button(root, text="Open Messenger.com (CHROME ONLY)", command=open_messenger)
btn_open_messenger.pack()
btn_exit_program = tk.Button(root, text="Exit", command=exit)
btn_exit_program.pack()
btn_test = tk.Button(root, text="test", command=test)
btn_test.pack()


root.mainloop()
