import os, sys
import platform
from PyQt4.QtGui import QDesktopServices

def isOSX():
    return sys.platform == "darwin"

def isWin32():
    return sys.platform == "win32"

def isLinux():
    return sys.platform.startswith("linux")

def isOSXBundle():
    return isOSX() and (os.path.abspath('.').find(".app") != -1)

def isOSXLeopard():
    return isOSX() and platform.mac_ver()[0].startswith("10.5")

def osVer():
    if isWin32():
        return " ".join(platform.win32_ver())
    elif isOSX():
        ver = platform.mac_ver();
        return " ".join((ver[0], " (", ver[2], ")"))
    elif isLinux():
        return " ".join(platform.linux_distribution())

def getDataDir():
    if isOSX():
        return os.path.join(str(QDesktopServices.storageLocation(QDesktopServices.DataLocation).toLatin1()), "Pesterchum/")
    elif isLinux():
        return os.path.join(str(QDesktopServices.storageLocation(QDesktopServices.HomeLocation).toLatin1()), ".pesterchum/")
    else:
        return os.path.join(str(QDesktopServices.storageLocation(QDesktopServices.DataLocation).toLatin1()), "pesterchum/")
