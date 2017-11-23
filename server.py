from flask import render_template
from app import app, db
from models import Advertisement


@app.route('/')
@app.route('/page/<int:page>')
def ads_list(page=1):

    per_page = 5

    ads = Advertisement.query.filter(Advertisement.active == True)

    ads = ads.paginate(page, per_page, False)

    return render_template('ads_list.html', ads=ads)


if __name__ == "__main__":
    app.run(debug=True)
