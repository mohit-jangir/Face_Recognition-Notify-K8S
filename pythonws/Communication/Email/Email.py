def Email():
    import smtplib
    import imghdr
    from email.message import EmailMessage
    from getpass import getpass

    Sender_Email = "mohitjangir.dev.testing@gmail.com"
    Reciever_Email = "mohitjangir700@gmail.com"
    Password = getpass('Enter your email account password: ')

    newMessage = EmailMessage()                         
    newMessage['Subject'] = "Python Notifier"
    newMessage['From'] = Sender_Email                 
    newMessage['To'] = Reciever_Email                   
    newMessage.set_content('Thanks For choosing our Python Notifier!!')             

    with open('/summer-2021-ws/test-img.png', 'rb') as f:
     image_data = f.read()
     image_type = imghdr.what(f.name)
     image_name = f.name

    newMessage.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
      smtp.login(Sender_Email, Password)              
      smtp.send_message(newMessage)

    print("\n\n Your E-mail sent successfully... ")
