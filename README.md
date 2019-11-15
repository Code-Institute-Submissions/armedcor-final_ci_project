[![Build Status](https://travis-ci.org/armedcor/final_ci_project.svg?branch=master)](https://travis-ci.org/armedcor/final_ci_project)

# Six String King

A fictional High end electric guitar website focusing primarily on Gibson Les Paul Guitars.

A live version of the site can be found [here](https://six-string-king.herokuapp.com/)
 
## UX
 
A simple layout that features bootstrap cards that display an image of the guitar along with information like the description of the guitar along with the price.

In Desktop format it displays the cards three across before moving to the next line of cards. In mobile format it switches to displaying the cards one per line.

## Features

 
### Existing Features
- Admin panel - This allows the admin to add, remove or edit items onto the shop page
- User sign up / Login - This feature allows new users to sign up to the website and allows current users to log in to their account.
- Stripe Checkout - A checkout was built which incorporated the Stripe API to allow the site to take secure payments for items on the website
- Search Functionality - A search function was designed to allow users to search for their favourite guitar but key words, eg Searching for a specific color or feature. This was built within the search app which can be found in the project folder.


### Features Left to Implement
- A number of functionality and overall styling is left to implement, I would like to build up the site to include individual product pages and add a specific style to the overall website. The website is extremely bare bones right now because of a lack of time.

## Technologies Used

- HTML
- CSS
- Javascript
- Python
- Django
- Bootstrap 4
- AWS 
- Heroku
- Stripe Payment processing

## Testing

Travis CI was used at all times to make sure the project was functional and validating with all updates and pushes.

## Deployment

The project files are hosted on Github which is linked to the Heroku server to allow automatic updates when a new update is pushed to github.
All static CSS and JS files along with my Media files are hosted on AWS S3 and deployed within the website.



### Media
- The photos used in this site were obtained from sweetwater.com
