# College-Notices-Fetcher
To get daily updates about any new notice uploaded on the IMS notice board, a python script is created that scrapes notices from IMS notice board and is deployed on an AWS backend. The script is made to run daily with the help of cron job(scheduled task).

## Requirements
    -An AWS account and a SendGrid API.
    -Install putty for SSH and Filezilla for FTP to your server instance.

I
## Install the modules
    pip install pandas numpy sendgrid bs4 lxml xlrd --user

pandas and numpy are modules to handle data, sendgrid is the emailing API, bs4 is to parse HTML, lxml is a HTML parser, xlrd is                    used to handle excel files ( The attenders list is an excel file.) "--user" grants the privilege to make permanent changes to your server
