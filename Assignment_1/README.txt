Requirements:

Python version 3.8 or 3.9
Python Libraries
-Pandas
-Python-dateutil
-json
-re (Regular expression)
-math

===================================================

Submission Structure:

1) Data:
-vaccine.csv - cowin vaccine data
-diff.csv - The csv is manually made to match the difference spelling in neighbour.json and vaccine data
-census.csv - Census data was cleaned partially by using python script and manually
-disctricts.csv - The covid cases data 
2) For each question there is seperate folder and respective shell script to run the question
3) Assign1.sh script runs the whole assignment
4) Output contains csv generated as output till Q9

===================================================
Steps to execute assignement :

1) To run the specific question move into the folder and run the script
2) To run the whole assignment run assign1.sh
3) Generated output will be stored in outut folder

Note - You may delete the csv from 'output' but do not delete the output folder itself

====================================================

Note 

1) Q2 generates on (i,j) edges not (j,i) i.e only unique edges
2) Q4 to find peaks daily confirmed cases were used
3) In Q7 where covaxin admistered dose were 0 in analysis corresponding was replaced with NA
4) Covid cases are considered from 15th march 2020 to 14 august 2021
5) Vaccince dose are considered upto 14th august 2021

	







