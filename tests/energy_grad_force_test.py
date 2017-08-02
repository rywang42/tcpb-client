# Test for simple energy, gradient, and force calculation

import numpy as np
import os
import signal
import subprocess
import sys
import time

from tcpb import TCProtobufClient

from mock_server import MockServer


# JOB INPUT
h2o_system = {
    'atoms': ['O', 'H', 'H'],
    'geom': [0.00000,  0.00000, -0.12948,
             0.00000, -1.49419,  1.02744,
             0.00000,  1.49419,  1.02744],
    'method': 'pbe0',
    'basis': '6-31g',
    'charge': 0,
    'spinmult': 1,
    'closed': True,
    'restricted': True,
    }

# JOB OUTPUT
tol = 1e-5
h2o_energy = -76.300505
h2o_gradient = [[  0.0000002903,    0.0000000722,   -0.033101313],
                [ -0.0000000608,   -0.0141756697,    0.016550727],
                [ -0.0000002294,    0.0141755976,    0.016550585]]

# RUN TEST
def run_test(port=56789, run_real_server=False):
    """Run the test

    Args:
        port: Port to use for server and client in testing
        run_real_server: If True, we expect a real TCPB server and record a packet trace
                         If False, run the test with MockServer and the recorded packet trace
    Returns True if passed the tests, and False if failed the tests
    """
    # Set up MockServer for testing
    if not run_real_server:
        mock = MockServer(port, 'energy_grad_force/client_recv.bin', 'energy_grad_force/client_sent.bin')

    with TCProtobufClient(host='localhost', port=port, trace=run_real_server, **h2o_system) as TC:
        # Energy calculation
        energy = TC.compute_energy(h2o_system['geom'])
        if not np.allclose([h2o_energy], [energy], atol=tol):
            print('Failed energy test')
            return False

        # Gradient calculation
        energy, gradient = TC.compute_gradient(h2o_system['geom'])
        if not np.allclose([h2o_energy], [energy], atol=tol) or not np.allclose(h2o_gradient, gradient, atol=tol):
            print('Failed gradient test')
            return False

        # Force calculation
        energy, force = TC.compute_forces(h2o_system['geom'])
        if not np.allclose([h2o_energy], [energy], atol=tol) or not np.allclose(h2o_gradient, -force, atol=tol):
            print('Failed force test')
            return False

    return True

if __name__ == '__main__':
    run_test()
    #run_test(run_real_server=True)
