# AI-Powered Product Review Rating System

## Project Description

In response to the growing popularity of online shopping, we've developed a platform that provides users with easy access to product reviews. This project focuses on automatically converting text reviews into numerical ratings using a custom-built DistilBERT model with a classification layer for multi-class classification.

## Features

- Converts text reviews into numerical ratings
- Utilizes a custom DistilBERT model for natural language processing
- Implements multi-class classification for accurate rating prediction
- The application interface runs on Django with an added application of a DBMS, SQLite.
- Check the directory `notebooks` to access training and testing notebooks. For test access `test_AI.ipynb` and training access `Midsemester_Group_15.ipynb`.

## Requirements

- Python 3.7+
- torch==2.3.1
- Transformers==4.42.4
- Django==5.0.7

## Installation

1. Clone this repository:
2. Navigate to the project directory:
3. Set Up python virtual environment: pip -
4. Install the required dependencies: pip install -r requirements.txt

## Hosting the Application: Locally
1. Clone the Repository
   
```bash
git clone https://github.com/baaba-midnight/ReviewsToRating.git
```
```bash
cd ReviewsToRating.git
```
   
2. Create a Virtual Environment
   
```bash
python -m venv env
```
```bash
env\Scripts\activate (cmd)
```

3. Install Dependencies
   
```bash
pip install -r requirements.txt
```

4. Start the Development Server
   
```bash
python manage.py runserver
```

5. Access the Appliction: Open your web browser and go to `https://localhost:8000`.

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

https://youtu.be/FBXTA4LexNA

## Contact

Baaba O. Amosah - baaba.amosah@gmail.com/baaba.amosah@ashesi.edu.gh

Kevin K. Cudjoe - kevin13cudjoe@gmail.com/kevin.cudjoe@ashesi.edu.gh

Project Link: https://github.com/baaba-midnight/ReviewsToRating
