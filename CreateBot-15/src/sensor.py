'''
Created on Mar 17, 2015

@author: Botball
'''
import kovan as link
import constants as c
import time

def cameraTrack() :
    print "cameraTrack"
    link.camera_update()
    link.camera_update()
    time.sleep (0.5)
    link.camera_update()
    if link.get_object_area( c.chanGreen, 0 ) >= c.blobSize:
        print "green"
        print link.get_object_area( c.chanGreen, 0 )  
        
    elif link.get_object_area(c.chanRed, 0 ) >= c.blobSize:
        print "red"
        print link.get_object_area( c.chanRed, 0 )
        
    else:
        print "nothing found"
