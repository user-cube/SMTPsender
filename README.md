# Gmail STMP Sending
A simple tool to send emails with your gmail account in python.

## Usage
To run this tool you should do:
```shell
$ python3 emailSend.py
```
Although this uses the default inputs:
```python3
parser = argparse.ArgumentParser()
parser.add_argument("--to", help="Recipient's Email", default="teste@teste.pt")
parser.add_argument("--sub", help="Email subject", default="Teste")
parser.add_argument("--text", help="Email content", default="Here is an email generated with python")
parser.add_argument("--spam", help="Number of emails to spam", default=1)
parser.add_argument("--email", help="Sender email", default="teste@gmail.com")
parser.add_argument("--pwd", help="Sender password", default="1234")
args = parser.parse_args()
```
```shell
usage: sendEmail.py [-h] [--to TO] [--sub SUB] [--text TEXT] [--spam SPAM]
                    [--email EMAIL] [--pwd PWD]
```
To change the default inputs you only have to run the program with the option you want:
```shell
$ python3 emailSend.py --sub "Example" --text "Email text" --email teste@user.pt --pwd defaultPWD
```
## Extra features
With my implementation is possible to spam a person with the spam email:
### Spam
An example of usage is:
```shell
$ python3 emailSend.py --sub "Example" --text "Email text" --email teste@user.pt --pwd defaultPWD --spam 70
```
This will send the email 70 times.
