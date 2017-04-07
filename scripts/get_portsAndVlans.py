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


def main():
    portsAndVlans = [
        {'port': 'port-channel100', 'portvlans': '130-139'},
        {'port': 'port-channel101', 'portvlans': '130-139'},
        {'port': 'port-channel102', 'portvlans': '130-139'},
        {'port': 'port-channel103', 'portvlans': '130-139'},
        {'port': 'port-channel104', 'portvlans': '130-139'},
        {'port': 'port-channel105', 'portvlans': '130-139'},
        {'port': 'port-channel106', 'portvlans': '130-139'},
        {'port': 'port-channel107', 'portvlans': '130-139'},
        {'port': 'port-channel108', 'portvlans': '130-139'},
        {'port': 'port-channel109', 'portvlans': '130-139'},
        {'port': 'port-channel110', 'portvlans': '130-139'},
        {'port': 'port-channel111', 'portvlans': '130-139'},
        {'port': 'port-channel112', 'portvlans': '130-139'},
        {'port': 'port-channel113', 'portvlans': '130-139'},
        {'port': 'port-channel114', 'portvlans': '130-139'},
        {'port': 'port-channel115', 'portvlans': '130-139'},
        {'port': 'port-channel116', 'portvlans': '130-139'},
        {'port': 'port-channel117', 'portvlans': '130-139'},
        {'port': 'port-channel118', 'portvlans': '130-139'},
        {'port': 'port-channel119', 'portvlans': '130-139'},
        {'port': 'port-channel120', 'portvlans': '130-139'},
        {'port': 'port-channel121', 'portvlans': '130-139'},
        {'port': 'port-channel122', 'portvlans': '130-139'},
        {'port': 'port-channel123', 'portvlans': '130-139'},
        {'port': 'port-channel124', 'portvlans': '130-139'},
        {'port': 'port-channel125', 'portvlans': '130-139'},
        {'port': 'port-channel126', 'portvlans': '130-139'},
        {'port': 'port-channel129', 'portvlans': '130-139'},
        {'port': 'port-channel130', 'portvlans': '130-139'},
        {'port': 'port-channel131', 'portvlans': '130-139'},
        {'port': 'port-channel132', 'portvlans': '130-139'},
        {'port': 'port-channel133', 'portvlans': '130-139'},
        {'port': 'port-channel134', 'portvlans': '130-139'},
        {'port': 'port-channel135', 'portvlans': '130-139'},
        {'port': 'port-channel136', 'portvlans': '130-139'},
        {'port': 'port-channel137', 'portvlans': '130-139'},
        {'port': 'port-channel138', 'portvlans': '130-139'},
        {'port': 'port-channel139', 'portvlans': '130-139'},
        {'port': 'port-channel140', 'portvlans': '130-139'},
        {'port': 'port-channel141', 'portvlans': '130-139'},
        {'port': 'port-channel142', 'portvlans': '130-139'},
        {'port': 'port-channel143', 'portvlans': '130-139'},
        {'port': 'port-channel144', 'portvlans': '130-139'},
        {'port': 'port-channel145', 'portvlans': '130-139'},
        {'port': 'port-channel146', 'portvlans': '130-139'},
        {'port': 'port-channel147', 'portvlans': '130-139'},
        {'port': 'port-channel148', 'portvlans': '130-139'},
        {'port': 'port-channel149', 'portvlans': '130-139'},
        {'port': 'port-channel150', 'portvlans': '130-139'},
        {'port': 'port-channel151', 'portvlans': '130-139'},
        {'port': 'port-channel152', 'portvlans': '130-139'},
        {'port': 'port-channel153', 'portvlans': '130-139'},
        {'port': 'port-channel154', 'portvlans': '130-139'},
        {'port': 'port-channel155', 'portvlans': '130-139'},
        {'port': 'port-channel156', 'portvlans': '130-139'},
        {'port': 'port-channel157', 'portvlans': '130-139'},
        {'port': 'port-channel158', 'portvlans': '130-139'},
        {'port': 'port-channel159', 'portvlans': '130-139'},
        {'port': 'port-channel160', 'portvlans': '130-139'},
        {'port': 'port-channel160', 'portvlans': '130-139'},
        {'port': 'port-channel161', 'portvlans': '130-139'},
        {'port': 'port-channel162', 'portvlans': '130-139'},
        {'port': 'port-channel163', 'portvlans': '130-139'},
        {'port': 'port-channel164', 'portvlans': '130-139'},
        {'port': 'port-channel165', 'portvlans': '130-139'},
        {'port': 'port-channel166', 'portvlans': '130-139'},
        {'port': 'port-channel167', 'portvlans': '130-139'},
        {'port': 'port-channel168', 'portvlans': '130-139'},
        {'port': 'port-channel169', 'portvlans': '130-139'},
        {'port': 'port-channel170', 'portvlans': '130-139'},
        {'port': 'port-channel171', 'portvlans': '130-139'},
        {'port': 'port-channel172', 'portvlans': '130-139'},
        {'port': 'port-channel173', 'portvlans': '130-139'},
        {'port': 'port-channel174', 'portvlans': '130-139'},
        {'port': 'port-channel175', 'portvlans': '130-139'},
        {'port': 'port-channel176', 'portvlans': '130-139'},
        {'port': 'port-channel177', 'portvlans': '130-139'},
        {'port': 'port-channel178', 'portvlans': '130-139'},
        {'port': 'port-channel179', 'portvlans': '130-139'},
        {'port': 'port-channel180', 'portvlans': '130-139'},
        {'port': 'port-channel181', 'portvlans': '130-139'},
        {'port': 'port-channel182', 'portvlans': '130-139'},
        {'port': 'port-channel183', 'portvlans': '130-139'},
        {'port': 'port-channel184', 'portvlans': '130-139'},
        {'port': 'port-channel185', 'portvlans': '130-139'},
        {'port': 'port-channel186', 'portvlans': '130-139'},
        {'port': 'port-channel187', 'portvlans': '130-139'},
        {'port': 'port-channel188', 'portvlans': '130-139'},
        {'port': 'port-channel189', 'portvlans': '130-139'},
        {'port': 'port-channel190', 'portvlans': '130-139'},
        {'port': 'port-channel191', 'portvlans': '130-139'},
        {'port': 'port-channel192', 'portvlans': '130-139'},
        {'port': 'port-channel193', 'portvlans': '130-139'},
        {'port': 'port-channel194', 'portvlans': '130-139'},
        {'port': 'port-channel195', 'portvlans': '130-139'},
        {'port': 'port-channel196', 'portvlans': '130-139'},
        {'port': 'port-channel197', 'portvlans': '130-139'},
        {'port': 'port-channel198', 'portvlans': '130-139'},
        {'port': 'port-channel199', 'portvlans': '130-139'},
        {'port': 'port-channel200', 'portvlans': '130-139'},
        {'port': 'port-channel201', 'portvlans': '130-139'},
        {'port': 'port-channel202', 'portvlans': '20-24,158-160'},
        {'port': 'port-channel203', 'portvlans': '130'},
        {'port': 'port-channel204', 'portvlans': '139'}
    ]
    print json.dumps(portsAndVlans)

    #return portsAndVlans





if __name__ == '__main__':
    main()

