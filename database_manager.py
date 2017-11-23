import argparse
import json


from app import db
from models import Advertisement


def get_ads_from_json(filepath):

    with open(filepath) as file_handler:
        return json.load(file_handler)


def create_new_base():

    db.drop_all()
    db.create_all()


def load_ads(ads):

    db.session.add_all([

        Advertisement(**ad)
        for ad in ads

    ])

    db.session.commit()


def deactivate_ads():

    Advertisement.query.filter_by(
        active=True
    ).update(
        dict(active=False)
    )

    db.session.commit()


if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument('--newbase', action='store_true')
    parser.add_argument('--loaddata')

    args = parser.parse_args()

    if args.newbase:
        create_new_base()

    if args.loaddata:

        deactivate_ads()

        load_ads(
            get_ads_from_json(args.loaddata)
        )
