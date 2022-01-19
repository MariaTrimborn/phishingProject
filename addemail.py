from firebase import firebase 
from firebase.firebase import FirebaseApplication

print("enter one email or list of emails from text document?: ")

userchoice= input("Enter 1 for one email or enter 2 for list of emails. Enter 3 to exit: ")

if userchoice == '1':
    enteraddress = input("Enter email address to add to database: ")

    firebase = firebase.FirebaseApplication('https://email-48310-default-rtdb.firebaseio.com/', None)  
    data =  { 'address': enteraddress  
                
            }  
    result = firebase.post('email-48310-default-rtdb/emailstosend',data)  
    print("email added.")

if userchoice == '2':
    while True: 
        try:
            file_loc = input("enter file path: ")
            openfile = open(file_loc)
            emailaddress = []
            
            for line in openfile:
                line = line.strip()
                emailaddress.append(line)

            for x in emailaddress:
                enteraddress = x
                firebase2 = firebase.FirebaseApplication('https://email-48310-default-rtdb.firebaseio.com/', None)  
                data =  { 'address': enteraddress  
                    
                }  
                result = firebase2.post('email-48310-default-rtdb/emailstosend',data)  
                print("adding: " + x)
            break    
        except FileNotFoundError:
            print("File not found! Make sure your input includes the extension of .txt. Try again")

if userchoice == '3':
    print("Exiting menu. Goodbye")
          
