import datetime
import speech_recognition as sr
from colorama import init
from termcolor import colored
from simple_colors import *
import os
import random
import os
import pyttsx3
from fpdf import FPDF
init()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)
print("Say hey bank to activate you voice assistant")

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def greetme():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning Sir !")

    elif 12 <= hour < 18:
        speak("Good Afternoon Sir !")

    else:
        speak("Good Evening Sir !")

    assistant_name = "banker"
    speak("I am your Assistant")
    speak(assistant_name)
    speak('how may i help you ')

customerNames = ["Akshat Shah","Tattvam Shah","Harshit Sapra"]
customerNum=[1102,1101,1100]
customerPins = ['1111','2222','3333']
customerBalances = [100000,200000,300000]
customerLoans=[1000,5000,0]
remove_pin = random.randint(100000, 1000000)


def bill_generator(text): 
    file_name=input("Enter name with which you want to save: ")
    with open(f'{file_name}.txt', 'w') as f:
        f.write(text)
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size = 15)
    f = open(f"{file_name}.txt", "r")
    for x in f:
        pdf.cell(200, 10, txt = x, ln = 1, align = 'C')
    pdf.output(f"{file_name}.pdf")


class my_bank():
    def __init__(self):
        pass

    def create_account(self):
        print(cyan('You have selected to Create a New Account.', ['bright']))
        speak("You have selected to Create a New Account.")
        speak('enter your name')
        name = input("Input Fullname : ")
        customerNames.append(name)
        num = random.randint(1000, 10000)
        print(colored(f'Your account number is {num}', 'green'))
        speak(f'Your account number is {num}')
        customerNum.append(num)
        speak('Please input a password of your choice ')
        pin = input("Please input a password of your choice : ")        
        customerPins.append(pin)
        balance = 0
        speak('Please input a value to deposit to start an account')
        deposition = eval(input("Please input a value to deposit to start an account : "))        
        balance = balance + deposition
        customerBalances.append(balance)
        print(colored(f'An account was created in the name of {name}', 'green'))
        speak(f'An account was created in the name of {name}')
        customerLoans.append(int(0))
        while True:
            speak('Do you want a written statement for account opening, enter Y or N')
            xyz = input("Do you want a written statement for account opening, enter Y/N: ")
            if xyz.lower() == "y":
                o=datetime.datetime.now()
                n = f'         ----The India Bank---- \n\n                         {o}\n\n\nAn Account was opened In the name of {name}.\nAccount number:{num}\nBalance: {deposition}\n\n\n----Thank you for banking with us!----'
                bill_generator(n)
                break
            elif xyz.lower() == "n":
                print("Thank you for banking with us!")
                speak("Thank you for banking with us!")
                break
            else:
                print("Enter valid input")
                speak('"Enter valid input"')

    def withdraw(self):
        print(cyan('You have selected to Withdraw From An Account.', ['bright']))
        speak('You have selected to Withdraw From An Account')
        speak("Enter your account number ")
        a = int(input("Enter your account number : "))
        
        while True:
            if a in customerNum:
                speak('Enter amount to be withdrawn')
                amount = int(input("Enter amount to be withdrawn : "))                
                x = customerNum.index(a)
                speak('Enter your account password')
                passcode = str(input("Enter your account password : "))                
                if passcode == customerPins[x]:
                    if amount <= customerBalances[x]:
                        customerBalances[x] = customerBalances[x] - amount
                        print(colored('Successful!', 'green'))
                        speak('successful')
                        print(colored(f'Your new balance is : {customerBalances[x]}', 'red'))
                        speak(f'Your new balance is, {customerBalances[x]}')
                        while True:
                            speak('Do you want a written statement for account opening, enter Y or N:')
                            xyz = input("Do you want a written statement for account opening, enter Y/N: ")
                            if xyz.lower() == "y":
                                o=datetime.datetime.now()
                                n = f'         ----The India Bank---- \n\n                         {o}\n\n\nFor Account Number {customerNum[x]} a withdrawal of Rs.{amount} was made.\n\n\n----Thank you for banking with us!----'
                                bill_generator(n)
                                break
                            elif xyz.lower() == "n":
                                print("Thank you for banking with us!")
                                speak("Thank you for banking with us!")
                                break
                            else:
                                print("Enter valid input")
                                speak("Enter valid input")
                                break
                    else:
                        print(colored("Insufficient balance", 'red'))
                        speak("Insufficient balance")
                        break
                else:
                    print(colored("Incorrect Password. ", 'red'))
                    speak("Incorrect Password. ")
            else:
                print(colored("Enter valid account number. ", 'red'))
                speak("Enter valid account number. ")
                print(colored("No account with the given account number exists with us. ", "red"))
                break
            break

    def deposit(self):
        print(cyan('You have selected to Deposit To An Account.', ['bright']))
        speak('You have selected to Deposit To An Account.')
        while True:
            speak('Enter your account number')
            a = int(input("Enter your account number : "))            
            if a in customerNum:
                speak('Enter amount to be deposited')
                amount = int(input("Enter amount to be deposited : "))                
                x = customerNum.index(a)
                speak('Enter your account password')
                passcode = str(input("Enter your account password : "))                
                if passcode == customerPins[x]:
                    customerBalances[x] = customerBalances[x] + amount
                    print(colored('Successful!', 'green'))
                    speak('successful')
                    print(colored(f"Your current balance is : {customerBalances[x]}", "red"))
                    speak(f"Your current balance is : {customerBalances[x]}")
                    while True:
                        speak("Do you want a written statement for account opening, enter Y or N : ")
                        xyz = input("Do you want a written statement for account opening, enter Y/N : ")
                        if xyz.lower() == "y":
                            o=datetime.datetime.now()
                            n = f'         ----The India Bank---- \n\n                         {o}\n\n\nFor Account Number {customerNum[x]} a deposit of Rs.{amount} was made.\n\n\n----Thank you for banking with us!----'
                            bill_generator(n)
                            break
                        elif xyz.lower() == "n":
                            print("Thank you for banking with us!")
                            speak("Thank you for banking with us!")
                            break
                        else:
                            print("Enter valid input")
                            speak("Enter valid input")
                else:
                    print(colored("Incorrect Password. ", "red"))
                    speak("Incorrect Password. ")
            else:
                print(colored("Enter valid account number. ", "red"))
                speak("Enter valid account number. ")
                print(colored("No account with the given account number exists with us. ", "red"))
                speak('No account with the given account number exists with us. ')
                break
            break

    def check_details(self):
        print(cyan('You have selected to Check Account Details.', ['bright']))
        speak("You have selected to Check Account Details.")
        while True:
            speak('enter your account number')
            a = int(input("Enter your account number: "))            
            if a in customerNum:
                x = customerNum.index(a)
                speak('enter your account password:')
                passcode = str(input("Enter your account password: "))                
                if passcode == customerPins[x]:
                    print("__________________________________")
                    speak('These are your bank details ')
                    print(colored(f"Account Holder Name : {customerNames[x]}", "white"))
                    print(colored(f"Account Number : {customerNum[x]}", "white"))
                    print(colored(f"Account Balance : {customerBalances[x]}", "red"))
                    print(colored(f"Outstanding Loan : {customerLoans[x]}", "red"))
                    print("__________________________________")
                else:
                    print(colored("Incorrect Password. ", "red"))
                    speak('Incorrect Password. ')
            else:
                print(colored("Enter valid account number. ", "red"))
                speak("Enter valid account number. ",)
                print(colored("No account with the given account number exists with us. ", "red"))
                break
            break

    def loan(self):
        print(cyan('You have selected to Take A Loan.', ['bright']))
        speak('You have selected to Take A Loan.')
        speak('the terms and conditions are -')

        print("Terms and conditions:-")
        print("->  We offer a loan to all our customers at a rate of interest of 6%. ")
        print(
            "->  Time for repaying the loan will be between 12 to 24 months as per your requirement and accordingly EMIs will be calculated. ")
        print(
            "->  Maximum amount of the loan will be of which, a single installment's is already there in the account. ")
        print(
            "->  Incase of failure of paying any installment 1% of the loan will be directly deducted from your account balance. ")
        speak('1. We offer a loan to all our customers at a rate of interest of 6% , 2. Time for repaying the loan will be between 12 to 24 months as per your requirement and accordingly E M eyes will be calculated,'
              "3. Maximum amount of the loan will be of which, a single installment's is already there in the account, 4. Incase of failure of paying any installment 1% of the loan will be directly deducted from your account balance. ")

        speak("Enter your account number ")
        a = int(input("Enter your account number: "))
        
        speak("Enter amount you want loan for ")
        loan_amount = int(input("Enter amount you want loan for: "))
        
        speak("Enter duration of the loan in which all installments will be cleared  ")
        duration = int(input("Enter duration of the loan in which all installments will be cleared : "))
        
        while True:
            if a in customerNum:
                x = customerNum.index(a)
                speak("Enter your account password")
                passcode = str(input("Enter your account password: "))                
                if passcode == customerPins[x]:
                    l = (loan_amount * 1.06) / duration
                    if l < customerBalances[x]:
                        print(colored("Loan Passed. ", "green"))
                        speak('Your loan have been passed')
                        print("Each installment will be of: ", l)
                        speak("Each installment will be of: ", l)
                        customerBalances[x] = customerBalances[x] + loan_amount
                        overdue = loan_amount * 0.01
                        m = round(l, 2)
                        print(colored("In case of failure of payment of any installment a fee of Rs." + str(
                            overdue) + " will be charged.", "red"))
                        speak("In case of failure of payment of any installment a fee of Rs." + str(
                            overdue) + " will be charged.")
                        customerLoans[x] = customerLoans[x] + loan_amount
                        while True:
                            speak("Do you want a written statement for account opening, enter Y or N: ")
                            xyz = input("Do you want a written statement for account opening, enter Y/N: ")
                            if xyz.lower() == "y":
                                o=datetime.datetime.now()
                                n = f'         ----The India Bank---- \n\n                             {o}\n\n\nFor Account Number {customerNum[x]} a loan of Rs.{loan_amount} was passed.\nInstallments of Rs.{round(l, 2)} on {o.day}th of every month for {duration} months.\n\n\n----Thank you for banking with us!----'
                                bill_generator(n)
                                break
                            elif xyz.lower() == "n":
                                print("Thank you for banking with us!")
                                speak('Thank you for banking with us!')
                                break
                            else:
                                print("Enter valid input")
                                speak('Enter valid input')
                    else:
                        print(colored("Loan request denied. ", "red"))
                        speak("Loan request denied. ")
                else:
                    print(colored("Incorrect Password. ", "red"))
                    speak('"Incorrect Password.')
            else:
                print(colored("Enter valid account number. ", "red"))
                speak("Enter valid account number. ")
                print(colored("No account with the given account number exists with us. ", "red"))
                break
            break

    def overseas_transfers(self):
        print(cyan('You have selected to Make An Overseas Transfer. ', ['bright']))
        speak('You have selected to Make An Overseas Transfer')
        print("Terms and Conditions:-")
        speak('Terms and conditions are ')
        print("-> We levy a transaction fees of 2 percent on overseas transfer")
        print("-> Transaction time will be around 1-2 hours depending on the server load, please be patient.")
        print(
            "-> Please fill all the details including the overseas Bank account number carefully! Management is not responsible for the data you provide.")
        print("-> In case of any error from your side, notify us the details and we will try to rectify the issue.")
        speak('1.  We levy a transaction fees of 2 percent on overseas transfer, 2. Transaction time will be around 1-2 hours depending on the server load, please be patient'
              ', 3.  Please fill all the details including the overseas Bank account number carefully,  Management is not responsible for the data you provide, 4.  In case of any error from your side, notify us the details and we will try to rectify the issue')

        speak('Enter the country you want to transfer your funds')
        country = str(input('Enter the country you want to transfer your funds: '))
        
        speak('"Enter the name of the bank in your selected country')
        namebank = str(input("Enter the name of the bank in your selected country: "))
        
        speak('Enter account number to deposit')
        internationalacc = int(input("Enter account number to deposit: "))
        
        speak("Enter the amount you want to transfer to the specified account ")
        transferoff = int(input("Enter the amount you want to transfer to the specified account: "))
        
        fees = transferoff * 0.02
        final = transferoff - fees
        print("Transaction Fees: ", fees)
        speak("Transaction Fees is  ")
        speak(fees)
        print("Final amount :", final)
        speak('final amout is')
        speak(final)

        print(
            "Please recheck your input as the management will not be responsible for wrong information provided by the customer!")
        speak('Please recheck your input as the management will not be responsible for wrong information provided by the customer!')
        print("Country to transfer: ", country)
        speak('Country to transfer is')
        speak(country)
        print("Bank name: ", namebank)
        speak('bank name is')
        speak(namebank)
        print("Account number in specified bank: ", internationalacc)
        speak("Account number in specified bank is ")
        speak(internationalacc)
        print("Amount you want to transfer: ", transferoff)
        speak("Amount you want to transfer is")
        speak(transferoff)
        print("Transaction fees: ", fees)
        speak('transaction fees is')
        speak(fees)
        print("Final amount which will be transferred: ", final)
        speak('Final amount which will be transferred is ')
        speak(final)
        print("Do you wish to continue?")
        speak('do you wish to continue press y or n to responf')
        question = input("Press Y/N to respond \n")        
        if question.lower() == "n":
            return
        elif question.lower() == "y":
            print("Y acknowledged!")
            speak('Y acknowledged')
        else:
            print("Please enter valid option  ")
            speak("Please enter valid option ")
        while True:
            speak('input your account number')
            a = int(input("Input your account number: "))
            
            if a in customerNum:
                x = customerNum.index(a)
                speak('enter your account password')
                passcode = str(input("Enter your account password: "))                
                if passcode == customerPins[x]:
                    if transferoff < customerBalances[x]:
                        customerBalances[x] = customerBalances[x] - transferoff
                        print(colored(
                            "Funds transferred to the given bank details. Please wait for 1-2 hours for funds to show in the account statement of overseas account.",
                            "green"))
                        speak('Funds transferred to the given bank details. Please wait for 1-2 hours for funds to show in the account statement of overseas account')
                        print("Your new balance is: ", customerBalances[x])
                        speak("Your new balance is ")
                        speak(customerBalances[x])
                        while True:
                            speak("Do you want a written statement for account opening, enter Y or N")
                            xyz = input("Do you want a written statement for account opening, enter Y/N: ")                            
                            if xyz.lower() == "y":
                                o=datetime.datetime.now()
                                n = f'         ----The India Bank---- \n\n                             {o}\n\n\nFor Account Number {customerNum[x]} an overseas transfer to {internationalacc} at {namebank},{country}.\n\n\n----Thank you for banking with us!----'
                                bill_generator(n)
                                break
                            elif xyz.lower() == "n":
                                print("Thank you for banking with us!")
                                speak("Thank you for banking with us!")
                                break
                            else:
                                print("Enter valid input")
                                speak("Enter valid input")
                                break
                    else:
                        print(colored("Insufficient balance", "red"))
                        speak("Insufficient balance")
                        break
                else:
                    print(colored("Incorrect Password. ", "red"))
                    speak('Incorrect Password.')
            else:
                print(colored("Enter valid account number. ", "red"))
                speak('Enter valid account number.')
                print(colored("No account with the given account number exists with us. ", "red"))
                speak("No account with the given account number exists with us ")
                break
            break

    def money_transfer(self):
        print(cyan('You have selected to Transfer To Another Account.', ['bright']))
        speak('You have selected to Transfer To Another Account.')
        while True:
            speak("Enter your account number ")
            a = int(input("Enter your account number: "))            
            if a in customerNum:
                x = customerNum.index(a)
                speak("Enter your account pin ")
                passcode = str(input("Enter your account pin: "))             
                if passcode == customerPins[x]:
                    print("Account Holder Name: ", customerNames[x])
                    speak("Account Holder Name ")
                    speak( customerNames[x])
                    print("Account Balance: ", customerBalances[x])
                    speak("Account Balance is")
                    speak(customerBalances[x])
                    speak('enter the account number to which you wish to tranfer money to ')
                    c = int(input('enter the account number to which you wish to tranfer money to: '))                    
                    if c in customerNum:
                        g = customerNum.index(c)
                        speak('how much do you wish to transfer')
                        v = int(input('how much do you wish to transfer'))
                        if v <= customerBalances[x]:
                            customerBalances[x] = customerBalances[x] - v
                            customerBalances[g] = customerBalances[g] + v
                            print(colored("Successful!", "green"))
                            speak('successful')
                            print(colored(f'Your current balance is now: {customerBalances[x]}', 'red'))
                            speak(f'Your current balance is now: {customerBalances[x]}')
                            while True:
                                speak("Do you want a written statement for account opening, enter Y or N: ")
                                xyz = input("Do you want a written statement for account opening, enter Y/N: ")
                                if xyz.lower() == "y":
                                    speak("File name you want to save it as ")
                                    fileName = input("File name you want to save it as: ") + ".txt"
                                    o=datetime.datetime.now()
                                    n = f'         ----The India Bank---- \n\n                         {o}\n\n\nFor Account Number {customerNum[x]} a transfer of Rs.{v} to an Account Number {c} within our bank.\n\n\n----Thank you for banking with us!----'
                                    bill_generator(n)
                                    break
                                elif xyz.lower() == "n":
                                    print("Thank you for banking with us!")
                                    speak("Thank you for banking with us!")
                                    break
                                else:
                                    print("Enter valid input")
                                    speak('enter valid input')
                        else:
                            print(colored('insufficient bank balance', 'red'))
                            speak('insufficient bank balance')
                    else:
                        print(colored('no such account exists with us', 'red'))
                        speak('no such account exists with us')

                else:
                    print(colored("Incorrect Password. ", "red"))
                    speak('incorrect Password')
            else:
                print(colored("Enter valid account number. ", "red"))
                speak('enter valid account number')
                print(colored("No account with the given account number exists with us. ", "red"))
                break
            break

    def remove_account(self):
        print(cyan('You have selected to Remove An Account. ', ['bright']))
        print("You have selected to delete an account. ")
        speak("You have selected to delete an account ")
        print("To delete an account a pin will be generated and given to you. ")
        speak("To delete an account a pin will be generated and given to you ")
        speak('Enter the a pin generated by the bank')
        t = int(input("Enter the a pin generated by the bank: "))
        if t == remove_pin:
            while True:
                speak('Enter account number you want to delete')
                a = int(input("Enter account number you want to delete: "))
                if a in customerNum:
                    x = customerNum.index(a)
                    if customerLoans[x] != 0:                        
                        print("You have outstanding loan amount, please clear that before removing account. ")
                        speak("You have outstanding loan amount, please clear that before removing account. ")
                        print(f"Loan amount pending={customerLoans[x]}")
                        speak(f"Loan amount pending={customerLoans[x]}")
                        speak("Enter your pin ")
                        passcode = input("Enter your pin: ")
                        if passcode == customerPins[x]:
                            print(colored("Successful!", "green"))
                            speak('successful')
                            while True:
                                speak("Do you want a written statement for account opening, enter Y or N: ")
                                xyz = input("Do you want a written statement for account opening, enter Y/N: ")
                                if xyz.lower() == "y":
                                    o=datetime.datetime.now()
                                    n = f'         ----The India Bank---- \n\n                         {o}\n\n\nFor Account Number {customerNum[x]} was removed from our Bank.\n\n\n----Thank you for banking with us!----'
                                    bill_generator(n)
                                    break
                                elif xyz.lower() == "n":
                                    print("Thank you for banking with us!")
                                    speak('Thank you for banking with us')
                                    break
                                else:
                                    print("Enter valid input")
                                    speak('Enter valid input')
                                    break
                            customerNum.pop(x)
                            customerPins.pop(x)
                            customerBalances.pop(x)
                            customerLoans.pop(x)
                            customerNames.pop(x)
                            break
                        else:
                            print(colored("Incorrect PIn", "red"))
                            speak('incorrect pin')
                    else:
                        speak("Enter your pin" )
                        passcode = input("Enter your pin: ")
                        if passcode == customerPins[x]:
                            print(colored("Successful!", "green"))
                            speak('successful')
                            while True:
                                speak("Do you want a written statement for account opening, enter Y or N: ")
                                xyz = input("Do you want a written statement for account opening, enter Y/N: ")
                                if xyz.lower() == "y":
                                    o=datetime.datetime.now()
                                    n = f'         ----The India Bank---- \n\n                         {o}\n\n\nFor Account Number {customerNum[x]} was removed from our Bank.\n\n\n----Thank you for banking with us!----'
                                    bill_generator(n)
                                    customerNum.pop(x)
                                    customerPins.pop(x)
                                    customerBalances.pop(x)
                                    customerLoans.pop(x)
                                    customerNames.pop(x)
                                    break
                                elif xyz.lower() == "n":
                                    print("Thank you for banking with us!")
                                    speak("Thank you for banking with us!")
                                    customerNum.pop(x)
                                    customerPins.pop(x)
                                    customerBalances.pop(x)
                                    customerLoans.pop(x)
                                    customerNames.pop(x)
                                    break
                                else:
                                    print("Enter valid input")
                                    speak('enter valid input')

                        else:
                            print(colored("Incorrect PIn", "red"))
                            speak("Incorrect PIn")
                        break
                else:
                    print(colored("Incorrect account number. ", "red"))
                    speak("Incorrect account number. ")

    def repay_loan(self):
        print(cyan('You have selected for Repayment Of Loan.', ['bright']))
        speak('You have selected for Repayment Of Loan.')
        while True:
            speak("Enter Account number")
            a = int(input("Enter Account number: "))
            if a in customerNum:
                x = customerNum.index(a)
                speak("Enter your pin ")
                passcode = input("Enter your pin: ")
                if passcode == customerPins[x]:

                    if customerLoans[x] != 0:
                        print(f"Loan amount pending={customerLoans[x]}")
                        speak(print(f"Loan amount pending={customerLoans[x]}"))
                        while True:
                            speak("press 1 to clear your entire Loan from your balance\nPress 2 for Clear a certain amount of loans")
                            f = int(input(
                                'press 1 to clear your entire Loan from your balance\nPress 2 for Clear a certain amount of loan: '))
                            if f == 1:
                                customerBalances[x] = customerBalances[x] - customerLoans[x]
                                print('Loan paid, your current balance is: ', customerBalances[x])
                                speak('Loan paid, your current balance is ')
                                speak(customerBalances[x])
                                while True:
                                    speak("Do you want a written statement for account opening, enter Y or N: ")
                                    xyz = input("Do you want a written statement for account opening, enter Y/N: ")
                                    if xyz.lower() == "y":
                                        o=datetime.datetime.now()
                                        n=f'         ----The India Bank---- \n\n                         {o}\n\n\nFor Account Number {customerNum[x]} the loan amount{amount} was cleared.\n\n\n----Thank you for banking with us!----'
                                        bill_generator(n)
                                        break
                                    elif xyz.lower() == "n":
                                        print("Thank you for banking with us!")
                                        speak('Thank you for banking with us!')
                                        break
                                    else:
                                        print("Enter valid input")
                                        speak('enter valid input')
                            if f == 2:
                                speak("Enter amount you want to repay ")
                                amount = int(input("Enter amount you want to repay: "))
                                if amount <= customerBalances[x]:
                                    customerBalances[x] = customerBalances[x] - amount
                                    customerLoans[x] = customerLoans[x] + amount
                                    while True:
                                        speak("Do you want a written statement for account opening, enter Y or N: ")
                                        xyz = input("Do you want a written statement for account opening, enter Y/N: ")
                                        if xyz.lower() == "y":
                                            o=datetime.datetime.now()
                                            n = f'         ----The India Bank---- \n\n                         {o}\n\n\nFor Account Number {customerNum[x]} an installment of Rs.{amount} was cleared.\nOustanding Loan: {customerLoans[x]}\n\n\n----Thank you for banking with us!----'
                                            bill_generator(n)
                                            break
                                        elif xyz.lower() == "n":
                                            speak('thank you for banking with us')
                                            print("Thank you for banking with us!")
                                            break
                                        else:
                                            speak('enter valid input')
                                            print("Enter valid input")                                            
                                else:
                                    print(colored("Insufficent Balance", "red"))
                                    speak('insufficient balance')
                                    break
                            else:
                                print('exiting......')
                                break
                    else:
                        print('you have no exisiting loans')
                        speak('you havr no existing loans')
                        break
                else:
                    print('incorrect pin')
                    speak('incorrect pin ')
                    break
            else:
                print('invalid account number')
                speak('invalid account number')
                break


