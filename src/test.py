#!/usr/bin/env python 
'''
This is the test module for arepa. 
'''
import arepa 
import subprocess  
import sfle
import os 
import csv 
import pickle 
import sys 

if len(sys.argv[1:]) > 0:
	f_scons = True if sys.argv[1] == "scons" else False 
else:
	f_scons = False 

#=====================================================#
#		ARepA Submodules		      #
#=====================================================#

c_strGEO 	= "GEO"
c_strRegulonDB	= "RegulonDB"
c_strMPIDB	= "MPIDB"
c_strSTRING	= "STRING"
c_strIntAct	= "IntAct"
c_strBioGrid	= "BioGrid" 

#=====================================================#
#		General Helper Functions 
#=====================================================#

def _readstr( instr ):
	return map(lambda x: x.split("\t"),instr.strip().split("\n"))

def _read( infile, iRange = None, strDelim = None ):
	if not strDelim:
		strDelim = "\t"
	dummy = [line for line in csv.reader( open( infile ), delimiter= strDelim )]
	return ( dummy[:iRange] if iRange else dummy )

def _test( infile, aFixed, parse_function = None ):
	pTest = parse_function( infile ) if parse_function else\
		_read( infile, len( aFixed ) )
	if pTest == aFixed:
		print "test passed for", infile 
	else:
		raise Exception("!test failed", infile)

def exec_test( strDir, fParse = None, *aCouple ):
	strCur = os.getcwd( )
	os.chdir( strDir )
	if f_scons:
		subprocess.call( "scons" )
	for strTest, strVal in aCouple:
		_test( strTest, strVal, fParse )
	os.chdir( strCur )    

#=====================================================#
#			GEO
#=====================================================#
''' 
instead of testing for python pkl files, which are huge, 
test for tab delimited printed text files
'''
#constants for GEO testing 
'''
<GSEs>
manual curation - GSE8126 
multiple platforms - GSE10645, GSE16560, GSE8402 
multiple files, one platform - GSE10183
no curated file - GSE10183 

<GDSs> 
bacterial data - GDS1849, GDS3421, GDS3421. GDS3572, 
GDS3174
'''

c_strGSE8126		= 	"GSE8126"
c_strGSE10645		=	"GSE10645"
c_strGSE16560		= 	"GSE16560"
c_strGSE8402		=	"GSE8402"
c_strGSE10183		=	"GSE10183"
c_strGDS1849		=	"GDS1849"
c_strGDS3421		=	"GDS3421"
c_strGDS3572		=	"GDS3572"
c_strGDS3174		=	"GDS3174"

c_astrMetaKeys		= 	["taxid","pmid","platform","gloss","channels","conditions"]

c_dirGEO		=	sfle.d( arepa.path_arepa( ), "GEO")
c_dirGEOData		= 	sfle.d( c_dirGEO, sfle.c_strDirData )

###GSE10183###
 
c_dirGSE10183base	=	sfle.d( c_dirGEOData,c_strGSE10183 )
c_dirGSE10183		=	sfle.d( c_dirGSE10183base, c_strGSE10183 )
c_fileGSE10183EXP	= 	sfle.d( c_dirGSE10183, c_strGSE10183 + "_exp_metadata.txt" )
c_fileGSE10183PCL	=	sfle.d( c_dirGSE10183, c_strGSE10183 + "_00raw.pcl" ) 


