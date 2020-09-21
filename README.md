# CRUD App with Django / Python

## Task:
Create a basic REST API enabling CRUD operations with respect to basic information about the host system.

## Requirements:
* Either a Rails or Django application

* Use the native auth system (i.e. the basic one that comes with Rails or Django) to secure all routes.

* Has a SQLite DB with a table named `requests` that has the following columns:

  * id (viz. autoincrementing int)

  * type of request (e.g. GET, POST, PUT, DELETE) 

  * time of request (datetime)

  * comment (text, NULL by default)

* Has the following routes:

  * /: index page, which upon a GET request…

  * …creates a new entry in the `requests` table logging the request.

* …and displays:

  * A table listing the last 10 times the page was loaded.

  * Results of running the shell commands `date` and `cat /proc/cpuinfo`.

## /api/:id

* GET: displays the info for the request with ID=:id, returning a 404 if the entry is not found.

* POST: sets the `comment` for the request with ID=:id with the submitted payload, returning a 200 if successful, else a 400.

* PUT: return a 405.

* DELETE: removes the entry with ID=:id, returning a 200 if successful and a 400 if not.

---
### To run the app:
```
python3 manage.py runserver
```

### Database
* SQLite DB
* Upon making changes in 'models.py', be sure to run 
```
python3 manage.py makemigrations requests
```
* Verify migration worked by running:
```
python3 manage.py sqlmigrate polls 0001
```
* Now migrate the model tables into the database:
```
python3 manage.py migrate
```

### External Libraries
* [py-cpuinfo](https://github.com/workhorsy/py-cpuinfo) - Utilizes one of the following approaches for retrieving CPU info depending on user's OS:

  1. Windows Registry (Windows)
  2. /proc/cpuinfo (Linux)
  3. sysctl (OS X)
  4. dmesg (Unix/Linux)
  5. /var/run/dmesg.boot (BSD/Unix)
  6. isainfo and kstat (Solaris)
  7. cpufreq-info (BeagleBone)
  8. lscpu (Unix/Linux)
  9. sysinfo (Haiku)
  10. device-tree ibm features flags (Linux PPC)
  11. Querying the CPUID register (Intel X86 CPUs)
