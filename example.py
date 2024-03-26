example = [
    {
        "Query": "display details of all procedures in the increasing order of price where procedure type is GENERAL SURGERIES",
        "SQLQuery": "SELECT  ProcedureType,Description,Price FROM ProceduresDetails WHERE ProcedureType='GENERAL SURGERIES' ORDER BY Price;",
        "SQLResult": "Result of the SQL query",
        "Answer": ''' 'GENERAL SURGERIES', 'Dissolvable Suture', '15'
'GENERAL SURGERIES', 'Peritoneal Lavage', '85'
'GENERAL SURGERIES', 'Aural Hematoma', '108'
'GENERAL SURGERIES', 'Declaw', '125'
'GENERAL SURGERIES', 'Anal Gland Caut', '150'
'GENERAL SURGERIES', 'Umbilical', '175'
'GENERAL SURGERIES', 'Perineal Adenoma', '175'
'GENERAL SURGERIES', 'Unilat Inquinal', '195'
'GENERAL SURGERIES', 'Tail Dock-Amputation', '250'
'GENERAL SURGERIES', 'Ear Crop', '350'
'GENERAL SURGERIES', 'Perineal', '375'
'GENERAL SURGERIES', 'Splenectomy', '375'
'GENERAL SURGERIES', 'Hernia', '390'
'GENERAL SURGERIES', 'Pyloric Stenosis', '425'
'GENERAL SURGERIES', 'Gastric Torsion', '450'
'GENERAL SURGERIES', 'Radical Mastectomy', '450'
'GENERAL SURGERIES', 'Open Chest Surgery', '500'
'GENERAL SURGERIES', 'Salivary Cyst Ex', '570'
'GENERAL SURGERIES', 'Intestinal Anas', '775'
''',
    },
    {
        "Query": "How many pets are male?",
        "SQLQuery": "SELECT count(*) from pets where gender='male'",
        "SQLResult": "Result of the SQL query",
        "Answer": "59",
    },
    
            ]