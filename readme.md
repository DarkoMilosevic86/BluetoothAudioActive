# Silenzio
* Silenzio is an NVDA add-on that keeps the sound card always active, which is essential for Bluetooth headphones or speakers.
* This is necessary because Bluetooth headphones or speakers may go into sleep mode after some time, causing sound interruptions.

# License
* Silenzio is protected under the [GPL 2](https://www.gnu.org/licenses/old-licenses/gpl-2.0.html) license.

# Installation
You can install Silenzio from the NVDA add-ons store or from the add-on's source page: [https://github.com/DarkoMilosevic86/Silenzio](https://github.com/DarkoMilosevic86/Silenzio).

# Usage
Silenzio can be toggled on and off using the Shift+NVDA+L key combination.  
Each time you enable or disable Silenzio, the setting will be automatically saved to the Silenzio configuration file. For example, if you leave Silenzio enabled and restart NVDA, it will remain enabled.

# Localization of the Silenzio add-on
The Silenzio add-on is available in English and Serbian.  
If you want to localize the Silenzio add-on, follow these steps:  
* Fork the repository [https://github.com/DarkoMilosevic86/Silenzio](https://github.com/DarkoMilosevic86/Silenzio).
* Clone the repository using the following command:
```cmd
git clone https://github.com/DarkoMilosevic86/Silenzio.git
```
* In the addon/locale folder, you will find the localization structure. Add the desired language and perform the translation.
* Push the changes to your copy of the Silenzio repository and create a pull request.
