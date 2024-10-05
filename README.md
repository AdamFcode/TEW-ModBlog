# The Unofficial TEW IX Mod-Blog
The Unofficial TEW IX Mod-Blog is a website designed to present streamlined information regarding mod releases for TEW IX.

Total Extreme Warfare (TEW) is a game originally developed in 1995 as Extreme Warfare by programmer Adam Ryland. A complex simulator for wrestling, the game has seen twelve iterations total and nine under the TEW moniker, the most recent of which released in 2024. The game boasts its own internal fantasy world of wrestling promotions but fully supports mods to produce any number of interesting, real-life scenarios.

The GreyDog Software(GDS) forums provide a hub for discussing, uploading and downloading mods. However, the forums can be very overwhelming for new players as the community serves a very niche pool of players who have mostly been playing for years. As such, the forums can be difficult for aspiring players to navigate, as I learned when I started playing the 2016 version of the game.

The Unofficial TEW IX Mod-Blog is envisioned as a streamlined place to find information regarding upcoming mods and current releases for new players who have not yet been fully integrated into the community. Like any niche endeavour, the forums are full of in-jokes and memetic posts that can be very confusing for new players; the hope is that this website can provide more general information on how to approach modding the game and hopefully serve as a palatable bridge for those who wish to try the game for themselves using real-life companies and workers.

