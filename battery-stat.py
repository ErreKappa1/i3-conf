#!/usr/bin/env python
from subprocess import check_output

ac_adaptor = str()
battery = str()

try:
    ac_adaptor = check_output(['acpi', '-a']).decode("utf-8")
    battery = check_output(['acpi', '-b']).decode("utf-8")
except FileNotFoundError:
    print(" install acpi")
    exit()


status = ""
if "on-line" in ac_adaptor:
    if battery is not "":
        status = " "
        battery_percentage = battery.split(' ')[3].replace(',', '  ').replace('\n', '')
        try:
            battery_lifetime = battery.split(' ')[4]
            status += battery_percentage + battery_lifetime
        except IndexError:
            status = " " + battery_percentage
else:
    battery_percentage = battery.split(' ')[3].replace(',', '  ')
    battery_value = int(battery_percentage.replace('%', ''))
    battery_lifetime = battery.split(' ')[4]
    status += (
        " " if battery_value > 75 else
        " " if battery_value > 40 else
        " " if battery_value > 20 else
        " "
    ) + battery_percentage + battery_lifetime

print(status)
