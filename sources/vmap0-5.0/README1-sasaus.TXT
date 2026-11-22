Readme1 File
 
	At the top directory level of this CDROM, the user will find this 
readme1.txt file and two directories named "vmaplv0" and "view."  There is 
also a file named "fgdc_dat.txt" which contains the Federal Geographic Data 
Committee (FGDC) Content Standard for Spatial Metadata as it pertains to 
VMap level 0.

	The directory named "vmaplv0" contains the VMap level 0 (VMap0) 
data.  The next level within the directory "vmaplv0" contains two 
metadata files ("dht" and "lat") and two directories named "sasaus" 
and "rference."  The directory "sasaus" is the VMap0 library where the 
actual data coverages reside. The directory "rference" is a reference 
library for the whole world.  The sasaus library is 502.1 megabytes 
and the reference library is 6.5 megabytes.

	The directory named "view" contains a tailored view, "viewsas," 
that NIMA has created to be used with VPFVIEW software version 2.1 and 
a readme2.txt file with information on the use and installation of the 
provided view. The user must have VPFVIEW software version 2.1 for the 
view to work as intended. The readme2 file provides further information 
regarding the provided view.  VPFVIEW Version 2.1 is available to all 
users from NIMA.  Refer to NIMA's Home page (http://www.nima.mil) on 
the Internet for information on acquiring VPFVIEW version 2.1


REFERENCE LIBRARY

	The reference library for this database was built to describe 
the limits of VMap libraries as they existed at the time of production.  
While the coverage limits of these libraries are essentially static, 
there are occasional small modifications to limits in order to better 
reflect sovereignty, production schedules, and other factors.  A change to 
the boundaries of libraries will drive an update to the reference library 
and will be reflected on all disks produced subsequent to the modification.  
A change to the reference library will not be sufficient to drive the 
release of a new library (disk) edition.


VECTOR PRODUCT FORMAT STANDARD

	This version of VMap0 conforms to the current version of Vector 
Product Format Standard (MIL-STD-2407) published in June 1996.


METADATA

	The VPF data structure allows for metadata to be input at all 
levels within the data.  As such, NIMA has utilized this capability to 
provide users with information regarding assumptions and 
interpretations, to describe source deficiencies, and to explain 
conventions that have been adopted during production. Generally, the 
metadata may be found at the level most appropriate to that particular 
information. 
	The metadata can reside:
		1. within the lineage.doc, 
		2. within the Data Quality Coverage, 
		3. as a Data Quality feature within a coverage, or 
		4. as a document file associated with a coverage, table 
		   or column.  

	The Data Quality Coverage describes the sources used to create 
the library.  Data quality features are associated with specific 
features within any coverage and describe conditions not fully 
addressed by the attribute choices.  Most commonly, data quality 
features will highlight uncertainties related to alignment or placement 
for the given feature.  Data quality area features will most commonly 
describe areas void of some information.  For example, Contour Lines in the 
Elevation Coverage.

	The lineage.doc is a metadata file at the data library level 
that allows free text entry.  NIMA utilizes the lineage.doc to describe 
production methodology including library specific problems and resolutions. 
Document files may describe collection strategies and will be found at 
the feature table level.  Document files may also describe conventions 
used when populating specific attributes and are associated with columns 
within tables.


SOURCE DEFICIENCIES

	VMap0 is primarily based on capturing hardcopy source data. 
Many of these sources pre-date a nominal currency cut-off date.  
Specific source information may be found in the Data Quality Coverage.  
In addition, a number of irreconcilable differences exist at source 
sheet boundaries, largely the result of source date differences.


DATA LIMITATIONS

	VMap0 is a low resolution database derived in large part from 
hardcopy sources.  In order to properly exploit the data the user 
must be aware that the factors of scale and source contribute to some 
limitations resident in the data.  Attempts to position features beyond 
the accuracy statements contained in the Data Quality Coverage are 
meaningless.  For a typical VMap0 library the user may refer to the 
Accuracy Section in the VMap Level 0 Specification (Mil-V-89039, 
9 February 1995).  For example, VMap0 collected from an Operational 
Navigation Chart (ONC) source may only be expected to be accurate to 
within 2040 meters on the ground.  This level of accuracy was not 
achieved in the Antarctic.  

	Features in VMap are collected into topologically structured 
