# Survey Text
In this directory, we include a pdf of the text we used for our survey, which we ran on Prolific. The survey is organized by blocks, whose headers are indicated by bolded text.
We list and explain each block here, and then we explain the survey flow, which cannot be seen from the pdf.
To summarize, participants were first shown the IntroBlock. Then, they were randomly assigned one of three mental model blocks, datahubModel, 5W1HDataCatalog, or GoogleDataCatalog blocks, each of which contained mental models, and some subset of the data questions displayed in Table 1 of our paper. For this subset of questions, they were asked to choose a mental model concept and rate the difficulty of making this choice.

## Consent Form
We, of course, displayed a consent form to participants, as required for IRB approval. Most notably, we are not allowed to release the raw results, which is why we are only posting our aggregate results here.

## IntroBlock
In this block, we asked questions to screen participants for familiarity with data science and/or databases in order to avoid spurious answers due to a lack of familiarity with the context of our survey, which was storing and retrieving metadata from data catalogs.
Specifically, if participants answered "None of the Above" for how they would characterize their interactions with datasets and databases, or they answered "I rarely download datasets or process data", we excluded these participants from our analysis.

We also asked participants whether they had used a data catalog recently (within the past year) and showed them a list of catalogs.
If participants chose "Google's Data Catalog" and were then assigned the GoogleDataCatalog block, we excluded them from our analysis. Similarly, if participants chose "LinkedIn's Datahub" and were then assigned the datahubModel block, we excluded them form our analysis as well, to avoid familiarity effects.

We then displayed our list of questions from Table 1 of our paper and asked users to rate their familiarity with each of these questions. If a participant responded "I do not understand this question" to any question, they were not shown that question when assigned one of the blocks with the mental models.
As a result, participants were only shown questions for which they had a minimum level of familiarity.

## Mental Model Blocks
We randomly displayed one of three mental model blocks to survey participants: datahubModel (containing the Datahub Mental Model), 5W1HDataCatalog (containing the 5W1H+R Mental Model), or GoogleDataCatalog (containing the Google Cloud Service (GCS) Mental Model).

In each of these blocks, we displayed a mental model example first, to help participants understand how to read our mental model diagrams, which consisted of concepts, their definitions, and their relationships to other concepts.
We then explained the participant's task using language they could understand even if they had not directly used a data catalog before.

Then, we displayed the mental model itself, and the subset of data questions participants claimed at least a minimum familiarity with, according to their responses in the IntroBlock.

For each question, we asked them to choose the concept that best described the answer to the question, and then we asked them how difficult it was to make that choice. Note that we used the language "How difficult did the catalog make it..." instead of asking "How difficult was it to choose a concept..." to avoid reactivity effects (e.g. participants choosing a low difficulty rating because they feel they would be perceived as less intelligent if they chose otherwise).

### datahubModel
In this block, we displayed Datahub's mental model to participants, following the structure above.

### 5W1HDataCatalog
In this block, we displayed the 5W1H+R mental model to participants, following the structure above.

### GoogleDataCatalog
In this block, we displayed the GCS mental model to participants, following the structure above.
