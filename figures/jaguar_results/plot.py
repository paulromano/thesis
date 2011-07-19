#!/usr/bin/env python

import matplotlib.pyplot as pyplot

procs = [960,1920,3840,7680,15360]
nps = [40101808, 79675323, 151996979, 289912517, 600969298]
ideal = [20*160000000*2**i/77.4964 for i in range(5)]

pyplot.plot(procs,nps,'bo',label='Observed')
pyplot.plot(procs,ideal,'k-.',label='Ideal')
pyplot.xlabel('Processors')
pyplot.ylabel('Particles per second')
pyplot.grid(True)
pyplot.savefig('jaguar.eps', format='eps')
