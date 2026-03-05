import Data
class Login_Section:
    def __init__(self):
        pass
    
    def ASK_AND_STORE(self):
        self.students = int(input("How many object are there?: "))
        for i in range(self.students):
            self.name = input(f"Enter the name of object {i}: ")
            self.id = input(f"Enter the ID of object {i} or you can create the ID: ")
            self.email = input(f"Enter the email of object{i}: ")
            # Store in Data.py
            Data.User_data_1.append({
                "Name": self.name,
                "ID": self.id,
                "Email": self.email
            })

            # Write data into Data.py
            with open("Data.py","w") as file:
                file.write("User_data_1 = [\n")
                for user in Data.User_data_1:
                    file.write("     {\n")
                    file.write(f"         'Name': '{user["Name"]}', \n")
                    file.write(f"         'ID': '{user["ID"]}', \n")
                    file.write(f"         'E-mail': '{user["Email"]}'\n")
                    file.write("     },\n")
                file.write("]\n")
        print("Your data succcess fully saved! Restart your software again for those changes.")

    def CLEAR_DATA(self):
        with open("Data.py", "w") as file:
            file.write("User_data_1 = []")
        print("Your data removed succcess fully! Restart your software again for those changes.")

