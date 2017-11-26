import argparse
import json


from app import db
from models import Advertisement


def get_ads_from_json(filepath):

    with open(filepath) as file_handler:
        return json.load(file_handler)


def load_ads(ads):

    db.session.add_all([

        Advertisement(**ad)
        for ad in ads

    ])


def deactivate_ads():

    Advertisement.query.filter_by(
        active=True
    ).update(
        dict(active=False)
    )


if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument('--newbase', action='store_true')
    parser.add_argument('--loaddata')

    args = parser.parse_args()


    if args.newbase:

        db.drop_all()
        db.create_all()

    if args.loaddata:

        try:

            deactivate_ads()

            load_ads(
                get_ads_from_json(args.loaddata)
            )

            db.session.commit()

        except:
            db.session.rollback()
