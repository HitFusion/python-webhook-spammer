from discord import SyncWebhook

def send_message(webhook_url, message, sex):
    webhook = SyncWebhook.from_url(webhook_url)
    for _ in range(sex):
        webhook.send(message)
print("webhook bomber by hitfusion (0 effort)")

webhook_url = input("webhook link: ")
message = input("thing u want to send: ")
sex = int(input("number of messages you want: "))

send_message(webhook_url, message, sex)
