##############################################################################
#
# An example of converting a Pandas dataframe to an xlsx file
# with column formats using Pandas and XlsxWriter.
#
# SPDX-License-Identifier: BSD-2-Clause
# Copyright 2013-2023, John McNamara, jmcnamara@cpan.org
#

import pandas as pd
import numpy as np
import pprint
import copy

# Create a Pandas dataframe from some data.
df = pd.DataFrame()

Ships = [
    "ANZAC",
    "ARUNTA",
    "WARRAMUNGA",
    "STURT",
    "PARAMATTA",
    "BALLARAT",
    "TOWOOMBA",
    "PERTH"
]

Phasing = [0,0,0,0,0,0,0,0]

Parameters = {
    'Years': { #Years Parameters 
        'Value': 20,
        'Boundaries': [10, 20]
    },
    'Start': {
        'Value': 1000,
        'Boundaries': [0, 4500]
    },
    'End': {
        'Value': 2000,
        'Boundaries': [0, 4500]
    },
    'IMAV': {
        'Value': 9,
        'Boundaries': [0, 15]
    },
    'SRA': {
        'Value': 13,
        'Boundaries': [0, 20]
    },
    'DSRA': {
        'Value': 14,
        'Boundaries': [0, 20]
    },
    'DOM_to_DOM': { #Constraint Defines the maximum period wh
        'Value': 52,
        'Boundaries': [30, 80]
    },
    'CI': { # Capability Insertion 
        'Value': 86,
        'Boundaries': [50, 100]
    },
    'FG_IMAV': { #Length
        'Value': 2,
        'Boundaries': [0, 5]
    },
    'FG_SRA': {
        'Value': 25,
        'Boundaries': [0, 50]
    },
    'FG_DSRA': {
        'Value': 25,
        'Boundaries': [0, 50]
    },
    'FG_CI': {
        'Value': 30,
        'Boundaries': [0, 50]
    },
    'CI_Baseline_Insertion_Round': {
        'Value': 7,
        'Boundaries': [0, 20]
    },
    'Phasing_Multiple': {
        'Value': 0,
        'Boundaries': [0, 100]
    }
}

Pattern = [
    {
        'name': "IMAV",
        'duration': Parameters['IMAV']['Value'],
        'start': 0,
        'class': 3
    }, {
        'name': "FG",
        'duration': Parameters['FG_IMAV']['Value'],
        'start': 0,
        'class': 2
    }, {
        'name': "OPS",
        'duration':(Parameters['DOM_to_DOM']['Value']-Parameters['FG_IMAV']['Value']-Parameters['SRA']['Value']),
        'start': 0,
        'class': 1
    }, {
        'name': "SRA",
        'duration': Parameters['SRA']['Value'],
        'start': 0,
        'class': 3,
    }, {
        'name': "FG",
        'duration': Parameters['FG_SRA']['Value'],
        'start': 0,
        'class': 2,
    }, {
        'name': "OPS",
        'duration': (Parameters['DOM_to_DOM']['Value']-Parameters['FG_SRA']['Value']-Parameters['IMAV']['Value']),
        'start': 0,
        'class': 1
    }, {
        'name': "IMAV",
        'duration': Parameters['IMAV']['Value'],
        'start': 0,
        'class': 3
    }, {
        'name': "FG",
        'duration': Parameters['FG_IMAV']['Value'],
        'start': 0,
        'class': 2
    }, {
        'name': "OPS",
        'duration': (Parameters['DOM_to_DOM']['Value']-Parameters['FG_IMAV']['Value']-Parameters['DSRA']['Value']),
        'start': 0,
        'class': 1
    }, {
        'name': "DSRA",
        'duration': Parameters['DSRA']['Value'],
        'start': 0,
        'class': 3
    }, {
        'name': "FG",
        'duration': Parameters['FG_DSRA']['Value'],
        'start': 0,
        'class': 2
    }, {
        'name': "OPS",
        'duration': (Parameters['DOM_to_DOM']['Value']-Parameters['FG_DSRA']['Value']-Parameters['IMAV']['Value']),
        'start': 0,
        'class': 1
    }
]

#t
def setBaseline(Pattern, Parameters):
    Schedule = []
    Schedule = copy.deepcopy(Pattern)
    Schedule[0]['start'] = 0
    for i,a in enumerate(Schedule[1:]):
        Schedule.append(copy.deepcopy(Pattern[i]))
        Schedule[i]['start'] = Pattern[(i-1)]['start'] + Pattern[(i-1)]['duration']
    return Schedule



def createIndex(Baseline):
    Indexed = []
    for e in Baseline:
        for i in range(e['duration']):
            Indexed.append(e['class'])
    return Indexed


def getShipUUCS(Index, Parameters, PhasingValues):
    ShipUUCS = [[],[],[],[],[],[],[],[]]
    for i in range(len(PhasingValues)):
        opSqueeze = 0
        for j in range(Parameters['Start']['Value'],Parameters['End']['Value']):
            ShipUUCS[i].append(Index[j+PhasingValues[i]])
    return ShipUUCS

Baseline = setBaseline(Pattern,Parameters)
pprint.pprint(Baseline)
Index = createIndex(Baseline)
pprint.pprint(Index)
UUC = getShipUUCS(Index,Parameters,Phasing)

#pprint.pprint(Baseline)
#print(Index)
#print(UUC)
# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter("pandas_column_formats.xlsx", engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='Sheet1')

# Get the xlsxwriter workbook and worksheet objects.
workbook  = writer.book
worksheet = writer.sheets['Sheet1']


for i in range(8):
    worksheet.write_row(('G'+str(i)), UUC[i])

worksheet.hide_gridlines(2)
# Add some cell formats.
format1 = workbook.add_format({})
red_format = workbook.add_format({'bg_color': '#FF0000',
                               'font_color': '#FF0000'})
green_format = workbook.add_format({'bg_color': '#92D051',
                               'font_color': '#92D051'})
orange_format = workbook.add_format({'bg_color': '#FEC000',
                               'font_color': '#FEC000'})

# Note: It isn't possible to format any cells that already have a format such
# as the index or headers or any cells that contain dates or datetimes.

# Set the column width and format.
worksheet.set_column_pixels(6,1000,1)

worksheet.conditional_format('G1:ALN8', {'type':     'cell',
                                        'criteria': '=',
                                        'value':    3,
                                        'format':   green_format})

worksheet.conditional_format('G1:ALN8', {'type':     'cell',
                                        'criteria': '=',
                                        'value':    2,
                                        'format':   orange_format})

worksheet.conditional_format('G1:ALN8', {'type':     'cell',
                                        'criteria': '=',
                                        'value':    1,
                                        'format':   red_format})

# Close the Pandas Excel writer and output the Excel file.
writer.close()