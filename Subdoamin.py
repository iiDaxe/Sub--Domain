import requests
import re
from termcolor import cprint
logo = """
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'               `$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$  
$$$$$$$$$$$$$$$$$$$$$$$$$$$$'                   `$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$'`$$$$$$$$$$$$$'`$$$$$$!                       !$$$$$$'`$$$$$$$$$$$$$'`$$$
$$$$  $$$$$$$$$$$  $$$$$$$                         $$$$$$$  $$$$$$$$$$$  $$$$
$$$$. `$' \' \$`  $$$$$$$!      Find SubDoamin     !$$$$$$$  '$/ `/ `$' .$$$$
$$$$$. !\  i  i .$$$$$$$$         By Mr.Daxe        $$$$$$$$. i  i  /! .$$$$$
$$$$$$   `--`--.$$$$$$$$$             &             $$$$$$$$$.--'--'   $$$$$$
$$$$$$L        `$$$$$^^$$           Beroni          $$^^$$$$$'        J$$$$$$
$$$$$$$.   .'   ""~   $$$    $.                 .$  $$$   ~""   `.   .$$$$$$$
$$$$$$$$.  ;      .e$$$$$!    $$.             .$$  !$$$$$e,      ;  .$$$$$$$$
$$$$$$$$$   `.$$$$$$$$$$$$     $$$.         .$$$   $$$$$$$$$$$$.'   $$$$$$$$$
$$$$$$$$    .$$$$$$$$$$$$$!     $$`$$$$$$$$'$$    !$$$$$$$$$$$$$.    $$$$$$$$
$JT&yd$     $$$$$$$$$$$$$$$$.    $    $$    $   .$$$$$$$$$$$$$$$$     $by&TL$
                                 $    $$    $
                                 $.   $$   .$
                                 `$        $'
                                  `$$$$$$$$
"""
cprint(logo, 'cyan')
info = "Enter Your Target \n Ex : (google or yahoo ... ) ,\n Dont Write http/https and Dont write (.com) only Name For Your Target  "
print(" ")
cprint(info, 'blue')
print(" ")
target = input("Enter Your Target  :  ")
crf = "https://crt.sh/?q="
com = ".com"
url = crf + target + com
res = requests.get(url)
findtd = r'<TD>(.*)</TD>'
src = res.text
findl = re.findall(findtd, src)
findings = []
for found in findl:
    testing = found.lower()
    if "<br>" in testing:
        for splited in testing.split("<br>"):
            findings.append(splited)
with open('Subdomaint.txt', mode='w') as f:
    for found in findings:
        f.write(found + "\n")

print("*"*70)
cprint("                                            Done  .   ", 'white')
print("*"*70)
