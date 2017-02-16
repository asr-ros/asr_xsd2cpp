#!/usr/bin/env python

""" 

Copyright (c) 2016, Meissner Pascal, Schleicher Ralf
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE. 
 
"""

import os
import shutil

def main():
	'''
	creates the cpp object from xmlschema
	'''
	basepath = os.path.abspath(os.path.curdir)
	projectName = os.path.basename(basepath)
	xmlschemapath = os.path.join(basepath, "xsd")
	xmlschemagenpath = os.path.join(basepath, "xsd_gen")
	xmlschemagenprojectnamepath = os.path.join(xmlschemagenpath, projectName)

	if not os.path.exists(xmlschemapath):
		return

	if os.path.exists(xmlschemagenpath):
		shutil.rmtree(xmlschemagenpath)
	os.mkdir(xmlschemagenpath)
	os.mkdir(xmlschemagenprojectnamepath)
	
	os.chdir(xmlschemagenprojectnamepath)
	for root, dirs, files in os.walk(xmlschemapath):
		for file in files:
			f = os.path.splitext(file)
			if f[1] == ".xsd":
				os.system("xsd cxx-tree --std c++11 --guard-prefix %s --cxx-suffix .cpp --hxx-suffix .h --polymorphic-type-all %s" % (f[0], os.path.join(root, file)))

if __name__ == "__main__":
	main()
