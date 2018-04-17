import win32com.client as win32

outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)

def emailer(message, subject, recipient, attachment):
    if recipient == "":
        mail.VotingOptions = "Approve; Reject"
    mail.To = recipient
    mail.Subject = subject
    if not "null" in attachment:
        if 'null' in list:
            mail.Attachments.Add(attachment)
        else:
            for item in attachment:
                mail.Attachments.Add(item)
    mail.GetInspector
    index = mail.HTMLbody.find('>', mail.HTMLbody.find('<body'))
    mail.HTMLbody = mail.HTMLbody[:index + 1] + message + mail.HTMLbody[index + 1:]
    mail.Send()