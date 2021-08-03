# Survey Text
In this directory, we include a pdf of the text we used for our survey, which we ran on Prolific. The survey is organized by blocks, whose headers are indicated by bolded text.
We list and explain each block here, and then we explain the survey flow, which cannot be seen from the pdf.
To summarize, participants were first shown the IntroBlock. Then, they were randomly assigned one of the datahubModel, 5W1HDataCatalog, or GoogleDataCatalog blocks, each of which contained mental models, and some subset of the data questions displayed in Table 1 of our paper. For this subset of questions, they were asked to choose a mental model concept and rate the difficulty of making this choice.

## IntroBlock
In this block, we asked questions to screen participants for familiarity with data science and/or databases in order to avoid spurious answers due to a lack of familiarity with the context of our survey, which was storing and retrieving metadata from data catalogs.
Specifically, if participants answered "None of the Above" for how they would characterize their interactions with datasets and databases, or they answered "I rarely download datasets or process data", we excluded these participants from our analysis.

We also asked participants whether they had used a data catalog recently (within the past year) and showed them a list of catalogs.
If participants chose "Google's Data Catalog" and were then assigned the GoogleDataCatalog block, we excluded them from our analysis. Similarly, if participants chose "LinkedIn's Datahub" and were then assigned the datahubModel block, we excluded them form our analysis as well, to avoid familiarity effects.

We then displayed our list of questions from Table 1 of our paper and asked users to rate their familiarity with each of these questions. If a participant responded "I do not understand this question" to any question, they were not shown that question when assigned one of the blocks with the mental models.

## datahubModel
In this block, we...

## 5W1HDataCatalog
In this block, we...

## GoogleDataCatalog
In this block, we...

## Survey Flow
We displayed the IntroBlock first. Then, based on the participant's response to the question, we...
