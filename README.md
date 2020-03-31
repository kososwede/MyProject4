# Unicorn Attractor
#### Milestone Project 4

[![Build Status](https://travis-ci.org/kososwede/MyProject4.svg?branch=master)](https://travis-ci.org/kososwede/MyProject4)

## ABOUT MY APP
___
This is my fourth and final milestone project for [Code Institute](https://www.codeinstitute.net). The app that I have created is for a made up game called Unicorn Attractor. My site allows users to log bug reports that they have found in the game or to add feature requests for a small fee that when the target amount has been reached the feature that was requested will be worked on and then implemented into the game.

Here you will find a link to my website via HEROKU: <https://myproject4-mcilgrew.herokuapp.com>

Here you will find a link to my code via GITHUB: <https://kososwede.github.io/MyProject4/>

## UX
___
#### USER STORIES

As a user to this website I would like to be able to:
* Register an account
* Log BUG tickets
* Add a FEATURE request tickets
* Upvote a ticket someone else has created
* Comment on any tickets that have been created by myself and others
* Delete tickets I have created
* Edit tickets that I have created
* Reset my password if forgotten
* View all tickets created by myself and others
* Edit my account/profile if information changes

#### WIREFRAMES
I created these wireframes using [BALSAMIQ](https://balsamiq.com). I created wireframes for desktop and mobile versions of my app so that it would be available and easy to navigate no matter what device you have.
The wireframes can be found here:
* MOBILE <https://github.com/kososwede/MyProject4/blob/master/wireframes/msproject4-mobile.png>
* DESKTOP <https://github.com/kososwede/MyProject4/blob/master/wireframes/msproject4-desktop.png>

## FEATURES
___
#### FUNCTIONALITY
My app uses Python logic so users can login or register. The app offers Create, Read, Update and Delete
features that allow users to create, read, update and delete tickets. Upvoting tickets require a small donation

#### FEATURES AVAILABLE NOW
* **Navbar Links** - When the user is logged in the navbar shows Home, Tickets, Logout, Profile and About and if the user is not logged in it displays Home, Tickets, About, Login, Register.
* **SideNav** - A sidenav is activated on smaller screen sizes and displays the same info as the navbar.
* **Login** - Users who have already registered can log into their account using their username they registered with and their password
* **Logout** - Users can log out of their account using the LOGOUT link on the navbar or sidenav
* **Register** - Users can register for an account by supplying a username, first and last name, email address and password that needs to be entered twice to match. usernames and email addresses that are entered must be unique and there are checks to ensure this
* **Reset password** - Users can reset their password if they have forgotten it, the user is redirected to a page where they must enter their email address they registered with, they will then be sent a link to reset their password
* **Edit profile** - Users can edit their profile in the profile page. They can can then change whatever info they need to
* **Profile page** - When a user is logged in they can see their profile page that displays the tickets they have added, their user info and also can edit this info
* **Tickets** - All the tickets are visible when on the tickets page is loaded and they are ordered with the most upvotes first
* **Single view Ticket** - When a ticket has been clicked on the user is directed to a page which shows the ticket details in full
* **Flash messages** - These messages appear at the top of the screen to give the user information like if they were successfully logged in or out or if they where successful at creating a ticket
* **Edit tickets** - The user can edit a ticket but only if it was them who had created it
* **Delete tickets** - The user can delete a ticket but again only if it was created by them
* **Upvote tickets** - This allows users to upvote other users tickets only if they are logged in
* **Comment on a ticket** - This feature allows users to comment on tickets but only if logged in

#### FUTURE FEATURES
With alot more knowledge and time I would like to add the followinf features:
* **SEARCH** - I would like to add search functionality so that users can search to see if a particular bug or feature has been created
* **FILTER** - I would like to add a filter option on the tickets page so that users can choose what tickets they want to see

## TECHNOLOGIES USED
___
* [Balsamiq](https://balsamiq.com) - Balsamiq was used to create my wireframes for my app
* [HTML](https://en.wikipedia.org/wiki/HTML) - **HTML** was used to create the basic elements and content of my app
* [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) - **CSS** was used to apply custom styles to the elements and contents of my app
* [Materialize](https://materializecss.com/) - This project uses the  **Materialize** framework with built in components to add style to my app
* [jQuery](https://jquery.com/) - I have used **jQuery** as the main javascript functionality
* [Python](https://www.python.org/) - **Python** is used as the back-end programming language to my app
* [Django](https://www.djangoproject.com/) - **Django** is used as the Python web framework
* [Jinja](https://jinja.palletsprojects.com/en/2.11.x/) - **Jinja** is used for templating Python and Django in my HTML code
* [Stripe API](https://stripe.com/en-se?utm_campaign=paid_brand-SE_en_Search_Brand_Stripe-1436985502&utm_medium=cpc&utm_source=google&ad_content=275927467364&utm_term=stripe%20api&utm_matchtype=e&utm_adposition=&utm_device=c&gclid=Cj0KCQjw1Iv0BRDaARIsAGTWD1unrSFWPSGo-1fRd2iAY6i7W7vEUtOOrSs6fcUufRz9S00YtknllQYaAkF_EALw_wcB) - **Stripe** was used in my project to make secure payments
* [SQLite](https://www.sqlite.org/) - **SQLite** was used when running the app locally
* [Postgres](https://www.heroku.com/postgres) - **Postgres** in Heroku was used when deployed remotely
* [Google Fonts](https://fonts.google.com/) - **Google Fonts** was used to add style to the text
* [Font Awesome](https://fontawesome.com/) - **Font Awesome** was used for the icons in my app
* [Gitpod](https://www.gitpod.io/) - **Gitpod** was used as the IDE to write my code for my APP
* [Git](https://git-scm.com/) - **Git** was used for version control so that i could add and commit my code before pushing to github
* [GitHub](https://github.com/) - **GitHub** was used to push and save the commited changes my app from Git
* [Heroku](https://www.heroku.com/) - The hosting platform **Heroku** was used to deploy my app

## TESTING
___
My website was tested in Chrome, Firefox, Safari, Opera 
and Microsoft Edge. It was also tested on android and ios
 devices and all worked as it should. A link from **HEROKU** was sent to my 
 family and friends in England to make sure that it worked on all of their devices. 
All buttons worked and opened in a different browser window. 
 I was testing my website at every major point in production to make sure everything 
 I was implementing was working and running smoothly. Every button has been tested to make sure 
 that it has the correct reaction. My HTML5 CSS3 and my PYTHON code have all been checked in:
 * <https://validator.w3.org/> - to check **HTML** code
 * <https://jigsaw.w3.org> - to check **CSS** code
 * <https://extendsclass.com/python-tester.html> to check my Python code

 #### TRAVIS CONTINUOUS INTEGRATION
 [Travis CI](https://www.googleadservices.com/pagead/aclk?sa=L&ai=DChcSEwjAk_mPnsXoAhVM5poKHQpTALYYABAAGgJsbQ&ohost=www.google.com&cid=CAESQOD2FldjfBPo4QjkuA3N-qI7gFEUpooQymrmAfHBMyNB5i_qq-7kqtBO3jqzaG14c_cpkDDO1jqMd4ud6bxk5Ss&sig=AOD64_1sVw1TKc74_s33lk7ZdJGc87shyA&q=&ved=2ahUKEwj-hfKPnsXoAhWawMQBHddNDswQ0Qx6BAgeEAE&adurl=) - Used for continuous Integration testing of my code

## DEPLOYMENT
___
GitHub was used for my version control and Heroku to host the live version of my website. To deploy it to Heroku i used these steps:

1. I created the app in Heroku
2. Clicked on Resources and typed in **Postgres** and select **Free hobby level**
3. Add the DATABASE_URL info to my env.py
4. Create an environment variable in my settings.py that can grab the info from my env.py
5. Import the dj_database_url package in my settings.py
6. Ran `python3 manage.py makemigrations` then `python3 manage.py migrate` to migrate models into Heroku Postgres
7. Copied and pasted the contents of my env.py file and added them to the config vars in Heroku
8. Connected my app to the GitHub repository in the **Deploy** tab and selected **Enable Automatic DEPLOYMENT
9. In **Stripe** I went to the **Developers** section and selected the **API Keys**
10. I copied and pasted the **Publishable Key** and the **Secret Key** and then set them
as the `STRIPE_PUBLISHABLE` and `STRIPE_SECRET` environment variables in my env.py file in my local workspace
11. I then updated the settings.py file with the new Stripe environment variables
12. Created a new S3 Bucket in the **S3** section of **AWS**
13. In the bucket permissions, I changed the **CORS Configurations to:
```<?xml version="1.0" encoding="UTF-8"?>
<CORSConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
<CORSRule>
    <AllowedOrigin>*</AllowedOrigin>
    <AllowedMethod>GET</AllowedMethod>
    <AllowedMethod>HEAD</AllowedMethod>
    <MaxAgeSeconds>3000</MaxAgeSeconds>
    <AllowedHeader>Authorization</AllowedHeader>
</CORSRule>
</CORSConfiguration>
```
14. Also in the **S3** section, the **Bucket Policy** was changed to this:
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::<my-bucket-name>/*"
        }
    ]
}
```
15. I then replaced ```<my-bucket-name>``` in the ```Resource``` line with my own **S3** Buckets name instead
16. In the **IAM** section of **AWS** I created a new group and attached my **S3** Bucket details into it
17. Also in the **IAM** section I created a 'New Policy' along with 'New User' and attached these to the new group
18. I then updated the settings.py file in my local workspace with the relevant **S3** Bucket details
```
AWS_S3_OBJECT_PARAMETERS = {
    'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
    'CacheControl': 'max-age=9460800',
}

AWS_STORAGE_BUCKET_NAME = 'mcilgrews-myproject4'
AWS_S3_REGION_NAME = 'eu-north-1'
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_DEFAULT_ACL = None
```
19. The settings.py file was then updated with configuration for static file storage
20. Ran ``python3 manage.py collectstatic`` to push the static files to the **S3** Bucket I created
21. I then created a requirements.txt file using ``pip3 freeze > requirements.txt`` in the terminal window
22. A **Procfile** was then created in the terminal window ``echo web: gunicorn unicorn_attractor.wsgi:application > Procfile``
23. Ran ``git add .``, ``git commit -m "<message>"`` and then ``git push`` to push all my changes to my **GitHub** Repository

**My app was then deployed to Heroku**

To be able to run my code locally, users can download a copy of my code to their desktop by following these steps:

1. Go to my [GitHub repository](https://github.com/kososwede/MyProject4)

2. Click on 'Clone or download' under the repository name

3. Then copy the clone URL for the repository in the 'Clone with HTTPs section'

4. Open 'Git Bash' in your local IDE

5. Change your current working directory to the location where you want the cloned directory to be made

6. Type ``git clone``, then paste the URL you copied in Step 3:

``git clone https://github.com/USERNAME/REPOSITORY``

7. Press Enter to complete and create your local clone.

8. In your local workspace set your own credentials for the environment variables:
Create a ``.env,py`` file with your own credentials and import this into the settings.py file
9. Install the ``requirements.txt`` file by running this command in your CLI Terminal:
``pip3 install -r requirements.txt``
10. Then run the following command in your Terminal to launch the Django project:
``python3 manage.py runserver $IP:$PORT``
11. Click the ``http://`` link in the terminal, and the project will load
12. Then you can run the following commands to migrate the database models and create a super user:
```
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
```
When migrations are complete and super user created, the site should run locally.

## CREDITS
___
* I have to start of by saying that for my project I got inspiration from a fellow Code Institute Student [hebs87](https://github.com/hebs87)'s project 4. Therefore I have used some code from this project as I was struggling to get to terms with the back-end side of this project.
* w3schools https://www.w3schools.com/html/default.asp
* Materialize https://materializecss.com/
* CSS-tricks https://css-tricks.com/
* stackoverflow https://stackoverflow.com/
* Various videos on youtube https://youtube.com
* FreeCodeCamp.org
* Code Sketch

#### MEDIA
* The background image was from [Pixabay.com](https://pixabay.com)
* Logo was found at https://cdn3.iconfinder.com


#### AKNOWLEDGEMENTS
* Student Support for letting me have extensions as I have been struggling with the later parts of the course.
* Code Institute tutors for their assistance in getting me this far in the course.
* All the guys and girls in the Code Institute Slack for all of their help.
* My Mentor Dick for all the sound advice he has given me.