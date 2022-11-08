# my-grapevine
![Logo](./website/static/images/grapevine_photo.png)
---
## Description

- Our project looked at creating a website which compiled events from a variety of cultural event websites. We decided to allow the user to book tickets externally through links to each external website, but have the search option within our own page. This allows the user the find relevant activities in one page only, rather than visiting a number of websites separately. 
- Users must have set up an account first, to be able to see the search results. This means that they have exclusive access to add their own notes and comments about the upcoming and past events. 
This will use data extracted from Ticketmaster API and web scraping art and gallery data from another website called Art fund. 
- Grapevine is different to other events websites as we include a profile section where users can make notes on their excitement for the events as well as make some comments after the events. This can be used to keep track of their interests. 

**Problems to solve:**
  - How to retrieve information from Eventbrite when their API search functionality was removed?
  - How to integrate the different API and other website data that has been web scraped?
  - Can we give the users a private space to comment on the events, so that the user experience is enhanced?
  - What is the essential information that can be provided from all websites to ensure we can use OOP throughout, as it is already used in the database?
---

## Table of Contents 

- [Installation](#installation)
- [Usage](#usage)
- [Credits](#credits)
- [License](#license)
- [Features](#features)
- [Tests](#tests)
---
## Installation

The Python packages to install before running the app are listed in the requirements.txt
You will need to update the information contained within **.env** file with your own credentials: database, API Keys

Once you have followed these steps, navigate to **main.py** and run the command `**app.run()**`. Click the link that appears in the terminal.

This will display the home page for the web app.

The webapp has a modular construction, achieved from using *blueprints*.

Latest Blueprint documentation is at: https://flask.palletsprojects.com/en/2.2.x/blueprints


- **Database Configuration**

According to the official documentation,
> SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.
This toolkit is designed to operate with a DBAPI implementation built for a particular database, and includes support for the most popular databases.

Our choice for this project is MySQL.

Python will create an empty database named **website** and all tables and the relationship are defined within the **create_db.py** file using SQLAlchemy models. There is also a **FlaskForm** for adding notes.

Latest SQLAlchemy documentation is at:  https://www.sqlalchemy.org/docs/

---

## Usage

###Navigation

**Welcome page**

Select the *Sign Up* hyperlink which will redirect you to the sign-up page.

**Sign Up Page**

Enter your credentials here to register - first name, email and password. Once you have successfully registered your account, a welcome message will be displayed with your first name on it, and you will be redirected to the home page.

**Admin Page**

At the moment, the first user to sign up has the Admin role and access to the Admin page. This role and its page will be further developed.

**Home Page**

From here,  there are a couple of options for you:
- click on *Events* to see the full list of events advertised on our website
- click on *Search* to retrieve the events based on your keyword
- click on *Add Note* to add your feedback or notes about the events/ places you have visited. The note is saved in the database.
- click on *Notes* to read other users notes. If there are no notes to display, you are invited to add yours first.
- click on *Logout* returns you to the home page


**Events/ Search Pages**

 All details are retrieved via live APIs requests.

Under each event, you will see a *More info* button and a mapp showing the location of the event. *More info* will open a new page which will display additional information about that particular event, and you will have the option to *Buy Ticket*  by pressing a button which will redirect you to the partner's website.

---

## Credits

- [Divya](https://github.com/orgs/my-grapevine/people/divyasinghchouhan) for APIs, Back-end and testing
- [Mutiyat](https://github.com/orgs/my-grapevine/people/mutiyat) for Front-end and testing
- [Neneh](https://github.com/orgs/my-grapevine/people/NenehPatel) for APIs and testing
- [Mihaela](https://github.com/orgs/my-grapevine/people/Mi-Str) for Back-end, database and testing
---
## License

Licensed under the MIT license

---
## Features

 - modular construction
 - live APIs requests
 - OOP paradigm
 - SQLAlchemy models and Flask form
 - enhanced password protection by using hashed salted algorithm
 - HTML, CSS, Bootstrap
---
## Tests 

Navigate to the **tests folder** file and run the **`unittest.main()`** command at the bottom of each file.

Part of the aims of the tests are to ensure that the tests are accurate to the current date, however it is possible that when the tests are reviewed, the live data will be different to what we have tested, and they will not work. To retrieve new test data, you can achieve this by using the following method - 
Run the selected function in event.py in the website>api folder which corresponds to the relevant test that you would like to run. Enter the selected data (location, id, slug, etc) into the test. For example, you may need to retrieve an event from the function by searching for an event query. Enter the relevant information into the test and press the green arrow to run it.
Due to the use of unofficial APIS, the shape of the data that we receive can change at any time and therefore it is essential that we test with live data.