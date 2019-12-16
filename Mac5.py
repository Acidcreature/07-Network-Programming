#!/usr/bin/env python

import subprocess

interface = input("interface > ")
new_mac = input("New Mac > ")

print("Changing Mac address: " + interface + " to " + new_mac)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])
subprocess.call(["ifconfig"])
