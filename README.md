# qc-modernization
## Electronic Inspection Record Conversion
### Goal
With our current process, all the inspection data and its accompanying metadata is stored in macro-enabled Excel workbooks. Obviously, this is untenable for long-term use. So this script will examine all EIRs and scrape the relevant data into a cleaner format which can then be used to insert into a relational database.

### Issues
* Operator and Inspector names were inconsistently entered. Some users entered their initials, others entered their first name, others entered multiple names of different formats, and so on. I ended up using an approach inspired by NLP to standardize the cell content.
* There are a few types of EIR formats used over the years, so there are some formatting differences. I had to introduce a process that locates a consistent anchor point then searches for the other data labels.
* 

## PC-DMIS Program Evaluation