c_GSE10183EXP		=	_readstr( 'Series_platform_taxid\tSeries_contact_department\tSeries_contact_name\tSeries_status\tgloss\tSeries_relation\tSeries_contact_state\tSeries_contact_address\tSeries_contact_city\tplatform\tSeries_contact_laboratory\tSeries_overall_design\tSeries_contributor\tSeries_contact_country\tSeries_contact_zip/postal_code\tSeries_supplementary_file\tSeries_geo_accession\tSeries_sample_id\ttaxid\tSeries_contact_institute\tSeries_submission_date\tSeries_last_update_date\r\n9606\tGenetics, USP Medical School at Ribeirao Preto\tRicardo,Z.N.,V\xc3\xaancio\tPublic on Jan 14 2009\tCancer cells were MACS sorted from tumor tissue specimem 05-179. Self replicates of CD26+ cancer cells were generated and the expression profiles were determined using Affymetrix U133 Plus 2.0 arrays. These data represent cancer cell type specific transcriptome. Keywords: disease state analysis\tBioProject: http://www.ncbi.nlm.nih.gov/bioproject/108397\tSP\tAv. Bandeirantes, 3900\tRibeirao Preto\tGPL570\thttp://labpib.fmrp.usp.br\tSelf replicates of the sorted were done.\tAlvin,,Liu\tBrazil\t14049-900\tftp://ftp.ncbi.nlm.nih.gov/pub/geo/DATA/supplementary/series/GSE10183/GSE10183_RAW.tar\tGSE10183\tGSM257248 GSM257249 \t9606\tUniversidade de S\xc3\xa3o Paulo\tJan 15 2008\tJun 06 2012\r\n')

c_GSE10183PCL		= 	[['GID', 'NAME', 'GWEIGHT', 
				'GSM257248: CD26+ cancer cell, replicate 1', \
				'GSM257249: CD26+ cancer cell, replicate 2'], 
				['EWEIGHT', '', '', '1', '1'],
				['1007_s_at', 'U48705', '1', '10.34880883', '10.25328334'],
				['1053_at', 'M87338', '1', '7.096953279', '7.16038339'],
				['117_at', 'X51757', '1', '10.89463506', '10.85675361'],
				['121_at', 'X69699', '1', '8.020897183', '7.84238035']]

exec_test( c_dirGEO, None, [c_fileGSE10183PCL,c_GSE10183PCL] )

###GSE8126###

c_dirGSE8126base	=	sfle.d( c_dirGEOData,c_strGSE8126 )
c_dirGSE8126		= 	sfle.d( c_dirGSE8126base, c_strGSE8126 )
c_fileGSE8126EXP	= 	sfle.d( c_dirGSE8126, c_strGSE8126 + "_exp_metadata.txt" )
c_fileGSE8126PCL	=	sfle.d( c_dirGSE8126, c_strGSE8126 + ".pcl" ) 

