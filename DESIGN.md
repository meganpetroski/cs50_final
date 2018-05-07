A "design document" for your project in the form of a Markdown file called DESIGN.md that discusses, technically,
how you implemented your project and why you made the design decisions you did. Your design document should be at least several paragraphs in length.
Whereas your documentation is meant to be a user’s manual, consider your design document your opportunity to give the staff a technical tour of your project underneath its hood.

Heartbeat was originally born out of the frustration of doing manual, repeative, frankly boring, but overall necessary, quality checks to the
data produced in house at our company. These datasets have grown larger and larger over the years and it is still critical to perform all of these checks.
Over the past year Betsy and I have worked together to design the system, create the SQL queries for all of the checks, store the code in version control,
and work with fellow engineers to wrap the code in an automated executor (Jenkins). But we needed to take this one step further. The Jenkins console ouput
was mediocre at best and required user to ctrl+f to find the tables they were looking for. We now have a csv output of the data each time a build number and
product are chosen and run but it's still not as pretty as we want it to be. This class gave us the skills and confidence to do what we really wanted -
create a simple webpage that displays the results in different ways based on user input.

The first step in implementing this project was creating a mock dataset. We have a number of rules around our data so this is a subset we mocked up
that we will be able to scale up in house. It took a few tries to get the table organized and the column field types correctly labeled. Instead of adding the
1000+ rows of data we wanted available for this project, we created a CSV that we could both work on and uploaded that via the phpliteadmin interface. This took
a bit of finagling because I sillily enough forgot that a CSV is divided by commas not semi-colons.

Once the data was in place we started tackling the website portion. Again, it took a bit of trial and error, but we found that starting our website from the beginning
and adding in modules as we need them,