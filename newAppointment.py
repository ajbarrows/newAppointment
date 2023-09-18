#!/usr/bin/env python

"""
Create folder structure for Graduate Writing Center Appointments.

Tony Barrows 20230918 
"""

import os
import shutil

from datetime import date

def get_user_input():

    netid = input("Enter client's UVM NetID: ")
    return netid

def make_directories(netid):

    top_dir = '../' + netid

    sub_dir = str(date.today()) + '_' + netid
    sub_dir = os.path.join(top_dir, sub_dir)

    for d in [top_dir, sub_dir]:
        os.makedirs(d, exist_ok=True)
    
    subsub = ['download', 'edit']

    for s in subsub:
        dir = os.path.join(sub_dir, s)
        os.makedirs(dir, exist_ok=True)

    return sub_dir

def copy_template(netid, sub_dir, infile='01_crf_template.docx'):

    outfile = str(date.today()) + '_' + netid + '_crf.docx'
    outfile = os.path.join(sub_dir, outfile)

    shutil.copy2(infile, outfile)
    

if __name__ == "__main__":

    netid = get_user_input()
    sub_dir = make_directories(netid)
    copy_template(netid, sub_dir)