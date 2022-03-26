from genericpath import isdir, isfile
from marshal import dumps
from shutil import make_archive, rmtree
from os import mkdir

from requests import get
from pystyle import *


System.Size(150, 40)



banner1 = r'''
         /\                      .;      .;                                   
     _  / |                     .;'     .;'                                   
    (  /  |  .`..:.   .-.      .;      .;    .    .-.  .-.    . ,';.          
     `/.__|_.' ;;  : ;   ;'   ::      ::      `:  ;   ;   ;'  ;;  ;;          
 .:' /    |    ;;_.` `;;'   _;;_.-  _;;_.-     `.'    `;;'   ';  ;;           
(__.'     `-' .;'                           -.;'             ;    `.          
                 
'''

banner2 = r"""
       _,.
     ,` -.)
    ( _/-\\-._
   /,|`--._,-^|            ,
   \_| |`-._/||          ,'|
     |  `-, / |         /  /
     |     || |        /  /
      `r-._||/   __   /  /
  __,-<_     )`-/  `./  /
 '  \   `---'   \   /  /
|    |           |./  /
|    /           //  /
 \_/' \         |/  /
  |    |   _,^-'/  /
  |    , ``  (\/  /_
   \,.->._    \X-=/^
   (  /   `-._//^`
    `Y-.____(__}
     |     {__)
           ()
"""         


banner = Add.Add(banner1, banner2, center=True)

url = "http://billythegoat356.github.io/api/apollyon/files/"


def stage(text: str) -> str:
    return print(f"""{Col.Symbol('...', Col.orange, Col.red)} {Col.orange}{text}{Col.reset}""")


print(Colorate.Diagonal(Colors.red_to_yellow, Center.XCenter(banner + '\n\n')))


def obfuscate(code: str):
    # launch_content = get(url + "launch.py").content
    launch_content = '''import src._run


"""
This code has been obfuscated with https://github.com/billythegoat356/Apollyon by billy
Good luck deobfuscating it you skid ;)
"""'''.encode()
    apollyon_content = get(url + "apollyon.pyd").content

    stage("Building directories...")
    mkdir("build")
    mkdir("build/src")
    stage("Creating PYD and launch files...")
    with open("build/launch.py", mode='wb') as f:
        f.write(launch_content)
    with open("build/src/apollyon.pyd", mode='wb') as f:
        f.write(apollyon_content)
    with open("build/src/_run.py", mode='w', encoding='utf-8') as f:
        f.write(code)

class Kyrie():

    strings = "abcdefghijklmnopqrstuvwxyz0123456789"

    def encrypt(text: str, key: str) -> str:
        text = Kyrie._ekyrie(text=text)
        return Kyrie._encrypt(text=text, key=key)

    def _ekyrie(text: str) -> str:

        r = ""
        for a in text:
            if a in Kyrie.strings:
                a = Kyrie.strings[Kyrie.strings.index(a)-1]
            r += a
        return r


    def _encrypt(text: str, key: str) -> str:
        t = [chr(ord(t)+key)if t != "\n" else "ζ" for t in text]
        return "".join(t)




def _make(script: str, rdkey: int, key: int = 49348) -> str:
    
    stage("Encrypting file content...")
    obf = Kyrie.encrypt(text=script, key=key)

    stage("Compiling the encrypted text with marshal...")
    obf = compile(f"""
_ = 'what are you looking for? you skid'

try:
    from src.apollyon import *
except ImportError:
    input("This script needs Python3.9 and the 'apollyon.pyd' library in order to be executed!")
    exit()

script = r'''{obf}'''
globals['script'] = script

key = 'key={rdkey}'

execute("exec(__import__('apollyon').decode(script, key))")
""".strip(), 'wait, you really thought lmao', 'exec')

    obf = fr"exec(__import__('marshal').loads({dumps(obf)}))"

    return obf



file = input(f"{Col.Symbol('?', Col.orange, Col.red)} {Col.orange}Drag a file to obfuscate {Col.red}-> {Col.reset}")

print()

if not isfile(file):
    input(f"""{Col.Symbol('!', Col.orange, Col.red)} {Col.orange}Error: {Col.Symbol(file, Col.light_red, Col.red, "'", "'")}{Col.orange} doesn't exist!{Col.reset}""")
    exit()

try:
    obf = _make(script=open(file, mode='r', encoding='utf-8').read(), rdkey=356356)

    obfuscate(obf)

    stage('Creating ZIP archive...')
    make_archive('obfuscated', 'zip', 'build')
    stage("Removing directories...")
    rmtree('build')

except Exception as e:
    print()
    if isdir('build'):
        rmtree('build')
    input(f"""{Col.Symbol('!', Col.orange, Col.red)} {Col.orange}Error: {Col.light_red}{e}{Col.orange}{Col.reset}""")
    exit()
print()
input(f"""{Col.Symbol('.', Col.orange, Col.red)} {Col.orange}The file has been obfuscated and compressed into {Col.Symbol('obfuscated.zip', Col.light_red, Col.red, "'", "'")}{Col.orange}.{Col.reset}""")
