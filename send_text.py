from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC6bd4e9606ea598d9f8aa25783293e3a7"
auth_token  = "618d624c4dfca5aabfb816c165beaf49"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Hello David!  This is David Teo!",
    to="+14254638741",    # Replace with your phone number
    from_="+14255239466") # Replace with your Twilio number
print message.sid
