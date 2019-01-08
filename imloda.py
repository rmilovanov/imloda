# -*- coding: utf-8 -*-

import argparse
import os
import urllib
from subprocess import call
import shlex

REP = "https://raw.githubusercontent.com/teracow/googliser/master/googliser.sh"
DLD_CMD = 'bash googliser.sh -p "{}" -n {} -N -P 40 -c -m 2mp --timeout 3'
CWD = os.getcwd()       # Current user's work directory


def get_googliser(fold):
    if not os.path.isfile(fold+"/googliser.sh"):
        print "Current path: ", CWD
        print "Target folder: ", fold
        if not os.path.exists(fold):
            print fold, " does not exist"
            os.makedirs(fold)
        print "Download Googliser to {}".format(fold)
        googliser = urllib.URLopener()
        googliser.retrieve(REP, fold+"/googliser.sh")
    else:
        # print "Googliser already exists"
        pass


def main(amount, query, dest_folder):
    WD = dest_folder

    # print "Look for {} images of {} and put them into {}".format(
    #                        amount, query, dest_folder)

    get_googliser(WD)
    os.chdir(WD)
    print WD
    print query
    some_command = DLD_CMD.format(query.encode('utf8'), amount)
    # some_command = DLD_CMD.format(query, amount)
    print some_command
    call(shlex.split(some_command))
    os.chdir(CWD)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='Don\'t fuck with me',
        epilog="Motherfucker"
    )
    parser.add_argument('-q', '--query',
                        action='store',
                        required=True,
                        help="What you're looking for")
    parser.add_argument('-a', '--amount',
                        type=int,
                        help="Number of images to download",
                        default=100)
    parser.add_argument('-d', '--dest_folder',
                        help="Script result destination folder",
                        default=CWD)

    parser.add_argument('--version', action='version', version='%(prog)s 1.0')
    args = parser.parse_args()
    main(args.amount, args.query, args.dest_folder)
