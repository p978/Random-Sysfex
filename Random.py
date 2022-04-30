import os
import random

Mycommands=["sysfex --ascii-path " + "ascii/cat.txt", 
"sysfex --ascii-path " + "ascii/arch.txt", 
"sysfex --ascii-path " + "ascii/tux.txt",
"sysfex --ascii-path " + "ascii/SUS.txt"]

execcmd = random.choice(Mycommands)

os.system(execcmd)