![Am I Responsive Mockup](static/readmeimg/amiresponsive.webp)
[Live Deployment](https://tewmodblog-2cfe2f71314a.herokuapp.com/)

# Design & Planning
## User Stories
- As a user I want to
  - Easily and intuitively navigate the website
  - Register for an account so I can contribute
  - Have control over my contributions
  - Logout and Login with ease
  - Understand each posts intention without clicking into it
  - Click into and view any post I'm interested in
  - Browse a set of resources related to the website

 The above will be addressed under Testing below
 
## Wireframes
The Wireframes for this website were designed using Balsamiq and have been mostly adhered to. A Bootstrap 3 theme, Jumbotron Narrow, was used and modified to suit the needs of the project as it closely resembled the desired layout and allowed for increased focus on the more technical aspects of the code. This theme had many components altered in order to more closely represent the intentions laid out in the wireframes below.

#### Wireframe for Homepage:
![Homepage Wireframe](static/readmeimg/modblog-home.webp)

#### Wireframe for Blog Posts:
![Blog Posts Wireframe](static/readmeimg/modblog-posts.webp)

#### Wireframe for External Resources:
![External Resources Wireframe](static/readmeimg/modblog-links.webp)

## Agile Methodology
This website was designed using an Agile Methodology. Features for this project were planned ahead of time and tracked using a Kanban Board which was hosted on the programmers Github profile.

This can be seen [here](https://github.com/users/AdamFcode/projects/2)

## Typography
Standard fonts were used across the project to mimic the style of presentation on the GDS forums and in the game itself. TEW has often been lovingly declared a "spreadsheet simulator", with the outdated UI and lack of animation pointed out to support this. For better or for worse, the stripped down style of TEW is one of the major things, along with its internal complexity, that has differentiated it from its competition over the years. Most players are quite fond of this barebones approach and so it was decided to emulate this for the website.

## Colour Scheme
Once again, it was decided to mimic the general presentation of TEW with a basic colour palette, one inspired by TEW 2016 specifically. A dark grey tone was used for background colours with gold implemented for headlines and highlights. 

Text was originally presented using a Royal Blue, similar to the text colour used both in-game and on the GDS forums. This returned problems during lighthouse testing with readibility which were initially deemed acceptable. However, the project mentor pointed out the dull contrast which led to the text colour being reevaluated. Standard white was settled upon as the text colour as it provided the most readability without straying to far from the generally drab tones of TEW.

#### Colour Palette
![Colour Palette](static/readmeimg/modblog-coolors.webp)

## Database Schema
![Database Diagram](static/readmeimg/modblog-erd.webp)

# Features
* Note: As noted above in Colour Scheme and below in Testing, the text colour for the website was changed from royal blue to white late in development for the sake of readability. As a result of project deadlines, the following images showcase the original text colour. The change can be seen in the live deployment of the website but unfortunately there was not enough time to capture and upload new images showcasing this change.
  
## Navbar
The top of the website has a navbar to allow easy navigation of the site. It includes an anchor for the homepage, titled as TEW IX Modblog. The navigational links change depending on the login status of the user. 'Blog' and 'Links' appear regardless of login status. Should the user not be logged in, they're are presented with 'Signup' and 'Login'. If the user is already logged in, these two options are replaced with 'Logout'.

* Note, the 'Blog' navigation was initially listed as 'Home'. The project mentor recommended that this be changed as the Home Page serves as the Blog Posts page and it led to confusion when navigating the website. As this was pointed out late in development, the below image showcases the original 'Home' navigation, though this change has been made on the deployed website. The same is true of the 'Signup' navigation, which initially read 'Register'.

![Navbar](static/readmeimg/2-navbar.webp)

## Jumbotron
A jumbotron sitting at the top of each page provides a description of the website's intent along with an inset image of TEW IX's main-menu image. It also recommends that users either Signup or Sign in  to leave a comment. 

![Jumbotron](static/readmeimg/3-jumbotron.webp)

## Blog Preview
Below the jumbotron on the 'Blog' homepage, three blog post previews are presented. These previews provide the title, author, upload date and a truncated excerpt of the blog content, allowing the user to see whether the specific blog post is of any interest to them.

![Blog Preview](static/readmeimg/3.5-blogtitle.webp)

## Blog Post Pagination
Three preview blog posts are displayed to the user, deemed the ideal amount before the page became overly cluttered. Below these posts is a 'next' button to allow the user to scroll through different blog posts. Once clicked, a 'previous' button appears allowing the user to scroll back the way they came. Should they reach the last page, the next button is then hidden.

![Blog Next](static/readmeimg/4-posts1.webp)
![Blog Prev](static/readmeimg/5-posts2.webp)

## Singular Blog Post
Upon clicking on the desired post, the user is shown the full post complete with a comment section below. The post also lists the GDS username of the individual or individuals who made the associated mod. The users login status dictates what functionality is presented to them in the comment section (covered further down).

![Blog Post](static/readmeimg/6-singlepost.webp)
![Comment Section](static/readmeimg/7-commentsection.webp)

## Links Section
Hoping to curtail any unrelated links from being commented on the website, a ban against any links whatsoever has been instigated, with a dedicated section open to users to navigate off-site to related, trusted domains. This was done via a Model so that the SuperUser can change these links through the admin panel. These links have titles that lead to the listed website when clicked upon and a short description of the site in question.

![Links](static/readmeimg/8-links.webp)

## Signup
Signing up for the website is easy, with a form given to the user to fill out before being submitted. This form captures basic information with the email section being optional. 

![Signup](static/readmeimg/10-signupfill.webp)

Should the user input incorrect information, they receive a feedback message which lets them know that a mistake has been made.

![Signup Incorrect](static/readmeimg/11-signupincorrect.webp)

Upon signing up successfully, a mesage is related to the User to inform them that they are now signed into the website under their chosen username.

![Signup Success](static/readmeimg/12-signupsuccess.webp)

## Comments 
Once signed in, a textfield appears beside the comments section of each blog post, allowing the user to leave a comment if they wish. These comments require approval in the admin panel in order to moderate content.

![Comment Field](static/readmeimg/13-commentbox.webp)

Should the user decide to leave a comment, they receive a message to confim their comment submission and to inform them that they're awaiting approval.

![Comment Notification](static/readmeimg/14-commentsuccess.webp)

Once a comment is aprroved it can be seen by all. The user is also presented with two buttons below their comment; one to edit their comment and the other to delete it.

![Comment Buttons](static/readmeimg/15-commentbutton.webp)

Should they click the edit button, the comment textfield becomes auto-populated with their current comment, allowing them to edit it. The submit button is also replaced with an update button.

![Comment Edit](static/readmeimg/16-commentedit.webp)

Upon clicking update, the user is presented with an update success message and, as seen below, their comment is updated to the current state.

![Update notification](static/readmeimg/17-updatesuccess.webp)
![Updated Comment](static/readmeimg/18-editedcomment.webp)

Should the user decided to delete their comment, they can click the delete button. This will bring up a modal for them to confirm whether they want to delete their comment or not. Should they close the modal, their comment will remain untouched.

![Delete Confirm](static/readmeimg/19-commentdelete.webp)

If the user confirms the deletion, the comment will be removed and they will be given a notification informing them of the successful deletion.

![Delete Notification](static/readmeimg/20-deletesuccess.webp)

## Signing Out
The Logout option provides the user with a sign out button. This extra step was added to ensure that any user who accidentally clicked the Logout button does not have to then go through the process of signing in again.

![Logout Confirm](static/readmeimg/21-signout.webp)

If this button is clicked, the user is signed out, provided with a message to confirm this and the navbar gets reset to the state any unregistered user is presented with.

![Logout Success](static/readmeimg/22-signoutsuccess.webp)

## Signing In
When a user returns and clicks on the Login button, they will be redirected to a form requesting their user details.

![Sing In](static/readmeimg/23-signin.webp)

If incorrect information is entered, the user is presented with a message informing them that their username/password is invalid.

![Sign In incorrect](static/readmeimg/24-signinincorrect.webp)

Once the user has entered the correct information, they are redirected to the Blog Posts page and given a notification confirming their successful sign in.

![Sign In Success](static/readmeimg/25-signinsuccess.webp)

## Footer
A simple, themeatically consistent footer was decided upon, displaying only the name of the programmer. 

![Footer](static/readmeimg/26-footer.webp)

# Features Earmarked for Future Implementation 

# Testing

# Bugs

# Deployment

# Credits 
