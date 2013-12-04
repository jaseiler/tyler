===============================
Tyler
===============================

<<<<<<< HEAD
.. image:: https://travis-ci.org/runmycode/tyler.png?branch=master
        :target: https://travis-ci.org/runmycode/tyler

This is a proof of concept for a Django-based RunMyCode site.

* Free software: MIT license
* Documentation: http://tyler.rtfd.org.

* Issue tracker: https://github.com/codersquid/tyler/issues
* Kanban board: https://trello.com/b/8KC8wAye/rmc
* Wiki: https://github.com/runmycode/tyler/wiki/_pages


Features
--------

This is a proof of concept; please pardon the mess.

* `home`: this handles the landing page, faq, and similar concerns that don't call for separate apps.
* `members`: this handles member profiles. It's very spare for now.
* `news`: this handles short twitteresque announcements and news. I'll probably dump this app. I just exists to demonstrate quickly something akin to newsfeed on the main page.
* `supportingmaterials`: this handles pages for article companion sites with code and data. It's spare for now. I wanted a generic name so I picked supportingmaterials. what a meh name?


* TODO
=======
.. image:: https://travis-ci.org/researchcompendia/tyler.png?branch=master
        :target: https://travis-ci.org/researchcompendia/tyler

A proof of concept for a research compendia webapp.

Introduction and Goals
----------------------

ResearchCompendia is a project to allow scientists to create compendium as
introduced by Gentleman and Temple Lang [#]_. Now that much of that data and analysis is generated
computationally, it is natural to expect that code and parameters also be
shared. Additionally, it is right to expect that researchers ought to document
the computational portions of their research methods as thoroughly as they
would document a tabletop experiment.

The application has the following goals.

* We will make it possible to archive all of the data, codes, documentation, parameters,
  and environmental settings linked with published research in a versioned form.
* We will support the verification and validation processes by providing for the execution
  of shared code and the visualization of results.
* We want to help and encourage researchers to manage their research in a way that makes it mixable and executable.
* Most of all we wish to make these tools heavily automated, and easy to access and
  utilize to lessen the exertion required from already overburdened academic researchers in the process of
  publishing fully reproducible work.


If you are a programmer, you may find yourself thinking that some of these goals remind you of
a continuous integration and build system. And yes, in some sense the goal with this
prototype is to create a continuous integrations system for computational research.

Project milestones are loosely organized on our `planning wiki page <https://github.com/researchcompendia/tyler/wiki/planning-scratchpads>`_.

Project Structure
-----------------

This is a django project with the following structure.

* `home`: this handles the landing page, faq, and similar concerns that don't call for separate apps.
* `users`: this handles users and profiles by using django-allauth and cookiecutter-django's user template
* `compendia`: this handles the archiving and representation of a compendium.
* `lib`: this holds code that does not call for an app
* `api`: this handles our service apis.

Resources
---------

* Free software: `MIT License <http://opensource.org/licenses/MIT>`_
* Technical Documentation: http://tyler.rtfd.org
* Issue tracker: https://github.com/researchcompendia/tyler/issues
* Issue kanban: https://huboard.com/researchcompendia/tyler
* Wiki: https://github.com/researchcompendia/tyler/wiki
* IRC: #hackingscience on freenode.net

Development Environments
++++++++++++++++++++++++
* Live beta http://researchcompendia.org
* Pre-prod: http://labs.researchcompendia.org
>>>>>>> upstream/master

Acknowledgements
----------------

<<<<<<< HEAD
* Many thanks to future contributors
* My coworkers
* The reproducible science community
* Many thanks to Audrey Roy and Daniel Greenfeld for writing https://django.2scoops.org/ and many other useful blog posts and repos.
* Many thanks to everyone who has posted helpful information on using Heroku with Django.

Random Stuff
------------

tyler is named after Rose Tyler, who was a companion of The Doctor. Django is named after a person too.

if I was an artist, original ascii art would go here.
=======
Make a separate acknowledgements page?

References
----------

.. [#] Gentleman, Robert, and Duncan Temple Lang. 2007. “Statistical Analyses and Reproducible Research.” Journal of Computational and Graphical Statistics 16 (1): 1–23. doi:10.1198/106186007X178663. http://www.tandfonline.com/doi/abs/10.1198/106186007X178663.
>>>>>>> upstream/master
