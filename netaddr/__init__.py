#-----------------------------------------------------------------------------
#   Copyright (c) 2008-2009, David P. D. Moss. All rights reserved.
#
#   Released under the BSD license. See the LICENSE file for details.
#-----------------------------------------------------------------------------
"""
network address manipulation, done Pythonically
"""
import sys as _sys
if _sys.version_info[0:2] < (2, 4):
    raise RuntimeError('Python 2.4.x or higher is required!')

__version__ = '0.7'

from netaddr.core import AddrConversionError, AddrFormatError

from netaddr.ip import IP, cidr_abbrev_to_verbose, cidr_exclude, cidr_merge, \
    iprange_to_cidrs, spanning_cidr, within_iprange, iter_iprange, \
    iter_unique_ips

from netaddr.ipglob import cidr_to_glob, glob_to_cidrs, glob_to_iprange, \
    valid_glob, iprange_to_globs

from netaddr.eui import NotRegisteredError, EUI, IAB, OUI

from netaddr.strategy.eui48 import mac_eui48, mac_unix, mac_cisco, mac_bare, \
    mac_pgsql

__all__ = """AddrConversionError
AddrFormatError
EUI
IAB
IP
NotRegisteredError
OUI
cidr_abbrev_to_verbose
cidr_exclude
cidr_merge
cidr_to_glob
glob_to_cidrs
glob_to_iprange
iprange_to_cidrs
iprange_to_globs
iter_iprange
iter_unique_ips
mac_bare
mac_cisco
mac_eui48
mac_pgsql
mac_unix
spanning_cidr
valid_glob
within_iprange""".split("\n")
