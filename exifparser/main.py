# -*- coding: cp1252 -*-
from __future__ import division
from fractions import Fraction
import os
import exifread
import sys
import math

folder = os.getcwd()

# iso =  tags['EXIF ISOSpeedRatings']
# length35mm = float(tags['EXIF FocalLengthIn35mmFilm'].printable)

# To be done:
# def calculateEffectiveFocalLength(focal_length):

def getExposureRatio(tags):
	if "EXIF ExposureTime" in tags:
		exposure = tags["EXIF ExposureTime"]
		exposure = eval(exposure.printable)
		if exposure < 1/1000: # alle 1/1000 valotusaika lasketaan teräväksi
			return 0.0;
		if exposure > 1/4: # yli 1/4 valotusaika lasketaan epäteräväksi
			return 1.0
		exposure = math.log(exposure, 2)
		min = -10 
		max = -2 
		normalized = (exposure-(min))/(max-min)
		return normalized
	return "Couldn't find exposure-data"

def parseExif(pathToImage):

	# Open image file for reading (binary mode)
	image = open(pathToImage, 'rb')
	
	# Return Exif tags
	tags = exifread.process_file(image)
	
	return tags;

if __name__ == "__main__":
	tiedosto = sys.argv[1]
	tags = parseExif(tiedosto)
	print getExposureRatio(tags)

