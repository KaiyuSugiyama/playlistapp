![Sushi](https://cdn.discordapp.com/attachments/783082777020203061/799906807388307496/unknown.png)
# Sushi
Group Project for tri2!
### Links
- [Project Board](https://github.com/zenxha/sushi/projects/1)
- [Week 1/15 Project Board](https://github.com/zenxha/sushi/projects/2)
- Runtime link: rubinfamily.dyndns.org:5000
### Grading
#### Scrum Master Grade: 19/20
#### Individual
- Allen Xu:5/5
- Chris Rubin: 5/5
- Devam Shrivastava:5/5
- Komay Sugiyama:5/5

### Collaborators
- Allen Xu ID: #72947445
- Komay Sugiyama ID: #30739783
- Chris Rubin ID: #72892271
- Devam Shrivastava ID: 51984972

## Summary
- We aim for a simple and clean site that contains everything about sushi. On the site you’ll be able to search our database of sushi’s and read about each sushi’s description and origin. If you sign up, you’ll be able to save your favorite sushi’s and post

## Additions for 1/15/2021 Week:

### Project Plan webpage:
- We have a page dedicated to our project plan, which we have embeded.
  ![Project Plan](https://cdn.discordapp.com/attachments/783082777020203061/799907431709671455/unknown.png)

### Upload Page: 
- This is our new updated Upload page. This is a combination of HTML and CSS (which was for the design of the form).
  ![Upload](https://cdn.discordapp.com/attachments/783082777020203061/799908471565975572/unknown.png)

### Login (Probably the hardest thing to do all year):
- Created a login page and when the first login occurs, the username and password is stored in Users.db
  ![Login](https://cdn.discordapp.com/attachments/783082777020203061/799911326968840192/unknown.png)
- The code that helps save the username and password in the database is shown below:
  ![Code](https://cdn.discordapp.com/attachments/783082777020203061/799912990979784724/unknown.png)
- When you click submit, it takes you to the User confirmation page shown below (and also has the project page embedded):
![User](https://cdn.discordapp.com/attachments/783082777020203061/799913571285991444/unknown.png)
## Things we want to have:
- Database of every sushi
- Types of sushi: https://www.tablespoon.com/posts/know-your-sushi-types-and-terms-before-ordering
- Menu example: https://www.toasttab.com/rbsushi-ranchobernardo/v3
- Login system that people can create/save accounts with
- Have users be able to upload their own sushis (picture, desc, reviews)[SQLAlchemy]
- Do this with database that will store sushi name, images, description, user reviews onto database (CB Big Idea #2 and #3)
- Have an option to view the descriptions and reviews of the sushi
- Pull from the database and display that information
- Library of all the tier lists other people have made that the user can browse
- Redirects to social media to draft messages

## Structure/Design:

* Function on flask
* Navbar that lets user navigate the website from info on sushi to posting their favorite sushis
* Data driven UI designs will be storyboarded through google drawings, then implemented into the website once approved. (CB Big Idea #3)
* Login function to save information the user performs in database
* Upload page will allow user to add own sushi images into database
* Database holds information to
  * Sushi types, descriptions, and rating out of 10
  * Login information (this has to be dynamic)
  * Saved tier lists
  * Images to sushis submitted by the users (will include file size limiter, file type selector)


## Planned Features
- Database of every sushi
  - Types of sushi: https://www.tablespoon.com/posts/know-your-sushi-types-and-terms-before-ordering
  - Menu example: https://www.toasttab.com/rbsushi-ranchobernardo/v3
- Login system that people can create/save accounts with
- Library of all the tier lists other people have made that the user can browse
- Redirects to social media to draft messages

## Current Assignments
- Allen Xu: Work on website navbar, edit and upload code video
- Chris Rubin: Help set up navbar and assist Devam in backend
- Devam Shrivastava: Work on backend code which consits of the database
- Komay Sugiyama: Help with website blueprint, brainstorm backend

## Weekly Updates
### Week 4
- Upload page is fully functional, CSS will be incorporated later
- Login working, sessions are saved in cookies, planning on adding a password function later on
- Database working on Devam's individual github, will add to main github soon
### Week 3
- Continued work on upload page, mainly fixing file directory path and adding CSS
- Continued work on log in page
- Began using SQLite for database creation
### Week 2
- Changed backgorund to use an api for many different sushi pictures
- Started work on an upload page that adds images into our database upload via user
- Started work on a log in page for the site
### Week 1
- Added a navbar to the website
- Added a custom moving background
- Added a projects page which displays our project plan
- Started work on the database setup
### Week 0
- Created README layout
- Started storyboarding UI layouts for the website
- Transfered information from google docs onto github readme
