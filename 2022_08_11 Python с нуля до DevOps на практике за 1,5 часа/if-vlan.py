nativeVlan =  input("Input nativeVlan?")
dataVlan = input("Input dataVlan?")

if nativeVlan == dataVlan:
    print("The native VLAN and the data VLAN are the same")
else:
    print("The native VLAN and the data VLAN are different")