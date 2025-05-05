# Flightmate

Flightmate is a ride-sharing web application designed for students to coordinate shared Uber rides to and from airports. This project uses Flask for the web framework and SQLAlchemy for database integration to store and manage user requests.

*Key Features*
Database Integration: User ride requests are stored using SQLAlchemy.

*Matching Algorithm:*

A primary matching tolerance window of 30 minutes is set to find ride partners.

The algorithm starts after the first 10 requests have been submitted.

A secondary 60-minute tolerance window is used to notify users via email about potential matches.

Email Notifications: Implemented via smtplib, allowing users to receive emails when potential matches are found.

Web Interface: Running flask_app.py launches a local web server for user interaction.

*Future Plans*
Deploy the application to a cloud platform to allow public access.
Improve the matching algorithm and introduce user authentication.