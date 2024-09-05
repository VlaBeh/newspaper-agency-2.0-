# newspaper-agency-2.0-
# Newspaper Agency Management System

This project is designed to manage and track newspapers published by a team of redactors in a newspaper agency. The system allows you to assign redactors to different newspapers and topics, ensuring you always know who the publishers of each newspaper are.

## Features

- **Redactor Management**: Track and manage redactors within the agency, including their experience level, contact details, and assigned newspapers.
- **Newspaper Tracking**: Keep records of all newspapers, including their title, content, publication date, and associated topics.
- **Topic Assignment**: Assign one or more topics to each newspaper to categorize and organize content effectively.

## Database Structure

The database consists of the following tables:

1. **Topic**: 
   - `name`: The name of the topic (e.g., Politics, Crime, Business).
   
2. **Newspaper**:
   - `title`: The title of the newspaper.
   - `content`: The content of the newspaper.
   - `published_date`: The publication date of the newspaper.
   - `topics`: A many-to-many relationship with the `Topic` model, allowing each newspaper to be associated with multiple topics.
   - `publishers`: A many-to-many relationship with the `Redactor` model, tracking which redactors have contributed to the newspaper.

3. **Redactor**:
   - `username`: The username of the redactor.
   - `email`: The redactor's email address.
   - `first_name`: The first name of the redactor.
   - `last_name`: The last name of the redactor.
   - `years_of_experience`: The number of years the redactor has been in the industry.
   - `password`: The password for the redactor's account.

## Installation and Setup

### Prerequisites

- Python 3.x
- Django 3.x or later
- SQLite (default Django database)

### Steps to Set Up the Project

1. **Clone the repository**:
   ```bash
   git clone https://github.com/VlaBeh/newspaper-agency-2.0-
   cd newspaper-agency
