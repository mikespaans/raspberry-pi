import bluetooth

TargetName = "iPhone van Mike"
DeviceFound = False


def DeviceSearch(PhoneName, TargetFind):
    # checken of er apparaten met bluetooth in de buurt zijn
    NearbyDevices = bluetooth.discover_devices()
    for Check in NearbyDevices:
        # kijken of de naam van de target overeen komt met de naam die het programma vindt
        if PhoneName == bluetooth.lookup_name(Check):
            TargetFind = True
    # als de naam overeen komt dan wordt er Iphone gevonden geprint
    if TargetFind == True:
        print ("Iphone gevonden")
        return True
    else:
        print ("Iphone niet gevonden")
        return False

DeviceSearch(TargetName, DeviceFound)