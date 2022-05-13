# 858D Final project: Benchmarking Learned Index Data Structure for the FM-index over the Compacted dBG
### Yiheng Xu, and Le Chang

## Repo Layout
This repo contains six folders and two documents. 
- The CodeReadingNotes and LiteratureSurveyNotes are the notes we take from reading the paper and code. 
- Data folder includes the reference data and query data that we used for benchmarks. There are 10 reference data, 5 are prokaryotics genomes and others are human chromosomes. There are 40 query files each reference has 4 with different query lengths (32, 64, 96, 128)
- Figs folder contains all the figures we generated or used for the report.
- LiSA-modification folder contains the files that we changed from LiSA source code in order to run it and do benchmark
- Pufferfish-modification folder has the file that we modified to test the time of querying
- Result folder has four .csv file that stores the explicit data of our benchmark. Each table has the columns of tool name, reference name, reference length, #k of k-mer, query length, number of threads, query time, stored data size (train data, rmi and ipbwt size for LiSA; mphf and pos vec for Pufferfish).
Scripts folder contains all the python scripts we wrote for testing these tools and generating data.

## Testing Scripts
All the testing scripts are placed in the scripts folder. 
- generate_queries.py will generate random queries for testing
- parseLisa.py parses LiSA output and writes them into a .csv file
- pf\_plot.py and plot.py are the two files we used to draw the chart of generated data. pf\_plot is used to draw the chart of pufferfish and plot is used to draw the figure of LiSA\
- pufferfish\_calculateTime.py takes an input document that contains the runtime of each querying. It parses the input and calculates the total querying time. 
- runLisa.py and runPufferfish.py are the scripts that can execute the system commands for running each tool. runPufferfish.py has two modes: build and query. Build mode will run the index command and query mode will run the kquery command.

## Data
For prokaryotics reference, we use the data that was provided by homework.

## Version of software
We use the most up-to-date version of both tools
- LiSA doesn't specify the accurate version
- Pufferfish: VERSION_MAJOR 1?
