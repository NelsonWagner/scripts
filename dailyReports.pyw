import win32com.client as win32

outlook = win32.Dispatch('outlook.application').GetNamespace("MAPI")
inbox = outlook.GetDefaultFolder('6').Folders('') # Put name of folder you're looking in if not the generic inbox
subject = "" # Subject line of email you're looking for
output = () # Where the script puts the attachment
reports = []

messages = inbox.Items
for message in messages:
    if subject in message.Subject:
        reports.append(message)
x = len(reports)
x -= 1

attachments = reports[x].Attachments
attachment = attachments.Item(1)
attachment.SaveASFile(output)