open_file_answer = '''All
coordinates.put(new PdfObjectType(PdfObjectType.PDF_OBJECT_TYPE.T1_FIRST_NAME), new PdfObjectCoord(461, 325, 754, 43));
coordinates.put(new PdfObjectType(PdfObjectType.PDF_OBJECT_TYPE.T1_LAST_NAME), new PdfObjectCoord(461, 375, 754, 43));
coordinates.put(new PdfObjectType(PdfObjectType.PDF_OBJECT_TYPE.T1_STREET), new PdfObjectCoord(461, 578, 754, 43));
coordinates.put(new PdfObjectType(PdfObjectType.PDF_OBJECT_TYPE.T1_STREET_1), new PdfObjectCoord(461, 525, 216, 43));				
coordinates.put(new PdfObjectType(PdfObjectType.PDF_OBJECT_TYPE.T1_PO), new PdfObjectCoord(461, 624, 754, 43));
coordinates.put(new PdfObjectType(PdfObjectType.PDF_OBJECT_TYPE.T1_RR), new PdfObjectCoord(461, 624, 754, 43));
coordinates.put(new PdfObjectType(PdfObjectType.PDF_OBJECT_TYPE.T1_CITY), new PdfObjectCoord(461, 679, 754, 43));
coordinates.put(new PdfObjectType(PdfObjectType.PDF_OBJECT_TYPE.T1_PROVINCE), new PdfObjectCoord(461, 729, 140, 43));
coordinates.put(new PdfObjectType(PdfObjectType.PDF_OBJECT_TYPE.T1_POSTAL_CODE), new PdfObjectCoord(910, 729, 300, 43));
coordinates.put(new PdfObjectType(PdfObjectType.PDF_OBJECT_TYPE.T1_SIN), new PdfObjectCoord(2114, 324, 341, 43));
coordinates.put(new PdfObjectType(PdfObjectType.PDF_OBJECT_TYPE.T1_DOB), new PdfObjectCoord(2114, 376, 341, 43));
coordinates.put(new PdfObjectType(PdfObjectType.PDF_OBJECT_TYPE.T1_EMAIL), new PdfObjectCoord(461, 1023, 793, 43));
coordinates.put(new PdfObjectType(PdfObjectType.PDF_OBJECT_TYPE.T1_PROV_OF_RES), new PdfObjectCoord(487, 1226, 793, 43));
coordinates.put(new PdfObjectType(PdfObjectType.PDF_OBJECT_TYPE.T1_SPOUSE_NAME), new PdfObjectCoord(1892,1175, 572, 43));
coordinates.put(new PdfObjectType(PdfObjectType.PDF_OBJECT_TYPE.T1_SPOUSE_SIN), new PdfObjectCoord(2116, 1126, 342, 43));
coordinates.put(new PdfObjectType(PdfObjectType.PDF_OBJECT_TYPE.T1_MARRIED), new PdfObjectCoord(1918, 875, 535, 52));

BC
coordinates.put(new PdfObjectType(PdfObjectType.PDF_OBJECT_TYPE.T1_CITIZENSHIP_Y), new PdfObjectCoord(2037, 2116, 105, 61));
coordinates.put(new PdfObjectType(PdfObjectType.PDF_OBJECT_TYPE.T1_CITIZENSHIP_N), new PdfObjectCoord(2312, 2116, 105, 61));

ON
coordinates.put(new PdfObjectType(PdfObjectType.PDF_OBJECT_TYPE.T1_CITIZENSHIP_Y), new PdfObjectCoord(2037, 1916, 105, 61));
coordinates.put(new PdfObjectType(PdfObjectType.PDF_OBJECT_TYPE.T1_CITIZENSHIP_N), new PdfObjectCoord(2312, 1916, 105, 61));

NT
coordinates.put(new PdfObjectType(PdfObjectType.PDF_OBJECT_TYPE.T1_CITIZENSHIP_Y), new PdfObjectCoord(2037, 2316, 105, 61));
coordinates.put(new PdfObjectType(PdfObjectType.PDF_OBJECT_TYPE.T1_CITIZENSHIP_N), new PdfObjectCoord(2312, 2316, 105, 61));

NL
coordinates.put(new PdfObjectType(PdfObjectType.PDF_OBJECT_TYPE.T1_CITIZENSHIP_Y), new PdfObjectCoord(2037, 2116, 105, 61));
coordinates.put(new PdfObjectType(PdfObjectType.PDF_OBJECT_TYPE.T1_CITIZENSHIP_N), new PdfObjectCoord(2312, 2116, 105, 61));

YT
coordinates.put(new PdfObjectType(PdfObjectType.PDF_OBJECT_TYPE.T1_CITIZENSHIP_Y), new PdfObjectCoord(2037, 2216, 105, 61));
coordinates.put(new PdfObjectType(PdfObjectType.PDF_OBJECT_TYPE.T1_CITIZENSHIP_N), new PdfObjectCoord(2312, 2216, 105, 61));

QC
coordinates.put(new PdfObjectType(PdfObjectType.PDF_OBJECT_TYPE.T1_CITIZENSHIP_Y), new PdfObjectCoord(2037, 1916, 105, 61));
coordinates.put(new PdfObjectType(PdfObjectType.PDF_OBJECT_TYPE.T1_CITIZENSHIP_N), new PdfObjectCoord(2312, 1916, 105, 61));

None
coordinates.put(new PdfObjectType(PdfObjectType.PDF_OBJECT_TYPE.T1_CITIZENSHIP_Y), new PdfObjectCoord(2037, 1916, 105, 61));
coordinates.put(new PdfObjectType(PdfObjectType.PDF_OBJECT_TYPE.T1_CITIZENSHIP_N), new PdfObjectCoord(2312, 1916, 105, 61));'''

