import sys,socket
from EnsoMetricsLib import EnsoAmpl, EnsoMu
import numpy as npy
#
# Wrapper of EnsoMetricsLib for testing
#
# Numpy initialisation
npy.set_printoptions(precision=2)

# Define model and simulation

# define where we are working
hostname = socket.gethostname()
if 'locean-ipsl.upmc.fr' in hostname:
    baseDir = '/Volumes/hciclad/data/Density_binning/'
elif 'waippo.local' in hostname:
    baseDir = '/Volumes/hciclad/data/Density_binning/'
elif 'private.ipsl.fr' in hostname:
    baseDir = '/prodigfs/project/CMIP5/main/IPSL/IPSL-CM5A-LR/historical/mon/atmos/Amon/r1i1p1/latest'
elif 'crunchy.llnl.gov' in hostname:
    baseDir = '/work/guilyardi/'
else:
    print hostname
    sys.exit('Unknown hostname')

# source activate PMP

# Variable name and nino box
sstName = 'ts'
ninoBox = 'nino3'
tauxName= 'tauu'

sstFile = baseDir+'/ts/ts_Amon_IPSL-CM5A-LR_historical_r1i1p1_185001-200512.nc'
tauxFile = baseDir+'/tauu/tauu_Amon_IPSL-CM5A-LR_historical_r1i1p1_185001-200512.nc'

print sstFile

# Call metrics calculation

# ENSO Amplitude
ensoAmpl = EnsoAmpl(sstFile, sstName, ninoBox)

print ensoAmpl['name']+':',ensoAmpl['value'],'('+ensoAmpl['units']+')'
print ensoAmpl['method']+' - (', ensoAmpl['nyears'],' years)'

# Mu
ensoMu = EnsoMu(sstFile, tauxFile, sstName, tauxName)

print ensoMu['name']+':',ensoMu['value'],'('+ensoMu['units']+')'
print ensoMu['method']+' - (', ensoMu['nyears'],' years)', ensoMu['intercept']
print 'Nonlinearity:',ensoMu['nonlinearity'],'('+ensoMu['units']+')'

EnsoMetrics =[{'col1':'IPSL-CM5A-LR','col2':ensoAmpl,'col3':ensoMu},
              {'col1':'IPSL-CM5A-MR','col2':ensoAmpl*2.,'col3':ensoMu*2}]

# -> ecrit dans/update/ajoute a fichier json avec Custom name

# Generate plot
#fig=EnsoMetricsTable(EnsoMetrics, 'EnsoMetrics')
