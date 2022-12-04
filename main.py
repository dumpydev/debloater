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
    os.system("adb wait-for-device")
    window.close()



def main():
    ui_file = os.path.join(os.path.dirname(__file__), 'main.ui')
    window = uic.loadUi(ui_file)
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
            os.system("curl -o debloat.bat https://raw.githubusercontent.com/invinciblevenom/debloat_samsung_android/main/adbdebloat.bat")
            window.Status.setText("Status: Debloating")
            os.system(".\debloat.bat")
        else:
            os.system("curl -o debloat.sh https://raw.githubusercontent.com/invinciblevenom/debloat_samsung_android/main/adbdebloat.sh")
            window.Status.setText("Status: Debloating")
            os.system("bash debloat.sh")
    def realme():
        # debloat realme
        window.Status.setText("Status: Downloading debloat script")
        # check os 
        if os.name == 'nt':
            os.system("curl -o debloat.bat https://raw.githubusercontent.com/realKarthikNair/realme-ui-debloater/main/Windows%20Version/DebloatRealme.bat")
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
        msg.setText("Made by Dumpy. \n\nSamsung debloat script by invinciblevenom\nRealme debloat script by realKarthikNair (linux slightly modified by dumpy.)")

        msg.exec()

    window.Samsung.clicked.connect(lambda: samsung())
    window.Credits.clicked.connect(lambda: credits())
    window.Realme.clicked.connect(lambda: realme())
    sys.exit(app.exec())
wait_for_device()
main()