parse_input = '''All
coordinates.put(new PdfObjectType(PdfObjectType.PDF_OBJECT_TYPE.T1_FIRST_NAME), new PdfObjectCoord(461, 325, 754, 43));
coordinates.put(new PdfObjectType(PdfObjectType.PDF_OBJECT_TYPE.T1_LAST_NAME), new PdfObjectCoord(461, 375, 754, 43));
coordinates.put(new PdfObjectType(PdfObjectType.PDF_OBJECT_TYPE.T1_STREET), new PdfObjectCoord(461, 578, 754, 43));
coordinates.put(new PdfObjectType(PdfObjectType.PDF_OBJECT_TYPE.T1_STREET_1), new PdfObjectCoord(461, 525, 216, 43));				
coordinates.put(new PdfObjectType(PdfObjectType.PDF_OBJECT_TYPE.T1_PO), new PdfObjectCoord(461, 624, 754, 43));
coordinates.put(new PdfObjectType(PdfObjectType.PDF_OBJECT_TYPE.T1_RR), new PdfObjectCoord(461, 624, 754, 43));
coordinates.put(new PdfObjectType(PdfObjectType.PDF_OBJECT_TYPE.T1_CITY), new PdfObjectCoord(461, 679, 754, 43));
coordinates.put(new PdfObjectType(PdfObjectType.PDF_OBJECT_TYPE.T1_PROVINCE), new PdfObjectCoord(461, 729, 140, 43));
coordinates.put(new PdfObjectType(PdfObjectType.PDF_OBJECT_TYPE.T1_POSTAL_CODE), new PdfObjectCoord(910, 729, 300, 43));
coordinates.put(new PdfObjectType(PdfObjectType.PDF_OBJECT_TYPE.T1_SIN), new PdfObjectCoord(2114, 324, 341, 43));
coordinates.put(new PdfObjectType(PdfObjectType.PDF_OBJECT_TYPE.T1_DOB), new PdfObjectCoord(2114, 376, 341, 43));
coordinates.put(new PdfObjectType(PdfObjectType.PDF_OBJECT_TYPE.T1_EMAIL), new PdfObjectCoord(461, 1023, 793, 43));
coordinates.put(new PdfObjectType(PdfObjectType.PDF_OBJECT_TYPE.T1_PROV_OF_RES), new PdfObjectCoord(487, 1226, 793, 43));
coordinates.put(new PdfObjectType(PdfObjectType.PDF_OBJECT_TYPE.T1_SPOUSE_NAME), new PdfObjectCoord(1892,1175, 572, 43));
coordinates.put(new PdfObjectType(PdfObjectType.PDF_OBJECT_TYPE.T1_SPOUSE_SIN), new PdfObjectCoord(2116, 1126, 342, 43));
coordinates.put(new PdfObjectType(PdfObjectType.PDF_OBJECT_TYPE.T1_MARRIED), new PdfObjectCoord(1918, 875, 535, 52));

BC
coordinates.put(new PdfObjectType(PdfObjectType.PDF_OBJECT_TYPE.T1_CITIZENSHIP_Y), new PdfObjectCoord(2037, 2116, 105, 61));
coordinates.put(new PdfObjectType(PdfObjectType.PDF_OBJECT_TYPE.T1_CITIZENSHIP_N), new PdfObjectCoord(2312, 2116, 105, 61));

ON
coordinates.put(new PdfObjectType(PdfObjectType.PDF_OBJECT_TYPE.T1_CITIZENSHIP_Y), new PdfObjectCoord(2037, 1916, 105, 61));
coordinates.put(new PdfObjectType(PdfObjectType.PDF_OBJECT_TYPE.T1_CITIZENSHIP_N), new PdfObjectCoord(2312, 1916, 105, 61));

NT
coordinates.put(new PdfObjectType(PdfObjectType.PDF_OBJECT_TYPE.T1_CITIZENSHIP_Y), new PdfObjectCoord(2037, 2316, 105, 61));

NL
coordinates.put(new PdfObjectType(PdfObjectType.PDF_OBJECT_TYPE.T1_CITIZENSHIP_Y), new PdfObjectCoord(2037, 2116, 105, 61));

YT
coordinates.put(new PdfObjectType(PdfObjectType.PDF_OBJECT_TYPE.T1_CITIZENSHIP_Y), new PdfObjectCoord(2037, 2216, 105, 61));
coordinates.put(new PdfObjectType(PdfObjectType.PDF_OBJECT_TYPE.T1_CITIZENSHIP_N), new PdfObjectCoord(2312, 2216, 105, 61));

QC
coordinates.put(new PdfObjectType(PdfObjectType.PDF_OBJECT_TYPE.T1_CITIZENSHIP_Y), new PdfObjectCoord(2037, 1916, 105, 61));

None
coordinates.put(new PdfObjectType(PdfObjectType.PDF_OBJECT_TYPE.T1_CITIZENSHIP_Y), new PdfObjectCoord(2037, 1916, 105, 61));'''

