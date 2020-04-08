# Python Test Task


You must develop a small REST API service that facilitates redirection to third-party resources. The purpose of this service is to collect information that may be needed for statistical analysis and to perform redirection.

The service does not provide any user authorization or actions related to it.

The estimated time to complete the task is from 3 to 4 hours.

## Start Project

### Prerequisites

Make sure to have the following on your host:

- Python >= 3.7
- PostgreSQL >=10
- Redis >= 5
- git

### Setting Up Development Environment

Clone this repo:

```bash
$ git clone <repo url>
```

Create a virtualenv:

```bash
$ python3 -m venv <virtual env path>
```

Activate the virtualenv you have just created:

```bash
$ source <virtual env path>/bin/activate
```

Install requirements:

```bash
$ pip install -r requirements.txt
```

Create a new PostgreSQL database using `createdb`:

```bash
$ createdb python_test_task -h localhost -U postgres
```

Create a file with environment variables:

```bash
$ cp env.example .env
```

Apply migrations:

```bash
$ python manage.py migrate
```

Run celery worker:

```bash
$ celery -A config worker -l info
```

Run development server:

```bash
$ python manage.py runserver
```

## Requirements

### General Requirements

- Use the latest stable version of Django and Django REST Framework.
- Follow the rules of `PEP 8` and `Django Coding Style`.
- Update the `requirements.txt` file every time after adding a dependency. You can also update any other version of this file if you think that the new version would be better than the used one.
- Use English as the main language for all string constants and comments.
- When developing, try to avoid duplicating queries to the database. Make sure to optimize the code (with Django Debug Toolbar or any other tool, this choice is up to you).
- Use Django migrations for all changes in fields and models.
- Use class-based views or viewsets for all views on the API. If you think that using a function-based view in a particular case would be better, please use it, but add the reasons  why in the comments.
- Use `pytest` as the main testing framework.

### Basic Project Requirements

- Create an endpoint that will collect all necessary data about the performed redirect, the referrer, and the requester. After data saving, the redirect must be done. Keep in mind that the redirect must be done as fast as possible.

  Below, there’s an example of what an endpoint might look like:

  `GET /analyzer/redirect?to=https://example.com/jobs/`
  
  This is just an example. You can use this example and make it more convenient for you and more optimal in terms of project development.

   List of data that must be retrieved from the request and stored:
    - Domain name, full url and get parameters of the redirect
    - Domain name and full url of the referrer
    - IP address, browser, OS, and the platform of the requester

- Create endpoints to get statistic information:

    - List of all performed redirects paginated by 20 items. Implement search by redirect and referrer domain name. Add sorting by creation date (the newest by default).
    - List of all performed redirects for certain redirect domain name and for certain referrer domain name with pagination and sorting by creation date (the newest by default).
    - List of performed redirects grouped by full urls without get parameters. Each returned redirect must be annotated by the number of unique records of redirects with full url, must contain a list of referrers of the redirect, and the date and time of the latest redirect.

        For example, you have 2 records in the database:

        ```txt
        id: 1
        redirect_full_url: https://example.com/jobs/
        referrer_domain_name: site1.com
        created_at: 22-01-2020 18:00:00

        id: 2
        redirect_full_url: https://example.com/jobs/
        referrer_domain_name: site2.com
        created_at: 22-01-2020 18:02:00
        ```

        Result must contain item like this one:

        ```json
        "redirect_full_url": "https://example.com/jobs/",
        "redirects": 2,
        "referrers": ["site1.com", "site2.com"],
        "last_redirected": "22-01-2020 18:02:00"
        ```

    - List of top 10 domains for which redirects were made this month.

- The business logic of the project should be covered by tests.
- All models should be accessible via Admin site.

### Advanced Project Requirements

- Add the API documentation based on the OpenAPI schema.
- Implement a management command that generates the CSV file with all collected redirects.

## How to submit results

Once you complete the test task, create a merge request to this repository and send a link to the HR you’ve been communicating with so far.
