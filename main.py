import requests
import time
import pystyle
import os
import json
import fore
from pystyle import Colors, Colorate

def send_webhook_message(webhook_url, username, message, num_messages, cooldown, avatar_url=None):
    payload = {
        'username': username,
        'content': message,
        'avatar_url': avatar_url
    }
    print(Colorate.Horizontal(Colors.cyan_to_blue, """
    Spamming..."""))

    for _ in range(num_messages):
        requests.post(webhook_url, json=payload)
        time.sleep(cooldown)

    print(Colorate.Horizontal(Colors.cyan_to_blue, """
    Spamming done."""))

def delete_webhook(webhook_url):
    requests.delete(webhook_url)

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_webhook_info(webhook_url):
    try:
        response = requests.get(webhook_url)
        if response.status_code == 200:
            webhook_data = response.json()
            print(Colorate.Horizontal(Colors.cyan_to_blue, "Webhook Information:"))
            print(Colorate.Horizontal(Colors.cyan_to_blue, f"Webhook İsmi: {webhook_data['name']}"))
            print(Colorate.Horizontal(Colors.cyan_to_blue, f"Created by: {webhook_data['user']['username']}"))

            # Check if the webhook provides server (guild) and channel information
            if 'guild_id' in webhook_data and 'channel_id' in webhook_data:
                guild_id = webhook_data['guild_id']
                channel_id = webhook_data['channel_id']
                print(Colorate.Horizontal(Colors.cyan_to_blue, f"Server ID : {guild_id}"))
                print(Colorate.Horizontal(Colors.cyan_to_blue, f"Channel ID: {channel_id}"))
            else:
                print(Colorate.Horizontal(Colors.cyan_to_blue, "Server and Channel information not available."))
        else:
            print(Colorate.Horizontal(Colors.cyan_to_blue, "Unable to retrieve webhook information. Make sure the URL is correct."))
    except Exception as e:
        print(Colorate.Horizontal(Colors.cyan_to_blue, f"An error occurred: {str(e)}"))

def return_to_menu():
    input(Colorate.Horizontal(Colors.cyan_to_blue, "\nMenüye Dönmek İçin Entera Basınız"))
    clear_console()
    show_menu()

def exit_program():
    clear_console()
    print(Colorate.Horizontal(Colors.cyan_to_blue, "Programdan çıkma."))
    exit()

def show_menu():
    clear_console()
    print(Colorate.Horizontal(Colors.cyan_to_blue, """
╦ ╦╔═╗╔╗ ╦ ╦╔═╗╔═╗╦╔═  ╔╦╗╔═╗╔═╗╦  ╔═╗
║║║║╣ ╠╩╗╠═╣║ ║║ ║╠╩╗   ║ ║ ║║ ║║  ╚═╗
╚╩╝╚═╝╚═╝╩ ╩╚═╝╚═╝╩ ╩   ╩ ╚═╝╚═╝╩═╝╚═╝                            
"""))

    menu_choice = input(Colorate.Horizontal(Colors.cyan_to_blue, """
   (1) Webhook Spam     
   (2) Webhooku Sil
   (3) Webhook info
   (4) Quit
                                 
  Seçimini Gir : """))

    if menu_choice == "1":
        webhook_url = input(Colorate.Horizontal(Colors.cyan_to_blue, "Webhook URL: "))
        username = input(Colorate.Horizontal(Colors.cyan_to_blue, "Webhook Adı: "))
        message = input(Colorate.Horizontal(Colors.cyan_to_blue, "Mesaj: "))
        num_messages = int(input(Colorate.Horizontal(Colors.cyan_to_blue, "Kaç mesaj: ")))
        cooldown = int(input(Colorate.Horizontal(Colors.cyan_to_blue, "Bekleme Süresi (0 = Bekleme Süresi Yok): ")))
        avatar_url = input(Colorate.Horizontal(Colors.cyan_to_blue, "Avatar link: "))

        send_webhook_message(webhook_url, username, message, num_messages, cooldown, avatar_url)
        return_to_menu()

    elif menu_choice == "2":
        webhook_url = input(Colorate.Horizontal(Colors.cyan_to_blue, "Webhook URL: "))
        delete_webhook(webhook_url)
        print(Colorate.Horizontal(Colors.cyan_to_blue, "Webhook deleted."))
        return_to_menu()

    elif menu_choice == "3":
        webhook_url = input(Colorate.Horizontal(Colors.cyan_to_blue, "Webhook URL: "))
        get_webhook_info(webhook_url)
        return_to_menu()

    elif menu_choice == "4":
        exit_program()

    else:
        print(Colorate.Horizontal(Colors.cyan_to_blue, "Invalid choice."))
        return_to_menu()

# Start the program
show_menu()
