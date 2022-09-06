# kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi
# kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi
# kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi
import socket # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi
from time import sleep # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi
from os import system # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi
system("cls") # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi
m = "\033[1;31m"# kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi
h = "\033[1;32m"# kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi
k = "\033[1;33m"# kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi
r = "\033[1;39m"# kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi
c = "\033[1;36m"# kode dibuat oleh rofi # kode dibuat oleh rofi
print("""
""") # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi
while True: #kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi
  domain = input(f"{k}masukan domain {r}: {c}") # kode dibuat oleh rofi
  try: # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi
    ip_adress = socket.gethostbyname(domain) # kode dibuat oleh rofi # kode dibuat oleh rofi
  except socket.gaierror: # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi
    sleep(5) # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi
    print(f"{k}domain {r}: {c}{domain} {m}tidak ditemukan {r}") # kode dibuat oleh rofi
    sleep(3) # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi
    print(f"{k}ip address {r}: {h}0{r}\n") # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi
    break # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi
  except socket.herror: # kode dibuat oleh rofi # kode dibuat oleh rofi
    sleep(5) # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi
    print(f"{k}domain {r}: {c}{domain} {m}tidak ditemukan {r}") # kode dibuat oleh rofi
    sleep(3) # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi
    print(f"{k}ip address {r}: {h}0{r}\n") # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi
    break # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi
  else: # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi
    if ip_adress == "36.86.63.182": # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi
      sleep(5) # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi
      print(f"{k}domain {r}: {c}{domain} {m}tidak ditemukan {r}") # kode dibuat oleh rofi
      sleep(3)# kode dibuat oleh rofi# kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi
      print(f"{k}ip address {r}: {h}0{r}\n") # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi
      break # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi
    else: # kode dibuat oleh rofi # kode dibuat oleh rofi# kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi
      sleep(3) # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi
      print(f"{k}domain {r}: {c}{domain} {h}ditemukan {r}") # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi
      sleep(3)# kode dibuat oleh rofi# kode dibuat oleh rofi# kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi
      print(f"{k}ip address {r}: {h}{ip_adress}{r}\n") # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi
      break # kode dibuat oleh rofi # kode dibuat oleh rofi# kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi
# kode dibuat oleh rofi # kode dibuat oleh rofi# kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi
# kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi
# kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi # kode dibuat oleh rofi