c_GSE8126PCL		=	[['GID',
				  'NAME',
				  'GWEIGHT',
				  'GSM201402: Prostate tumor patient 1',
				  'GSM201403: Prostate tumor patient 2',
				  'GSM201404: Prostate tumor patient 4',
				  'GSM201405: Prostate tumor patient 5',
				  'GSM201406: Prostate tumor patient 6',
				  'GSM201407: Prostate tumor patient 7',
				  'GSM201408: Prostate tumor patient 8',
				  'GSM201409: Prostate tumor patient 9',
				  'GSM201410: Prostate tumor patient 10',
				  'GSM201411: Prostate tumor patient 12',
				  'GSM201412: Prostate tumor patient 13',
				  'GSM201413: Prostate tumor patient 14',
				  'GSM201414: Prostate tumor patient 15',
				  'GSM201415: Prostate tumor patient 16',
				  'GSM201416: Prostate tumor patient 17',
				  'GSM201417: Prostate tumor patient 18',
				  'GSM201418: Prostate tumor patient 20',
				  'GSM201419: Prostate tumor patient 21',
				  'GSM201420: Prostate tumor patient 22',
				  'GSM201421: Prostate tumor patient 23',
				  'GSM201422: Prostate tumor patient 26',
				  'GSM201423: Prostate tumor patient 27',
				  'GSM201424: Prostate tumor patient 28',
				  'GSM201425: Prostate tumor patient 29',
				  'GSM201426: Prostate tumor patient 30',
				  'GSM201427: Prostate tumor patient 33',
				  'GSM201428: Prostate tumor patient 34',
				  'GSM201429: Prostate tumor patient 35',
				  'GSM201430: Prostate tumor patient 36',
				  'GSM201431: Prostate tumor patient 37',
				  'GSM201432: Prostate tumor patient 38',
				  'GSM201433: Prostate tumor patient 39',
				  'GSM201434: Prostate tumor patient 40',
				  'GSM201435: Prostate tumor patient 41',
				  'GSM201436: Prostate tumor patient 42',
				  'GSM201437: Prostate tumor patient 43',
				  'GSM201438: Prostate tumor patient 44',
				  'GSM201439: Prostate tumor patient 45',
				  'GSM201440: Prostate tumor patient 47',
				  'GSM201441: Prostate tumor patient 48',
				  'GSM201442: Prostate tumor patient 49',
				  'GSM201443: Prostate tumor patient 51',
				  'GSM201444: Prostate tumor patient 52',
				  'GSM201445: Prostate tumor patient 53',
				  'GSM201446: Prostate tumor patient 54',
				  'GSM201447: Prostate tumor patient 55',
				  'GSM201448: Prostate tumor patient 56',
				  'GSM201449: Prostate tumor patient 57',
				  'GSM201450: Prostate tumor patient 58',
				  'GSM201451: Prostate tumor patient 59',
				  'GSM201452: Prostate tumor patient 60',
				  'GSM201453: Prostate tumor patient 61',
				  'GSM201454: Surrounding normal prostate tissue patient 63',
				  'GSM201455: Surrounding normal prostate tissue patient 65',
				  'GSM201456: Prostate tumor patient 65',
				  'GSM201457: Surrounding normal prostate tissue patient 68',
				  'GSM201458: Prostate tumor patient 68',
				  'GSM201459: Surrounding normal prostate tissue patient 70',
				  'GSM201460: Prostate tumor patient 70',
				  'GSM201461: Surrounding normal prostate tissue patient 72',
				  'GSM201462: Prostate tumor patient 72',
				  'GSM201463: Prostate tumor patient 73',
				  'GSM201464: Prostate tumor patient 74',
				  'GSM201465: Surrounding normal prostate tissue patient 76',
				  'GSM201466: Prostate tumor patient 76',
				  'GSM201467: Prostate tumor patient 77',
				  'GSM201468: Surrounding normal prostate tissue protate cancer patient A',
				  'GSM201469: Surrounding normal prostate tissue protate cancer patient B',
				  'GSM201470: Surrounding normal prostate tissue protate cancer patient C',
				  'GSM201471: Surrounding normal prostate tissue patient 31',
				  'GSM201472: Surrounding normal prostate tissue patient 45',
				  'GSM201473: Surrounding normal prostate tissue patient 16',
				  'GSM201474: Surrounding normal prostate tissue patient 21',
				  'GSM201475: Surrounding normal prostate tissue patient D',
				  'GSM201476: Surrounding normal prostate tissue patient 4',
				  'GSM201477: Surrounding normal prostate tissue patient 57'],
				['EWEIGHT',
				 '',
				 '',
				 '1',
				 '1',
				 '1',
				 '1',
				 '1',
				 '1',
				 '1',
				 '1',
				 '1',
				 '1',
				 '1',
				 '1',
				 '1',
				 '1',
				 '1',
				 '1',
				 '1',
				 '1',
				 '1',
				 '1',
				 '1',
				 '1',
				 '1',
				 '1',
				 '1',
				 '1',
				 '1',
				 '1',
				 '1',
				 '1',
				 '1',
				 '1',
				 '1',
				 '1',
				 '1',
				 '1',
				 '1',
				 '1',
				 '1',
				 '1',
				 '1',
				 '1',
				 '1',
				 '1',
				 '1',
				 '1',
				 '1',
				 '1',
				 '1',
				 '1',
				 '1',
				 '1',
				 '1',
				 '1',
				 '1',
				 '1',
				 '1',
				 '1',
				 '1',
				 '1',
				 '1',
				 '1',
				 '1',
				 '1',
				 '1',
				 '1',
				 '1',
				 '1',
				 '1',
				 '1',
				 '1',
				 '1',
				 '1',
				 '1',
				 '1',
				 '1'],
				 ['1-1-1',
				  'hsa-mir-034',
				  '1',
				  '7.45457',
				  '7.92907',
				  '8.78136',
				  '8.26444',
				  '7.59952',
				  '8.01238',
				  '8.39339',
				  '8.40088',
				  '7.91197',
				  '8.05438',
				  '8.60053',
				  '7.94109',
				  '8.28517',
				  '8.40749',
				  '8.27413',
				  '8.21189',
				  '8.36442',
				  '8.2671',
				  '8.51252',
				  '7.5588',
				  '8.18831',
				  '8.4012',
				  '7.89355',
				  '8.62727',
				  '8.2855',
				  '8.74316',
				  '8.07681',
				  '8.58933',
				  '8.46303',
				  '8.54537',
				  '8.45671',
				  '8.22317',
				  '8.58956',
				  '8.52748',
				  '8.36434',
				  '8.13126',
				  '8.21104',
				  '8.17819',
				  '7.81314',
				  '8.09199',
				  '8.47929',
				  '7.39181',
				  '8.14474',
				  '7.29921',
				  '7.08275',
				  '7.23832',
				  '7.79223',
				  '6.86027',
				  '7.51307',
				  '7.83938',
				  '7.15214',
				  '7.98261',
				  '7.87965',
				  '8.14721',
				  '8.58918',
				  '7.83463',
				  '8.27768',
				  '8.08971',
				  '7.83638',
				  '8.46889',
				  '7.95253',
				  '8.39846',
				  '8.82055',
				  '8.48902',
				  '8.44045',
				  '8.11779',
				  '7.98595',
				  '8.26084',
				  '8.78295',
				  '8.65199',
				  '7.48803',
				  '8.20176',
				  '7.66612',
				  '8.17493',
				  '7.86796',
				  '8.42501']]


