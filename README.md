# AI-Powered Product Review Rating System

## Project Description

In response to the growing popularity of online shopping, we've developed a platform that provides users with easy access to product reviews. This project focuses on automatically converting text reviews into numerical ratings using a custom-built DistilBERT model with a classification layer for multi-class classification.

## Features

- Converts text reviews into numerical ratings
- Utilizes a custom DistilBERT model for natural language processing
- Implements multi-class classification for accurate rating prediction
- The application interface runs on Django with an added application of a DBMS, SQLite.

## Requirements

- Python 3.7+
- torch==2.3.1
- Transformers==4.42.4
- Django==5.0.7

## Installation

1. Clone this repository:
2. Navigate to the project directory:
3. Install the required dependencies: pip install -r requirements.txt

## Usage

[Provide instructions on how to use your application, including any command-line arguments or configuration files needed]

## Hosting the Application

#### Deployment on PythonAnywhere

To deploy this application on PythonAnywhere, follow these steps:

1. If you haven't already, Sign up for a PythonAnywhere account at https://www.pythonanywhere.com.
2. Log in to your PythonAnywhere dashboard.
3. Open a Bash console from the dashboard.

5. Clone this repository
```
git clone https://github.com/senseicudjoe/Ratings.git
```

6. Create a virtual environment
```
python -m venv env
```

8. Activate the virtual environment: Powershell (env/Scripts/Activate.ps1)
  
10. Navigate to your project directory: cd [repo-name]
11. Install the requirements
```
pip install -r requirements.txt
```

13. Go to the "Web" tab in the PythonAnywhere dashboard and click on "Add a new web app".
14. Choose "Manual configuration" and select the Python version that matches your virtual environment.
    
16. Set the path to your virtual environment when prompted. It should be something like:
 ```
 /home/[your-pythonanywhere-username]/.virtualenvs/myenv
 ```

12. Set your working directory to:
 ```
 /home/[your-pythonanywhere-username]/[your-repo-name]
 ```

13. Modify the WSGI configuration file (there will be a link to edit it in the Web tab). 
 Replace the contents with:

 ```python
 import sys
 path = '/home/[your-pythonanywhere-username]/[your-repo-name]'
 if path not in sys.path:
     sys.path.append(path)
 
 from [your_main_app_file] import app as application
 ```

 Replace `[your_main_app_file]` with the name of your main application file (without the .py extension).

14. Go back to the Web tab and hit the Reload button for your domain.

Your application should now be live at your PythonAnywhere URL (usually `[your-username].pythonanywhere.com`).

Note: Make sure your application is set up to use environment variables for any sensitive information like secret keys or database credentials. PythonAnywhere allows you to set environment variables in the Web tab.

## Project Structure
```
.
├── README.md
├── Ratings
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── manage.py
├── media
│   └── product_images
│       ├── Chocolate.jpeg
│       ├── Chocolate_NEcknpR.jpeg
│       ├── Mac.jpeg
│       ├── Perfume.jpeg
│       ├── pen.jpeg
│       └── skate_board.jpeg
├── notebooks
│   ├── Midsemester_Group_15.ipynb
│   └── test_AI.ipynb
├── ratingsApp
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── bert_model.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_reviews.py
│   │   ├── 0003_alter_reviews_product.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── 0001_initial.cpython-312.pyc
│   │       ├── 0002_reviews.cpython-312.pyc
│   │       ├── 0003_alter_reviews_product.cpython-312.pyc
│   │       └── __init__.cpython-312.pyc
│   ├── models
│   │   ├── G15_model.pth
│   │   └── G15_tokenizer
│   │       └── G15_tokenizer
│   │           ├── special_tokens_map.json
│   │           ├── tokenizer.json
│   │           ├── tokenizer_config.json
│   │           └── vocab.txt
│   ├── models.py
│   ├── templates
│   │   ├── base.html
│   │   ├── products.html
│   │   └── reviews.html
│   ├── templatetags
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-312.pyc
│   │   │   └── custom_filters.cpython-312.pyc
│   │   └── custom_filters.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
└── requirements.txt
```

## Demo

To see a demonstration of how this application works, please watch our video tutorial:

[YouTube Link to Your Demo Video]

## License

[Specify the license under which your project is released]

## Contact

Baaba O. Amosah - baaba.amosah@gmail.com/baaba.amosah@ashesi.edu.gh

Kevin K. Cudjoe - kevin13cudjoe@gmail.com/kevin.cudjoe@ashesi.edu.gh

Project Link: https://github.com/baaba-midnight/ReviewsToRating
