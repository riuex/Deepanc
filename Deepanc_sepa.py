import numpy
import os
import option
import openslide
from openslide import open_slide,openslide



parser = OptionParser(usage = "usage% option <file>")
    parser.options("-L","--ignore-bound",dest = "limit_bounds"
        default = True ,action = "store_false"
        help = "this is the first option of the test")
    parsee.options("-s","--dont-get"
        default = False)

slide = OpenSlide("test.svs")
"""
#  this is opneslide reader of the testslide which the format is svs
testjpg = slide.read_region((0,0),0,slide.dimensions)
# this line is ignored
"""
