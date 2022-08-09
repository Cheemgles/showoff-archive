from pathlib import Path
import pathlib 
import shelve
import os 
mode = input("Do you want to add or remove a reservation?:")
if mode == "add":
    name = "Name:" + input("Who is the reservation for?:")
    time = "Time:" + input("What time is the reservation for?:")
    file = open("Reservations.CSV", "a")
    file.write(name)
    file.write(",")
    file.write(time)
    file.write('\n')
elif mode == "remove":
     file = open("Reservations.CSV", "r")
     res_number = int(input("What reservation do you want to remove (In order added from first to last)?:"))
     reservations = file.readlines()
     blank = ""
     file.close()
     file = open("Reservations.CSV", "w")
     file.write(reservations[res_number])
     file.close
file = open("Reservations.CSV", "r")
reslist = file.readlines()
for i in enumerate(reslist):
    print(reslist[i[0]])
    


    



    


