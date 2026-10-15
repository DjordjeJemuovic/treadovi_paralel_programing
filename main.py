import asyncio
import random
import subprocess
import threading
import webbrowser

from desktop_notifier import DesktopNotifier

mesages = ["Take a break", "Odmori malo", "Vreme je za odmor"]


async def reminder():
    notifier = DesktopNotifier(app_name="Moja aplikacija")
    while True:
        await notifier.send(title="Obavestenje", message=random.choice(mesages), timeout=5)
        await asyncio.sleep(20)


def reminder_nit():
    asyncio.run(reminder())


async def main():
    # poziv remindera preko niti
    treadReminder = threading.Thread(target=reminder_nit, daemon=True)
    treadReminder.start()

    subprocess.Popen(["code"])
    await asyncio.sleep(5)

    webbrowser.get("google-chrome").open("https://itskola.net")

    # drzi program zivim, jer je nit daemon
    while True:
        await asyncio.sleep(1)

asyncio.run(main())