exec_test( c_dirGEO, None, [c_fileGSE8126PCL,c_GSE8126PCL] )

###GDS1849### 

c_dirGDS1849base	=	sfle.d( c_dirGEOData, c_strGDS1849 )
c_dirGDS1849		=	sfle.d( c_dirGDS1849base, "GDS1849-GPL1821" )
c_fileGDS1849PKL	=	sfle.d( c_dirGDS1849, "GDS1849-GPL1821.pkl" )
c_fileGDS1849EXP	=	sfle.d( c_dirGDS1849, "GDS1849-GPL1821_exp_metadata.txt")
c_fileGDS1849PCL	=	sfle.d( c_dirGDS1849, "GDS1849-GPL1821_00raw.pcl" ) 

c_GDS1849PKL		= 	{'channels': '1',
 'conditions': '42',
 'gloss': 'Analysis of Bacteroides thetaiotaomicron (BT) from the ceca of mice on polysaccharide or simple sugar diets. BT is involved in the breakdown of plant polysaccharides. BT-colonized mice is a human gut ecosystem model. Results identify genes that may endow flexibility in adapting to dietary changes.',
 'platform': 'GPL1821',
 'pmid': '16735464',
 'taxid': '818',
 'title': 'Intestine-adapted bacterial symbiont response to polysaccharide and simple sugar diets',
 'type': 'expression profiling'}


exec_test( c_dirGEO, lambda f: pickle.load(open(f,"r")), [c_fileGDS1849PKL, c_GDS1849PKL] ) 

###GSE8402###

c_dirGSE8402base	=	sfle.d( c_dirGEOData, c_strGSE8402 )
c_dirGSE8402		= 	sfle.d( c_dirGSE8402base, c_strGSE8402 )
c_fileGSE8402PCL	=	sfle.d( c_dirGSE8402, c_strGSE8402 + "_00raw.pcl" )

c_GSE8402PCL		=	['DAP1_0003',
 				'NM_000405',	
	 			'1',
 				'0.3345',
 				'0.6069',
 				'0.301',
 				'-0.2263',
 				'-0.0335',
 				'0.4686',
				'0.5545',
 				'0.539',
 				'0.8853',
 				'-0.3253',
 				'0.8535',
 				'0.3553',
 				'0.6095',
 				'0.4287',
 				'0.2953',
 				'-0.8379',
 				'0.614',
 				'0.5594',
 				'-0.3064',
 				'0.0301',
 				'0.2157',
 				'0.7615',
 				'-0.83',
 				'0.8972',
 				'-0.0167',
 				'0.6985',
 				'0.3632']

