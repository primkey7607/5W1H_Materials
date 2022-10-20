# Content Description
This folder contains the following:

1. datahub_mmq_counts.csv: the CSV file containing the frequency distributions on the Datahub MM partitions.
2. gcs_mmq_counts.csv: the CSV file containing the frequency distributions on the GCS MM partitions.
3. our_mmq_counts.csv: the CSV file containing the frequency distributions on the 5W1H+R MM partitions.
4. genEntropies.py: the python file used to generate the values for tables III, IV, and V in our paper. Run the command genTable3Entropies(), genTable4NonePropsTable(), or genTable5NormalizedEntropies() to generate a latex table of values for the corresponding table.
5. table3entropies.txt: the latex table output of running genTable3Entropies() in genEntropies.py.
6. table4normentropies.txt: the latex table output of running genTable4NormalizedEntropies() in genEntropies.py.
7. table5noneproptable.txt: the latex table output of running genTable5NonePropsTable() in genEntropies.py.
