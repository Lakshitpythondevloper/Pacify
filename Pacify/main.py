import Data
import smtplib
import Login_page
from Background import pacify, Login_logo
import prettytable
from email.message import EmailMessage
from pprint import pformat

def remove_data(Logout):
    Logout.CLEAR_DATA()

def Find_the_object():
    Programm = True
    while Programm:
        Object_found = None
        user_input = input("Type the ID of the object: ")
        for object in Data.User_data_1:
            if object['ID'] == user_input:
                datum = prettytable.PrettyTable()
                datum.field_names = ["ID","Name","Email"]
                datum.add_row([f"{object['ID']}",f"{object['Name']}",f"{object['E-mail']}"])
                print(datum)
                # Message
                Object_found = True
        if Object_found:
            print("I sucessfully found the object.")
            Programm = False
        else:
            print("\033[96m"+"Sorry! I could'nt find that object.Try again! ☹️"+"\033[0m")

def Edit_details():
    user_id = input("Enter the ID of the perosn you want to Edit: ")
    for person in Data.User_data_1:
        if person['ID'] == user_id:
                user_details = prettytable.PrettyTable()
                user_details.field_names = ["ID","Name","Email"]
                user_details.add_row([f"{person['ID']}",f"{person['Name']}",f"{person['E-mail']}"])
                print(user_details)
                user_id = input("Did you want to edit this object? (Y/N): ").lower()
                
                if user_id == "y":
                    user_name = input("Enter the name of object: ")
                    user_id = input("Enter th ID of object: ")
                    user_email = input("Enter the email of object: ")

                    #Editing the details
                    person['Name'] = user_name
                    person['ID'] = user_id
                    person['E-mail'] = user_email
                    print("All details success fully saved!")

                    with open("Data.py","w") as file:
                        file.write("User_data_1 = ")
                        file.write(pformat(Data.User_data_1))
                else:
                    print("Okay fine!")

def Email_all_obeject():
    #Warning table: -
    User_warning = prettytable.PrettyTable()
    User_warning.field_names = ["S.NO","Warning ⚠️"]
    User_warning.add_row(["1.","\033[91m"+"In this content you must have internet if internet is gone it may give error. Internet is  very important" + "\033[0m"])
    User_warning.add_row(["2.","\033[91m"+"Enter your email correctly and make sure you have an app password (From google)."+ "\033[0m"])
    User_warning.add_row(["3.","\033[91m"+"In this content onlt G-mail email IDs are working other will comming soon. In next update" + "\033[0m"])
    print(User_warning)

    #Information section: -
    Email = input("Enter your Gmail-ID please: ")
    message = input("Enter your long message here: ")
    Subject = input("Enter subject of your email please: ")
    App_password = input("Paste or write you app_password of google: ")
    # Connect to SMTP server
    try:
        server = smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login(Email, App_password)
        # Seding Data
        for user_sender in Data.User_data_1:
            msg = EmailMessage()
            msg["From"] = Email
            msg["To"] = user_sender["E-mail"]
            msg["Subject"] = Subject
            msg.set_content(message)
            server.send_message(msg)
            print(f"Email sent to ID: {user_sender['ID']}")
        # Message
        server.quit()
        print("Email sended succesfully!")
    except smtplib.socket.gaierror:
        print("\033[91m"+"Error: "+"\033[0m"+"An error is occured during this procces may be you type wrong email or your internet is not working. Try again later with proper internet and Email ID!")


def Email_specific_object():
     #Warning table: -
    User_warning = prettytable.PrettyTable()
    User_warning.field_names = ["S.NO","Warning ⚠️"]
    User_warning.add_row(["1.","\033[91m"+"In this content you must have internet if internet is gone it may give error. Internet is  very important" + "\033[0m"])
    User_warning.add_row(["2.","\033[91m"+"Enter your email correctly and make sure you have an app password (From google)."+ "\033[0m"])
    User_warning.add_row(["3.","\033[91m"+"In this content onlt G-mail email IDs are working other will comming soon. In next update" + "\033[0m"])
    print(User_warning)
    user_id = input("Enter the user ID which you want to E-mail: ")
    Object_found = False
    try:
        for datum in Data.User_data_1:
            if datum['ID'] == user_id:
                Object_found = True
                user_table = prettytable.PrettyTable()
                user_table.field_names = ["ID","Name","E-mail"]
                user_table.add_row([f"{datum['Name']}",f"{datum['ID']}",f"{datum['E-mail']}"])
                print(user_table)
                ask_user = input("Did you want to email this object? (Y/N): ").lower()

                if ask_user == "y":
                    Email = input("Enter you G-mail ID: ")
                    Subject = input("Enter the subject of your E-mail: ")
                    Content = input("Enter your long message here: ")
                    App_password = input("Paste or write you app_password of google: ")
                    To = datum["E-mail"]
                    ms = EmailMessage()
                    ms["From"] = Email
                    ms["To"] = To
                    ms["Subject"] = Subject
                    ms.set_content(Content)
            
                    server_1 = smtplib.SMTP("smtp.gmail.com",587)
                    server_1.starttls()
                    server_1.login(Email,App_password)
                    server_1.send_message(ms)
                    server_1.quit()
            else:
                print("I did'nt find the object please try again!")
                break
        if Object_found:
            print("Email is sended succesfully to the object!")
            print("\033[96m"+"Sorry! I could'nt find that object.Try again! ☹️"+"\033[0m")
    except smtplib.socket.gaierror:
        print("\033[91m"+"Error: "+"\033[0m"+"An error is occured during this procces may be you type wrong email or your internet is not working. Try again later with proper internet and Email ID!")

Login = Login_page.Login_Section()
print("\033[92m" + pacify + "\033[0m")
# Checking have a data or not: -
data_length = len(Data.User_data_1)

if data_length == 0:
    print("You have zero data on. You have to login to store data ⚠️")
    print(Login_logo)
    Login.ASK_AND_STORE()
else:
    print("Welcome to Pacify!")
    print("\033[95m" + f"Total object Data: {len(Data.User_data_1)}" + "\033[0m")
    table = prettytable.PrettyTable()
    table.field_names = ["Number","Options You have"]
    table.add_row(["1.","Remove the all data from your device."])
    table.add_row(["2.","E-mail all objects."])
    table.add_row(["3.","E-mail specifc object by ID."])
    table.add_row(["4.","Edit all the details on your data."])
    table.add_row(["5.","Find the object by his ID."])

    programm_running = True
    while programm_running:
        print(table)
        input_user = input("Type the option number from the tabel: ")
        # Controler: -
        if input_user == "1":
            remove_data(Login)
            programm_running = False
        elif input_user == "2":
            Email_all_obeject()
            programm_running = False
        elif input_user == "4":
            Edit_details()
        elif input_user == "5":
            Find_the_object()
            programm_running = False
        elif input_user == "3":
            Email_specific_object()
            programm_running = False
        else:
            print("Sorry! You type wrong option try again!")