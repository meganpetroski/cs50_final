OVERALL THOUGHTS ON HEARTBEAT
Overall, we wanted the implementation to be simple, user friendly, and meet the need of displaying the results of a software program
we’ve already implemented at work. This heavily influenced the design choices and languages that we used in the project.
Python and Flask were used because we felt most familiar with those tools and they had an incredible number of resources available.
W3 Schools has this amazing tool where you can play with snippets of code and this helped us test out different fonts, background
colors, header placements, and text alignment before we implemented it in our project. Python3 documentation, Google Sheets embedding
documentation, and Stack Overflow were also heavily consulted to help us tweak minor bits and pieces as we got stuck. The last section
of our site, Compare, relies on pieces of pset6 (Similarities-Less). Going through that pset after many more weeks of experience and
tearing apart the code to find the pieces we wanted really made us feel like we understood it infinitely more than we had the first time.

HTML files
Starting with the layout.html page, we borrowed from past psets and a number of W3 School resources to design the template for the
website. We played with fonts and colors to make the website pleasing and adjusted headers and paragraph sections to appropriate,
readable sizes. The nav bar took a little bit of trial and error to get the Heartbeat name to stay a different color and static and
then set up the other links. Home has a few special elements to it like the embedded Smartsheets calendar and the ability to email
staff with questions or additonal queries. The email was incredibly easy to set up with the "mailto" function. Smartsheets offers
users the ability to download a report (in this case a calendar) into Google sheet and then we read the documentation (via Google)
on how to add an embedded sheet to the webpage. The quality team is the biggest consumer of the results Heartbeat provides so the
Smartsheet we added was the calendar of releases for the product we picked for the dataset. Our users often have suggestions for
queries to add, so we've added a supportemail using the mailto tag that allows them to send a note to us with their idea.
The query page is simply a listing of text seperated by line breaks <br>. The result page is where we needed to iterate through a
list of buildnumbers in a drop down menu and allow a user to select a particular run. The submit button needed to be implemented so
that it would kick off the printing to the screen and the downloading a CSV file. Compare is pretty much the same as what we did for
pset6 - takes 2 input files and then allows the user to look at them side by side. This was the most difficult element to make work
but more on that in the application.py section.

PY files
Compare.py and helpers.py are both from pset 6 with a few minor changes. We wanted compare to always work on a line by line basis
since the queries are always done in the same order so we removed the other options that were available in pset6 and defaulted to
always checking line by line. Application.py followed a similar format as the psets, main differences being our heartbeat.db database
and the data table within it (more on that shortly). As we added new features and bits of code, we added to the modules at the top
of the file. At first we had tried to start with a fully fleshed out version of application.py from another pset and replace as we
went but that proved to be more complicated than starting from scatch.  Other highlights of application.py was the results section.
One of the harder and more fun things we aimed for was being able to download the results selected into a csv. Quite satisfying when
the csv spit out! This served two purposes - gave users a hard copy to manipulate as they wanted and provided a csv for uploading in
the compare section. We noted all of our resources in the resources.txt file as they quickly became more numerous than our code had
room for.

HEARTBEAT.DB
The database needed to be set up properly before we could do much of the implementation of the tougher parts of our goal so this
was the first thing we started with. Phpliteadmin is pretty amazing in the CS50 interface. We simply made a csv with all the mock
data we wanted to include with the project and then created a table (data) and were able to add all the fields and field types easily.
From there we uploaded the csv and boom, 1100+ records later we were ready to go.
