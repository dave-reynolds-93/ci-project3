<h1 align="center">Reynolds Recipes Website</h1>

![index.html](/recipes/static/images/recipesDesktop.png)

[View the live project here.](https://reynolds-recipes-15f735067036.herokuapp.com)

This is a recipe site with the aim of clients sharing recipes. It is aimed at people wanting to share there recipes and learn new ones. Features include information about the recipes, with full crud functionality for recipes and cuisine types. with easy navigation between pages.

## User Experience (UX)

-   ### User stories

    -   #### First Time Visitor Goals

        1. As a First Time Visitor, I want to easily understand the main purpose of the site and learn more about the recipes.
        2. As a First Time Visitor, I want to be able to easily navigate throughout the site to find content.

    -   #### Returning Visitor Goals

        1. As a Returning Visitor, I want to find new recipes, and add new ones.

    -   #### Frequent User Goals
    
        1. As a Frequent User, I want to find new recipes and add new ones.

-   ### Design
    -   #### Bootstrap Theme
        -   My original plan was to use a bootstrap theme. However, I couldn't get this to work with the version of Js I used. Instead of changing the version of Js, I stopped using the bootstrap theme, but kept a lot of the css styling that it gave me. I kept using the fonts and colour scheme that came from the theme.
    -   #### Colour Scheme
        -   The three main colours used are rgba(255, 255, 255, 0.7), #e6a756 and rgba(47, 23, 15, 0.9). The failures for the colour contrast are for the colours that don't interact on the website. All the colours that interact pass. ![](recipes/static/images/colourContrast.png)
    -   #### Typography
        -   Raleway and Lora are the 2 fonts used throughout the website, with many backups for both as the fallback font in case for any reason the fonts aren't being imported into the site correctly. The 2 fonts are very clean, and give the website a professional feel.

*   ### Wireframes

    -   All wireframes - [View](/recipes/static/wireframes/wireframes.pdf)


## Features

-   Responsive on all device sizes

-   CRUD design for recipes and cuisines.

## Technologies Used

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
-   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
-   [Flask](https://en.wikipedia.org/wiki/Flask_(web_framework))
-   [SQL Alchemy](https://en.wikipedia.org/wiki/Flask_(web_framework))

### Frameworks, Libraries & Programs Used

1. [Bootstrap 5.3.3:](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
    - Bootstrap was used to assist with the responsiveness and styling of the website.
1. [Google Fonts:](https://fonts.google.com/)
    - Google fonts were used to import the 'Lora' and 'Raleway' fonts into the style.css file which is used on all pages throughout the project.
1. [Git](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
1. [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.
1. [Balsamiq:](https://balsamiq.com/)
    - Balsamiq was used to create the [wireframes](/recipes/static/wireframes/wireframes.pdf) during the design process.

## Testing

The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project. JsHint was used to validate the Javascript.

-   [W3C Markup Validator](https://jigsaw.w3.org/css-validator/#validate_by_input)
-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input)

1.  base.html validated. Jinja errors and warnings.
![base.html Validated](/recipes/static/images/baseValidated.png)
2.  add_recipe.html validated. Jinja errors and warnings.
![add_recipe.html Validated](/recipes/static/images/addRecipeValidated.png)
3.  add_cuisine.html validated. Jinja errors and warnings.
![add_cuisine.html Validated](/recipes/static/images/addCuisineValidated.png)
4.  edit_cuisine.html validated. Jinja errors and warnings.
![edit_cuisine.html Validated](/recipes/static/images/editCuisineValidated.png)
5.  edit_recipe.html validated. Jinja errors and warnings.
![edit_recipe.html Validated](/recipes/static/images/editRecipeValidated.png)
6.  recipes.html validated. Jinja errors and warnings.
![recipes.html Validated](/recipes/static/images/recipesValidated.png)
7.  cuisines.html validated. Jinja errors and warnings.
![cuisines.html Validated](/recipes/static/images/cuisinesValidated.png)
8.  Css validated. There were 5 warnings from external links and extensions.
![Css Validated](/recipes/static/images/cssValidated.png)

### Testing User Stories from User Experience (UX) Section

-   #### First Time Visitor Goals

    1. As a First Time Visitor, I want to easily understand the main purpose of the site and learn more about the cuisines and recipes, and how to implement CRUD functionality for both.

        1. Upon entering the site, users are automatically greeted with a clean and easily readable navigation bar to go to the page of their choice.
        2. The user has two options, read what's on the homepage to see what recipes are already there, or click through to one of the other pages, to add a recipe or cuisine to the site.

    2. As a First Time Visitor, I want to be able to easily be able to navigate throughout the site to find content.

        1. The site has been designed to be fluid and never to entrap the user. At the top of each page there is a clean navigation bar, each link describes the page they will end up at clearly.

-   #### Returning Visitor Goals

    1. As a Returning Visitor, I want to be able to create, read, update and delete recipes and cuisines.

        1. The navigation bar clearly highlights the different pages.

-   #### Frequent User Goals

    1. As a Frequent User, I want to be able to create, read, update and delete recipes and cuisines.

        1. The navigation bar clearly highlights the different pages.

### Further Testing

-   The Website was tested on Google Chrome, Internet Explorer, Microsoft Edge and Safari browsers.
-   The website was viewed on a variety of devices such as Desktop, Laptop, iPhone7, iPhone 8 & iPhoneX.
-   A large amount of testing was done to ensure that all pages were linking correctly.
-   Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.

### Known Bugs

-   Duration field currently accepts negative integers.
-   Haven't implemented adding ingredients to the recipes.
-   The date in the footer is not dynamically added.
-   Whitespace at bottom of some of the pages on some device sizes.
-   When there are no recipes, it still says here are the recipes. Same for cuisine page.
-   Reynolds Recipes in the nav link isn't working.
-   Recipe description text area won't allow typing longer than 2 lines.


### Bugs that were fixed

-   I tried to use a bootstrap theme, but the version of the css in the theme was different to the bootstrap js cdn version included at the bottom of my template. This caused it to not work, so I ended up not using a theme at all, and using my own bootstrap styling. 

### Screenshots

1. Recipes page desktop and mobile.  

Desktop
![Recipes page desktop](/recipes/static/images/recipesDesktop.png)
Desktop Accordion Expanded
![Recipes page desktop accordion expanded](/recipes/static/images/recipesAccordionExpanded.png)
Mobile
![Recipes page mobile](/recipes/static/images/recipesMobile.png)
Mobile Accordion Expanded
![Recipes page mobile accordion expanded](/recipes/static/images/recipesAccordionExpandedMobile.png)

2. Cuisines page desktop and mobile  
Desktop
![Cuisines page desktop](/recipes/static/images/cuisinesDesktop.png)
Mobile
![Cuisines page mobile](/recipes/static/images/cuisinesMobile.png)

3. Add/Edit recipe page desktop and mobile  

Desktop
![Add/Edit recipe page desktop](/recipes/static/images/addRecipeDesktop.png)
Mobile
![Add/Edit recipe page mobile](/recipes/static/images/addRecipeMobile.png)

4. Add/Edit cuisine page desktop and mobile  

Desktop
![Add/Edit cuisine page desktop](/recipes/static/images/addCuisineDesktop.png)
Mobile
![Add/Edit cuisine page mobile](/recipes/static/images/addCuisineMobile.png)

5. Footer desktop and mobile

![Footer](/recipes/static/images/footer.png)

6. Header desktop and mobile

![Header desktop](/recipes/static/images/headerDesktop.png)
![Header mobile](/recipes/static/images/headerMobile.png)


# Deployment

## How to run this project locally

To run this project on your own IDE follow the instructions below:

Ensure you have the following tools: 
    - An IDE such as [Visual Studio Code](https://code.visualstudio.com/)

The following **must be installed** on your machine:
    - [PIP](https://pip.pypa.io/en/stable/installing/)
    - [Python 3](https://www.python.org/downloads/)
    - [Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03)

### Instructions
1. Save a copy of the github repository located at https://github.com/dave-reynolds-93/ci-project3 by clicking the "download zip" button at the top of the page and extracting the zip file to your chosen folder. If you have Git installed on your system, you can clone the repository with the following command.
    ```
    git clone https://github.com/dave-reynolds-93/ci-project3
    ```

2. Open your preferred IDE, open a terminal session in the unzip folder or cd to the correct location.

3. A virtual environment is recommended for the Python interpreter, I recommend using Pythons built in virtual environment. Enter the command:
    ```
    python -m venv venv
    ```  
_NOTE: The `python` part of this command and the ones in other steps below assumes  you are working with a windows operating system. Your Python command may differ, such as `python3` or `py`_

4. Activate the venv with the command:
    ```
    venv\Scripts\activate 
    ```
_Again this **command may differ depending on your operating system**, please check the [Python Documentation on virtual environments](https://docs.python.org/3/library/venv.html) for further instructions._

5. If needed, Upgrade pip locally with
    ```
    pip install --upgrade pip
    ```

6. Install all required modules with the command 
    ```
    pip -r requirements.txt
    ```

7. Set up the following environment variables within your IDE. 

    - If using VSCode, locate the `settings.json` file within the .vscode directory and add your environment variables as below. Do not forget to restart your machine to activate your environment variables or your code will not be able to see them: 

    ```json
    "terminal.integrated.env.windows": {
        "IP": "<enter ip here>",
        "PORT": "<enter port here>",
        "SECRET_KEY": "<enter secret key here>",
        "DEBUG": "<enter debug True/False here>",
        "DEVELOPMENT": "<enter development True/False here>",
        "DB_URL": "<enter db url here>",
    }
    ```

    - If using an IDE that includes a `bashrc` file, open this file and enter all the environment variables listed above using the following format: 
    ```
    HOSTNAME="<enter key here>"
    ```
    - `HOSTNAME` should be the local address for the site when running within your own IDE.
    - `DEV` environment variable is set only within the development environment, it does not exist in the deployed version, making it possible to have different settings for the two environments. For example setting DEBUG to True only when working in development and not on the deployed site.

8. If you have restarted your machine to activate your environment variables, do not forget to reactivate your virtual environment with the command used at step 4.

9. Migrate the admin panel models to create your database template with the terminal command
    ```
    python manage.py migrate
    ```

10. Create your superuser to access the django admin panel and database with the following command, and then follow the steps to add your admin username and password:
    ```
    python manage.py createsuperuser
    ```

11. You can now run the program locally with the following command: 
    ```
    python manage.py runserver
    ```

12. Once the program is running, go to the local link provided and add `/admin` to the end of the ur. Here log in with your superuser account and create instances of ShippingDestination and Product within the new database.

13. Once instances of these items exist in your database your local site will run as expected.


## Heroku Deployment

To deploy The House of Mouse webshop to heroku, take the following steps:

1. Create a `requirements.txt` file using the terminal command `pip freeze > requirements.txt`.

2. Create a `Procfile` with the terminal command `echo web: python app.py > Procfile`.

3. `git add` and `git commit` the new requirements and Procfile and then `git push` the project to GitHub.

3. Create a new app on the [Heroku website](https://dashboard.heroku.com/apps) by clicking the "New" button in your dashboard. Give it a name and set the region to whichever is applicable for your location.

4. From the heroku dashboard of your newly created application, click on "Deploy" > "Deployment method" and select GitHub.

5. Confirm the linking of the heroku app to the correct GitHub repository.

6. In the heroku dashboard for the application, click on "Settings" > "Reveal Config Vars".

7. Set the following config vars:

| Key | Value |
--- | ---
IP | `<your IP key>`
PORT | `<your port here>`
DATABASE_URL | `<your postgres database url>`
SECRET_KEY | `<your secret key>`
DEBUG | `<True>`

DEBUG is only set temporarily in case we have any errors during deployment.

8. From the command line of your local IDE:
    - Enter the heroku postres shell 
    - Migrate the database models 
    - Create your superuser account in your new database
    
     Instructions on how to do these steps can be found in the [heroku devcenter documentation](https://devcenter.heroku.com/articles/heroku-postgresql).

9. In your heroku dashboard, click "Deploy". Scroll down to "Manual Deploy", select the master branch then click "Deploy Branch".

10. Once the build is complete, click the "View app" button provided.

11. From the link provided add `/admin` to the end of the url, log in with your superuser account and create instances of ShippingDestination and Product within the new database.

12. Once instances of these items exist in your database your heroku site will run as expected.


## Credits

### Code

-   [Bootstrap 5.3.2](https://getbootstrap.com/): Bootstrap Library used throughout the project mainly to make site responsive using the Bootstrap Grid System, navbar and also for styling.
-   [Bootstrap Theme, Start Bootstrap, Business Casual](https://startbootstrap.com/theme/business-casual/): Bootstrap theme used for a lot of the styling. Colours, fonts and layout used.
-   I got the code for the form on the contact page from the [Bootstrap Documentation](https://getbootstrap.com/docs/5.3/forms/overview/#overview)
-   I got a lot of inspiration for my code from the code institute Task manager walkthrough project. This helped me with all the routed and crud functionality. [Code intitute.](https://codeinstitute.net/)


### Content

-   All content was written by the developer.


### Acknowledgements

-   My Mentor for continuous helpful feedback.

-   Tutor support at Code Institute for their support.