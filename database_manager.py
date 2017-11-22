from app import db
from models import Advertisement


db.drop_all()
db.create_all()


args = list()
args.append(dict(description='test 1'))
args.append(dict(description='test 2'))


db.session.add_all(
    [
        Advertisement(**arg)
        for arg in args
    ]
)

db.session.commit()


Advertisement.query.filter_by(

    active=True

).update(

    dict(active=False)

)


db.session.commit()