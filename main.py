import os
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic
app = QApplication(sys.argv)
# wait for device and show dialog


def wait_for_device():
    # load ui file

    ui_file = os.path.join(os.path.dirname(__file__), 'waitfordevice.ui')
    window = uic.loadUi(ui_file)
    # show dialog
    window.show()
    # os.system("adb wait-for-device")
    window.close()



def main():
    wait_for_device()
    ui_file = os.path.join(os.path.dirname(__file__), 'main.ui')
    window = uic.loadUi(ui_file)
    # set the title
    window.setWindowTitle("Debloat")
    # show window
    window.show()
    # run app
    window.device.setText("Device: " + os.popen("adb get-serialno").read())
    # add button click event
    def samsung():
        # debloat samsung
        window.Status.setText("Status: Downloading debloat script")
        # check os 
        if os.name == 'nt':
            os.system("curl -o debloat.bat https://raw.githubusercontent.com/khlam/debloat-samsung-android/master/commands.txt")
            # Open the input file in read mode
            with open('debloat.bat', 'r') as f:
                # Read all the lines in the file
                lines = f.readlines()

            # Open the output file in write mode
            with open('df.bat', 'w') as f:
                # Iterate over the lines
                for line in lines:
                    # Add the prefix to each line and write it to the output file
                    f.write('adb shell ' + line)
            
            window.Status.setText("Status: Debloating")
            os.system(".\df.bat")
        else:
            os.system("curl -o debloat.sh https://raw.githubusercontent.com/khlam/debloat-samsung-android/master/commands.txt")
            with open('debloat.bat', 'r') as f:
                # Read all the lines in the file
                lines = f.readlines()

            # Open the output file in write mode
            with open('df.bat', 'w') as f:
                f.write('#!/bin/bash')
                # Iterate over the lines
                for line in lines:
                    # Add the prefix to each line and write it to the output file
                    f.write('adb shell ' + line)
            window.Status.setText("Status: Debloating")
            os.system("bash debloat.sh")
    def realme():
        # debloat realme
        window.Status.setText("Status: Downloading debloat script")
        # check os 
        if os.name == 'nt':
            os.system("curl -o debloat.bat https://raw.githubusercontent.com/dumpydev/realme-ui-debloater/main/Windows%20Version/DebloatRealme.bat")
            window.Status.setText("Status: Debloating")
            os.system(".\debloat.bat")
        else:
            os.system("curl -o debloat.sh https://raw.githubusercontent.com/dumpydev/realme-ui-debloater/main/Linux%20Version/debloat.sh")
            window.Status.setText("Status: Debloating")
            os.system("bash debloat.sh")
    def credits():
        from PySide6.QtWidgets import QMessageBox
        msg = QMessageBox()
        msg.setWindowTitle("Credits")
        msg.setText("Made by Dumpy. \n\nSamsung debloat script by khlam\nRealme debloat script by realKarthikNair\nThanks to them for making the scripts.")

        msg.exec()

    window.Samsung.clicked.connect(lambda: samsung())
    window.Credits.clicked.connect(lambda: credits())
    window.Realme.clicked.connect(lambda: realme())
    sys.exit(app.exec())

main()
