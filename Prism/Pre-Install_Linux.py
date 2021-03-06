# -*- coding: utf-8 -*-
#
####################################################
#
# PRISM - Pipeline for animation and VFX projects
#
# www.prism-pipeline.com
#
# contact: contact@prism-pipeline.com
#
####################################################
#
#
# Copyright (C) 2016-2018 Richard Frangenberg
#
# Licensed under GNU GPL-3.0-or-later
#
# This file is part of Prism.
#
# Prism is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Prism is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Prism.  If not, see <https://www.gnu.org/licenses/>.

import os

pysideInstalled = True
pyside2Installed = True

try:
	from PySide2.QtCore import *
except:
	pyside2Installed = False


try:
	from PySide.QtCore import *
except:
	pysideInstalled = False

if not pysideInstalled and not pyside2Installed:
	libPath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "PrismFiles", "PythonLibs", "lib-inactive")
	libtPath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "PrismFiles", "PythonLibs", "lib")

	if os.path.exists(libPath) and not os.path.exists(libtPath):
		os.rename(libPath, libtPath)