exec_test( c_dirGEO, lambda f: [a for a in csv.reader(open(f,"r"),csv.excel_tab)][2][:30], \
	[ c_fileGSE8402PCL, c_GSE8402PCL ] )


#=====================================================#
#               	Bacteriome
#=====================================================#
#single dataset 

c_dirBacteriome		= 	sfle.d( arepa.path_arepa( ), "Bacteriome" )
c_dirBacteriomeData	=	sfle.d( c_dirBacteriome, sfle.c_strDirData )
c_fileBacteriomeDat	= 	sfle.d( c_dirBacteriomeData, "bacteriome.dat" )
c_fileBacteriomeQuant	=	sfle.d( c_dirBacteriomeData, "bacteriome.quant")

c_BacteriomeQuantLst	=	[["0.5","1.5"]]
c_BacteriomeDatLst	= 	[["b0002","b0003","0.408408"],["b0002","b0004","0.408408"]]

exec_test( c_dirBacteriome, None, [c_fileBacteriomeQuant, c_BacteriomeQuantLst], \
	[ c_fileBacteriomeDat, c_BacteriomeDatLst ] )
 	
#=====================================================#
#                       BioGrid
#=====================================================#
#single dataset 

c_strBioGrid		= "taxid_224308"
c_dirBioGrid		= sfle.d( arepa.path_arepa( ), "BioGrid" )
c_dirBioGridData	= sfle.d( c_dirBioGrid, sfle.c_strDirData, c_strBioGrid )
c_fileBioGridPKL	= sfle.d( c_dirBioGridData, "taxid_224308.pkl" )
c_fileBioGridDat	= sfle.d( c_dirBioGridData, "taxid_224308.dat" )
c_fileBioGridQuant	= sfle.d( c_dirBioGridData, "taxid_224308.quant" )

c_BioGridDat		= [['rsbV', 'rsbW', '1']] 
c_BioGridPKL		= {'platform': 'Co-purification', 'pmid': '8144446', 'type': '857505', 'taxid': '855787'}
c_BioGridQuant		= [["0.5", "1.5"]]

exec_test( c_dirBioGrid, None, [c_fileBioGridDat, c_BioGridDat], [c_fileBioGridQuant, c_BioGridQuant] )
exec_test( c_dirBioGrid, lambda f: pickle.load( open(f, "r") ), [c_fileBioGridPKL, c_BioGridPKL] )

#=====================================================#
#                       IntAct
#=====================================================#
#multiple datasets

c_astrIntActIDs		=	[ "taxid_9606_pmid_10383454", "taxid_1061", "taxid_1063" ] 
c_dirIntAct		=	sfle.d( arepa.path_arepa( ), "IntAct" ) 
c_dirIntActData		=	sfle.d( c_dirIntAct, sfle.c_strDirData )

f_dirIntActData		=	lambda x: sfle.d( c_dirIntActData, x )
f_fileIntActDAT		= 	lambda x: sfle.d( f_dirIntActData( x ), x + ".dat" )
f_fileIntActQUANT	=	lambda x: sfle.d( f_dirIntActData( x ), x + ".quant" )
f_fileIntActPKL		=	lambda x: sfle.d( f_dirIntActData( x ), x + ".pkl" ) 

c_fileIntActData1DAT	=	f_fileIntActDAT( c_astrIntActIDs[0] )
c_fileIntActData1QUANT	=	f_fileIntActQUANT( c_astrIntActIDs[0] )
c_fileIntActData1PKL	=	f_fileIntActPKL( c_astrIntActIDs[0] )

c_fileIntActData2DAT	=	f_fileIntActDAT( c_astrIntActIDs[1] )
c_fileIntActData2QUANT	=	f_fileIntActQUANT( c_astrIntActIDs[1] )
c_fileIntActData2PKL	=	f_fileIntActPKL( c_astrIntActIDs[1] )

c_fileIntActData3DAT	=	f_fileIntActDAT( c_astrIntActIDs[2] )
c_fileIntActData3QUANT	=	f_fileIntActQUANT( c_astrIntActIDs[2] )
c_fileIntActData3PKL	=	f_fileIntActPKL( c_astrIntActIDs[2] )

