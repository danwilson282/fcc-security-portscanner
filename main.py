# This entrypoint file to be used in development. Start by reading README.md
import port_scanner
from unittest import main
import difflib

def test_diff(cases):
    for a,b in cases:     
        print('{} => {}'.format(a,b))  
        for i,s in enumerate(difflib.ndiff(a, b)):
            if s[0]==' ': continue
            elif s[0]=='-':
                print(u'Delete "{}" from position {}'.format(s[-1],i))
            elif s[0]=='+':
                print(u'Add "{}" to position {}'.format(s[-1],i))    
        print()  





# Called with URL
ports = port_scanner.get_open_ports("137.74.187.104", [440, 450], True)
print("Open ports:", ports)

# Called with ip address
ports = port_scanner.get_open_ports("104.26.10.78", [8079, 8090])
print("Open ports:", ports)

# Verbose called with ip address and no host name returned -- single open port
ports = port_scanner.get_open_ports("104.26.10.78", [440, 450], True)
print(ports + '\n')

# Verbose called with ip address and valid host name returned -- single open port
ports = port_scanner.get_open_ports("137.74.187.104", [440, 450], True)
print(ports + '\n')

# Verbose called with host name -- multiple ports returned
ports = port_scanner.get_open_ports("scanme.nmap.org", [20, 80], True)
print(ports + '\n')

# Run unit tests automatically
main(module='test_module', exit=False)

