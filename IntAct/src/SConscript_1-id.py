#!/usr/bin/env python

import arepa
import os
import sfle
import sys
import metadata
import glob

def test( iLevel, strID, hashArgs ):
	return ( iLevel == 1 )
if locals( ).has_key( "testing" ):
	sys.exit( )

pE = DefaultEnvironment( )

c_strID					= arepa.cwd( )
c_fileInputIntactC			= sfle.d( pE, arepa.path_repo( ), sfle.c_strDirTmp, "intactc" )
c_fileIDPKL				= sfle.d( pE, c_strID + ".pkl" )
c_fileIDDAB				= sfle.d( pE, c_strID + ".dab" )
c_fileIDDAT             		= sfle.d( pE, c_strID + ".dat" )
c_fileIDQUANT           		= sfle.d( pE, c_strID + ".quant" )

c_fileProgUnpickle                      = sfle.d( pE, arepa.path_arepa( ), sfle.c_strDirSrc, "unpickle.py" )
c_fileProgC2Metadata                    = sfle.d( pE, arepa.path_repo( ), sfle.c_strDirSrc, "c2metadata.py" )
c_fileProgC2DAT                         = sfle.d( pE, arepa.path_repo( ), sfle.c_strDirSrc, "c2dat.py" )

c_fileInputSConscriptGM                 = sfle.d( pE, arepa.path_arepa(),sfle.c_strDirSrc,"SConscript_genemapping.py")
c_fileInputSConscriptDAB                = sfle.d( pE, arepa.path_arepa(), sfle.c_strDirSrc, "SConscript_dat-dab.py" )

c_fileStatus 	    			=  sfle.d(pE, "status.txt")
c_strGeneFrom 				= "S"

afileIDDAT = sfle.pipe( pE, c_fileInputIntactC, c_fileProgC2DAT, c_fileIDDAT, [c_strID] )

##############################################
#- Gene id mapping from Uniprot to Genesymbols
##############################################

#Launch gene mapping 
execfile(str(c_fileInputSConscriptGM))
astrMapped = funcGeneIDMapping( pE, c_fileIDDAT, c_fileStatus, None )

#Make identifiers unique 
astrUnique = funcMakeUnique( pE, astrMapped[0] )

afileIDTXT = sfle.pipe( pE, c_fileInputIntactC, c_fileProgC2Metadata, c_fileIDPKL,[c_strID,[c_fileStatus]] )

execfile(str(c_fileInputSConscriptDAB))

#DAT to DAB
astrDAB = funcDAB( pE, c_fileIDDAB, [c_fileIDDAT, astrUnique[0]] )
funcQUANT( pE, c_fileIDQUANT )

