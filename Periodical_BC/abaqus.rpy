# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 6.13-1 replay file
# Internal Version: 2013_05_15-22.28.56 126354
# Run by zehaiwang on Mon Mar 07 23:57:46 2016
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=180.16667175293, 
    height=121.330726623535)
session.viewports['Viewport: 1'].makeCurrent()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
print 'RT script done'
#: RT script done