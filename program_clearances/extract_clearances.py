# import dependencies
from os import system, getcwd, listdir
from os.path import join, isfile
from clearance_functions import extract_probe_info
import pandas as pd

# import confidential values
from sys import path
path.insert(0, "..")
from config import pc_raw_source, pc_raw_export, clr_root_dir, clr_path_dir

# transform arguments to a Windows friendly format
pcdmis_arg_source = pc_raw_source.replace(" ", "%")
pcdmis_arg_export = pc_raw_export.replace(" ", "%")
sldwks_arg_root_dir = f"\"{clr_root_dir}\""
sldwks_arg_path_dir = f"\"{clr_path_dir}\""
sldwks_arg_output_dir = f"\"{join(getcwd(), 'data')}\""

# console arguments
pcdmis_arg = f"program_export.vbs {pcdmis_arg_source} {pcdmis_arg_export}"
sldwks_arg = f"{join('solidworks_api_app', 'bin', 'Debug', 'net7.0', 'solidworks_api_app.exe')} {sldwks_arg_root_dir} {sldwks_arg_path_dir} {sldwks_arg_output_dir}"

# run the vb script for pc-dmis export
print("Exporting PC-DMIS files to .xml format...")
system(pcdmis_arg)

# run the c# console application
print("Exporting part and fixture clearances from SolidWorks...")
system(sldwks_arg)

# interpret the pc-dmis xml files
print("Interpreting PC-DMIS xml files...")

# look through the pc-dmis xml export folder
ext = ".xml"
all_files = listdir(pc_raw_export)
filtered_files = list(filter(lambda item: isfile(join(pc_raw_export, item)) and item[-len(ext):].lower() == ext, all_files))

# initialize the target lists
drawing_arr = []
revision_arr = []
fixture_arr = []
py_arr = []
px_arr = []
ny_arr = []
nx_arr = []

# iterate through the available files
for file in filtered_files:

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
df.to_csv(join("data", "path_clearances.csv"), index = False)