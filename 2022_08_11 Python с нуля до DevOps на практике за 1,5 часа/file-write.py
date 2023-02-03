from fileinput import close

#devices = []
#file = open("devices.txt", "a")

#for item in file:
#    item = item.strip()
#    devices.append(item)
#file.close()   

#print(devices)
 
newdevice = input("Input your divece name")
file = open("devices.txt", "a") 
file.seek(0, 2)       # перемещение курсора в конец файла
file.write('newdevice')  # собственно, запись
file.close()
