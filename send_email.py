import smtplib

ob = smtplib.SMTP('smtp.gmail.com',587) # gamil da port no 587 hai
ob.ehlo()
ob.starttls()

def mail():
    ob.login('ajay.kumar.695632@gmail.com', 'aezcewmrzbckzhnl')
    print("-" * 50)
    print(" <--> WelCome To Smart Mail sender <--> ")
    print("-" * 50)


    subject = input("Enter Subject = ")
    body = input("Type your Message = ")
    messsage = "subject:{}\n\n{}".format(subject, body)
    mail_list = input(r"Enter reciver mail or path of the file of maillist  = ")
    # listadd =[mail_list]

    if ".txt" in mail_list:
        file = open(mail_list, "r")
        for i in file:

        # or yeh bhi iski jagah use kar sskate hai by the niche wala jyda acha lag raha hai

            ob.sendmail('ajay.kumar.695632@gmail.com',i,messsage) #sendermail, recivermail,message

            print("send mail")

    else:
        list = [mail_list]
        ob.sendmail('ajay.kumar.695632@gmail.com', list, messsage)  # sendermail, recivermail,message

        print("send mail")
    ob.quit()

mail()

