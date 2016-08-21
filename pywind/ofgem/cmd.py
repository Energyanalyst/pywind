# coding=utf-8

# This is free and unencumbered software released into the public domain.
#
# Anyone is free to copy, modify, publish, use, compile, sell, or
# distribute this software, either in source code form or as a compiled
# binary, for any purpose, commercial or non-commercial, and by any
# means.

# In jurisdictions that recognize copyright laws, the author or authors
# of this software dedicate any and all copyright interest in the
# software to the public domain. We make this dedication for the benefit
# of the public at large and to the detriment of our heirs and
# successors. We intend this dedication to be an overt act of
# relinquishment in perpetuity of all present and future rights to this
# software under copyright law.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
# For more information, please refer to <http://unlicense.org/>

import sys

from pywind.ofgem.CertificateSearch import CertificateSearch
from pywind.ofgem.Certificates import CertificatesList
from pywind.ofgem.StationSearch import StationSearch


def ofgem_certificate_search(args):
    print("Ofgem Certificate Search\n")

    if args.period is None and args.scheme is None:
        print("You must supply at least a period or scheme.")
        sys.exit(0)

    ocs = CertificateSearch()
    if ocs.start() is False:
        print("Unable to get the form from Ofgem website.")
        sys.exit(0)

    if args.period is not None:
        if ocs.set_period(args.period) is False:
            print("There was an error setting the period.")
            sys.exit(0)
    if args.scheme is not None:
        if ocs.filter_scheme(args.scheme) is False:
            print("There was an error setting the scheme.")
            sys.exit(0)

    if ocs.get_data() is False:
        print("Unable to get the data from Ofgem.")
        sys.exit(0)
    return ocs


def ofgem_certificates(args):
    print("Ofgem Certificate File Parser\n")

    if args.input is None:
        print("You must supply an input filename")
        sys.exit(0)

    ocl = CertificatesList(filename=args.input)
    print("Certificates for {} stations found.".format(len(ocl)))

    return ocl


def ofgem_station_search(args):
    print("Ofgem Station Search\n")

    oss = StationSearch()
    if oss.start() is False:
        print("Unable to get the form from the Ofgem website")
        sys.exit(0)

    if args.station is not None:
        oss.filter_name(args.station)

    print("get_data() => {}".format(oss.get_data()))

    return oss




