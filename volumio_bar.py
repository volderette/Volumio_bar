import rumps
import requests

class VolumioBar(rumps.App):

    @rumps.clicked("Volume down")
    def volume_down(self, _):
        r = requests.get('http://volumio.local/api/v1/commands/?cmd=volume&volume=minus')

    @rumps.clicked("Volume up")
    def volume_up(self, _):
        r = requests.get('http://volumio.local/api/v1/commands/?cmd=volume&volume=plus')

if __name__ == "__main__":
    VolumioBar("Volumio bar").run()
