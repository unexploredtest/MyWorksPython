import smtplib

sender = "aaliPMPAINT@gmail.com"
reciever = "ali.PMPAINT@tutanota.com"
password = input("Enter The Password of aaliPMPAINT@gmail.com:")
massage = "My first mail via python."

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender, password)
print("Loged in")
server.sendmail(sender, reciever, massage)
print("Email recieved.")

server.quit()
