import json

# configuration.json dosyasını açıp JSON verisini okuyalım
with open('configuration.json', 'r') as file:
    config = json.load(file)

# URL'leri, admin e-postasını ve hedef e-posta adreslerini alalım
urls = config['urls']
admin_email = config['admin']
destination_emails = config['destinationEmails']

# Alınan bilgileri ekrana basalım
print('URLs:', urls)
print('Admin Email:', admin_email)
print('Destination Emails:', destination_emails)