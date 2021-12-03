import requests 
from requests.auth import HTTPDigestAuth
from getpass import getuser
from os import mkdir

system_user = getuser()
IPC_user = ""
IPC_password = ""
screenshots_path = "C:\\Users\\" + system_user + "\\screenshots\\"

mkdir(screenshots_path)

ip_dicc = {"baños-llenado":"172.30.3.31", "rampa-carga":"172.30.3.56", "llenado-hacia-dentro":"172.30.3.52"}


for name, ip in ip_dicc.items(): 
    resp = requests.get("http://" + ip + "cgi-bin/snapshot.cgi", auth=HTTPDigestAuth(IPC_user,IPC_password))
    open(screenshots_path + name + ".jpg").write(resp.content)


