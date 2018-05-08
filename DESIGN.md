A "design document" for your project in the form of a Markdown file called DESIGN.md that discusses, technically,
how you implemented your project and why you made the design decisions you did. Your design document should be at least several paragraphs in length.
Whereas your documentation is meant to be a user’s manual, consider your design document your opportunity to give the staff a technical tour of your project underneath its hood.

DISTRIBUTION
All the files needed to run the Heartbeat web app are included in the cs50_final submission.
You should see the following files and folders:

DESIGN.MD   README.md   application.py  compare.py  heartbeat.db    helpers.py  requirements.txt    resources.txt
static/ templates

UNDERSTANDING - how it does it (Betsy doing what they do)
html files in general; mention special things we did
.py files in general; focus on application.py
heartbeat.db
txt files - resources are listed




Heartbeat is a project that was originally born out of the frustration of doing manual, repeative, but overall necessary, quality checks to the
data produced in house at our company. These datasets have grown larger and larger over the years and it is still critical to perform all of these checks but they
were taking longer and hampering our QC capacity. Over the past year Betsy and I have worked together to design the system, create the SQL queries for all of
the checks, store the code in version control, and work with fellow engineers to wrap the code in an automated executor (Jenkins).

But we needed to take this one step further. The Jenkins console ouput was mediocre at best and required users to ctrl+f to find the tables they were looking for.
We now have a csv output of the data each time a build number and product are chosen and run but it's still not as pretty as we want it to be.
CS50 gave us the skills and confidence to do what we really wanted - create a simple webpage that displays the results in different ways based on user input.

The first step in implementing this project was creating a mock dataset. This was the first time we had uploaded a CSV of data to phpliteadmin so it took a few tries
to get the columns labeled, in order, with the correct field types in both the csv and the phpliteadmin database. Then we fiddled with the import controls (it took us awhile
to remember that commas, not semi-colons were what csv's ended in...!) in phpliteadmin until we had our database up and running.

Once the data was in place we started tackling the website portion. We found that this particular website was much easier to build than any in the psets we had
tackled in class because the topic was something we knew inside and out and we started with a blank slate. Using pset7 (CS50 Finance) and a number of web resources listed
in the resources.txt file, we built up our application.py script to allow us to visualize the home.html page with layout.html. We were able to find a lot of help with the
artistic design components from W3 Schools which had a neat application that allowed you to fiddle with their sample code and then implement the concepts (text size, font,
colors, heading styles, etc) in our website. The quality team is the biggest consumer of the results Heartbeat provides so we added the calendar of releases for the product
we picked for the dataset. We use smartsheets inhouse to track the quarterly releases and were able to embed the appropriate calendar on the homepage. Our users often have
suggestions for queries to add, so we've added a support email using the mailto tag that allows them to send a note to us with their idea.

The query page serves as a reference for folks who are interested in SQL either because they are trying to make their own queries or they are looking for more detail about
the queries that we've implemented. We wrote up the queries and descriptions of what the queries were designed to look for, as well as expected outcome, and implemented a simple
table format for display.

The results page is designed to allow users to display the results of a particular run on the webpage. We used db.execute like we had in pset7 to pull all the results for a
build number the user enters and put the output in a table format for easier reading. This is important for the Quality team here because they need to record the results before the
final check off on the product.

The download page allows a user to choose up to 2 run numbers and download the csv's. The csv's can be used by the QC team to replace the checklist they fill out before product release or
by product managers and production teams to narrow down errors. The download page allows a user to download up to 2 runs so that they can be used on the compare page.

The compare page is one of the coolest elements of the webpage because it allows the user to upload 2 csv's (from the download page!) and compare one day against another. This is
a really important component of the project because the ideas is to be able to track change over time and see when something has gone wrong without teams having to pour
through the data manually and frequently. The compare page was heavily influenced by pset6 when we did the Similarities problem. This allows users to see where results differ quickly
and visually.
