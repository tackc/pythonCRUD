# CRUD App with Django / Python

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
