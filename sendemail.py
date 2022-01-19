import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import smtplib, ssl
from firebase import firebase
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import mimetypes
from email.mime.image import MIMEImage

# Fetch the service account key JSON file contents
cred = credentials.Certificate('email-48310-firebase-adminsdk-1w2m5-a78b953bdb.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://email-48310-default-rtdb.firebaseio.com/'
})

# As an admin, the app has access to read and write all data, regradless of Security Rules
ref = db.reference('email-48310-default-rtdb/emailstosend/')


snapshot = ref.order_by_child('address').get()
emailaddress = []

for key, val in snapshot.items():
    unparsed = ('{1}'.format(key, val))
    x = (unparsed.replace('}', '').replace('{', '').replace('address','').replace(':', '').replace("'", "").replace('"', "").replace(' ',''))
    emailaddress.append(x)

print("Would you like to send emails or enter emails into database?")
enterorsend = input("Type 'enter', 'send', or any other key to exit: ")

if enterorsend == 'send':
    for y in emailaddress:
        try:
            port = 465  # For SSL
            smtp_server = "smtp.gmail.com"
            sender_email = "seproj5@gmail.com"  # Enter your address
            receiver_email = y  # Enter receiver address
            password = "**********"
            message = MIMEMultipart("alternative")
            message["Subject"] = "We need to verify your account."
            message["From"] = sender_email
            message["To"] = receiver_email
            # write the plain text part
            text = """\
            Hi,
            
            We need to verify your spotify account. Click the link below to verfify your information
            http://localhost"""
            # write the HTML part
            html = """\
            <html>
    <head>
        <style>
            .logo {
                padding-top:20px;
                width: 200px;
            }
            .top {
                text-align: left;
            }
            .main {margin-left:auto; margin-right: auto; text-align: center; width: 750px;} 
            .submit {
                    color: rgb(255, 255, 255);
                    background-color: rgb(21, 136, 62);
                    border-bottom-color: rgba(0, 0, 0, 0);
                    border-bottom-style: solid;
                    border-bottom-width: 0px;
                    border-image-outset: 0;
                    border-image-repeat: stretch;
                    border-image-slice: 100%;
                    border-image-source: none;
                    border-image-width: 1;
                    border-left-color: rgba(0, 0, 0, 0);
                    border-left-style: solid;
                    border-left-width: 0px;
                    border-right-color: rgba(0, 0, 0, 0);
                    border-right-style: solid;
                    border-right-width: 0px;
                    border-top-color: rgba(0, 0, 0, 0);
                    border-top-style: solid;
                    border-top-width: 0px;
                    cursor: pointer;
                    padding: 16px 14px 18px;
                    border-radius: 500px; 
                    width: 50%;
                    text-transform: uppercase;
                    font-weight: 700;
                    font-size: 14px;
                    line-height: 1;
                    letter-spacing: 2px;
                    margin-top: 20px;
                    margin-left: auto;
                    margin-right: auto;
                    transition-property: background-color,border-color,color,box-shadow,filter;
                    transition-duration: .5s;
                    }

                    .submit:hover {
                        color: #fff;
                        background-color:#1db954;
                    }

                    .submit::after {
                        color: #fff;
                        background-color:#d8e2dc;
                    }
                
                .textbody{
                    text-align: left;
                }
                .line {
                    border: none;
                    height: 1px;
                    background: #DBDBDB;
                    margin-bottom: 30px;
                    margin-top: 3px;
                    }
                .line2 {
                    border: none;
                    height: 1px;
                    background: #adadad;
                    margin-bottom: 10px;
                    margin-top: 10px;
                }
                .bottom{
                    background-color: rgb(231, 231, 231);
                    padding-top: 10px;
                    padding-left: 30px;
                    padding-right: 30px;
                    padding-bottom: 20px;
                    text-align: left;
                }
                .bottomlogo{
                    width: 100px;
                    padding-top: 10px;
                    
                    padding-bottom: 3px;
                }
                .bottomtext{
                    text-align: left;
                    color: #918f8f;
                    
                }
                .bottomtext2{
                    text-align: left;
                    color: #918f8f;
                    padding-top:10px;
                    padding-bottom: 10px;
                }
                .bottomtext3{
                    text-align: left;
                    color: #918f8f;
                    padding-top: 20px;
                }

                .pic {
                    width: 750px;
                }
                
                
        </style>
    </head>
        <body>
            <div class="main">
            <img src = "cid:image1" class="pic">
                <form action="http://localhost">
                    <input type="submit" value="Verify Account" class="submit"/>
                </form>
            </p>
            <br>
            <br>
                <div class = "bottom">
                    <img src="cid:image2" class="bottomlogo">
                        <hr class="line2">
                    <p class ="bottomtext">Get Spotify For: <span style="color:#727272")>&nbsp;<b>iPhone</b> | <b>iPad</b> | <b>Android</b> |<b> Other</b></span></p>
                        <hr class="line2">
                    <p class ="bottomtext2">This email was sent to """ +str(y)+ """. If you have any questions or complaints, please <span style="color:#727272")><b>contact us.</b></span></p>
                    <p class ="bottomtext3"><span style="color:#727272")><b>Terms of Use</b> | <b>Privacy Policy</b> | <b>Contact Us</b></span></p>
                    <p class="bottomtext">Spotify USA, 4 World Trade Center, 150 Greenwich Street, 62nd Floor, New York, 10007, USA</p>
                </div>
            </div>
        </body>
</html>"""
            # convert both parts to MIMEText objects and add them to the MIMEMultipart message
            part1 = MIMEText(text, "plain")
            part2 = MIMEText(html, "html")
            message.attach(part1)
            message.attach(part2)

            fp = open('toppic.png', 'rb')
            msgImage = MIMEImage(fp.read())
            fp.close()

            msgImage.add_header('Content-ID', '<image1>')
            message.attach(msgImage)

            img2 = open('graylogo.png', 'rb')
            msgImage2 = MIMEImage(img2.read())
            img2.close()

            msgImage2.add_header('Content-ID', '<image2>')
            message.attach(msgImage2)

            print("sending emails to:", receiver_email)
            
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(
                sender_email, receiver_email, message.as_string()
    )
        except smtplib.SMTPException as e:
            print(e)
            print("error! email send failed!")

if enterorsend == 'enter':
    import addemail    

else:
    print("Goodbye")
    exit()


