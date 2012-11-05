#!/usr/bin/env python

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Use Latin Modern type 1 fonts
matplotlib.rcParams['ps.useafm'] = True
matplotlib.rcParams['pdf.use14corefonts'] = True
matplotlib.rcParams['text.usetex'] = True
matplotlib.rcParams['text.latex.preamble'] = '\usepackage[bitstream-charter]{mathdesign}'
matplotlib.rc('font',**{'family':'serif','serif':['Computer Modern']})

# Scaling on ORNL OLCF Jaguar (Cray XK6)
cray_x = np.array([32,64,128,256,512,1024,2048,4096,
                  8192,16384, 32768, 65536, 131072])
cray_y = np.array([69599, 140089, 276392, 558610, 1119110,
                   2232220, 4474940, 8910970, 17784500,
                   35604600, 71072600, 142213000, 282643000])
ideal_per_sec = 20.0*20000.0/183.73
cray_ideal = np.array([ideal_per_sec*nprocs for nprocs in cray_x])


# Scaling on ANL ALCF Intrepid (BlueGene/P)
bgp_x = np.array([4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096,
                  8192, 16384, 32768, 65536, 131072, 163840])
bgp_y = np.array([1578.45, 3140.03, 6252.14, 12558.3, 25018.3,
                  49718, 99393.3, 198267, 395558, 791765, 1581540,
                  3155620, 6308210, 12626800, 25177100, 50037000, 
                  62807000])
ideal_per_sec = 20.0*4000.0/198.12
bgp_ideal = np.array([ideal_per_sec*nprocs for nprocs in bgp_x])

plt.loglog(cray_x, cray_y, 'bo', label='Cray XK6 Observed')
plt.loglog(cray_x, cray_ideal, 'k--', label='Cray XK6 Ideal')
plt.loglog(bgp_x, bgp_y, 'ro', label='Blue Gene/P Observed')
plt.loglog(bgp_x, bgp_ideal, 'k-', label='Blue Gene/P Ideal')
plt.gca().set_xscale('log',basex=2)
plt.xlabel('Number of Processors', fontsize=16)
plt.ylabel('Particles per second', fontsize=16)
plt.grid(True, which='both')
plt.legend(loc='upper left')

# Save figure
#plt.show()
plt.savefig('scaling_loglog.pdf')
