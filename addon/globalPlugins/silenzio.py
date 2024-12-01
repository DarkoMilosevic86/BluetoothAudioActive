# Copyright (C) 2024 Darko Milošević
# This file is covered by the GNU General Public License.
# See the file COPYING.txt for more details.



import os
import threading
import winsound
from time import sleep
from globalPluginHandler import GlobalPlugin
import json
import ui
from scriptHandler import script
import addonHandler

addonHandler.initTranslation()

def get_json_data():
    json_path = os.path.join(os.path.dirname(__file__), "silenzio.json")
    with open(json_path, "r") as file:
        data = json.load(file)
    return data

def set_json_data(data):
    json_path = os.path.join(os.path.dirname(__file__), "silenzio.json")
    with open(json_path, "w") as file:
        json.dump(data, file, indent=4)

def get_configuration():
    config_data = get_json_data()
    return config_data["enabled"]

def set_configuration(config_value):
    config_data = get_json_data()
    config_data["enabled"] = config_value
    set_json_data(config_data)

class GlobalPlugin(GlobalPlugin):

        
    def __init__(self):
        super().__init__()
        self.enabled = get_configuration()
        self.soundThread = None
        if self.enabled:
            self.startSound()

    def startSound(self):
        self.enabled = True
        if self.soundThread and self.soundThread.is_alive():
            return
        self.soundThread = threading.Thread(target=self._playSound, daemon=True)
        self.soundThread.start()

    def stopSound(self):
        self.enabled = False

    def _playSound(self):
        sound_path = os.path.join(os.path.dirname(__file__), "wav", "sound.wav")
        while self.enabled:
            winsound.PlaySound(sound_path, winsound.SND_FILENAME)
            sleep(0.1)

    # Translators : Script description
    @script(description=_("Toggle Silenzio On/Off."))
    def script_toggleSilenzio(self, gesture):
        if self.enabled:
            self.stopSound()
            set_configuration(self.enabled)
            # Translators: Message when Silenzio is disabled
            ui.message(_("Silenzio disabled"))
        else:
            # Translations: Message when Silenzio is enabled
            ui.message(_("Silenzio enabled"))
            self.startSound()
            set_configuration(self.enabled)



    __gestures = {
        "kb:NVDA+l": "toggleSilenzio"
    }
    def terminate(self):
        self.stopSound()
        super().terminate()
