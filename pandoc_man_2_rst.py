#/usr/bin/python3
#requires pandoc v3 for man input format
#point OVIS_ROOT to the build directory

import os
import glob

OVIS_ROOT='/opt/ovis/build/ovis'
for d in ['man','src/contrib/sampler/*','src/contrib/store/*','src/ldmsd/test/','src/sampler/*','src/store/*']:
    files = glob.glob(f'{OVIS_ROOT}/ldms/{d}/*man')
    for i in files:
        fname = i.split('/')[-1].replace('.man','.rst')
        #print(f'/usr/local/bin/pandoc -f man -s -t rst --toc {i} -o man2rst/{fname}')
        os.system('mkdir -p man2rst')
        os.system(f'/usr/local/bin/pandoc -f man -s -t rst --toc {i} -o man2rst/{fname}')