parse_answer = {
    'All': '''coordinates.put(new PdfObjectType(PdfObjectType.PDF_OBJECT_TYPE.T1_FIRST_NAME), new PdfObjectCoord(461, 325, 754, 43));
coordinates.put(new PdfObjectType(PdfObjectType.PDF_OBJECT_TYPE.T1_LAST_NAME), new PdfObjectCoord(461, 375, 754, 43));
coordinates.put(new PdfObjectType(PdfObjectType.PDF_OBJECT_TYPE.T1_STREET), new PdfObjectCoord(461, 578, 754, 43));
coordinates.put(new PdfObjectType(PdfObjectType.PDF_OBJECT_TYPE.T1_STREET_1), new PdfObjectCoord(461, 525, 216, 43));				
coordinates.put(new PdfObjectType(PdfObjectType.PDF_OBJECT_TYPE.T1_PO), new PdfObjectCoord(461, 624, 754, 43));
coordinates.put(new PdfObjectType(PdfObjectType.PDF_OBJECT_TYPE.T1_RR), new PdfObjectCoord(461, 624, 754, 43));
coordinates.put(new PdfObjectType(PdfObjectType.PDF_OBJECT_TYPE.T1_CITY), new PdfObjectCoord(461, 679, 754, 43));
coordinates.put(new PdfObjectType(PdfObjectType.PDF_OBJECT_TYPE.T1_PROVINCE), new PdfObjectCoord(461, 729, 140, 43));
coordinates.put(new PdfObjectType(PdfObjectType.PDF_OBJECT_TYPE.T1_POSTAL_CODE), new PdfObjectCoord(910, 729, 300, 43));
coordinates.put(new PdfObjectType(PdfObjectType.PDF_OBJECT_TYPE.T1_SIN), new PdfObjectCoord(2114, 324, 341, 43));
coordinates.put(new PdfObjectType(PdfObjectType.PDF_OBJECT_TYPE.T1_DOB), new PdfObjectCoord(2114, 376, 341, 43));
coordinates.put(new PdfObjectType(PdfObjectType.PDF_OBJECT_TYPE.T1_EMAIL), new PdfObjectCoord(461, 1023, 793, 43));
coordinates.put(new PdfObjectType(PdfObjectType.PDF_OBJECT_TYPE.T1_PROV_OF_RES), new PdfObjectCoord(487, 1226, 793, 43));
coordinates.put(new PdfObjectType(PdfObjectType.PDF_OBJECT_TYPE.T1_SPOUSE_NAME), new PdfObjectCoord(1892,1175, 572, 43));
coordinates.put(new PdfObjectType(PdfObjectType.PDF_OBJECT_TYPE.T1_SPOUSE_SIN), new PdfObjectCoord(2116, 1126, 342, 43));
coordinates.put(new PdfObjectType(PdfObjectType.PDF_OBJECT_TYPE.T1_MARRIED), new PdfObjectCoord(1918, 875, 535, 52));''',

    'BC': '''coordinates.put(new PdfObjectType(PdfObjectType.PDF_OBJECT_TYPE.T1_CITIZENSHIP_Y), new PdfObjectCoord(2037, 2116, 105, 61));
coordinates.put(new PdfObjectType(PdfObjectType.PDF_OBJECT_TYPE.T1_CITIZENSHIP_N), new PdfObjectCoord(2312, 2116, 105, 61));''',

    'ON': '''coordinates.put(new PdfObjectType(PdfObjectType.PDF_OBJECT_TYPE.T1_CITIZENSHIP_Y), new PdfObjectCoord(2037, 1916, 105, 61));
coordinates.put(new PdfObjectType(PdfObjectType.PDF_OBJECT_TYPE.T1_CITIZENSHIP_N), new PdfObjectCoord(2312, 1916, 105, 61));''',
    'NT':'coordinates.put(new PdfObjectType(PdfObjectType.PDF_OBJECT_TYPE.T1_CITIZENSHIP_Y), new PdfObjectCoord(2037, 2316, 105, 61));',
    'NL':'coordinates.put(new PdfObjectType(PdfObjectType.PDF_OBJECT_TYPE.T1_CITIZENSHIP_Y), new PdfObjectCoord(2037, 2116, 105, 61));',
    'YT':'''coordinates.put(new PdfObjectType(PdfObjectType.PDF_OBJECT_TYPE.T1_CITIZENSHIP_Y), new PdfObjectCoord(2037, 2216, 105, 61));
coordinates.put(new PdfObjectType(PdfObjectType.PDF_OBJECT_TYPE.T1_CITIZENSHIP_N), new PdfObjectCoord(2312, 2216, 105, 61));''',
    'QC':'coordinates.put(new PdfObjectType(PdfObjectType.PDF_OBJECT_TYPE.T1_CITIZENSHIP_Y), new PdfObjectCoord(2037, 1916, 105, 61));',
    'None':'coordinates.put(new PdfObjectType(PdfObjectType.PDF_OBJECT_TYPE.T1_CITIZENSHIP_Y), new PdfObjectCoord(2037, 1916, 105, 61));'
}

