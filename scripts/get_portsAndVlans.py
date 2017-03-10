#!/usr/bin/env python
import json

"""
def main():
    portsAndVlans = [
        ('port-channel135', '20-24,40'),
        ('port-channel140', '20-24')
    ]
    print json.dumps(portsAndVlans)

    return portsAndVlans
"""

"""
{'port': 'port-channel135', 'portvlans': '20-24'},
{'port': 'port-channel145', 'portvlans': '20-24, 90'},
{'port': 'port-channel150', 'portvlans': '20-24'},
{'port': 'port-channel155', 'portvlans': '20-24'},
{'port': 'port-channel160', 'portvlans': '20-24'},
{'port': 'port-channel165', 'portvlans': '20-24'},
{'port': 'port-channel170', 'portvlans': '20-24'},
{'port': 'port-channel175', 'portvlans': '20-24'},
"""

def main():
    portsAndVlans = [
        {'port': 'port-channel125', 'portvlans': '20-24,40,159,160'},
        {'port': 'port-channel130', 'portvlans': '30-34,151'}
    ]
    print json.dumps(portsAndVlans)

    return portsAndVlans





if __name__ == '__main__':
    main()

