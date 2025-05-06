import shell.shell_math as shell_math
import shell.shell_shell as shell_shell
import os
import re

def input(ShellReserved0):
 
 words = re.findall(r'\b\w+\b', ShellReserved0)
 COUNT = len(words)

 if COUNT == 1:
    x=ShellReserved0
 else:
    x,y = ShellReserved0.split(" ",1)

#ImportantCMDs

 if x == "echo":
    shell_shell.echo(y)
 elif x == "cat":
    shell_shell.cat(y)
 elif x == "math":
    shell_math.math()
 elif x == "assign":
    shell_shell.assign()
 elif x == "addline":
    shell_shell.addline(y)
 elif x == "overwrite":
    shell_shell.overwrite(y)

#SystemShell
 elif x == "sys.sh":
    os.system(y)

#Help CMD
 elif x == "help":
    print("math,math.pi,echo,cat,addline,overwrite")

 else:
    print(x,"doesn't exist")
    print("Type help command for info")
