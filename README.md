# Election Analysis
## Overview of Election Audit
The purpose of the election analysis is to find out which candidate has won the election with what percentage, and which county has the highest election votes. Using python, extracted the useful information from the election_result csv file. Counted each candidates votes, found the percentage rate, and displayed the result in comprehensive way. All final results are displayed in the election_analysis text file.

- [PyPoll_Challenge.py](https://github.com/oyuka1112/election_analysis/blob/main/PyPoll_Challenge.py)
    - Python code 
- [election_results.csv](https://raw.githubusercontent.com/oyuka1112/election_analysis/main/Resources/election_results.csv)
    - CSV file for votes
- [election_analysis.txt](https://github.com/oyuka1112/election_analysis/blob/main/election_analysis.txt)
    - Text file that has the final results
## Election Audit Results
* Total Votes: 369,711 
    - How many votes recorded 
* County Votes:
    - Jefferson: 10.5% (38,855)
    - Denver: 82.8% (306,055)
    - Arapahoe: 6.7% (24,801)
* Largest County Turnout: Denver
* Candidate Votes: 
    - Charles Casper Stockham: 23.0% (85,213)
    - Diana DeGette: 73.8% (272,892)
    - Raymon Anthony Doane: 3.1% (11,606)
* Winner: Diana DeGette
* Winning Vote Count: 272,892
* Winning Percentage: 73.8%

## Election Audit Summary
### Summary for the script
[PyPoll_Challenge.py](https://github.com/oyuka1112/election_analysis/blob/main/PyPoll_Challenge.py) finds out that the following:
- number of total votes
- number of candidates
- number of votes for each candidates
- find out the percentage for each candidates (votes/total votes *100)
- number of counties
- number of votes per county
- finds out the largest number of all the votes per county. In other words, largest voting county
- finds oyt the biggest number of all candidates. In other words, find the winning candidate among all, find his/her percentage rate for winning, and the number of votes for winning.
### Summary for how it can be used in a general by modifying the written code
1. file_to_load = os.path.join("Resources",`"election_results.csv"`)
    Instead of `election_results.csv` upload the election result file into your Resources, and use another election result. This would give you the analysis result for the particular file.
2.  Instead of the `candidate_name = row[2]` and `county_name = row[1]`, depending on your file structure, you can change the row for candidate names and the county row. Therefore, you will be able to get all the correct info based on your file.


