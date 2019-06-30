import smtplib
import argparse


def connectAndSend(gmail__sender, gmail_passwd, TO, TEXT, SUBJECT, SPAM):

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_sender, gmail_passwd)

    BODY = '\r\n'.join(['To: %s' % TO,
                        'From: %s' % gmail_sender,
                        'Subject: %s' % SUBJECT,
                        '', TEXT])

    try:
        for i in range(0, SPAM):
            server.sendmail(gmail_sender, [TO], BODY)
            print(i)
            print("Email sent")
    except:
        print('Email not sent')
    server.quit()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--to", help="Recipient's Email", default="teste@teste.pt")
    parser.add_argument("--sub", help="Email subject", default="Teste")
    parser.add_argument("--text", help="Email content", default="Here is an email generated with python")
    parser.add_argument("--spam", help="Number of emails to spam", default=1)
    parser.add_argument("--email", help="Sender email", default="teste@gmail.com")
    parser.add_argument("--pwd", help="Sender password", default="1234")
    args = parser.parse_args()

    gmail_sender = args.email
    gmail_passwd = args.pwd
    TO = args.to
    SUBJECT = args.sub
    TEXT = args.text
    try:
        SPAM = args.spam
        SPAM = int(SPAM)
    except:
        print("Spam value not a number")

    connectAndSend(gmail_sender, gmail_passwd, TO, TEXT, SUBJECT, SPAM)
