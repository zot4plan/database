# **Zot4Plan - PostgreSQL database**

By: [`Loc Khong`](https://www.linkedin.com/in/lockhong/) and [`Tram La`](https://www.linkedin.com/in/tram-la-680417200/)

## **Description**

* Scrape courses and programs, and export data into JSON files.
* Build prerequisite/corequisite trees
* Convert JSON files into SQL files

## **Run App**
Open terminal and run the main.py file. 

```sh
cd web_scraper/app
python3 main.py
```

## **Set up database**

* Install PostgreSQL
* Create a user with password, and grant it all privileges.
    * user: mytestuser
    * password: My6$Password
* Create a database 
    * database: zot4plandb
* Import files in the following order:
    * create_tables.sql
    * courses.sql
    * programs.sql
    * general_education.sql
    * courses_in_ge.sql
    * full_text_search.sql