UNDERSTANDING - how it does it; how you implemented it and why you did what you did (Betsy doing what they do)
A "design document" for your project in the form of a Markdown file called DESIGN.md that discusses, technically, how you implemented your project and why you made the design
decisions you did. Your design document should be at least several paragraphs in length. Whereas your documentation is meant to be a user’s manual, consider your design
document your opportunity to give the staff a technical tour of your project underneath its hood.
all source code should be thoroughly commented.

HTML files
Starting with the layout.html page, we borrowed from past psets and a number of W3 School resources to design the template for the website. We played with fonts
and colors to make the website pleasing and adjusted headers and paragraph sections to appropriate, readable sizes. The nav bar took a little bit of trial and error
to get the Heartbeat name to stay a different color and static and then set up the other links. Home has a few special elements to it like the embedded Smartsheets calendar
and the ability to email staff with questions or additonal queries. The email was incredibly easy to set up with the "mailto" function. Smartsheets offers
users the ability to download a report (in this case a calendar) into Google sheet and then we read the documentation (via Google) on how to add an embedded sheet to
the webpage. The quality team is the biggest consumer of the results Heartbeat provides so the Smartsheet we added was the calendar of releases for the product
we picked for the dataset. Our users often have suggestions for queries to add, so we've added a support email using the mailto tag that allows them to send a note to us
with their idea. The query page is simply a listing of text seperated by line breaks <br>. The result page is where we needed to iterate through a list of buildnumbers
in a drop down menu and allow a user to select a particular run. The submit button needed to be implemented so that it would kick off the printing to the screen and the
downloading a CSV file. Compare is pretty much the same as what we did for pset6 - takes 2 input files and then shows the resulting highlighted differences. This was the
most difficult element to make work but more on that in the application.py section.

PY files
Compare.py and helpers.py are both from pset 6 with a few minor changes. We wanted compare to always work on a line by line basis since the queries are always done in the same
order so we removed the other options that were available in pset6 and defaulted to always checking line by line. This code reminded us about the difference between get and post
as well as checking for nulls and not leaving ourselves open to sql injection attacks. The hardest part of the later psets was taking code that we hadn't written from scratch so
this portion of our final project definitely proved the trickiest! Application.py followed a similar format as the psets, main differences being our heartbeat.db database and
the data table within it (more on that shortly). As we added new features and bits of code, we added to the modules at the top of the file. At first we had tried to start with
a fully fleshed out version of application.py from another pset and replace as we went but that proved to be more complicated than starting from scatch. Other highlights of
application.py was the results section. One of the harder and more fun things we aimed for was being able to download the results selected into a csv. Quite satisfying when
the csv spit out! This served two purposes - gave users a hard copy to manipulate as they wanted and provided a csv for uploading in the compare section.
Iterating over the output to provide the results in the format we liked (not just a dump of key:value pairs) took some time to tweak. We noted all of our resources in the
resources.txt file as they quickly became more numerous than our code had room for.

HEARTBEAT.DB
The database needed to be set up properly before we could do much of the implementation of the tougher parts of our goal so this was the first thing we started with.
Phpliteadmin is pretty amazing in the CS50 interface. We simply made a csv with all the mock data we wanted to include with the project and then created a table (data)
and were able to add all the fields and field types easily. From there we uploaded the csv and boom, 1100+ records later we were ready to go.

TXT files
We included requirements.txt for the comparison portion of things and resources.txt to fully list out all of the resources we consulted while solving the challenge of the
final project.

OVERALL THOUGHTS
Overall, we wanted the implementation of Heartbeat to be simple and this influenced every descision we made. Keeping the html pages free of distraction and crazy colors so that
the purpose of the site was clear for our end users. cd ..