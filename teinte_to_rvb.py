#!/usr/bin/env python3

# ( r=[0..1] , v=[0..1] , b=[0..1] ) = teinte_to_rvb( teinte=[0..360] )

def teinte_to_rvb(teinte):
    teinte /=360
    return (_v(teinte+1/3), _v(teinte), _v(teinte-1/3))

def _v(t):
    t = t % 1.0
    if t < (1/6):
        return t*6.0
    if t < 0.5:
        return 1
    if t < (2/3):
        return (2/3-t)*6.0
    return 0
