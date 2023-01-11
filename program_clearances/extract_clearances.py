# import dependencies
from os import system, getcwd
from os.path import join

# import confidential values
from sys import path
path.insert(0, "..")
from config import clr_root_dir, clr_path_dir

# transform the arguments to an argument-friendly format
arg_root_dir = "\"" + clr_root_dir + "\""
arg_path_dir = "\"" + clr_path_dir + "\""
arg_output_dir = "\"" + getcwd() + "\""

# console argument
arg = f"{join('solidworks_api_app', 'bin', 'Debug', 'net7.0', 'solidworks_api_app.exe')} {arg_root_dir} {arg_path_dir} {arg_output_dir}"

# run the c# console application
system(arg)