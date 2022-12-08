# import dependencies

# import functions
from eir_functions import scrape_all, to_binary, to_csv, binary_to_csvs

# bring in config values
from sys import path
path.insert(0, "..")
from config import eir_raw_source, eir_cleaned_destination_csv, eir_cleaned_destination_bin, eir_anchor_search_term, eir_file_extension

# toggle routine steps
save_load_binary = False
save_csv = True

# specify targeted data
scraped_workbook_qty = 3            # sets a limit on how many workbooks will be scraped, if 0 then no limit
randomize_workbooks = True          # will select workbooks at random, only use if qty is > 0
overwrite_targeted_workbooks = []   # if list is empty then scrape_all will use the quantity/randomized parameters

# scrape all the relevant data from the electronic inspection workbooks
results_all = scrape_all(
    eir_raw_source,
    eir_anchor_search_term,
    eir_file_extension,
    qty_limit = scraped_workbook_qty,
    is_random = randomize_workbooks,
    workbooks = overwrite_targeted_workbooks)

# saves results to then loads from a binary file
if save_load_binary:

    # binary file name
    bin_file_name = "results_all.pkl"

    # saves to binary
    to_binary(eir_cleaned_destination_bin, bin_file_name, results_all)

    # loads from binary and resaves to csv if the results aren't already being converted directly to csv
    if not save_csv:
        binary_to_csvs(eir_cleaned_destination_bin, bin_file_name, eir_cleaned_destination_csv, eir_file_extension)

# saves results directly to csv files
if save_csv:

    # saves to csv files
    to_csv(eir_cleaned_destination_csv, eir_file_extension, results_all)