#!/usr/bin/env python

import string1
import metadata
import sys
import csv 

def metadatum( funcMetadata, astrTokens, iIndex ):
	for strTokens in astrTokens:
		sys.stderr.write( str(strTokens) + "\n" )
		setstrTokens = set()
		for strToken in strTokens.split( "|" ):
			astrToken = string1.split( strToken )
			setstrTokens.add( astrToken[iIndex] or strToken )
		funcMetadata( setstrTokens )

def callback( pMetadata, strAs, strBs, strAltAs, strAltBs, strSynAs, strSynBs, strMethods, strAuthors, strPMIDs,	strTaxAs, strTaxBs, strTypes, strDBs, strIDs, strConfs ):
	metadatum( pMetadata.taxid, [strTaxAs, strTaxBs], 1 )
	metadatum( pMetadata.pmid, [strPMIDs], 1 )

if len( sys.argv ) < 2:
	raise Exception( "Usage: c2metadata.py <id> < <stringc>" )

strTarget = sys.argv[1]
strStatus = sys.argv[2] if len(sys.argv[1:]) > 1 else None 

pMetadata = metadata.open( )
string1.read( sys.stdin, strTarget, callback, pMetadata )
if strStatus:
        strMapped, strBool = [x for x in csv.reader(open(strStatus),csv.excel_tab)][0]
        fMapped = True if strBool == "True" else False 
        pMetadata.set(strMapped, fMapped)
pMetadata.save( sys.stdout )

