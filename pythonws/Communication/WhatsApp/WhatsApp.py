def WhatsApp():
    from twilio.rest import Client 
 
    account_sid = 'AC420c6f49479789b45004a678610b9e00' 
    auth_token = 'ea97be959bedc74f03ff750b882fedcc' 
    client = Client(account_sid, auth_token) 
 
    message = client.messages.create( 
       from_='whatsapp:+14155238886',
       body='Hello! This WhatsApp msg is sent by Python , Credits to Mohit...',
       media_url="http://71d1e6cb6705.ngrok.io/test-img.png",
       to='whatsapp:+917413924139' 
                          ) 
 
    print(message.sid)
    print("\n\n Your WhatsApp msg sent successfully... ")
