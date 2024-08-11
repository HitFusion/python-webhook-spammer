from discord import SyncWebhook
import threading

def send_message(webhook_url, message, count)
    webhook = SyncWebhook.from_url(webhook_url)
    for _ in range(count)
        webhook.send(message)

def threadprank(webhook_url, message, count, num_threads)
    threads = []
    mpt = count  num_threads
    for _ in range(num_threads)
        thread = threading.Thread(target=send_message, args=(webhook_url, message, mpt))
        thread.start()
        threads.append(thread)

    remaining = count % num_threads
    if remaining  0
        send_message(webhook_url, message, remaining)

    for thread in threads
        thread.join()

def main()
    print(webhook bomber by hitfusion (0 effort))
    webhook_url = input(webhook link )
    message = input(thing u want to send )
    count = int(input(number of messages you want ))

    usetheshit = input(Do you want to use threading (yesno) (Shit will prank) ).strip().lower()
    if usetheshit == 'yes'
        num_threads = int(input(Threads ))
        threadprank(webhook_url, message, count, num_threads)
    else
        send_message(webhook_url, message, count)

if __name__ == __main__
    main()
