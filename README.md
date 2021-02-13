# Prolexic-Checker

Python Script to check if the IP addresses are routed over the Prolexic DDOS mitigator or not. 

## To Setup as a scheduled task that runs every week on a CentOS server.

- The Prolexic Checker Program would require python3 to be installed if not available. This can be done by running the following command:

```console
root@user:~$ sudo yum install python3
```

-After installation copy or clone all the files found in the repository here [here](https://gitlab.com/vasu3797/prolexic-checker) or by using the command:

```console
root@user:~$ git clone https://gitlab.com/vasu3797/prolexic-checker.git
```

-Clone this file to your desired directory.

## Running the script as standalone

- Enter the command:

```console
root@user:~$ python3 /path/to/prolexic_checker.py
```

## Setting up the CRON job

- Enter this command:

```console
root@user:~$ crontab -e 
```

- append the file with this command to run this task every week on Monday at 8 am:

```console 
0 8 * * 1 /bin/python3 /path/to/prolexic_checker.py 
```