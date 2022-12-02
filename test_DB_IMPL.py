import socket

from numpy import random

import SingularRecordingsDB
import time
import database

# myIPAddr = socket.gethostbyname(socket.gethostname())

# print("this " + myIPAddr + " is my IP address")

myhostname = socket.gethostname()

extendedIP = socket.gethostbyname_ex(myhostname)
print(extendedIP[2][len(extendedIP[2]) - 1])
