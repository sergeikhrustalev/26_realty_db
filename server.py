from datetime import date

from sqlalchemy.sql.expression import true
from sqlalchemy import or_
from flask import render_template, request, url_for
from app import app, db
from models import Advertisement


@app.route('/')
def ads_list():

    ads = Advertisement.query.filter(Advertisement.active == true())

    oblast_district = request.args.get('oblast_district')
    min_price = request.args.get('min_price', None, type=int)
    max_price = request.args.get('max_price', None, type=int)
    new_building = request.args.get('new_building')
    page = request.args.get('page', 1, type=int)

    if oblast_district:

        ads = ads.filter(
            Advertisement.oblast_district == oblast_district
        )

    if min_price:

        ads = ads.filter(
            Advertisement.price >= min_price
        )

    if max_price:

        ads = ads.filter(
            Advertisement.price <= max_price
        )

    if new_building:

        ads = ads.filter(
            or_(
                Advertisement.under_construction == true(),
                Advertisement.construction_year >= date.today().year - 2
            )
        )

    per_page = 5
    ads = ads.paginate(page, per_page, False)

    return render_template(
        'ads_list.html',
        ads=ads,
        min_price=min_price,
        max_price=max_price,
        new_building=new_building
    )


if __name__ == "__main__":
    app.run(debug=True)
