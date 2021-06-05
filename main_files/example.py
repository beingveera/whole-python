
from win10toast import ToastNotifier 
import time 
toaster=ToastNotifier()
def alert():
    toaster.show_toast("Veera","You have to take rest...!!!!",threaded=True,icon_path=None,duration=10)
    while toaster.notification_active():
        time.sleep(0.1)

if __name__ == "__main__":
    alert()




'''
from plyer import notification 
notification.notify(
    title="Its me veera"
    message="now sleep ok..."
    app_icon=True
    timeout=10
)
'''