# import dependencies
from os import system

# import confidential values
from sys import path
path.insert(0, "..")
from config import pc_raw_source, pc_raw_export

# transform the arguments to an argument-friendly format
arg_source = pc_raw_source.replace(" ", "%")
arg_export = pc_raw_export.replace(" ", "%")

# console argument
arg = f"program_export.vbs {arg_source} {arg_export}"

# run the vb script
system(arg)