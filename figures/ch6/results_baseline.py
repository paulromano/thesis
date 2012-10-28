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

intrepid_d = np.zeros(7)
intrepid_mu = np.zeros(7)
titan_d = np.zeros(7)
titan_mu = np.zeros(7)

# Read Intrepid results
with open('data/results_intrepid.csv','r') as fh:
    reader = csv.reader(fh)
    for i, row in enumerate(reader):
        # Skip first eight rows
        if i < 1:
            continue
        elif i < 8:
            intrepid_d[i-1] = int(row[10])
            intrepid_mu[i-1] = float(row[12])/(2000*10)
        else:
            break

# Read Titan results
with open('data/results_titan.csv','r') as fh:
    reader = csv.reader(fh)
    for i, row in enumerate(reader):
        # Skip first eight rows
        if i < 1:
            continue
        elif i < 8:
            titan_d[i-1] = int(row[9])
            titan_mu[i-1] = float(row[11])/(2000*10)
        else:
            break

plt.plot(intrepid_d, intrepid_mu/intrepid_mu[0], 'o-', label='Intrepid')
plt.plot(titan_d, titan_mu/titan_mu[0], 'o-', label='Titan')
plt.xlabel('d (bytes)', fontsize=16)
plt.ylabel('$\mu/\mu_0$', fontsize=16)
plt.legend(loc='upper left')
plt.grid(which='both')
plt.savefig('results_baseline.pdf')
