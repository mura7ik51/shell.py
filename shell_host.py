import shell.shell_backend as shell_backend
import shell.shell_about as shell_about

print("ShellPrompt By SMK")
print("Copyright 2025 SMK")

X=1
while X==1:
 ShellReserved0 = (input("ShellHost>>"))

 if ShellReserved0 == "exit":
  print("Exiting Shell")
  X+=1

 elif ShellReserved0 == "about":
  shell_about.about()
 
 elif ShellReserved0 =="":
  abcdefgh = 1

 else:
  shell_backend.input(ShellReserved0)
