import smtplib
import argparse

def connectAndSend(gmail__sender, GMAIL_PASSWD, TO, TEXT, SUBJECT, SPAM, PORT, SERVER):
    """

    Parameters
    ----------
    gmail__sender - Sender email
    GMAIL_PASSWD - Sender password
    TO - Recipient's Email
    TEXT - Email content
    SUBJECT - Email subject
    SPAM - Number of times to spam
    SERVER - SMTP Server
    PORT - Outgoing port

    Returns
    -------
    True - if the email was sent
    without any problems, otherwise
    false.

    """

    server = smtplib.SMTP(SERVER, PORT)
    server.ehlo()
    server.starttls()
    server.login(GMAIL_SENDER, GMAIL_PASSWD)

    BODY = '\r\n'.join(['To: %s' % TO,
                        'From: %s' % GMAIL_SENDER,
                        'Subject: %s' % SUBJECT,
                        '', TEXT])

    try:
        for i in range(0, SPAM):
            server.sendmail(GMAIL_SENDER, [TO], BODY)
            print(i)
            print("Email sent")
    except:
        print('Email not sent')
        server.quit()
        return False
    server.quit()
    return True

if __name__ == '__main__':
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--to", help="Recipient's Email", default="teste@teste.pt")
    parser.add_argument("--sub", help="Email subject", default="Teste")
    parser.add_argument("--text", help="Email content", default="Here is an email generated with python")
    parser.add_argument("--spam", help="Number of emails to spam", default=1)
    parser.add_argument("--email", help="Sender email", default="teste@gmail.com")
    parser.add_argument("--pwd", help="Sender password", default="1234")
    parser.add_argument("--server", help="SMTP Server", default="smtp.gmail.com")
    parser.add_argument("--port", help="Outgoing port", default="587")
    args = parser.parse_args()

    #Set parsed arguments
    GMAIL_SENDER = args.email
    if("@" not in GMAIL_SENDER):
        print("Not an email")
        exit()
    GMAIL_PASSWD = args.pwd
    TO = args.to
    SUBJECT = args.sub
    TEXT = args.text
    SERVER = args.server
    try:
        PORT = args.port
        PORT = int(PORT)
    except:
        print("Port value not a number")
    try:
        SPAM = args.spam
        SPAM = int(SPAM)
    except:
        print("Spam value not a number")

    connectAndSend(GMAIL_SENDER, GMAIL_PASSWD, TO, TEXT, SUBJECT, SPAM, PORT, SERVER)
