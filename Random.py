import os
import random

Mycommands=["sysfex --ascii-path " + "~/.config/sysfex/ascii/cat.txt", 
"sysfex --ascii-path " + "~/.config/sysfex/ascii/arch.txt", 
"sysfex --ascii-path " + "~/.config/sysfex/ascii/tux.txt",
"sysfex --ascii-path " + "~/.config/sysfex/ascii/SUS.txt"]

execcmd = random.choice(Mycommands)

os.system(execcmd)
