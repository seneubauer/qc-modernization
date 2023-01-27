# import dependencies
from bs4 import BeautifulSoup
from os.path import join
from math import sin, cos, pi

# import confidential information
from sys import path
path.insert(0, "..")
from reference_values import probe_dict

# combine probe distances
def combine_distances(current:float, previous:float) -> float:
    if (current >= 0 and previous < 0) or (previous >= 0 and current < 0):
        return abs(current) + abs(previous)
    else:
        return current

# extract the probe information from an xml file
def extract_probe_info(file_path:str) -> dict:

    # read the file contents
    with open(file_path, "r", encoding = "utf-8") as file:
        file_contents = file.read()

    # instantiate a beautifulsoup object
    bs = BeautifulSoup(file_contents, "xml")

    # initialize the output dictionary
    output_dict = {
        "drawing": "empty",
        "revision": "empty",
        "fixture": "empty",
        "py": 0,
        "px": 0,
        "ny": 0,
        "nx": 0
    }

    # get a list of all the command features
    feature_list = bs.find_all("Command")

    # initialize parameters
    current_probe = ""
    probe_length = 0.0
    measurement_index = 0
    measurement_count = len([x for x in feature_list if "(CONTACT)" in str(x)])
    prev_x = 0
    prev_y = 0

    # extract elements
    for feature in feature_list:
        feature_type = str(feature.get("Type"))
        if feature_type == "File Header":
            output_dict["drawing"] = str(feature.find_all("DataField")[0].get("Value"))
            output_dict["revision"] = str(feature.find_all("DataField")[1].get("Value"))
        elif feature_type == "Recall Alignment":
            if str(feature.find_all("DataField")[0].get("Value")).lower() == "external":
                output_dict["fixture"] = str(feature.find_all("DataField")[2].get("Value"))
        elif feature_type == "Load Probe":
            current_probe = str(feature.find_all("DataField")[0].get("Value")).lower()
            probe_length = probe_dict[current_probe]
        elif feature_type == "Set Active Tip":
            tip_str = str(feature.find_all("DataField")[0].get("Value"))
            A, B = [float(x) * pi / 180 for x in tip_str[3:].split("B")]

            distance = probe_length * sin(A)
            dist_x = round(distance * sin(B), 4)
            dist_y = round(-distance * cos(B), 4)

            # assign the +/- x distances
            if dist_x >= 0:
                output_dict["nx"] = max([output_dict["nx"], combine_distances(dist_x, prev_x)])
            else:
                output_dict["px"] = max([output_dict["px"], combine_distances(dist_x, prev_x)])

            # assign the +/- y distances
            if dist_y >= 0:
                output_dict["ny"] = max([output_dict["ny"], combine_distances(dist_y, prev_y)])
            else:
                output_dict["py"] = max([output_dict["py"], combine_distances(dist_y, prev_y)])
            
            prev_x = dist_x
            prev_y = dist_y

        elif "(CONTACT)" in feature_type:
            measurement_index += 1
            if measurement_index == measurement_count:
                break

    # return the modified output dictionary
    return output_dict