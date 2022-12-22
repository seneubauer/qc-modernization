# import functions
from eir_functions import scrape_all, to_binary, to_csv, binary_to_csvs, clean_metadata, clean_measurements

# bring in config values
from sys import path
path.insert(0, "..")
from config import eir_raw_source, eir_cleaned_destination_csv, eir_cleaned_destination_bin, eir_anchor_search_term, eir_file_extension

# toggle routine steps
save_load_binary = True
save_csv = False

# specify targeted data
scraped_workbook_qty = 0            # sets a limit on how many workbooks will be scraped, if 0 then no limit
randomize_workbooks = False         # will select workbooks at random, only use if qty is > 0
overwrite_targeted_workbooks = []   # if list is empty then scrape_all will use the quantity/randomized parameters

# scrape all the relevant data from the electronic inspection workbooks
raw_results_all = scrape_all(
    eir_raw_source,
    eir_anchor_search_term,
    eir_file_extension,
    qty_limit = scraped_workbook_qty,
    is_random = randomize_workbooks,
    workbooks = overwrite_targeted_workbooks)

# saves results to then loads from a binary file
if save_load_binary:

    # binary file name
    raw_bin_file_name = "raw_results_all.pkl"
    cln_bin_file_name = "cln_results_all.pkl"

    # saves raw results to binary
    to_binary(eir_cleaned_destination_bin, raw_bin_file_name, raw_results_all)

    # saves cleaned results to binary
    raw_metadata_df, raw_measurements_df = raw_results_all
    cln_metadata_df = clean_metadata(raw_metadata_df)
    cln_measurements_df = clean_measurements(raw_measurements_df)
    to_binary(eir_cleaned_destination_bin, cln_bin_file_name, (cln_metadata_df, cln_measurements_df))

    # loads from binary and resaves to csv if the results aren't already being converted directly to csv
    if not save_csv:
        binary_to_csvs(eir_cleaned_destination_bin, eir_cleaned_destination_csv, raw_bin_file_name, cln_bin_file_name)

# saves results directly to csv files
if save_csv:

    # extract then clean the raw results
    raw_metadata_df, raw_measurements_df = raw_results_all
    cln_metadata_df = clean_metadata(raw_metadata_df)
    cln_measurements_df = clean_measurements(raw_measurements_df)

    # saves to csv files
    to_csv(eir_cleaned_destination_csv, raw_results_all, (cln_metadata_df, cln_measurements_df))