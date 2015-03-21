'''
Created on Mar 17, 2015

@author: Botball
'''

import kovan as link

# globalconstants
isClone = 0

# servo ports
arm = 3
claw  = 1

# motor ports
grabber = 2 #arm that is lifts the grabby thingy
razr = 3

# servo positions
clawOpen = 0
clawClose = 2000

armDown = 1900
armMesa = 1100
armHeight = 780
armMid = 600
armUp = 510
armMidDown = 200 # for optimization
armBackMesa = 40 # 30 before


# analog ports


# digital ports
clonePort = 0 

# hard code for now, but will be clone switch
isClone = link.digital(15)
        

# define clone values here
if isClone:
    clawOpen = 0
    clawClose = 2000
    
    armDown = 1900
    armMesa = 1050
    armHeight = 780
    armMid = 600
    armUp = 510
    armMidDown = 200 # for optimization
    armBackMesa = 40 # 30 before
    
#isClone