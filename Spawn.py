!/usr/bin/env python3
from mcpi.minecraft import Minecraft
from mcpi import block

###########################################################
#
# Initialise the Village. A clearing is made in front of the player.
# A road is placed along the z axis with grass either side of it.
# The Minecraft connection is returned.
#
###########################################################
def init():
    mc = Minecraft.create()
    x, y, z = mc.player.getTilePos()
    return mc

###########################################################
def makeGold(mc, x, y, z):

    # Fill in each end of the roof
    mc.setBlocks(x-1, y, z-1, x+1, y+1, z+1, block.Stone.id)

mc = init()
x, y, z = mc.player.getTilePos()
makeGold(mc, x, y, z)


