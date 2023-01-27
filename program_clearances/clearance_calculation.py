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

# add columns to the clearance dataframe

# iterate through the available files
drawing_arr = []
revision_arr = []
fixture_arr = []
py_arr = []
px_arr = []
ny_arr = []
nx_arr = []
for file in filtered_files:

    print(file)

    # extract the current program's data
    data = extract_probe_info(join(pc_raw_export, file))

    # assemble lists
    drawing_arr.append(data["drawing"])
    revision_arr.append(data["revision"])
    fixture_arr.append(data["fixture"])
    py_arr.append(data["py"])
    px_arr.append(data["px"])
    ny_arr.append(data["ny"])
    nx_arr.append(data["nx"])

# create the dataframe
df = pd.DataFrame({
    "drawing": drawing_arr,
    "revision": revision_arr,
    "fixture": fixture_arr,
    "py": py_arr,
    "px": px_arr,
    "ny": ny_arr,
    "nx": nx_arr
})

# save to file
df.to_csv("path_clearances.csv", index = False)