c_IntActData1DAT	=	[['O43187', 'P51617', '1'],
				['O43187', 'Q9Y616', '1'],
				['O43187', 'Q9Y4K3', '1'],
				['O43187', 'Q99836', '1'],
				['P51617', 'Q9Y616', '1'],
				['P51617', 'Q9Y4K3', '1'],
				['P51617', 'Q99836', '1'],
				['Q9Y616', 'Q9Y4K3', '1'],
				['Q9Y616', 'Q99836', '1']]	
c_IntActData1PKL	=	{'platform': 'anti tag coip', 'pmid': '10383454', \
					'type': 'physical association', 'taxid': '9606'}

c_IntActData1QUANT	= 	[["0.5","1.5"]]

c_IntActData2DAT	=	[['EBI-2011951', 'P13556', '1'],
				['P13556', 'Q52690', '1'],
				['P13556', 'Q2MHS1', '1'],
				['EBI-2011955', 'EBI-2011958', '1']] 
c_IntActData2PKL	=	{'platform': '2 hybrid',
 				 'pmid': '12923097',
				 'taxid': '1061',
				 'type': 'physical association'}
c_IntActData2QUANT	=	[["0.5","1.5"]]

c_IntActData3DAT	=	[['P33517', 'Q03736', '1'],
				['P33517', 'P84153', '1'],
				['P33517', 'Q8KRK5', '1']]
c_IntActData3PKL	=	{'platform': 'x-ray diffraction',
				 'pmid': '12144789',
 				 'taxid': '1063',
				 'type': 'physical association'}
c_IntActData3QUANT	= 	[["0.5","1.5"]]

#Test data 
exec_test( c_dirIntAct, None, [c_fileIntActData1DAT, c_IntActData1DAT], \
		[c_fileIntActData1QUANT, c_IntActData1QUANT], \
		[c_fileIntActData2DAT, c_IntActData2DAT], \
		[c_fileIntActData2QUANT, c_IntActData2QUANT], \
		[c_fileIntActData3DAT, c_IntActData3DAT], \
		[c_fileIntActData3QUANT, c_IntActData3QUANT] ) 
#Test metadata 
exec_test( c_dirIntAct, lambda f: pickle.load(open(f, "r")), \
		[c_fileIntActData1PKL, c_IntActData1PKL], \
		[c_fileIntActData2PKL, c_IntActData2PKL], \
		[c_fileIntActData3PKL, c_IntActData3PKL] )
#=====================================================#
#                       MPIDB
#=====================================================#
#multiple datasets

c_astrMPIDBIDs		= ["taxid_1772", "taxid_446", "taxid_899"]

c_dirMPIDB		= sfle.d( arepa.path_arepa( ), c_strMPIDB )
c_dirMPIDBData		= sfle.d( c_dirMPIDB, sfle.c_strDirData )

c_fileMPIDBData1DAT	= sfle.d( c_dirMPIDBData,c_astrMPIDBIDs[0],c_astrMPIDBIDs[0] + ".dat" )
c_fileMPIDBData1QUANT	= sfle.d( c_dirMPIDBData,c_astrMPIDBIDs[0],c_astrMPIDBIDs[0] + ".quant" )
c_fileMPIDBData1PKL	= sfle.d( c_dirMPIDBData,c_astrMPIDBIDs[0],c_astrMPIDBIDs[0] + ".pkl" )

c_fileMPIDBData2DAT	= sfle.d( c_dirMPIDBData,c_astrMPIDBIDs[1],c_astrMPIDBIDs[1] + ".dat" )
c_fileMPIDBData2QUANT	= sfle.d( c_dirMPIDBData,c_astrMPIDBIDs[1],c_astrMPIDBIDs[1] + ".quant" )
c_fileMPIDBData2PKL	= sfle.d( c_dirMPIDBData,c_astrMPIDBIDs[1],c_astrMPIDBIDs[1] + ".pkl" )

