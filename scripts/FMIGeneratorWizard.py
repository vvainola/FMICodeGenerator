#!/usr/bin/python
# -*- coding: utf-8 -*-

# The Wizard, that collects all data needed to generate the FMU from the user.
#
#
# This file is part of FMICodeGenerator (https://github.com/ghorwin/FMICodeGenerator)
#
# BSD 3-Clause License
#
# Copyright (c) 2018, Andreas Nicolai
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
# * Neither the name of the copyright holder nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


import sys
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtCore import pyqtProperty
from PyQt5 import QtCore, QtWidgets


class FMIGeneratorWizard(QtWidgets.QWizard):
	def __init__(self, parent=None):
		super(FMIGeneratorWizard, self).__init__(parent)
		self.addPage(PageBasicProperties(self))
		self.addPage(PageVariables(self))
		self.setWindowTitle("FMI Generator Wizard")
		self.resize(640,480)

class PageBasicProperties(QtWidgets.QWizardPage):
	def __init__(self, parent=None):
		super(PageBasicProperties, self).__init__(parent)
		layout = QtWidgets.QVBoxLayout()
		self.setLayout(layout)


class PageVariables(QtWidgets.QWizardPage):
	def __init__(self, parent=None):
		super(PageVariables, self).__init__(parent)
		self.label1 = QtWidgets.QLabel()
		self.label2 = QtWidgets.QLabel()
		layout = QtWidgets.QVBoxLayout()
		layout.addWidget(self.label1)
		layout.addWidget(self.label2)
		self.setLayout(layout)

	def initializePage(self):
		self.label1.setText("Example text")
		self.label2.setText("Example text")


if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	wizard = FMIGeneratorWizard()
	wizard.show()
	sys.exit(app.exec_())