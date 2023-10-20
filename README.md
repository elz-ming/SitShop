## How to run our project?

1. Open command prompt.

2. cd into the our source code root directory

```
cd P11_team68_sourceCode
```

3. Create a virtual environment, assuming sitEnv is the name of the virtual environment in this case

```
python -m venv sitEnv
```

4. Download the dependencies

```
pip install -r requirements.txt
```

## To view our GUI : 
5. Run the project

```
python manage.py runserver
```

At this point, the app runs at `http://127.0.0.1:8000/`. 

## To view our Data : 
5. cd into the our data directory

```
cd sitData
```

6. run jupyter notebook
```
python -m notebook
```


## Codebase structure

The project is coded using a simple and intuitive structure presented below:

```bash
P11_team68_sourceCode
   |
   |-- sitApp/                            
   |    |-- admin.py 
   |    |-- apps.py
   |    |-- models.py      # App data definitions
   |    |-- popdata.py     # Ingesting .csv into database
   |    |-- tests.py
   |    |-- urls.py        # App routing definitions
   |    |-- views.py       # App function definitions
   |
   |-- sitData/
   |    |-- analysis/      # Jupyter notebooks for analysis
   |    |-- asset/         # .csv files from scraping and analysis
   |    |-- scraper/       # scraper file and chromedriver
   |
   |-- sitProject/                            
   |    |-- asgi.py 
   |    |-- settngs.py    # Project configurations
   |    |-- urls.py       # Project routing definitions
   |    |-- wsgi.py
   |
   |-- templates/
   |    |-- components/   # To be included in all / some pages
   |    |-- pages/        # Individual pages to be rendered
   |
   |-- static/   
   |    |-- css/          # CSS  Files 
   |    |-- img/          # IMG  Files 
   |    |-- js/           # JS   Files 
   |    |-- scss/         # SCSS Files 
   |    
   |
   |-- requirements.txt   # Project Dependencies
   |
   |-- manage.py          # Run the project locally
   |-- requirements.txt   # States the dependencies
   |-- vercel.json        # Build the project online
   |
   |-- ************************************************************************
```
