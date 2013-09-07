#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ShiroRaven
#
# Created:     07/09/2013
# Copyright:   (c) ShiroRaven 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from TagExtractor import ReuterRooter as RR

def main():
    sgm = RR('reut2-000.sgm')

    #print out all article names
    num = sgm.NumberOfReuters()

    for i in range(0,num):
        print(sgm.ExtractTagData(i,"TITLE"))

if __name__ == '__main__':
    main()
