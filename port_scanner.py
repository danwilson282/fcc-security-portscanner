#!/usr/bin/python3
import socket
import common_ports as cp
import re

def get_open_ports(target, port_range, verbose=False):

    open_ports = []
    try:
        ip = socket.gethostbyname(target)
    except:
        #check if target is an ip address
        if re.search("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$", target):
            return "Error: Invalid IP address"
        else:
            return "Error: Invalid hostname"
    try:
        
        host_name = socket.gethostbyaddr(ip)[0]
    except:
        host_name=''
    if host_name=="":
        v_text = "Open ports for "+ip+"\n{:<9}{}\n".format("PORT", "SERVICE")
    else:
        v_text = "Open ports for "+host_name+" ("+ip+")\n{:<9}{}\n".format("PORT", "SERVICE")
    for i in range(port_range[0], port_range[1]+1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.3)
        if not s.connect_ex((ip, int(i))):
            open_ports.append(i)
            #v_text=v_text+str(i)+"     "+cp.ports_and_services[i]+"\n"
            v_text=v_text+"{:<9}{}\n".format(str(i),cp.ports_and_services[i])
        s.close()
    if verbose==True:
        v_text=v_text.rstrip()
        return v_text
    else:
        return(open_ports)

