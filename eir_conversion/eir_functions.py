# import dependencies
from openpyxl import load_workbook
from openpyxl.utils import get_column_letter
from datetime import date
from xlrd import xldate_as_datetime
from os import listdir
from os.path import isfile, join
from pickle import dump, load
from random import sample
import pandas as pd

# bring in config values
from sys import path
path.insert(0, "..")
from reference_values import alias_dict

# extract the contents of one electronic inspection record into a list of dictionaries
def scrape_one(qc_folder: str, anchor_search_term: str, workbook_name: str, metadata_index: int, worksheet_names = []) -> tuple:

    # define the file path
    file_path = join(qc_folder, workbook_name)

    # open the workbook
    wb = load_workbook(filename = file_path, read_only = True, data_only = True)

    # initialize the output DataFrames
    metadata_df = pd.DataFrame()
    measurements_df = pd.DataFrame()

    # check if worksheet names were supplied
    if len(worksheet_names) == 0:
        worksheet_names = wb.worksheets

    # iterate through the specified worksheets
    for ws in worksheet_names:

        # find the data anchor
        anchor_column = 0
        anchor_row = 1
        anchor_found = False
        for i in range(1, 21):
            if ws[f"{get_column_letter(i)}1"].value == anchor_search_term:
                anchor_column = i
                anchor_found = True
                break

        # continue if this is the correct worksheet
        if anchor_found:

            # define search parameters
            search_column = get_column_letter(anchor_column + 2)
            search_row = anchor_row + 17
            index_limit = 200
            initial_i = anchor_row + 17
            initial_j = anchor_column + 2

            # define iterator parameters
            cell_value = "initial"
            i = initial_i

            # get the item count
            while cell_value is not None:

                # exit the iterator
                if cell_value is None:
                    break

                # exit condition
                cell_value = ws[f"{search_column}{i}"].value

                # increment the iterator
                i += 1

                # limit the while loop
                if i >= index_limit:
                    print(f"Row search has exceeded index limit ({index_limit})")
                    break

            # define the item count
            item_count = i - 1 - initial_i

            # continue if there are items in the worksheet
            if item_count > 0:

                # define iterator parameters
                feature_index = 12
                gage_index = 16
                cell_value = "initial"
                j = initial_j

                # initialize the storage lists
                data_types = []
                features = []
                gauges = []
                measurements = []

                # search column by column
                while cell_value is not None:

                    # define the current column
                    column_index = get_column_letter(j)

                    # define the exit condition value
                    cell_value = ws[f"{column_index}{search_row}"].value

                    # exit the iterator
                    if cell_value is None:
                        break

                    # define metadata
                    data_type = str(type(cell_value)).replace("<class ", "").replace(">", "").replace("'", "").strip()
                    feature = ws[f"{column_index}{feature_index}"].value
                    gauge = ws[f"{column_index}{gage_index}"].value

                    # only add data when the feature number is defined
                    if feature != 0:

                        data_types.append(data_type)
                        features.append(feature)
                        gauges.append(gauge)

                        for x in range(item_count):
                            measurements.append(ws[f"{column_index}{x + initial_i}"].value)

                    # increment the iterator
                    j += 1

                    # limit the while loop
                    if j >= index_limit:
                        print(f"Column search has exceeded index limit ({index_limit})")
                        break

                # convert pass/fail to numerical data
                for x in range(len(measurements)):
                    if type(measurements[x]) == str:
                        if measurements[x].lower() in alias_dict.keys():
                            measurements[x] = alias_dict[measurements[x].lower()]
                        else:
                            measurements[x] = alias_dict["empty"]

                # slice the raw measurement list into constituent parts
                meas_lists = []
                for x in range(item_count):
                    temp_list = []
                    for y in range(0, len(measurements), item_count):
                        temp_list.append(measurements[x + y])
                    meas_lists.append(temp_list)

                # section 1 metadata
                section_1 = []
                for x in range(21):
                    find_column = get_column_letter(anchor_column + x)
                    data_column = get_column_letter(anchor_column + x + 2)
                    if str(ws[f"{find_column}{anchor_row + 5}"].value).lower() == "item number":
                        value0 = ws[f"{data_column}{anchor_row + 5}"].value			# item number
                        value1 = ws[f"{data_column}{anchor_row + 6}"].value			# drawing number
                        value2 = ws[f"{data_column}{anchor_row + 7}"].value			# revision
                        if value0 is not None:
                            section_1.append(value0)
                        else:
                            section_1.append(alias_dict["empty"])
                        if value1 is not None:
                            section_1.append(value1)
                        else:
                            section_1.append(alias_dict["empty"])
                        if value2 is not None:
                            section_1.append(value2)
                        else:
                            section_1.append(alias_dict["empty"])
                        break

                # section 2 metadata
                section_2 = []
                for x in range(21):
                    find_column = get_column_letter(anchor_column + x)
                    data_column = get_column_letter(anchor_column + x + 1)
                    if str(ws[f"{find_column}{anchor_row + 5}"].value).lower() == "date":
                        value0 = ws[f"{data_column}{anchor_row + 5}"].value			# date
                        value1 = ws[f"{data_column}{anchor_row + 6}"].value			# inspector
                        value2 = ws[f"{data_column}{anchor_row + 7}"].value			# disposition
                        value3 = ws[f"{data_column}{anchor_row + 8}"].value			# supplier
                        if value0 is not None:
                            try:
                                if type(value0) is int:
                                    value0 = xldate_as_datetime(value0, 0)
                                section_2.append(date(value0.year, value0.month, value0.day))
                            except AttributeError:
                                print(f"AttributeError in {ws.title} of {workbook_name}; {value0}")
                        else:
                            section_2.append(alias_dict["empty"])
                        if value1 is not None:
                            section_2.append(value1)
                        else:
                            section_2.append(alias_dict["empty"])
                        if value2 is not None:
                            section_2.append(value2)
                        else:
                            section_2.append(alias_dict["empty"])
                        if value3 is not None:
                            section_2.append(value3)
                        else:
                            section_2.append(alias_dict["empty"])
                        break

                # section 3 metadata
                section_3 = []
                for x in range(21):
                    find_column = get_column_letter(anchor_column + x)
                    data_column = get_column_letter(anchor_column + x + 1)
                    if str(ws[f"{find_column}{anchor_row + 5}"].value).lower() == "recv. #":
                        value0 = ws[f"{data_column}{anchor_row + 5}"].value			# receiver number
                        value1 = ws[f"{data_column}{anchor_row + 6}"].value			# purchase order
                        value2 = ws[f"{data_column}{anchor_row + 7}"].value			# job number
                        value3 = ws[f"{data_column}{anchor_row + 8}"].value			# operator
                        if value0 is not None:
                            section_3.append(value0)
                        else:
                            section_3.append(alias_dict["empty"])
                        if value1 is not None:
                            section_3.append(value1)
                        else:
                            section_3.append(alias_dict["empty"])
                        if value2 is not None:
                            section_3.append(value2)
                        else:
                            section_3.append(alias_dict["empty"])
                        if value3 is not None:
                            section_3.append(value3)
                        else:
                            section_3.append(alias_dict["empty"])
                        break

                # section 4 metadata
                section_4 = []
                for x in range(21):
                    find_column = get_column_letter(anchor_column + x)
                    data_column = get_column_letter(anchor_column + x + 2)
                    if str(ws[f"{find_column}{anchor_row + 6}"].value).lower() == "qc full inspect interval":
                        value0 = ws[f"{data_column}{anchor_row + 6}"].value			# qc full inspect quantity
                        value1 = ws[f"{data_column}{anchor_row + 7}"].value			# released quantity
                        value2 = ws[f"{data_column}{anchor_row + 8}"].value			# completed quantity
                        if value0 is not None:
                            section_4.append(value0)
                        else:
                            section_4.append(alias_dict["empty"])
                        if value1 is not None:
                            section_4.append(value1)
                        else:
                            section_4.append(alias_dict["empty"])
                        if value2 is not None:
                            section_4.append(value2)
                        else:
                            section_4.append(alias_dict["empty"])
                        break

                # ensure the section lists have contents
                if len(section_1) == 0:
                    section_1 = [alias_dict["empty"], alias_dict["empty"], alias_dict["empty"]]
                if len(section_2) == 0:
                    section_2 = [alias_dict["empty"], alias_dict["empty"], alias_dict["empty"], alias_dict["empty"]]
                if len(section_3) == 0:
                    section_3 = [alias_dict["empty"], alias_dict["empty"], alias_dict["empty"], alias_dict["empty"]]
                if len(section_4) == 0:
                    section_4 = [alias_dict["empty"], alias_dict["empty"], alias_dict["empty"]]

                try:
                    # store metadata in a DataFrame
                    current_metadata_df = pd.DataFrame({
                        "id": [metadata_index],
                        "item_number": section_1[0],
                        "drawing": section_1[1],
                        "revision": section_1[2],
                        "inspection_date": section_2[0],
                        "inspector": section_2[1],
                        "disposition": section_2[2],
                        "supplier": section_2[3],
                        "receiver_number": section_3[0],
                        "purchase_order": section_3[1],
                        "job_order": section_3[2],
                        "operator": section_3[3],
                        "full_inspect_qty": section_4[0],
                        "received_qty": section_4[1],
                        "completed_qty": section_4[2]
                    })

                    # store measurement data in a DataFrame
                    current_measurements_df = pd.DataFrame({
                        "metadata_id": [metadata_index for i in range(len(features))],
                        "feature_id": features,
                        "gauge": gauges,
                        "data_type": data_types
                    })

                    # advance the index
                    metadata_index += 1

                    # add measurement data to measurements_df
                    x = 0
                    for meas_list in meas_lists:
                        current_measurements_df[f"part_{x}"] = meas_list
                        x += 1

                    metadata_df = pd.concat([metadata_df, current_metadata_df], axis = 0, ignore_index = True)
                    measurements_df = pd.concat([measurements_df, current_measurements_df], axis = 0, ignore_index = True)

                except IndexError:
                    print(f"IndexError in {ws.title} of {workbook_name}")

    # close the workbook
    wb.close()

    # return the results
    return (metadata_df, measurements_df)

