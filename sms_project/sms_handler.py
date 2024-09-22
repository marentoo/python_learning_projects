from twilio.rest import Client


def send_msg():
    message_content = "Będzie padać dzisiaj. Weź parasolkę ☔"
    account_sid = ''
    auth_token = ""

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_ = '',
        body = message_content,
        to = ''
    )
    
    print(message.status)