import numpy
import os
from optparse import OptionParser
import openslide
from openslide import open_slide,OpenSlide
#this package is need to read SVSfiles.
from multiprocessing import pool
import multiprocessing as multi
#this package is need to make multitask possible
from PIL import Image
import argparse



#to make process of sepalating Unit
#def convert(data,pixeldef):


if __name__ == "__main__":
    #Read the command line.
    parser = argparse.ArgumentParser(description='This script is ...',
                                     formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("--input", "-i", default="./input",
                        help="Directory name where the input image is saved. default='./input'")
    parser.add_argument("--output", "-o", default="./output",
                        help="Directory name where the converted image is saved. default='./output'")
    parser.add_argument("--multi", "-m", type=int, default=2,
                        help="Number of CPU cores to use for conversion. default=2")
    parser.add_argument("--pixel","-p",default=512,
                        help = "Input the number of pixels")
    args = parser.parse_args()
    # "args" is object which contains all of parameter which user definded on command line
    #  this is opneslide reader of the testslide which the format is svs
    f_list = [f for f in os.listdir(args.input) if ".svs" in f]
    f_list = [[f,args.input,args.output] for f in f_list]
    pixes = args.pixel
    print("----------program start----------")
    #Set multi processing and run.
    UNIT_X,UNIT_Y = pixes,pixes
    # insert
    fname,f_input,f_output = f_list
    save_name = fname.split(".")[0] + ".jpg"
    print("processing : " + fname)
    simage = OpenSlide(f_input + "/" + fname)
    w,h = simage.dimensions
    w_rep,h_rep = int(w//UNIT_X)+1,int(h//UNIT_Y)+1
    w_end,h_end = w%UNIT_X,h%UNIT_Y
    w_size,h_size = UNIT_X,UNIT_Y
    w_start,h_start = 0,0
    for i in range(h_rep):
        if i == h_rep - 1:
            h_size = h_end
        for j in range(w_rep):
            if j == w_rep - 1:
                w_size = w_end
            img = simage.read_region((W_start,h_start),0,(w_size,h_size))
            img = img.convert("RGB")
            w_start += UNIT_X
            img_name = f_name + "_" + i + "_" + j + ".jpg"
        w_size = UNIT_X
        h_start += UNIT_Y
        w_start = 0
"""
    except:
        print("Can't open image file : " + fname)

    try:
        convert(f_lst,pixes)
        #testjpg = slide.read_region((0,0),0,slide.dimensions)
    except:
        print("WARNING!!!----------This command was failed-----------")
"""
