#!/usr/bin/env python
import sys
import json
from sqlalchemy.engine import create_engine



def getNovaSQL():
    """
    Get Nova Database Login Information
    :return: mysql_access string
    """
    novaConfFile = ''
    with open('/etc/nova/nova.conf', 'r') as file:
        for line in file:
            if 'sql_connection=mysql' in line:
                mysql_access = line.replace('sql_connection=', '')
    return mysql_access


def getHostsAndPorts():
    """
    :return: Dictionary with {'fqdn of the host': 'Port-channel on the Switch
     associated with the host'}
    """
    try:
        engine = create_engine(getNovaSQL(), echo=False)
        connection = engine.connect()
        result = connection.execute("""
                                    SELECT DISTINCT(
                                          compute_nodes.hypervisor_hostname),
                                          psvm_switchport_binding.switch_port
                                    FROM psvm_switchport_binding
                                    RIGHT JOIN compute_nodes
                                    ON psvm_switchport_binding.compute_node_id =
                                    compute_nodes.id ORDER BY switch_port
                                    """)
        connection.close()
    except:
        print "getHostsAndPorts - Error trying to create a mysql engine:"
        print "  - Check access to mysql"
        print "  - Check password in nova.conf"
    hostsAndPorts = {}
    for row in result:
        hostsAndPorts[row['hypervisor_hostname']] = row['switch_port']
    return hostsAndPorts

def getHostsAndVlans():
    """
    
    :return: List of tuples that contain ('fqdn of the host', 'vlan required
     to be trunked to the host')
    """
    try:
        engine = create_engine(getNovaSQL(), echo=False)
        connection = engine.connect()
        result = connection.execute("""
                                    SELECT instances.host, networks.vlan
                                    FROM instances
                                    LEFT JOIN networks ON
                                    instances.project_id = networks.project_id
                                    WHERE instances.deleted=0
                                    """)
        connection.close
    except:
        print "getHostsAndVlans - Error trying to create a mysql engine:"
        print "  - Check access to mysql"
        print "  - Check password in nova.conf"
    hostsAndVlans = []
    for row in result:
        hostsAndVlans.append((row['host'], int(row['vlan'])))
    return hostsAndVlans


def gen_HandV_dict():
    """
    
    :return: 
    """
    h_v = {}
    host_vlans = getHostsAndVlans()
    for host, vlan in host_vlans:
        if host in h_v:
            listval = h_v[host]
            if vlan in listval:
                continue
            else:
                listval.append(vlan)
                h_v[host] = listval
        else:
            h_v[host] = [vlan]
    return h_v


def gen_PSVM_JSON(global_vlans):
    """
    
    :return: 
    """
    hostsAndVlans = gen_HandV_dict()
    hostsAndPorts = getHostsAndPorts()
    psvm = []
    for host, vlans in hostsAndVlans.iteritems():
        vlanstr = ','.join(str(e) for e in sorted(vlans + global_vlans))
        hostport = hostsAndPorts[host]
        psvm.append({'port': hostport, 'portvlans': vlanstr})
    return psvm


def main():
    """
    
    :return:
    """
    global_vlans = []
    #for i in xrange(1, len(sys.argv)):
    #    required_vlans.append(sys.argv[i])
    if len(sys.argv) == 2:
        for i in sys.argv[1].split(','):
            try:
                i = int(i)
                global_vlans.append(i)
            except:
                print "Unable to parse {0}".format(i)
                pass
    psvm_data = gen_PSVM_JSON(global_vlans)
    print json.dumps(psvm_data, indent=4)
    return psvm_data


if __name__ == '__main__':
    main()

