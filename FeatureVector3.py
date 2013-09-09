#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ShiroRaven
#
# Created:     09/09/2013
# Copyright:   (c) ShiroRaven 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from TagExtractor import ReuterRooter as RR

def main():
    for i in range(0,23):
        filename = "reut2-%s.sgm" % ("%03d" % i)
        print filename + "\n"
        sgm = RR(filename)
        for j in range(0,sgm.NumberOfReuters()-1):
            title = sgm.ExtractTagData(j,"TITLE")
            print title

if __name__ == '__main__':
    main()
