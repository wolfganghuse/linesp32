import network
import machine
import time
import urequests as requests

lan = network.LAN(mdc=machine.Pin(23), mdio=machine.Pin(18), ref_clk=machine.Pin(16), ref_clk_mode=False, power=None, id=None, phy_addr=0, phy_type=network.PHY_KSZ8081)
lan.active(True)
# by default (no parameters), ifconfig() will request IP from DHCP
ipconfig = lan.ifconfig()
# set fixed IP (address, netmask, gateway, dns)
#lan.ifconfig(('192.168.178.253', '255.255.255.0', '192.168.178.1', '192.168.178.1'))
while (ipconfig[0]=="0.0.0.0"):
    print ("Waiting for DHCP...")
    time.sleep(1)
    ipconfig = lan.ifconfig()
print ("Received config, IP {}, NM {}, GW {}, DNS {}".format(ipconfig[0],ipconfig[1],ipconfig[2],ipconfig[3]))

print ("Fetching www.example.com ...")
res = requests.get(url='https://www.example.com')
print(res.text)
