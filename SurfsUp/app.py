# Import the dependencies.

import sqlalchemy
from flask import Flask, jsonify
import datetime as dt
import numpy as np
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect,text,desc




#################################################
# Database Setup
#################################################
# create engine to hawaii.sqlite
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# View all of the classes that automap found
Base.classes.keys()

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################

app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")

def main():
    return(
        f"Welcome to the Climate App Home Page!<br>"
        f"Available Routes:<br>"
        f"/api/v1.0/precipitation<br>"
        f"/api/v1.0/stations<br>"
        f"/api/v1.0/tobs<br>"
        f"/api/v1.0/<start><br>"
        f"/api/v1.0/<start>/<end><br>"
    )

@app.route('/api/v1.0/precipitation')

def prcp():

    last_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    percip_scores = session.query(Measurement.date, Measurement.prcp). \
    filter(Measurement.date >= '2016-08-23') .\
    all()
    scores_dict= dict(percip_scores)
    session.close()
    return jsonify(scores_dict)

@app.route("/api/v1.0/stations")
def stations():
    stations=


session.close()
return jsonify()



@app.route("/api/v1.0/<start>")
def start(start):
        

session.close()

return jsonify(tobsall)


@app.route('/api/v1.0/<start>/<end>')
def start_end()
    
    session.close()

    


