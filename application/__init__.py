from flask import Flask
import os
import pymongo
from dotenv import load_dotenv
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas


app=Flask(__name__)

load_dotenv()

password=os.getenv("PASSWORD")
connectionString="mongodb+srv://sonisir1920:"+password+"@cluster0.dkvhvap.mongodb.net/"
# connectionString="mongodb://localhost:27017"
app.config["SECRET_KEY"] = os.environ["SECRET_KEY"]



client=pymongo.MongoClient(connectionString)
db=client["FlaskDashboard"]

from application import routes


