# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.message import EmailMessage


# Gmail Security Notes
'''In the case that you are sending emails through GMAIL,  just go to your account(gmail) -> Account setting -> Scroll to the bottom of the page and you see Less Secured Apps tab ,now you just have to turn that feature ON. for more info visit this:

Links Less Secured Apps : https://support.google.com/accounts/answer/6010255
Third party sites & apps: https://support.google.com/accounts/answer/3466521


The reason that Google blocks this is because they do not trust your "app". Google states:
Less secure apps & your Google Account: If an app or site doesn’t meet our security standards, Google might block anyone who’s trying to sign in to your account from it. Less secure apps can make it easier for hackers to get in to your account, so blocking sign-ins from these apps helps keep your account safe.


I recommend turning that feature back OFF once done experimenting with email in the next video since it is an extra security feature for your gmail account.'''

email = EmailMessage()
email['from'] = 'Navin Subramani'
email['to'] = ''  # Update the TO email
email['subject'] = "Learning Python on Udemy"
email.set_content('Zero to Mastery - I sent this email via Python3')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    # Update the FROM email and APP password
    smtp.login('', '')
    smtp.send_message(email)
