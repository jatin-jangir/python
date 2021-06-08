import time
from plyer import notification

if __name__=="__main__":
    while True:
        notification.notify(
            title="please drink water",
            message="we have to drink 15.5 cups of water that is 3.5 liters.",
            app_icon="C:\\Users\\jatin\\Desktop\\Pyhon\\icon.ico",
            timeout=10
        )
        time.sleep(60*60)
