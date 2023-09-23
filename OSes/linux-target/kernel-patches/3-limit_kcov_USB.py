import os


dir_list = ['sound/usb/', 'drivers/usb/', 'drivers/media/usb/', 'drivers/hid/','drivers/input/', 'drivers/net/', 'drivers/nfc/', 'drivers/staging/greybus/', 'drivers/staging/most/cdev/', 'drivers/staging/most/net/', 'drivers/staging/most/sound/', 'drivers/staging/most/usb/', 'drivers/staging/most/video/', 'drivers/staging/rtl8188eu/', 'drivers/staging/vt6656/', 'drivers/staging/wlan-ng/']

file_list = []
for i in dir_list:
    for root, dirs, files in os.walk(i):
        for file in files:
            file_path = os.path.join(root, file)
            if 'Makefile' in file_path:
                file_list.append(file_path)

for mf in file_list:
    print(mf)
    with open(mf, 'a', encoding='utf-8') as file:
        file.write('\nKCOV_INSTRUMENT := y\n')
