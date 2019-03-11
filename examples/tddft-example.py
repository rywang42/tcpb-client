#!/usr/bin/env python
# Simple example showing a SA-CASSCF calculation

import sys
from tcpb import TCProtobufClient as TCPBClient

# Ethene system
atoms = ['C', 'C', 'H', 'H', 'H', 'H']
geom = [ 0.35673483, -0.05087227, -0.47786734,
         1.61445821, -0.06684947, -0.02916681,
        -0.14997206,  0.87780529, -0.62680155,
        -0.16786485, -0.95561368, -0.69426370,
         2.15270896,  0.84221076,  0.19314809,
         2.16553127, -0.97886933,  0.15232587]

if len(sys.argv) != 3:
    print('Usage: {} host port'.format(sys.argv[0]))
    exit(1)

with TCPBClient(host=sys.argv[1], port=int(sys.argv[2])) as TC:
    tddft_options = {
        'atoms':        atoms,
        'charge':       0,
        'spinmult':     1,
        'closed_shell': True,
        'restricted':   True,

        'method':       'wpbeh',
        'rc_w':         0.2,
        'basis':        '6-31g',

        'cis':          'yes',
        'cistarget':    1,
        'cisnumstates': 3,
        'cisrelaxdipole': 'yes',
        }

    results = TC.compute_job_sync("energy", geom, "bohr", **tddft_options)
    print results
