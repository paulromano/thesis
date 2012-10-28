#!/usr/bin/env python

import csv
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Use Latin Modern type 1 fonts
matplotlib.rcParams['ps.useafm'] = True
matplotlib.rcParams['pdf.use14corefonts'] = True
matplotlib.rcParams['text.usetex'] = True
matplotlib.rcParams['text.latex.preamble'] = '\usepackage[bitstream-charter]{mathdesign}'
matplotlib.rc('font',**{'family':'serif','serif':['Computer Modern']})

procs = [16, 32, 64, 128, 256, 512]
ratio = [1, 3, 7, 15]
data = [240*2**i for i in range(7)]
overhead = {}

# Read Intrepid results
with open('data/results_intrepid.csv','r') as fh:
    reader = csv.reader(fh)
    for i, row in enumerate(reader):
        # Skip first eight rows
        if i < 8:
            continue

        # Get number of processors, servers, and amount of data
        p, r, d = map(int, (row[3], row[4], row[9]))
        overhead[p,r,d] = float(row[13][:-1])/100.

# Plot Intrepid results
for r in ratio:
    for p in procs:
        plt.loglog(data, [overhead[p,r,d] for d in data], '.-',
                   label='p={0}'.format(p))

    # Set plotting options
    plt.xlim([data[0],data[-1]])
    plt.xlabel('Data per event (bytes)', fontsize=16)
    plt.ylabel('Overhead per batch', fontsize=16)
    plt.grid(True, which='both')
    plt.legend(loc='upper left')
    # plt.show()
    plt.savefig('results_intrepid_r{0}.pdf'.format(r))
    plt.close()

for r in ratio:
    plt.loglog(procs, [overhead[p,r,15360] for p in procs], '.-',
               label='$c/s={0}$'.format(r))

# plt.xlim([procs[0],procs[-1]])
plt.xlabel('Number of processors, $p$', fontsize=16)
plt.ylabel('Overhead per batch', fontsize=16)
plt.gca().set_xscale('log',basex=2)
plt.gca().set_xticklabels([str(p) for p in procs])
plt.grid(True, which='both')
plt.legend(loc='upper left')
# plt.show()
plt.savefig('results_intrepid_cs.pdf')
