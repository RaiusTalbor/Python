import os
import glob

anderedateien = os.listdir()
dateien = glob.glob("*.dat")

print(anderedateien)
print(dateien)