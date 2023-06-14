# Lantern

Django backend for Lantern.

[![pipeline status](https://gitlab.com/NETLINK360/cirrus/lantern/badges/main/pipeline.svg)](https://gitlab.com/NETLINK360/cirrus/lantern/-/commits/main)
[![Quality Gate Status](https://coeus.n-dns.net/sonar/api/project_badges/measure?project=NETLINK360_cirrus_lantern_AYcblc_2aIIW2sdvYWSx&metric=alert_status&token=ebbf164293ac91c03c5c0ec8fd4dfb1a07d26917)](https://coeus.n-dns.net/sonar/dashboard?id=NETLINK360_cirrus_lantern_AYcblc_2aIIW2sdvYWSx)

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)

[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

## Development Status

[![Maintainability Rating](https://coeus.n-dns.net/sonar/api/project_badges/measure?project=NETLINK360_cirrus_lantern_AYcblc_2aIIW2sdvYWSx&metric=sqale_rating&token=ebbf164293ac91c03c5c0ec8fd4dfb1a07d26917)](https://coeus.n-dns.net/sonar/dashboard?id=NETLINK360_cirrus_lantern_AYcblc_2aIIW2sdvYWSx)
[![Technical Debt](https://coeus.n-dns.net/sonar/api/project_badges/measure?project=NETLINK360_cirrus_lantern_AYcblc_2aIIW2sdvYWSx&metric=sqale_index&token=ebbf164293ac91c03c5c0ec8fd4dfb1a07d26917)](https://coeus.n-dns.net/sonar/dashboard?id=NETLINK360_cirrus_lantern_AYcblc_2aIIW2sdvYWSx)
[![Code Smells](https://coeus.n-dns.net/sonar/api/project_badges/measure?project=NETLINK360_cirrus_lantern_AYcblc_2aIIW2sdvYWSx&metric=code_smells&token=ebbf164293ac91c03c5c0ec8fd4dfb1a07d26917)](https://coeus.n-dns.net/sonar/dashboard?id=NETLINK360_cirrus_lantern_AYcblc_2aIIW2sdvYWSx)

## Security Status

[![Security Rating](https://coeus.n-dns.net/sonar/api/project_badges/measure?project=NETLINK360_cirrus_lantern_AYcblc_2aIIW2sdvYWSx&metric=security_rating&token=ebbf164293ac91c03c5c0ec8fd4dfb1a07d26917)](https://coeus.n-dns.net/sonar/dashboard?id=NETLINK360_cirrus_lantern_AYcblc_2aIIW2sdvYWSx)
[![Vulnerabilities](https://coeus.n-dns.net/sonar/api/project_badges/measure?project=NETLINK360_cirrus_lantern_AYcblc_2aIIW2sdvYWSx&metric=vulnerabilities&token=ebbf164293ac91c03c5c0ec8fd4dfb1a07d26917)](https://coeus.n-dns.net/sonar/dashboard?id=NETLINK360_cirrus_lantern_AYcblc_2aIIW2sdvYWSx)

## To Do

- Set up database
- Define database settings in Django project

## Settings

Moved to [settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).

## Basic Commands

### Setting Up Your Users

- To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

- To create a **superuser account**, use this command:

      $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

### Type checks

Running type checks with mypy:

    $ mypy lantern

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

#### Running tests with pytest

    $ pytest

### Live reloading and Sass CSS compilation

Moved to [Live reloading and SASS compilation](https://cookiecutter-django.readthedocs.io/en/latest/developing-locally.html#sass-compilation-live-reloading).

### Celery

This app comes with Celery.

To run a celery worker:

```bash
cd lantern
celery -A config.celery_app worker -l info
```

Please note: For Celery's import magic to work, it is important _where_ the celery commands are run. If you are in the same folder with _manage.py_, you should be right.

To run [periodic tasks](https://docs.celeryq.dev/en/stable/userguide/periodic-tasks.html), you'll need to start the celery beat scheduler service. You can start it as a standalone process:

```bash
cd lantern
celery -A config.celery_app beat
```

or you can embed the beat service inside a worker with the `-B` option (not recommended for production use):

```bash
cd lantern
celery -A config.celery_app worker -B -l info
```

### Email Server

In development, it is often nice to be able to see emails that are being sent from your application. For that reason local SMTP server [MailHog](https://github.com/mailhog/MailHog) with a web interface is available as docker container.

Container mailhog will start automatically when you will run all docker containers.
Please check [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html) for more details how to start all containers.

With MailHog running, to view messages that are sent by your application, open your browser and go to `http://127.0.0.1:8025`

### Sentry

Sentry is an error logging aggregator service. You can sign up for a free account at <https://sentry.io/signup/?code=cookiecutter> or download and host it yourself.
The system is set up with reasonable defaults, including 404 logging and integration with the WSGI application.

You must set the DSN url in production.

## Deployment

The following details how to deploy this application.

### Docker

See detailed [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html).

### Custom Bootstrap Compilation

The generated CSS is set up with automatic Bootstrap recompilation with variables of your choice.
Bootstrap v5 is installed using npm and customised by tweaking your variables in `static/sass/custom_bootstrap_vars`.

You can find a list of available variables [in the bootstrap source](https://github.com/twbs/bootstrap/blob/v5.1.3/scss/_variables.scss), or get explanations on them in the [Bootstrap docs](https://getbootstrap.com/docs/5.1/customize/sass/).

Bootstrap's javascript as well as its dependencies are concatenated into a single file: `static/js/vendors.js`.
