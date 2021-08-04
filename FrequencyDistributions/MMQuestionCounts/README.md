# Content Description
This folder contains the following:

1. datahub_mmq_counts.csv: the CSV file containing the frequency distributions on the Datahub MM partitions.
2. gcs_mmq_counts.csv: the CSV file containing the frequency distributions on the GCS MM partitions.
3. our_mmq_counts.csv: the CSV file containing the frequency distributions on the 5W1H+R MM partitions.
4. genEntropies.py: the python file used to generate the values for tables 3, 4, and 6 in our paper. Run the command genTable3Entropies(), genTable4NonePropsTable(), or genTable6NormalizedEntropies() to generate a latex table of values for the corresponding table.
5. table3entropies.txt: the latex table output of running genTable3Entropies() in genEntropies.py.
6. table6normentropies.txt: the latex table output of running genTable6NormalizedEntropies() in genEntropies.py.
7. table4noneproptable.txt: the latex table output of running genTable4NonePropsTable() in genEntropies.py.
