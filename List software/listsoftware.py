import winreg
print('support: t.me/WebSecExplorers')
a=winreg.ConnectRegistry(None,winreg.HKEY_LOCAL_MACHINE)
b=winreg.OpenKey(a,'SOFTWARE')
for key in range(100):
    try:
        c=winregEnumKey(b,key)
        print(c)
    except:
        break
