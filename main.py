##-- INTERFADA --## 


## File Editor / Generator 


import os 
import sys
import colorama
from colorama import Fore, Back, Style
import time 


try: 
  def sellsex():
    print("This Is A File Editor (Replit).")
    global selection
    selection = input("Select An Option: (Create, Edit, Read, Delete, Mass Create, Hyper Goner): ")
    if selection == "Create":
      print(Fore.RED + "File Creator Selected" + Fore.RESET)
      createsex()
    elif selection == "Edit":
      print("File Editor Selected")
      editsex()
    elif selection == "Read":
      print("File Reader Selected")
      readsex()
    elif selection == "Delete":
      print(Fore.RED + "File Deleter Selected" + Fore.RESET)
      fileerase()
    elif selection == "Mass Create": 
      print("File Mass Creator Selected")
      gangbang()
    elif selection == "Hyper Goner":
      print(Fore.RED + "Hyper Goner Selected" + Fore.RESET)
      hypergoner()
    elif selection == "Kill":
      print("Termination Initiated....")
      sys.exit()
      ## sys.exit(0)
      print("Termination Failed")
    elif selection == "Error":
      tcause = "Trolling Error"
      try:
        raise NameError
      except NameError:
        (Fore.RED + "We Do A Bit Of Trolling" + Fore.RESET)
    else:
      print("Invalid Option")
      sellsex()
except: 
  print(Fore.RED + "Error 1422: An Exception Has Occured. Unknown Error Occured And Handled." + Fore.RESET)
  print(Fore.GREEN + "Reboot.Xela" + Fore.RESET)
  os.execl(sys.executable, sys.executable, *sys.argv)


try: 
  def createsex():
    try: 
      print(Fore.GREEN + "File Creator: " + Fore.RESET + "Enter Details Of File To Create")
      sexfell = input("Enter A File Name: ")
      sexfell2 = input("Enter The File's Contents: ")
      mattermake = open(sexfell + ".txt", "w")
      mattermake.write(sexfell2 + "\n")
      mattermake.close()
      opensubject = open(sexfell + ".txt", "r")
      print(opensubject.read() + " Is Your File Contents.")
    except:
      print(Fore.RED + "Error 1422: An Exception Has Occured. Unknown Error Occured And Handled." + Fore.RESET)
except: 
  print(Fore.RED + "Error 1422: An Exception Has Occured. Unknown Error Occured And Handled." + Fore.RESET)


def editsex():
  try: 
    print(Fore.GREEN + "File Editor: " + Fore.RESET + "Enter Details Of File To Edit")
    sexswap = input("Enter A File Name For Editing: ")
    sexswap2 = input("Enter The File's New Contents: ")
    matteredit = open(sexswap + ".txt", "w")
    matteredit.write(sexswap2 + "\n")
    matteredit.close()
    opensubject = open(sexswap + ".txt", "r") 
    print(opensubject.read() + " Is Your New File Contents.")
  except FileNotFoundError:
    error3119()
  except IOError:
    print(Fore.RED + "Error 1202: An Exception Has Occured. File Not Accessble Or File Not Found. (IOError)" + Fore.RESET)
    editsex()


def readsex():
  try:
    print(Fore.GREEN + "File Reader: " + Fore.RESET + "Enter Details Of File To Read")
    sexread = input("Enter A File Name To Read: ")
    matterread = open(sexread + ".txt", "r")
    print(matterread.read() + " Is Your File's Current Contents.")
    matterread.close()
  except FileNotFoundError:
    error3119()
  except IOError:
    print(Fore.RED + "Error 1202: An Exception Has Occured. File Not Accessble Or File Not Found. (IOError)" + Fore.RESET)
    readsex()


def fileerase(): 
  try: 
    print(Fore.RED + "File Deleter: " + Fore.RESET + "Enter Details Of Specimen To Erase")
    sexerase = input("Enter A File Name To Erase: ")
    sexerase2 = input("Enter The Specimen Type (.py, .txt, .exe): ") + ""
    mattererase = open(sexerase + sexerase2, "w")
    mattererase.write(" ")
    os.remove(sexerase + sexerase2)
    mattererase.close()
  except FileNotFoundError:
    error3119()
  except IOError:
    print(Fore.RED + "Error 1202: An Exception Has Occured. File Not Accessble Or File Not Found. (IOError)" + Fore.RESET)
    fileerase()


def gangbang():
  print(Fore.GREEN + "File Mass Creator: " + Fore.RESET + "Enter Details Of File To Mass Create")
  sexmass = input("Enter A File Name To Mass Create: ")
  sexmass1 = sexmass
  sexmass2 = input("Enter The File's Contents: ")
  halflife3 = input("How Much Of This File Do You Want To Create: (Integer) ")
  i = 0
  while i < int(halflife3):
    vamp = str(i)
    if i > 0:
      sexmass1 = sexmass + vamp
    mattermake = open(sexmass1 + ".txt", "w")
    mattermake.write(sexmass2 + "\n")
    mattermake.close()
    i += 1 


def hypergoner():
  print(Fore.YELLOW + "Hypergoner: " + Fore.RESET + "Enter Details Of Python File To Create")
  global sexpy
  global sexpy2 
  sexpy = input("Enter A File Name To Create: ")
  sexpy2 = input("Enter The File's Contents: ")
  matterpy = open(sexpy + ".py", "w")
  matterpy.write(sexpy2 + "\n")
  matterpy.close()
  opensubject = open(sexpy + ".py", "r")
  print("File Contents Include: \n" + opensubject.read())
  opensubject.close()
  time.sleep(1.5)
  print("Done!")
  quasisex = input("Do You Wish To Create More Lines? (Yes/No): ")
  if quasisex == "Yes":
    gb_spiral()
  if quasisex  == "No":
    print("Oh Ok.")
    running = input("Do You Wish To Run Your File? (Yes/No): ")
    if running == "Yes":
      matterpy.close()
      print("Running File....")
      time.sleep(1)
      exec(open(sexpy + ".py").read())
    elif running == "No":
      print("Oh Ok.")


def gb_spiral(): 
  quasi_details = input("Enter The Contents Of The Next Line: ")
  details = sexpy2 + " \n" + quasi_details
  matterispy = open(sexpy + ".py", "w")
  matterispy.write(details + "\n")
  quasirep = input("Do You Wish To Create More Lines? (Yes/No): ")
  if quasirep == "Yes":
    gb_spiral()
  elif quasirep == "No": 
    print("Oh Ok.")
    running = input("Do You Wish To Run Your File? (Yes/No): ")
    if running == "Yes":
      matterispy.close()
      print("Running File....")
      time.sleep(1)
      exec(open(sexpy + ".py").read())
    elif running == "No":
      print("Oh Ok.")





def error3119():
  print(Fore.RED + "Error 3119: An Exception Has Occured. File Does Not Exist (FileNotFoundError)" + Fore.RESET)
  print("Reloading....")
  time.sleep(4.44)
  if selection == "Edit":
    editsex()
  elif selection == "Read":
    readsex()
  elif selection == "Delete":
    fileerase()


sellsex()




