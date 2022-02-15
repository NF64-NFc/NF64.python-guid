import winreg

registry = winreg.HKEY_LOCAL_MACHINE
address = 'SOFTWARE\\Microsoft\\Cryptography'
key_args = winreg.KEY_READ | winreg.KEY_WOW64_64KEY
key = winreg.OpenKey(registry, address, 0, key_args)
value = winreg.QueryValueEx(key, 'MachineGuid')
winreg.CloseKey(key)

machineGuid = value[0]
print(machineGuid)
