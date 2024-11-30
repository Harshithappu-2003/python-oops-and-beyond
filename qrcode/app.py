# external dependencies
# python 3.9 - packages which are compatible with this version
# but not compatible other higher version
#venv
#python -m venv qr_env
#activating
# qr_env\Scripts\activate --- For Windows
# qr_env\Scripts\activate.ps1 --- For PowerShell
# source qr_env\Scripts\activate ---for linux/mac

#requirements.txt
# pip install -r requirements.txt --- it is used for installing the dependencies or packages which are typed in requirements.txtand to to install using that file

import pyqrcode
import png
link="https://www.linkedin.com/in/harshith-p-597968276/"
qr_code = pyqrcode.create(link)
qr_code.png("linkedin_qr.png", scale=6)  # save as png