from dns import resolver, reversename
from dns.exception import *
import sys


ADR = None
VERBOSE = False
    
    
def assemble_dict(adr=None):
    ret = {}
    if adr != None:
        global ADR
        ADR = adr
        
    try:
        ret['ip'] = resolver.query(ADR)[0]
    except Timeout:
        print 'The query timed out.'
        sys.exit()
    except resolver.NXDOMAIN:
        print 'The requested Domain does not exist.'
        sys.exit()
    except resolver.NoAnswer:
        print 'Received empty answer.'
        sys.exit()
    except resolver.NoNameservers:
        print 'Could not find a working Nameserver to answer the query.'
        sys.exit()
    except Exception:
        print 'Unknown error'
        
    try:
        ret['server'] = resolver.query(reversename.from_address(ret['ip'].__str__()), 'PTR')[0]
    except Exception:
        ret['server'] = 'No name found.'
        
    if VERBOSE:
        try:
            ret['ns'] = resolver.query(ADR, 'NS')
        except Exception:
            ret['ns'] = ['None found.',]
            
        try:
            ret['mx'] = resolver.query(ADR, 'MX')
        except Exception:
            ret['ns'] = ['None found.',]
            
    return ret
    

def print_dict(res):
    print 'WEBINFO for %s\n' % ADR
    print 'IP:          %s' % res['ip'].__str__()
    print 'Server:      %s' % res['server'].__str__()
    
    if VERBOSE:
        print '\nNameserver:'
        for result in res['ns']:
            print result
    
        print '\nMail:'
        for result in res['mx']:
            print result


def cmd():
    global ADR
    if len(sys.argv) <= 1 or '--help' in sys.argv:
        print 'Usage: webinfo <domain> [-v]'
        sys.exit()
    ADR = sys.argv[1]
    if '-v' in sys.argv[1:]:
        VERBOSE = True
    
    res = assemble_dict()
    print_dict(res)
    
    
if __name__ == '__main__':
    cmd()
