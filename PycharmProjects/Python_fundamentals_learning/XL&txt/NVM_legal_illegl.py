nvm = ['UGB30HH20256A1', 'VTDCFAPC256M-ECI', 'SFCF1024H1BO2TO-I-M0-543-ECI', 'SFCF1024H1BK2MT-I-MO-553-ECI',
        'TOSHIBA THNCF256MDG', 'ATP COMPACT FLASH', 'UGB30TSI0256A2', 'UTCF05THF', 'SimpleTech Flash', 'STI Flash 7.2.0',
        'SG9CF256HYB1A', 'SS9FD256H3B1CS01', 'VTDCFAPC256M-ECI', 'Delkin Devices', 'CE25MJBHS-X1000-5', 'MF0128M-07BT',
        'UTCF05THF', 'Tiger CF' ,'Virtium - VTDCFAPC256M-ECI']
model = "model"
f = open("C:/Users/ntatpuj/Desktop/scripts_small/NVM_legal_illegal.txt")
while True:
    line = f.readline()
    if line == "":
        break
    if model in line:
        nvm_name = line.split("=")[-1]
        nvm_name_1 = nvm_name.strip()
        print(nvm_name_1)
        print(nvm_name)
        if nvm_name_1 in nvm:
            print("Legal NVM")
        else:
            print("Illegal NVM")
