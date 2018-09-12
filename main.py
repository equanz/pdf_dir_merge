# coding: utf-8
import os
import glob
import argparse
from PyPDF2 import PdfFileMerger

def main():
    """main"""
    # setup argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument("dir", help="Target directory in here.")
    parser.add_argument("dest", help="Destination filename in here.")
    parser.add_argument("-l", "--level", type=int, default=1, help="Directory level in here. Default is 1.")
    parser.add_argument("--name", default="*.pdf", help="Target file's name in here(e.g. foo.pdf). Default is unique.")
    parser.parse_args()

    # arguments
    args = parser.parse_args()

    if args.level < 1:
        raise ValueError # ignore parent level

    files_path = [] # pdf files path
    if os.path.lexists(os.path.abspath(args.dir)): # check directory
        dirs_path = glob.glob(os.path.abspath(args.dir) + "/**/", recursive=False)
        dirs_path.sort() # sort directory
        for dir_path in dirs_path:
            local_files_path = glob.glob(dir_path + args.name)
            local_files_path.sort() # sort file
            files_path.extend(local_files_path) # add to files list
    else:
        raise ValueError # directory is not existed in system

    # merge PDF files
    merger = PdfFileMerger()
    for file_path in files_path:
        merger.append(file_path)

    merger.write(os.path.abspath(args.dest))
    merger.close()

if __name__ == "__main__":
    main()

