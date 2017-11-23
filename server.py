from flask import render_template
from app import app, db
from models import Advertisement


@app.route('/')
def ads_list():

    ads = Advertisement.query.all()
    return render_template('ads_list.html', ads=ads)

if __name__ == "__main__":
    app.run()
