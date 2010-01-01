#!/usr/bin/python
# -*- coding: utf-8 -*-
#################################################################################
# LAYMAN SVN OVERLAY HANDLER
#################################################################################
# File:       svn.py
#
#             Handles subversion overlays
#
# Copyright:
#             (c) 2005 - 2008 Gunnar Wrobel
#             Distributed under the terms of the GNU General Public License v2
#
# Author(s):
#             Gunnar Wrobel <wrobel@gentoo.org>
#
''' Subversion overlay support.'''

__version__ = "$Id: svn.py 236 2006-09-05 20:39:37Z wrobel $"

#===============================================================================
#
# Dependencies
#
#-------------------------------------------------------------------------------

from   layman.utils             import path
from   layman.overlays.overlay  import Overlay

#===============================================================================
#
# Class SvnOverlay
#
#-------------------------------------------------------------------------------

class SvnOverlay(Overlay):
    ''' Handles subversion overlays.'''

    type = 'Subversion'
    type_key = 'svn'

    def __init__(self, xml, config, ignore = 0, quiet = False):

        Overlay.__init__(self, xml, config, ignore)

    def add(self, base, quiet = False):
        '''Add overlay.'''

        self.supported()

        Overlay.add(self, base)

        if quiet:
            quiet_option = '-q '
        else:
            quiet_option = ''

        return self.cmd(self.command() + ' co ' + quiet_option +
                        '"' + self.src + '/@" "' + path([base, self.name]) + '"')

    def sync(self, base, quiet = False):
        '''Sync overlay.'''

        self.supported()

        if quiet:
            quiet_option = '-q '
        else:
            quiet_option = ''

        return self.cmd(self.command() + ' up ' + quiet_option +
                        '"' + path([base, self.name + '@']) + '"')

    def supported(self):
        '''Overlay type supported?'''

        return Overlay.supported(self, [(self.command(),  'svn',
                                         'dev-util/subversion'),])
