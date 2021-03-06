from bots.botsconfig import *
#from records004010 import recorddefs

syntax = {
        'version'    :  '00403',    #version of ISA to send
        #'functionalgroup'    :  'HC',
        }

#ST*315*2457277~
#B4*315**UA**MRKU*483747*3~
#N9*EQ*MRKU4837473~
#Q2*9303754*********ZZ*ZIMU*L~
#SE*5*2457277~
		
structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'B4', MIN: 1, MAX: 1},
    {ID: 'N9', MIN: 1, MAX: 3},
	{ID: 'Q2', MIN: 1, MAX: 3},
    {ID: 'SE', MIN: 1, MAX: 1},
    ]}
]


recorddefs = {
'B4': [
    ['BOTSID', 'M', 3,'AN'],
    ['B401', 'M', (2,3),'AN'],
    ['B402', 'C', 3,'R'],
    ['B403', 'M', 2,'AN'],
    ['B404', 'C', (8,8),'DT'],
    ['B405', 'M', (4,4),'AN'],
    ['B406', 'M', (3,6),'AN'],
    ['B407', 'M', 1,'AN'],
    ['B408', 'C', 10,'AN'],
    ['B409', 'C', 2,'AN'],
    ['B410', 'C', (4,4),'AN'],
    ['B411', 'C', 30,'AN'],
    ['B412', 'C', 2,'AN'],
    ['B413', 'C', 1,'R'],
],
'ST': [
    ['BOTSID', 'M', 3,'AN'],
    ['ST01', 'M', (3,3),'AN'],
    ['ST02', 'M', (4,9),'AN'],
],
'N9': [
    ['BOTSID', 'M', 3,'AN'],
    ['N901', 'M', (2,3),'AN'],
    ['N902', 'C', 30,'AN'],
    ['N903', 'C', 45,'AN'],
    ['N904', 'C', (8,8),'DT'],
    ['N905', 'C', (4,8),'TM'],
    ['N906', 'C', (2,2),'AN'],
    ['N907', 'C', [
        ['N907.01', 'M', (2,3),'AN'],
        ['N907.02', 'M', 30,'AN'],
        ['N907.03', 'C', (2,3),'AN'],
        ['N907.04', 'C', 30,'AN'],
        ['N907.05', 'C', (2,3),'AN'],
        ['N907.06', 'C', 30,'AN'],
    ]],
],
'Q2': [
    ['BOTSID', 'M', 3,'AN'],
    ['Q201', 'C', 8,'AN'],
    ['Q202', 'C', (2,3),'AN'],
    ['Q203', 'C', (8,8),'DT'],
    ['Q204', 'C', (8,8),'DT'],
    ['Q205', 'C', (8,8),'DT'],
    ['Q206', 'C', 7,'R'],
    ['Q207', 'C', 10,'R'],
    ['Q208', 'C', 2,'AN'],
    ['Q209', 'C', (2,10),'AN'],
    ['Q210', 'M', (2,4),'AN'],
    ['Q211', 'C', 30,'AN'],
    ['Q212', 'C', 1,'AN'],
    ['Q213', 'C', (2,28),'AN'],
    ['Q214', 'C', 8,'R'],
    ['Q215', 'C', 1,'AN'],
    ['Q216', 'C', 1,'AN'],
],
'SE': [
    ['BOTSID', 'M', 3,'AN'],
    ['SE01', 'M', 10,'R'],
    ['SE02', 'M', (4,9),'R'],
],
}

