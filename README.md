# How to use Heartbeat
First log into cs50.io, then within a terminal window execute the following commands:
update50
cd ~/workspace/cs50_final/
Once your terminal window is in the cs50_final folder type: flask run (and hit enter), click directly on the web link and hit open. This will open the webpage in a new tab.

Background:
Heartbeat is a series of automated sequel queries that run nightly on our various boundary data products. For the purposes of this final it will run on our neighborhoods product only.
We wrote and automated these queries last year in an effort to streamline our work and become more efficient by eliminating repetitive manual work. This project is to help us create an
interactive web interface where editors will be able to view deadlines, results, and compare day to day change in the boundary products that they are working on. It will also be a resource
for the quality team to help during times of product release. Hopefully, this will be a tool to help move more quality work upstream and heighten awareness throughout the production teams.

Distribution:
Included with this project are a number of files.
what each does
html files
python files
text files
database

Home Page:
The home page consists of the production calendar. Here you will see upcoming product releases, who they are assigned to and the deadline. You will also find a shortened explanation of how the website works.

Query Page:
The query page shows all of the queries that run nightly and provides a brief explanation of what each is doing. The queries we have included in this project

Results Page:
The results page features a drop down menu that selects the most recent run number and displays the results from the queries run.

Compare Page:
The compare page allows you to select two different runs and compare the results. This will help you to evaluate the change over time in the product that you chose.
