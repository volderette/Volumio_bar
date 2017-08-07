import rumps
import requests

class VolumioBar(rumps.App):

# Get meta data
    meta_json = requests.get('http://volumio.local/api/v1/getstate').json()
    meta_title = "▶ "  + meta_json['artist'] + " - " + meta_json['title']

    @rumps.timer(2)
    def repeating_function(sender):
        meta  = requests.get('http://volumio.local/api/v1/getstate')
        meta_text = meta.text

    @rumps.clicked(meta_title)
    def meta(self, _):
        print()

    @rumps.clicked("▼ Volume down")
    def volume_down(self, _):
        r = requests.get('http://volumio.local/api/v1/commands/?cmd=volume&volume=minus')

    @rumps.clicked("▲ Volume up")
    def volume_up(self, _):
        r = requests.get('http://volumio.local/api/v1/commands/?cmd=volume&volume=plus')

if __name__ == "__main__":
    VolumioBar("▶︎").run()