c_fileMPIDBData3DAT	= sfle.d( c_dirMPIDBData,c_astrMPIDBIDs[2],c_astrMPIDBIDs[2] + ".dat" )
c_fileMPIDBData3QUANT	= sfle.d( c_dirMPIDBData,c_astrMPIDBIDs[2],c_astrMPIDBIDs[2] + ".quant" )
c_fileMPIDBData3PKL	= sfle.d( c_dirMPIDBData,c_astrMPIDBIDs[2],c_astrMPIDBIDs[2] + ".pkl" )

c_MPIDBData1DAT		= [["Q9F408", "Q9F409", "1"]] 
c_MPIDBData1QUANT	= [["0.5", "1.5"]]
c_MPIDBData1PKL		= {'platform': 'ubiquitin reconstruction',
 				'pmid': '12427759',
 				'taxid': '1772',
				'type': 'physical association'}

c_MPIDBData2DAT		= [["O54568","O54635","1"]] 
c_MPIDBData2QUANT	= [["0.5", "1.5"]]
c_MPIDBData2PKL		= {'platform': set(['coimmunoprecipitation',
      				'enzyme linked immunosorbent assay']),
 				'pmid': '11401716',
 				'taxid': '446',
 				'type': 'physical association'}

c_MPIDBData3DAT		= [['P13063', 'P13065', '1']]
c_MPIDBData3QUANT	= [["0.5", "1.5"]]
c_MPIDBData3PKL		= {'platform': 'x-ray crystallography',
				 'pmid': '10378275',
				 'taxid': '899',
				 'type': 'physical association'}

#test data 
exec_test( c_dirMPIDB, None, [c_fileMPIDBData1DAT, c_MPIDBData1DAT],\
		[c_fileMPIDBData2DAT, c_MPIDBData2DAT],\
		[c_fileMPIDBData3DAT, c_MPIDBData3DAT],\
		[c_fileMPIDBData1QUANT, c_MPIDBData1QUANT],\
		[c_fileMPIDBData2QUANT, c_MPIDBData2QUANT],\
		[c_fileMPIDBData3QUANT, c_MPIDBData3QUANT] )

#test metadata 
exec_test( c_dirMPIDB, lambda f: pickle.load( open(f,"r") ), 
		[c_fileMPIDBData1PKL, c_MPIDBData1PKL],\
		[c_fileMPIDBData2PKL, c_MPIDBData2PKL],\
		[c_fileMPIDBData3PKL, c_MPIDBData3PKL] )

#=====================================================#
#                       RegulonDB 
#=====================================================#
#single dataset  

c_dirRegulon		= sfle.d( arepa.path_arepa( ), "RegulonDB" )
c_dirRegulonData	= sfle.d( c_dirRegulon, sfle.c_strDirData ) 

c_RegulonDatLst		= [['AccB', 'accB', '1'],
			['AccB', 'accC', '1'], 
			['AcrR', 'acrA', '1'], 
			['AcrR', 'acrB', '1']]
c_RegulonQuantLst	= [["0.5", "1.5"]]

c_fileRegulonDat	= sfle.d( c_dirRegulonData, "regulondb.dat" )
c_fileRegulonQuant	= sfle.d( c_dirRegulonData, "regulondb.quant" ) 

#test data  
exec_test( c_dirRegulon, None, [c_fileRegulonDat, c_RegulonDatLst], [c_fileRegulonQuant, c_RegulonQuantLst] ) 

#=====================================================#
#                       STRING
#=====================================================#
#multiple datasets 

c_strSTRINGtaxid		= "taxid_189918_mode"
c_strSTRINGtaxidBinding		= c_strSTRINGtaxid + "_binding" 
c_strSTRINGtaxidExpression	= c_strSTRINGtaxid + "_expression"
c_strSTRINGtaxidPtmod		= c_strSTRINGtaxid + "_ptmod"

c_dirSTRING		= sfle.d( arepa.path_arepa( ), "STRING" )
c_dirSTRINGData		= sfle.d( c_dirSTRING, sfle.c_strDirData )

