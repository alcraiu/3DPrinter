'''OpenGL extension INGR.interlace_read

This module customises the behaviour of the 
OpenGL.raw.GL.INGR.interlace_read to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension provides a way to skip rows of pixels when reading
	or copying pixel rectangles.  This extension is complementary to
	the EXT_interlace extension except that it has no affect on getting
	texture images.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/INGR/interlace_read.txt
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.INGR.interlace_read import *
### END AUTOGENERATED SECTION