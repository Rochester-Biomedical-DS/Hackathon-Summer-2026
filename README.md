# University of Rochester Biomedical Data Science Hackathon Summer 2026
Welcome to the landing page for the hackathon. The hackathon will commence 8/18. It will be a prediction challenge. All predictions should be submitted through GitHub using the captain's handle. Scoring will also happen in GitHub. All details regarding the hackathon will be posted here.  

 Registration for the event is closed. Please make sure each individual competing on your team is fully registered. Each team needs a captain with a github handle. To receive a prize, you must supply your University of Rochester e-mail address. All teams scoring better than random will receive a participation prize. 1st and 2nd place winning teams in each division will get a cash prize (see below).
 **All team members must submit their own registration form to participate.**  

# Overview
This is a prediction challenge with spatial transcriptomics data. The objective of the hackathon is to correctly predict cell type labels in MERFISH_cell_type_annotation. Group performance will be measured by the confusion matrix overall accuracy: number of correct predictions / total number of predictions.

# Challenge description
The challenge is to classify cell types in a mouse neuronal tissue dataset collected using MERFISH, an imaging-based spatial transcriptomics technique that measures gene expression while preserving each cell's exact location in the tissue. The dataset covers ~10,000 cells and 200 genes, with sparse transcript counts paired with spatial coordinates and cell metadata (like cell volume, region, gender, and mouse ID). Participants must predict the cell type label for each cell in the test set. A full description of the challenge and dataset is here: [Data.Description.md](Data.Description.md).

# Logistics

0.   Each team must have a github handle associated with it in order to participate.  Make sure you edit your registration or email the organizers to provide this, if you haven't yet. Your team will not be scored if you do not provide a handle.
1.   You may add team members up
to noon EDT on 8/18 by editing your response to the google form or emailing the organizers.
2.  Teams of entirely undergraduates will be in the undergraduate
division, else they will be in the open division.
3. Further instructions for submitting predictions will be posted here as they become available
4.  Competition runs through 2:59 PM EDT 22-August-2026.  The predictions each team has committed to their repository at that time will be used to determine their final score. Captains must submit their own predictions. Any use of predictions from other teams is disqualifying. Winning teams must submit their code to organizers to claim their prize. **Update** To be eligible for a cash prize, teams must post their code on their captain's github by 3pm 8/22 and test its performance on a new dataset.

Scores will be posted shortly after 3pm EDT each day here [Leaderboard.Hackathon.2026.md](Leaderboard.Hackathon.2026.md). 

# Scoring 
The competition will conclude at 3pm Saturday Aug 22. At this point, all teams must submit their final predictions. Prizes for predictions that beat random guessing will be determined by overall accuracy.  
However, in order to compete for cash prizes, teams must use their existing model to **make predictions a new validation dataset.  By 3pm Saturday, teams must upload their code to their captain's GitHub repositories** and test their final model on a new validation dataset. Teams are not permitted to update their models before submitting their new predictions and only teams with code posted by 3pm Saturday Aug 22 will be eligible for a cash prize. 
The original test dataset (meta_test.csv and counts_test.csv) will be replaced with a validation dataset with the same name after 3pm on 8/22. We will confirm via e-mail and updated README when the dataset is replaced and you should re-run your code with these validation data. **New predictions (prediction/prediction.csv) on the validation data must be posted by 10 am Sunday morning 8/23**. 
Winning teams will be confirmed and announced by Monday 8/24.

# Prizes
   
1.  First place in each division: $300 + $75 x (team size)
2.  Second place in each division: 0 + $50 x (team size)
  
If your predictions on the original test dataset beat random guessing, each team member will win a prize. Cash prizes will be determined based on performance on a new dataset.