get_coordinates_output = {'All':{'FIRST_NAME': '461, 325, 754, 43', 'LAST_NAME': '461, 375, 754, 43', 
'STREET': '461, 578, 754, 43', 'STREET_1': '461, 525, 216, 43', 
'PO': '461, 624, 754, 43', 'RR': '461, 624, 754, 43', 
'CITY': '461, 679, 754, 43', 'PROVINCE': '461, 729, 140, 43', 
'POSTAL_CODE': '910, 729, 300, 43', 'SIN': '2114, 324, 341, 43', 
'DOB': '2114, 376, 341, 43', 'EMAIL': '461, 1023, 793, 43', 
'PROV_OF_RES': '487, 1226, 793, 43', 'SPOUSE_NAME': '1892,1175, 572, 43', 
'SPOUSE_SIN': '2116, 1126, 342, 43', 'MARRIED': '1918, 875, 535, 52'}, 
'BC': {'CITIZENSHIP_Y': '2037, 2116, 105, 61', 'CITIZENSHIP_N': '2312, 2116, 105, 61'}, 
'ON': {'CITIZENSHIP_Y': '2037, 1916, 105, 61', 'CITIZENSHIP_N': '2312, 1916, 105, 61'}, 
'NT': {'CITIZENSHIP_Y': '2037, 2316, 105, 61'}, 
'NL': {'CITIZENSHIP_Y': '2037, 2116, 105, 61'}, 
'YT': {'CITIZENSHIP_Y': '2037, 2216, 105, 61', 'CITIZENSHIP_N': '2312, 2216, 105, 61'}, 
'QC': {'CITIZENSHIP_Y': '2037, 1916, 105, 61'}, 
'None': {'CITIZENSHIP_Y': '2037, 1916, 105, 61'}}

pixels_to_pdf_points_input = {'All':{'FIRST_NAME': '461, 325, 754, 43'}}

pixels_to_pdf_points_output = {'All': {'FIRST_NAME': ('110.64018', '78.00012', '180.96029', '10.32002')}}

write_csv_output = 'All,FIRST_NAME,110.64018,78.00012,180.96029,10.32002'
