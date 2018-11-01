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
def convert(data,Wpixels,hpixels):
    try:
        UNIT_X,UNIT_Y = wpixels,hpixels
        # insert
        fname,f_input,f_output = data
        save_name = fname.split("/")[1]
        save_name = save_name.split(".")[0]
        print("processing : " + fname)
        simage = OpenSlide(fname)
        w,h = simage.dimensions
        w_rep,h_rep = int(w//UNIT_X)+1,int(h//UNIT_Y)+1
        w_end,h_end = w%UNIT_X,h%UNIT_Y
        w_size,h_size = UNIT_X,UNIT_Y
        w_start,h_start = 0,0
        print("program is ready!!")
        for i in range(h_rep):
            if i == h_rep - 1:
                h_size = h_end
            for j in range(w_rep):
                if j == w_rep - 1:
                    w_size = w_end
                img = simage.read_region((w_start,h_start),0,(w_size,h_size))
                img = img.convert("RGB")
                img_name = f_output+ "/" + save_name + "_" + str(i) + "_" + str(j) + ".jpg"
                img.save(img_name)
                print("saving image:" + img_name)
                w_start += UNIT_X
            w_size = UNIT_X
            h_start += UNIT_Y
            w_start = 0
    except:
        print("Can't open image file : " + fname)


if __name__ == "__main__":
    #Read the command line.
    parser = argparse.ArgumentParser(description='This script is ...',
                                     formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("--input", "-i", default="input/test.svs",
                        help="Directory name where the input image is saved. default='./input'")
    parser.add_argument("--output", "-o", default="./output",
                        help="Directory name where the converted image is saved. default='./output'")
    parser.add_argument("--multi", "-m", type=int, default=2,
                        help="Number of CPU cores to use for conversion. default=2")
    parser.add_argument("--widepixel","-w",default=512,
                        help = "Input the number of pixels")
    parser.add_argument("--heightpixel","-e",default=512,
                        help = "Input the number of height pixels")
    args = parser.parse_args()
    # "args" is object which contains all of parameter which user definded on command line
    #  this is opneslide reader of the testslide which the format is svs
    #f_lst = [f for f in os.listdir(args.input) if ".svs" in f]
    f_list = [args.input,"input",args.output]
    widepixels = args.widepixel
    heightpixels = args.heightpixel
    print("----------program start----------")
    #Set multi processing and run.

    try:
        convert(f_list,widepixels,heightpixels)
        #testjpg = slide.read_region((0,0),0,slide.dimensions)
    except:
        print("WARNING!!!----------This command was failed-----------")
