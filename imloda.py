import argparse
import os
import urllib
from subprocess import call
import shlex

import SETTINGS

CWD = os.getcwd()       # Current user's work directory


def get_googliser():
    if not os.path.isfile(CWD+"/googliser.sh"):
        print "Download Googliser to {}".format(CWD)
        googliser = urllib.URLopener()
        googliser.retrieve("https://raw.githubusercontent.com/teracow/googliser/master/googliser.sh", CWD+"/googliser.sh")
    else:
        print "Googliser already exists"

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


CWD = args.dest_folder

print "Look for {} images of {} and put them into {}".format(
                        args.amount, args.query, args.dest_folder)

get_googliser()
some_command = 'bash {}/googliser.sh -p "{}" -n {} -c -f 0'.format(CWD, args.query, args.amount)
print some_command
call(shlex.split(some_command))
