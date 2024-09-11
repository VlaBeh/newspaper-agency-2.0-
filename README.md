# **Newspaper Agency Tracking System**

## This is a Django-based application for tracking newspapers and the redactors responsible for their publication.

## The system allows management of newspapers, topics, and redactors, ensuring that you always know who was responsible for each publication.

**Features**
Manage Newspapers with titles, content, published dates, and topics.
Assign multiple redactors to each newspaper.
Track topics like Politics, Business, Crime, Art, and more.
Optionally assign more than one topic to each newspaper (feature to be implemented).
DB Structure
Redactor: Abstract User model with fields like years of experience, username, email, password, first name, and last name.
Topic: Represents the subject of the newspaper (e.g., Politics, Crime).
Newspaper: Contains title, content, published date, topic(s), and a list of publishers (redactors).

**Requirements**
Before running the project, ensure you have installed the following:
Python 3.x
Django 4.x
PostgreSQL (or another database, but PostgreSQL is recommended)

## Check it out!
[Newspaper Agency project deployed to Render](https://newspaper-agency-ktwk.onrender.com)

### You can also login!

login: paul_joh
password: X9NCJMan

### **Setup Instructions**

#### Step 1: Clone the Repository

First, clone this repository to your local machine:
git clone https://github.com/VlaBeh/newspaper-agency-2.0-.git
cd newspaper-agency

#### Step 2: Set Up a Virtual Environment

Create a virtual environment to install the required dependencies:
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

#### Step 3: Install Dependencies

Install the necessary Python packages listed in requirements.txt:
pip install -r requirements.txt

#### Step 4: Set Up the Database

Ensure you have PostgreSQL installed and running on your machine. Then, create a new database for the project:
CREATE DATABASE newspaper_agency;

#### Step 5: Configure Environment Variables

Create a .env file in the root of your project based on the .env.sample:
cp .env.sample .env
Update the .env file with your database credentials, secret key, and other settings:
SECRET_KEY=your-secret-key
DEBUG=True  # Set False in production
DATABASE_URL=postgres://username:password@localhost:5432/newspaper_agency

#### Step 6: Run Migrations

To set up the database schema, run the following Django commands:
python manage.py migrate

#### Step 7: Create a Superuser

Create an admin (superuser) to manage the application:
python manage.py createsuperuser
Follow the prompts to set the username, email, and password.

#### Step 8: Run the Development Server

Start the Django development server:
python manage.py runserver

#### Step 9: Access the Admin Panel

Open your web browser and go to:
http://127.0.0.1:8000/admin
Log in with the superuser credentials you created in step 7. From here, you can start managing redactors, topics, and newspapers.

**Optional Features to Implement**
Assign multiple topics to each newspaper: Modify the relationship between Newspaper and Topic from a ForeignKey to a ManyToManyField if needed:
topics = models.ManyToManyField(Topic)
Improve search and filtering: Add search functionality in the admin panel to filter newspapers by topics, redactors, or publication date.

#### Testing

To run the unit tests:
python manage.py test
