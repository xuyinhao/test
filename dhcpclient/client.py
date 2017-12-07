# -*- coding: utf-8 -*-
import string,binascii,signal,sys,threading,socket,struct,getopt
from scapy.all import *
from scapy.arch.windows import compatibility
from scapy.arch.windows import *
compatibility.log_runtime = log_runtime
compatibility.MTU = MTU
compatibility.PcapTimeoutElapsed = PcapTimeoutElapsed
compatibility.ETH_P_ALL = ETH_P_ALL
compatibility.plist = plist
compatibility.time =time
# data = struct.pack('s'*8,'x','u','y',"h",'t','e','s','t')
# pkt = IP(src='13.10.13.16', dst='13.10.13.15')/TCP(sport=12345,dport=5555)/data
# send(pkt, inter=1, count=5)

interface = "Realtek PCIe GBE Family Controller"
conf.checkIPaddr = False
hostname=''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(8))
#m="52:54:00:ba:29:8b"
myxid=random.randint(1, 900000000)
#print(hostname)
#print(myxid)
#print(interact)

def unpackMAC(binmac):
    mac=binascii.hexlify(binmac)[0:12]
    blocks = [mac[x:x+2] for x in xrange(0, len(mac), 2)]
    return ':'.join(blocks)

class myThread(threading.Thread):
    def __init__(self,threadname):
            threading.Thread.__init__(self)
            self.macaddr = macaddr
    def run(self):
           # sniffer()
            dhcpclient(self.macaddr)

class sniffer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        spp=sniff(filter="udp and src port 67 and dst port 68 and src host 13.10.12.20",timeout=3) # prn=lambda x:x.show(),
       # spp.show()
       #  print('DHCP server mac: ', spp[0][Ether].src)
       #  print('DHCP server ip: ', spp[0][IP].src)
       #  print('MY Get  IP :',spp[0][BOOTP].yiaddr)
        #***********#
        try:
            localm = unpackMAC(spp[0][BOOTP].chaddr)
            interface = "Realtek PCIe GBE Family Controller"
            localxid=spp[0][BOOTP].xid
            sip=spp[0][BOOTP].siaddr
            myip=spp[0][BOOTP].yiaddr
            print("offer_get :")
            print(localxid,localm,sip,myip)
            dhcp_req = Ether(src=localm,dst="ff:ff:ff:ff:ff:ff") /\
                   IP(src="0.0.0.0",dst="255.255.255.255") /\
                   UDP(sport=68,dport=67) /\
                   BOOTP(chaddr=[mac2str(localm)],xid=localxid) /\
                   DHCP(options=[("message-type","request"),("server_id",sip),("requested_addr",myip),("hostname",hostname),("param_req_list","0"*255),"end"])

            print("sent DHCP Request for "+ myip)
            sendp(dhcp_req,verbose=0,iface=interface)
        except (IOError ,IndexError),e:
            print("Error:",e)
        finally:
            pass




def dhcpclient(macaddr):
    dhcp_discover =  Ether(src=macaddr,dst="ff:ff:ff:ff:ff:ff") /\
                     IP(src="0.0.0.0",dst="255.255.255.255") /\
                     UDP(sport=68,dport=67)  /\
                     BOOTP(chaddr=[mac2str(macaddr)],xid=myxid)  /\
                     DHCP(options=[("message-type","discover"),("hostname",hostname),"end"])
    print("\n\n\nSending DHCPDISCOVER on " + interface)
    sendp(dhcp_discover,verbose=0,iface=interface)
    # ans, unans = srp(dhcp_discover, multi=True)
    # ans.summary()
    time.sleep(2)

class sniffack(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        spp=sniff(filter="udp and src port 67 and dst port 68 and src host 13.10.12.20",timeout=5) #prn=lambda x:x.show(),
        #spp.show()
        # print('DHCP server mac: ', spp[2][Ether].src)
        # print('DHCP server ip: ', spp[2][IP].src)
        # print('MY Get  IP :',spp[2][BOOTP].yiaddr)
        try:
            ackmac = unpackMAC(spp[3][BOOTP].chaddr)
            ackxid=spp[3][BOOTP].xid
            acksip=spp[3][BOOTP].siaddr
            ackmyip=spp[3][BOOTP].yiaddr
           # options=spp[2]["DHCP options"].options
            print("ack_get : ")
            print(ackxid,ackmac,acksip,ackmyip)
        except (IOError ,IndexError),e:
            print("Error:",e)
        finally:
            pass
       # print(options)
    # dhcp_req = Ether(src=macaddr,dst="ff:ff:ff:ff:ff:ff")/\
    #            IP(src="0.0.0.0",dst="255.255.255.255")/\
    #            UDP(sport=68,dport=67)/\
    #            BOOTP(chaddr=[mac2str(macaddr)],xid=myxid)/\
    #            DHCP(options=[("message-type","request"),("server_id",sip),("requested_addr",),("hostname",hostname),("param_req_list","pad"),"end"])
    #       sendp(dhcp_req,verbose=0,iface=interface)
    #       print "sent DHCP Request for "+myip
 #   spp=sniff(filter="", prn=lambda x:x.show())
 #    if DHCP in spp:
 #        if spp[DHCP].options[0][1]==1:
 #            print('\tDetected DHCP Discover from client: ', spp[Ether].src)

threadt = 5
threads = []
lines=[]
f = open('macip20','r')
for line in open('macip20','r'):
    linemac=f.readline().split('|')[2]
    lines.append(linemac)
f.close()
print(lines[:])
for i in range(0,threadt):
    macaddr = lines[i]
   # macaddr="52:54:00:43:D5:7D"
   # threads.append(myThread(macaddr))
    t1=sniffer()    ##开启监控offer
    t1.start()
    t2=myThread(macaddr)        ##discover
    t2.start()
    # t3=sniffack()               ##ack 接受
    # t3.start()
    time.sleep(0.2)             ##两个等待

# for t in threads:
#     t.start()
# for t in threads:
#     t.join()

