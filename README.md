# Welcome to Belongr!

In one [survey](https://idealdeisurvey.stanford.edu/explore-results/narrative-summary/undergraduate-students) of university students at a particular institution, almost half of respondents indicated at least one place where they felt marginalized or excluded. 

Belongr is here to change that.

Belongr is a web application for email-verified university students to anonymously see and rate the levels of inclusivity of university-recognized student organizations on their campus in the contexts of racial identity, ethnic identity, gender identity, sexual orientation, socioeconomic status, religious identity, and disability identity. For each university-recognized student organization, Belongr provides for each context a histogram of inclusivity ratings and their mean and median.

## Builders of Belongr

Belongr was programmed by Drake Du and Maya Dummett with some code from the Exploration Team of [Tech for Social Good of the Harvard Computer Society](https://socialgood.hcs.harvard.edu/). Further documentation can be accessed [here]().

## Getting Started

Ensure you have pip installed by opening your terminal and running `pip --version`. If pip is not installed, you will get an error such as "pip not found." To remediate this, you can install pip using this [Online Guide](https://www.geeksforgeeks.org/download-and-install-pip-latest-version/).

Next, make sure you are in the "webapp" folder. Then, execute: `pip install -r requirements.txt`.

## Running Flask

First, make sure you are in the "belongr" folder. To run Belongr in Flask, execute these three lines.

`export FLASK_APP=webapp`
<br/>
`export FLASK_ENV=development`
<br/>
`flask run`

If `flask run` is not working, try `python3 -m flask run`.

## Access Belongr

To access Belongr, find and copy from terminal the address http://127.0.0.1:5000. Then, enter and run this address into your browser. You are now ready to use Belongr!

## View Inclusivity Ratings

To view inclusivity ratings, you do not need to sign up for an account! All you have to do is simply click the "Search for Ratings" button in the navigation bar and input the student organization name for which you are looking for inclusivity ratings! For this version of Belongr, the only student organization name supported is "Harvard Computer Society" exactly as written.

## Provide Inclusivity Ratings

To provide inclusivity ratings, you must sign up for an account. You can do this by clicking the "Sign Up" button in the navigation bar and entering in all appropriate fields. Once you have done this, you will be redirected to the "Sign In" page. Enter in your account information, and you are all set to provide inclusivity ratings to Belongr! You can do this by clicking the "Rate" button in the navigation bar and filling out all appropriate fields.

## See Your Ratings

To see your inclusivity ratings, simply click the "Your Ratings" button in the navigation bar! To change your ratings for a student organization, simply click the "Rate" button in the navigation bar and rate again the student organization.

## Sign Out

To sign out, simply click the "Sign Out" button in the navigation bar!

## Change Password

To change your password, simply click the "Change Password" button in the naviation bar, and fill out all fields!