# extract the contents of multiple electronic inspection records into lists of dictionaries
def scrape_all(qc_folder: str, anchor_search_term: str, file_extension: str, qty_limit = 0, is_random = False, workbooks = []) -> tuple:

    # retrieve a list of the folder contents
    folder_contents = listdir(qc_folder)

    # filter the folder contents
    filtered_contents = list(filter(lambda item:
                            isfile(join(qc_folder, item))
                            and item[:1].lower() != "~"
                            and item[:1].lower() != "_"
                            and item[-len(file_extension):].lower() == file_extension
                            and "template" not in item.lower()
                            and "example" not in item.lower()
                            and "mi" not in item.lower()
                            and "qa1" not in item.lower(), folder_contents))

    # initialize the list of files
    files = []
    if is_random:
        files = sample(filtered_contents, qty_limit)
    else:
        files = filtered_contents

    # overwrite the list of files if requested
    if len(workbooks) > 0:
        files = workbooks

    # initialize the storage lists
    metadata_list = []
    measurements_list = []

    # initialize the counter
    iterator_count = 1

    # initialize the metadata index
    metadata_index = 0

    # iterate through the directory contents
    for item in files:

        # conditional break
        if qty_limit > 0:

            # exit the iterator
            if iterator_count > qty_limit:
                break

            # increment the iterator count
            iterator_count += 1

        # interpret the current workbook
        print(f"Current: {item}")
        metadata_df, measurements_df = scrape_one(qc_folder, anchor_search_term, item, metadata_index)

        # advance the metadata index
        metadata_index += len(metadata_df)

        # append results to the DataFrame lists
        if metadata_df is not None:
            metadata_list.append(metadata_df)
        if measurements_df is not None:
            measurements_list.append(measurements_df)

    # concatenate the DataFrame lists
    raw_metadata_df = pd.concat(metadata_list, axis = 0, ignore_index = True)
    raw_measurement_df = pd.concat(measurements_list, axis = 0, ignore_index = True)

    # return the results
    return (raw_metadata_df, raw_measurement_df)

# save results to a binary file
def to_raw_binary(destination_folder: str, file_name: str, data_object: tuple) -> None:

    # create, populate, then close the binary file
    my_file = open(join(destination_folder, file_name), "wb")
    dump(data_object, my_file)
    my_file.close()

# save results to csv files
def to_raw_csv(destination_folder: str, data_object: tuple) -> None:

    # extract DataFrames from the input
    raw_metadata_df, raw_measurements_df = data_object

    # save metadata
    raw_metadata_df.to_csv(join(destination_folder, "raw_metadata.csv"), index = False)
    raw_measurements_df.to_csv(join(destination_folder, "raw_measurements.csv"), index = False)

# convert binary file to multiple csv files
def raw_binary_to_csvs(binary_folder: str, binary_name: str, destination_folder: str, file_extension: str) -> None:

    # open, read, then close the binary file
    bin_file = open(join(binary_folder, binary_name), "rb")
    file_contents = load(bin_file)
    bin_file.close()

    # save the file contents to csv files
    to_raw_csv(destination_folder, file_extension, file_contents)