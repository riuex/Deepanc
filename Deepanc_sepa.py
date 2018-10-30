import numpy
import os
from optparse import OptionParser
import openslide
from openslide import open_slide,openslide
#this package is need to read SVSfiles.
from multiprocessing import pool
import multiprocessing as multi
#this package is need to make multitask possible



#to make process of sepalating Unit
def convert(data,args.pixel):
    pixel = args.pixel
    UNIT_X,UNIT_Y = pixel,pixel
    try:
        fname,f_input,f_output = data
        save_name = fname.split(".")[0] + ".jpg"
        print("processing : " + fname)
        simage = OpenSlide(f_input + "/" + fname)
        w,h = simage.dimensions
        w_rep,h_rep = int(w//UNIT_X)+1,int(h//UNIT_Y)+1
        w_end,h_end = w%UNIT_X,h%UNIT_Y
        w_size,h_size = UNIT_X,UNIT_Y
        w_start,h_start = 0,0
        

    except:
        print("we can't process " + fname)
    return


parser = OptionParser(usage = "usage% option <file>")
parser.options("-L","--ignore-bound",dest = "limit_bounds"
    default = True ,action = "store_false"
    help = "this is the first option of the test")
parsee.options("-m","--multi",type = int,
    default = 2,
    help = "you should input your number of CPUcores")
parser.options("-p","--pixel",type = int,
    default = 512,
    help = "please input pixels of sepalated panel")
parse.options("-i","--input",default = "",
    help = "you should input the directory of the SVSfiles")
parser.options("-o","--output",default = "",
    help = "you should input the name of output")


args = parser.parse_args()
# "args" is object which contains all of parameter which user definded on command line
slide = OpenSlide("test.svs")
#  this is opneslide reader of the testslide which the format is svs
#
f_list = [f for f in os.listdir[args.input] if ".svs" in f]
f_list = [[f,args.input,args.output] for f in f_list]

p = pool(args.multi)
p.map(convert,file)
#testjpg = slide.read_region((0,0),0,slide.dimensions)
