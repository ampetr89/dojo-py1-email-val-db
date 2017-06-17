# Email database

On the landing page, users input their email address. Upon hitting Submit, the email address is sent to the /process route, which checks that the string matches the email regular expression. If it does not, a flash message is created and the user is redirected to the form to try entering their email again. Upon successfully entering an email address, the user is routed to /success, which inserts the record into the database, and then looks up all email addresses and the timestamp at which they were created, and passes this list of tuples to the render\_template function for success.html. 

## Screenshots
### Landing Page

![Landing page](/doc/index.png?raw=true "index.html")


### Success / Email list
Note that the list gets a scrollbar if it becomes very long.

![Email list](/doc/success.png?raw=true "success.html")