def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "None"

    return query


if __name__ == '__main__':
    def do_command():
        clear = lambda: os.system('cls')

        clear()
        greetme()
        while True:
            print("______________________________________")
            print(' |----' + blue('Welcome to The India Bank', ['italic']) + '----|')
            print("______________________________________")
            print("|->  1. Open a new account           |")
            print("|->  2. Withdraw Money               |")
            print("|->  3. Deposit Money                |")
            print("|->  4. Check Customer details       |")
            print("|->  5. Remove account               |")
            print("|->  6. Take loan                    |")
            print("|->  7. Repay Loan                   |")
            print("|->  8. Overseas Transfer            |")
            print("|->  9. Interaccount Transfers       |")
            print("|->  10. Exit                        |")
            print("|____________________________________|")

            query = takeCommand().lower()
            '''
            stored in query

            '''
            if 'new account' in query:
                my_bank.create_account(None)
                mainMenu = input("Please press enter key to go back to main menu to perform another function or exit ...")

            elif 'withdraw' in query:
                my_bank.withdraw(None)
                mainMenu = input("Please press enter key to go back to main menu to perform another function or exit ...")

            elif 'deposit' in query:
                my_bank.deposit(None)
                mainMenu = input("Please press enter key to go back to main menu to perform another function or exit ...")

            elif 'details' in query:
                my_bank.check_details(None)
                mainMenu = input("Please press enter key to go back to main menu to perform another function or exit ...")

            elif 'remove account' in query:

                print(colored(f'Your ONE TIME PIN is {remove_pin}', 'red'))
                my_bank.remove_account(None)
                mainMenu = input("Please press enter key to go back to main menu to perform another function or exit ...")

            elif 'take loan' in query:
                my_bank.loan(None)
                mainMenu = input("Please press enter key to go back to main menu to perform another function or exit ...")

            elif 'repay loan' in query:
                my_bank.repay_loan(None)
                mainMenu = input("Please press enter key to go back to main menu to perform another function or exit ...")

            elif 'overseas transfer' in query:
                my_bank.overseas_transfers(None)
                mainMenu = input("Please press enter key to go back to main menu to perform another function or exit ...")

            elif 'money transfer' in query:
                my_bank.money_transfer(None)
                mainMenu = input("Please press enter key to go back to main menu to perform another function or exit ...")

            elif 'exit' in query:
                print(blue('Thank You For Banking With Us.', ['bright']))
                exit()
                break

            else:
                print(colored("Enter a valid choice from the list. ", "red"))



    def listen():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)

        try:
            recog_speech = str(r.recognize_google(audio)).lower()
            print(recog_speech)

            if 'bank' in recog_speech:
                do_command()



        except Exception as e:
            print('i did not hear hey banker')

    while True:
        listen()
