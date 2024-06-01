from telegram import Bot
import nmap
from getmac import get_mac_address
import asyncio

IP= '192.168.1.1'
KNOWN_DEVICES = []
chat_id = CHAT_ID = '-4069378436'
TELEGRAM_BOT_TOKEN = '6946135861:AAGTtOVEc7PmuLBtAPbWE5CkiBC_tY1ovNY'



# bot = Bot(token=TELEGRAM_BOT_TOKEN)

# async def send_telegram_messages(bot, chat_id):
#         for i in range(100):
#             sum = 1+i
#             print(sum)
#             await bot.send_message(chat_id = chat_id , text = sum)

# asyncio.run(send_telegram_messages(bot, CHAT_ID))





class networkscanner:
    def __init__(self,ip:str):
        self.ip = ip
        self.connected_devices = set()
    
    def scan(self):
        network = f"{self.ip}/24"
        nm= nmap.PortScanner()

        while True:
            nm.scan(hosts=network, arguments='-sn')
            host_list = nm.all_hosts()

            for host in host_list:
                mac = get_mac_address(ip=host)
                print(mac)

                if mac and mac not in self.connected_devices and mac not in KNOWN_DEVICES:
                    print(" New device found")
                    self.notify_new_devices(mac)
                    self.connected_devices.add(mac)

    async def send_telegram_messages(self, bot, chat_id, message):
        await bot.send_message(chat_id = chat_id , text = message)

    def notify_new_devices(self,mac):
        bot = Bot(token=TELEGRAM_BOT_TOKEN)
        asyncio.run(self.send_telegram_messages(bot, CHAT_ID, f"New device connected ! Mac address: {mac}"))


if __name__ == '__main__':
    scanner = networkscanner(IP)
    scanner.scan()




