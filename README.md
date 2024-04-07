# URL scanning Webservice

A Web service API to scan a given URL and return various artifacts
from it.



## Installation

1. Clone the repository: `https://github.com/kishorsDevelop/URL_Scanner_Webservice.git`
2. Install dependencies: 
```md
pip install django
pip install playwright
pip install bs4
```            
## Usage
1. Move to first parent url_scanner_project
and run the below commands in the terminal:
    ```md
    cd url_scanner_project/
    python manage.py runserver
    ```    
2. Now open the second terminal and move to url_scanner_app and run the below commands:
    ```md
    cd url_scanner_app/
    python run.py
    ```         
We provide URL to the scan_url variable present in run.py to scan the specified URL. All the returned artifacts will be saved into the database.

run.py is a script that I created in order to test the code.

NOTE: Some URLs might not get scanned properly because of some security reasons of that website. I have observed this while checking some URLs.


---