coverages, originally extracted from feature separates.  It is costly to 
fully resolve overlap and gaps between features in different coverages.  
The VMap0 Specification does not permit cross coverage topology, and 
does not require precise geographic coincidence of features between 
coverages.  Thus, the NIMA production policy is to allow gaps between 
features in different coverages according to the following guidelines.  

	1. Overlapping polygons have been eliminated where they existed 
           in the digital data contrary to natural occurrences (e.g. no 
 	   forest/lake overlap).  
	2. Gaps may exist naturally between features.  However, if the 
 	   source clearly indicates that two features should be coincident 
	   or adjacent, and the features by definition are coincident (e.g. 
	   where a river is used to construct a political boundary) then 
	   the gap in the digital VMap0 data will not be larger than 500 
	   meters.  
	3. If the source indicates that two features should be coincident 
	   or adjacent, but the features are not by definition coincident 
	   (as in number 2 above), then the gap in the digital VMap0 data 
	   will not be larger than 1000 meters.

	It is possible that a GIS application may allow for cross coverage 
spatial analysis queries through duplicate coordinate pairs.  Should the 
customer require such applications, it will be necessary to further process 
the data to dissolve the gaps.  These guidelines should provide the proper 
tolerances for such functions.


VPF TO ARC/INFO IMPORTER

	The horizontal resolution of the geographic coordinates for 
all VPF data is stored in the equivalent precision of 0.02 arc-seconds 
or 0.000005 decimal degrees.  Importing VPF data into ARC/INFO at a 
coarser resolution may result in topological errors. The correct procedure 
for importing this coverage requires "Clean and Build" to be performed 
and data manually imported.


DATA NOTES

	Certain features in the Boundaries Coverage and the Reference 
Library contain the intellectual property of Environmental Systems Research 
Institute, Inc. (ESRI) and its licensors.  Copyright (C) 1992-2000 ESRI 
and its licensors.  All rights reserved.  These features are the Boundaries 
Coverage (bnd) edge features representing administrative unit boundaries 
that have an FACC code (f_code) of FA000 and an attribute value of 26 in 
the USE field - First Order Administrative Division features.  Also included 
are Boundary face features with an FACC code (f_code) of FA001 and an 
administrative unit name present in the NAM field.  Within the Reference 
Library (rference) the Library Reference (libref), Place Name (placenam), 
and Political Boundary (polbnd) Coverages also contain intellectual property 
of ESRI.  See the ESRI Data License Agreement contained in this file for 
conditions of use.  

	Many software applications will allow display of attributes as text 
on the screen and at the same time features may be easily queried to obtain 
attribute information.  NIMA has utilized a strategy in which information 
has been stored in attribute strings whenever possible.  This limits the 
use of Text features to situations where information could not be stored 
as attributes.  

	Although the size and font for text is defined within the VMap 
dataset, users may find that their viewing software displays default 
sizes for text which overrides those set within the dataset.  Therefore, 
text displayed may appear too small or too large and cluttered, and thus 
cartographically incorrect.  

	The Vmap0 Military specification does not support the use of any 
diacritic characters for any native proper names and/or native generic 
terms.  

	When displaying the Hydrography or Vegetation coverages using 
VPFVIEW 2.1, anomalies and/or errors may occur.  These problems are due 
to a limitation within the VPFVIEW software.  VPFVIEW has a buffer that 
can only accomadate VPF primitive tables with up to 32,768 records.  The 
Hydrography and Vegetation Coverages each have primitive tables that 
have more than 32,768 records.  

	For this edition of VMap0, the tile sizes were enlarged.  The 
database now has a two-tiered tiling scheme.  Fifteen-by-fifteen degree 
tiles are used over continental landmasses and thirty-by-thirty degree 
tiles are used over the ocean areas.  Tiles are named according to the 
GeoRef value for the lower left (SouthWest) corner of the tile.  Some 
tiles are shared between libraries, but actual data is not shared between 
libraries although it is continuous along library boundaries.  


ESRI DATA LICENSE AGREEMENT 

	This ESRI Data License Agreement (referred to here after as the 
"Agreement") is between you (the "Licensee") and Environmental Systems 
Research Institute, Inc. ("ESRI"), a corporation, with its principal 
place of business at 380 New York Street, Redlands, California, 92373- 
8100, United States of America.  


APPLICABILITY 

	This Agreement ONLY applies to those data in Vmap Level 0 
edition 5.0 supplied by ESRI.  Certain features in the Boundaries 
Coverage and the Reference Library contain intellectual property of 
ESRI and its licensors.  These features are the Boundaries Coverage 
(bnd) edge features representing administrative unit boundaries that 
have an FACC code (f_code) of FA000 and an attribute value of 26 in the 
USE field.  Also included are Boundary face features with an FACC code 
(f_code) of FA001 and an administrative unit name present in the NAM 
field.  Within the Reference Library (rference) the Library Reference 
(libref), Place Name (placenam), and Political Boundary (polbnd) Coverages 
also contain intellectual property of ESRI.  The above described features 
are referred to here after as the "Data".  