c_dirSTRINGtaxidBinding 	= sfle.d( c_dirSTRINGData, c_strSTRINGtaxidBinding )
c_fileSTRINGtaxidBindingDat	= sfle.d( c_dirSTRINGtaxidBinding, c_strSTRINGtaxidBinding + ".dat" )
c_fileSTRINGtaxidBindingQuant	= sfle.d( c_dirSTRINGtaxidBinding, c_strSTRINGtaxidBinding + ".quant")

c_dirSTRINGtaxidExpression  	= sfle.d( c_dirSTRINGData, c_strSTRINGtaxidExpression )
c_fileSTRINGtaxidExpressionDat	= sfle.d( c_dirSTRINGtaxidExpression, c_strSTRINGtaxidExpression + \
					".dat" )
c_fileSTRINGtaxidExpressionQuant= sfle.d( c_dirSTRINGtaxidExpression, c_strSTRINGtaxidExpression + \
					".quant" )

c_dirSTRINGtaxidPtmod		= sfle.d( c_dirSTRINGData, c_strSTRINGtaxidPtmod )
c_fileSTRINGtaxidPtmodDat	= sfle.d( c_dirSTRINGtaxidPtmod, c_strSTRINGtaxidPtmod + \
					".dat" )
c_fileSTRINGtaxidPtmodQuant	= sfle.d( c_dirSTRINGtaxidPtmod, c_strSTRINGtaxidPtmod + \
					".quant" )

c_STRINGtaxidBindingDat		= [['Mkms_5492', 'Mkms_2727', '0.322'],
				['Mkms_5492', 'Mkms_2193', '0.322'],
				['Mkms_5492', 'Mkms_3950', '0.306'],
				['Mkms_5492', 'Mkms_3510', '0.298'],
				['Mkms_5492', 'Mkms_2005', '0.272'],
				['Mkms_5492', 'Mkms_1151', '0.28'],
				['Mkms_5492', 'Mkms_1004', '0.264'],
				['Mkms_5492', 'Mkms_4326', '0.322'],
				['Mkms_5492', 'Mkms_0514', '0.292'],
				['Mkms_5492', 'Mkms_0939', '0.3']]
c_STRINGtaxidBindingQuant	= [["0.5","1.5"]]

c_STRINGtaxidExpressionDat	= [['Mkms_1995', 'Mkms_2223', '0.346'],
				['Mkms_2223', 'Mkms_4068', '0.35'],
				['Mkms_2223', 'Mkms_2460', '0.181'],
				['Mkms_2223', 'Mkms_5148', '0.359'],
				['Mkms_2223', 'Mkms_1397', '0.272'],
				['Mkms_3390', 'Mkms_0476', '0.21'],
				['Mkms_0476', 'Mkms_0473', '0.714'],
				['Mkms_1345', 'Mkms_4126', '0.197'],
				['Mkms_4068', 'Mkms_5011', '0.181'],
				['Mkms_4068', 'Mkms_1397', '0.357'],
				['Mkms_3160', 'Mkms_3147', '0.265']] 
c_STRINGtaxidExpressionQuant	= [["0.5","1.5"]]

c_STRINGtaxidPtmodDat		= [['Mkms_0391', 'Mkms_0470', '0.173'],
				['Mkms_0391', 'Mkms_2458', '0.316'],
				['Mkms_1218', 'Mkms_5095', '0.226'],
				['Mkms_0025', 'Mkms_0023', '0.445'],
				['Mkms_3334', 'Mkms_3333', '0.365'],
				['Mkms_2004', 'Mkms_2003', '0.204']]
c_STRINGtaxidPtmodQuant 	= [["0.5","1.5"]]

exec_test( c_dirSTRING, None, [c_fileSTRINGtaxidBindingQuant, c_STRINGtaxidBindingQuant],\
		[c_fileSTRINGtaxidBindingDat, c_STRINGtaxidBindingDat],\
		[c_fileSTRINGtaxidExpressionQuant, c_STRINGtaxidExpressionQuant],\
		[c_fileSTRINGtaxidExpressionDat, c_STRINGtaxidExpressionDat],\
		[c_fileSTRINGtaxidPtmodQuant, c_STRINGtaxidPtmodQuant],\
		[c_fileSTRINGtaxidPtmodDat, c_STRINGtaxidPtmodDat] )

