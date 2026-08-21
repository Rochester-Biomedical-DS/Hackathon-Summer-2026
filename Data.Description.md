# University of Rochester
## Biomedical Data Science Hackathon — Summer 2026

**Overview**

Spatial transcriptomics measures gene expression while preserving each cell's physical location within a tissue. Unlike conventional single-cell RNA-seq, which dissociates cells and loses spatial context, spatial methods reveal how cell types are organized, interact, and form functional tissue architecture. This enables studies of cell-cell communication, developmental patterning, disease microenvironments, and tissue organization. Computationally, identifying cell types is challenging because each method measures only a subset of genes or has limited resolution, cells may be incompletely segmented, expression is sparse and noisy, and cell identities often must be inferred by integrating spatial data with reference single-cell RNA-seq datasets. This year's hackathon will be to call cell types in a spatial transcriptomics MERFISH dataset.

MERFISH (Multiplexed Error-Robust Fluorescence In Situ Hybridization) is an imaging-based spatial transcriptomics technique that identifies hundreds to thousands of RNA species directly within intact tissue. Each RNA molecule is assigned a unique binary barcode that is read out through multiple rounds of fluorescent hybridization and imaging. Error-correcting barcode designs enable accurate transcript identification despite imaging errors. The resulting data provide single-molecule resolution, allowing individual transcripts to be assigned to cells while preserving their precise spatial locations.

**Data**

MERFISH data was collected from 200 genes and 10k cells in mouse neuronal tissues.

Data are sparse counts with spatial information. This spatial information is relevant since cell types and transcriptional variation within and between cell types is spatially organized. In addition to gene expression counts and spatial information, cell features and tissue sections from different locations and animals are often integrated to classify different cell types.

Two files are provided for both the test/train data: counts and meta. Counts contains the number of MERFISH transcripts detected per cell with columns indicating gene names, and meta contains the following information for each cell.

| Variable | Description |
|---|---|
| Row label | Cell ID |
| Datasets | Dataset ID |
| volume | Cell volume |
| center_x | Cell x position |
| center_y | Cell y position |
| MERFISH_cell_type_annotation | Cell type |
| Region | Region ID for tissue section |
| Excitatory_vs_Inhibitory | Cell is excitatory or inhibitory |
| Segment | Segment ID for tissue section |
| Gender | Mouse gender |
| Mouse_ID | Mouse ID |
| AP_position | Anterior-Posterior ID of tissue section |
| Section_ID | Section ID |

**Hackathon objective and evaluation**

The objective of the hackathon is to correctly predict cell type labels in MERFISH_cell_type_annotation. Group performance will be measured by the confusion matrix overall accuracy: number of correct predictions / total number of predictions.

**Submission**

Predictions should be posted to your GitHub account as plain text with two columns in the same order listed in "meta_test.csv." The first column contains the cell ID, the second column contains the predicted cell type. Your predictions should be one of the 60 cell types in the training data. An example prediction file is posted at [prediction/prediction.csv](prediction/prediction.csv).

**Scoring**

Text files associated with hackathon-registered GitHub accounts will be assessed each day of the competition. To submit predictions, please make sure that your properly formatted prediction.txt file is in your forked repository of "/Hackathon-Summer-2026/main/prediction/prediction.csv." Prediction files will be pulled at 3 PM, and results will be posted shortly afterward here [Leaderboard.Hackathon.2026.md](Leaderboard.Hackathon.2026.md). 
See README and e-mail from organizers about final scoring for cash prize determination on validation dataset. All teams must submit their code to their captain's GitHub by 8/22 at 3pm and new predictions on the validation data by 8/23 at 10am in order to compete for cash prizes.
