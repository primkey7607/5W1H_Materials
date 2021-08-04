# Comprehensive and Comprehensible Data Catalogs: The What, Who, Where, When, Why, and How of Metadata Management
In this repository, we provide all materials used to produce the results presented in the paper with the above name, which can be found at the following link: https://arxiv.org/abs/2103.07532.

Specifically, we provide all materials that can be used to understand and generate our results in Section V. We explain what we include below.

## [Survey Language](https://github.com/primkey7607/5W1H_Materials/tree/main/SurveyLanguage)
We include a pdf with the survey text in the SurveyLanguage/ directory of this repository, where we explain the survey that was shown to participants in Section V-A of our paper. To avoid spurious survey responses and mitigate threats to validity, we made specific choices with regards to the language and flow of the survey, which we explain in this directory.

## [Frequency Distributions](https://github.com/primkey7607/5W1H_Materials/tree/main/FrequencyDistributions)
This directory contains all our data and code used to generate the consistency and ease-of-understanding results in Section V-A. Concretely, it contains the data and code that generates the values for Tables 3-6 in our paper.

## [Catalog Materialization Results](https://github.com/primkey7607/catalog_experiments)
We include the code for generating the datasets and running the experiments we describe in Section V-B in a separate repository which is linked above. Specifically, this code creates Normalized and Data Vault databases on SQLite and Neo4j, populates them with synthetic data, and then runs a comprehensive workload we describe in our paper on these databases.
Concretely, running this code would reproduce results close to those in Table 7 of our paper.