INTELLECTUAL PROPERTY RIGHTS AND RESERVATION OF OWNERSHIP 

	The Data are owned by ESRI and its licensor(s) and are protected 
by United States laws and applicable international laws, treaties, and 
conventions regarding intellectual property or proprietary rights.  ESRI 
and its licensor(s) retain all rights, title, and ownership not granted 
herein to all copies of the Data licensed under this Agreement.  Licensee 
agrees to use reasonable effort to protect the Data from unauthorized 
use, reproduction, or distribution.  All rights not specifically granted 
in this Agreement are reserved to ESRI and its licensor(s).


GRANT OF LICENSE 

	ESRI grants to Licensee a personal and nonexclusive license to 
use, copy, reproduce, prepared derivative works, redistribute, and 
retransmit the Data for any internal or noncommercial purposes so long 
as the metadata and license agreement files accompany any redistribution 
of the Data in digital format.  


SCOPE OF USE 

(a) Permitted Uses 
	Licensee may use, copy, reproduce, archive, alter, modify, merge, 
prepare derivative works, publicly display, redistribute, and retransmit 
the Data for any internal or noncommercial purpose. 
	Licensee may provide access to these Data to any consultant or 
contractor of the Licensee, provided that the consultant or contractor 
is using the Data for the benefit of the Licensee, and so long as the 
consultant or contractor agrees to be bound by the terms and conditions 
of this Agreement.  

(b) Uses Not Permitted 
	Licensee shall not rent, lease, sublicense, lend, assign, time- 
share, remarket, resell, or redistribute these Data, or derived portions 
of these Data to third parties in vector format (e.g. geographic Data 
coordinates and/or associated attributes) for commercial purposes 
without the expressed permission of ESRI.  
	Licensee shall not remove or obscure any ESRI or its licensors 
copyright, proprietary, or metadata notices.  


TERM AND TERMINATION 

	This Agreement shall commence upon the date of receipt of the 
Data and shall continue until such time that (i) the Licensee elects to 
discontinue using these Data, or (ii) ESRI elects to terminate for 
material breach.  


DATA DISCLAIMER 

	The Data has been obtained from sources believed to be reliable, 
but its accuracy, currency, and completeness are not guaranteed.  The Data 
may contain some nonconformities, defects, errors, or omissions.  ESRI 
and its Licensors do not warrant that the Data will meet the end users 
needs or expectations, or that all nonconformaities can or will be 
corrected.  ESRI and its Licensors are not inviting reliance on the Data 
and the user should always verify the map and attribute data.  

DISCLAIMER OF WARRENTY AND LIMITATION OF LIABILITY 

	LICENSEE EXPRESSLY ACKNOWLEDGES AND AGREES THAT THE DATA IS 
DELIVERED "AS-IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESS OR 
IMPLIED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF 
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, NONINTERFERENCE, 
SYSTEM INTEGRATION, AND NONINFRINGEMENT.  LICENSEE ASSUMES ALL RISK AS 
TO THE QUALITY AND PERFORMANCE OF THE DATA.  
	IN NO EVENT SHALL ESRI OR ITS LICENSOR BE LIABLE TO LICENSEE 
FOR COSTS OF PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOST PROFITS; 
LOST SALES OR BUSINESS EXPENDITURES; INVESTMENTS; OR COMMITMENTS IN 
CONNECTION WITH ANY BUSINESS, LOSS OF ANY GOODWILL, OR FOR ANY INDIRECT, 
SPECIAL, INCIDENTAL, OR CONSEQUENTIAL DAMAGES ARISING OUT OF OR RELATED 
TO THIS AGREEMENT OR USE OF THE DATA HOWEVER CAUSED, ON ANY THEORY OF 
LIABILITY, AND WHETHER OR NOT ESRI OR ITS LICENSOR HAS BEEN ADVISED OF 
THE POSSIBILITY OF SUCH DAMAGE.  THESE LIMITATIONS SHALL APPLY 
NOTWITHSTANDING ANY FAILURE OF ESSENTIAL PURPOSE OF ANY LIMITED REMEDY. 


GOVERNING LAW
	To the extent that federal law is not dispositive, this Agreement 
shall be governed by and construed in accordance with the laws of the 
State of California without reference to conflict of laws principles.  


ENTIRE AGREEMENT

This Agreement constitutes the sole and entire agreement between ESRI 
and the Licensee as to the subject matter set forth herein.


