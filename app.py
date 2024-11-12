# pylint: skip-file

from flask import Flask
import nltk

app = Flask(__name__)

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

import views
