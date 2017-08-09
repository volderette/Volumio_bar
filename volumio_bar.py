import rumps
import requests

class VolumioBar(rumps.App):

# Get meta data
    meta_json = {}
    title, artist, meta_info = "", "", ""
    meta_json = requests.get('http://volumio.local/api/v1/getstate').json()
    title = meta_json['title'] or ""
    artist = meta_json['artist'] or ""
    meta_info = artist + " - " + title

    @rumps.timer(2)
    def repeating_function(sender):
       meta  = requests.get('http://volumio.local/api/v1/getstate')
       title = meta_json['title'] or ""
       artist = meta_json['artist'] or ""
       meta_info = artist + " - " + title

    @rumps.clicked("▶ Play")
    def play(self, _):
        r = requests.get('http://volumio.local/api/v1/commands/?cmd=play')
    
    @rumps.clicked("❚❚ Pause")
    def pause(self, _):
        r = requests.get('http://volumio.local/api/v1/commands/?cmd=pause')

    @rumps.clicked("▲ Volume up")
    def volume_up(self, _):
        r = requests.get('http://volumio.local/api/v1/commands/?cmd=volume&volume=plus')

    @rumps.clicked("▼ Volume down")
    def volume_down(self, _):
        r = requests.get('http://volumio.local/api/v1/commands/?cmd=volume&volume=minus')



    @rumps.clicked("♫ Playing:")
    def meta(self, _):
        print()

    @rumps.clicked(meta_info)
    def meta(sender):
        sender.title = meta_info

if __name__ == "__main__":
    VolumioBar("▶︎").run()
