import subprocess  
import re
def getSchedule(state):
   # res = subprocess.run('C:\Windows\System32\WindowsPowerShell\\v1.0\powershell.exe Get-GESchedule -State '+state, shell=True, capture_output=True, text=True)
    res = subprocess.run(["powershell", "-Command", 'Get-GESchedule -State '+state], shell=True, capture_output=True, text=True)

    ret = res.stdout
    ret = ret.replace(" ","").replace("\n","#").replace("##","\n")
    ret= re.sub(r"(\w)([A-Z])", r"\1 \2", ret)
    ret =ret[1:].split("\n")
    ret.pop()
    ret.pop()
    for i in range(len(ret)):
        ret[i] = ret[i].split("#")
        ret[i][len(ret[i])-1] = ret[i][len(ret[i])-1].replace(" ", "")
        ret[i].pop(5)

    return ret
