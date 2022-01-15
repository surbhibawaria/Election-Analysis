# Election_Analysis

## Overview of Election Audit
A Colorado Board of Elections employee has given the following tasks to complete the election audit of a recent local congressional election, print to the terminal and then save the results to a text file:

#### Candidate Results

1. Calculate the total number of votes cast in the election.
2. Get a complete list of candidate who recieved votes.
3. Calculate the total number of votes, and percentage of votes each candidate recieved.
4. Calculate percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote, winning vote count, and winning percentage of votes.

#### County Results

1. Calculate the total number of votes cast in the election.
2. Get a complete list of county and its total vote count.
3. Calculate the total number of votes, and percentage of votes each county recieved.
4. Calculate percentage of votes each county recieved.
5. Determine the county with the largest number of voters

### Resources
- Data Source: election_results.csv
- Software: Python 3.10.1, Visual Studio Code, 1.63.2

## Election-Audit Results

The analysis of the election show that:

<img width="398" alt="Election _Analysis" src="https://user-images.githubusercontent.com/95826875/149589023-02c0440e-adba-4dc1-a13f-7e506504a586.png">

- There were 369,711 votes cast in this congressional election.

<img width="487" alt="Total_votes" src="https://user-images.githubusercontent.com/95826875/149606630-ce76b344-91ae-4a84-aa37-1a14fa0ab9b3.png">

- The counties were:
    - Jefferson
    - Denver
    - Arapahoe

- The county's result were:
    - Jefferson recieved 10.5% of the vote and 38,855 number of votes.
    - Denver recieved 82.8% of the vote and 306,055 number of votes.
    - Arapahoe recieved 6.7% of the vote and 24,801 number of votes.

- The county with the largest number of votes was:
    - Denver, which recieved 82.8% of the vote and 306, 055 number of votes.

<img width="810" alt="County_results" src="https://user-images.githubusercontent.com/95826875/149606816-cd94deb5-48b5-45d5-ad29-f13f9dea5080.png">
    
- The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Rymon Anthony Doane

- The candidate's result were:
    - Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
    - Diana DeGette 73.8% of the vote and 272,892 number of votes.
    - Rymon Anthony Doane recieved 3.1% of the vote and 11,606 number of votes.

- The winner of the election was:
    - Diana DeGette, who recieved 73.8% of the vote and 272,892 number of votes.
    
    <img width="588" alt="Candidate_results" src="https://user-images.githubusercontent.com/95826875/149606946-ce5ae480-a48f-46de-a3ae-375a660e9593.png">

## Election-Audit Summary

This script is so versatile that it can be further used for any election analysis. The business proposal to the election commission would be to use this script for any election with some modifications needed as per the requirement. For instance, this script can be modified to be used for other elections in following ways:

1. The script can be further modified to filter the results based on voting methods like Mail-in Ballot, Punch Cards and Direct Recording Electroning for each candidate or county to gather number of votes cast through each respective method.

2. The script can also be modified taking into account features like ballot ID, demographics, etc. Another way the script can be modified for different types of elections like general elections, primary elections, special elections, presidential elections and electoral college elections. 
