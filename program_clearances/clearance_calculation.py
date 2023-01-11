# import dependencies
from os import listdir
from os.path import isfile, join
from clearance_functions import extract_probe_info
import pandas as pd

# import confidential information
from sys import path
path.insert(0, "..")
from config import pc_raw_export

# look through the pc-dmis xml export folder
ext = ".xml"
all_files = listdir(pc_raw_export)
filtered_files = list(filter(lambda item: isfile(join(pc_raw_export, item)) and item[-len(ext):].lower() == ext, all_files))

# read the fixture clearance data
clearance_data = pd.read_csv("fixture_clearances.csv")

# add columns to the clearance dataframe


# iterate through the available files
data = []
for file in filtered_files:

    # extract the current program's data
    data.append(extract_probe_info(join(pc_raw_export, file)))