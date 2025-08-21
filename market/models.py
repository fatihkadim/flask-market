from market import db,login_manager
from market import bcrypt
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model,UserMixin):
    id = db.Column(db.Integer(),primary_key=True)
    username = db.Column(db.String(length=30),nullable=False,unique=True)
    email_address = db.Column(db.String(length=50),nullable=False,unique=True)
    password_hash= db.Column(db.String(length=60),nullable=False)
    budget = db.Column(db.Integer(),nullable=False,default=1000)
    items = db.relationship('Item',backref='owned_user',lazy=True )

    @property
    def prettier_budget(self):
        budget_str = str(self.budget)
        if len(budget_str) >= 4:
            return f'{budget_str[:-3]},{budget_str[-3:]}'
        else:
            return f"{budget_str}$"

    @property
    def password(self):
        raise AttributeError("Password is not a readable attribute.")

    @password.setter
    def password(self,plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self,attempted_password):
        return bcrypt.check_password_hash(self.password_hash,attempted_password)

    def can_purchase(self,item_obj):
        return self.budget >= item_obj.price

    def add_to_budget(self,price):
        self.budget += price
        db.session.commit()



class Item(db.Model):
    id = db.Column(db.Integer(),primary_key =True)
    name = db.Column(db.String(length=30),nullable=False,unique=True)
    barcode = db.Column(db.String(length=12),nullable=False,unique=True)
    price = db.Column(db.Integer(),nullable=False)
    description = db.Column(db.String(length=1024),nullable =False,unique=True)
    owner = db.Column(db.Integer(),db.ForeignKey('user.id'))
    def __repr__(self):
        return f'Item {self.name}'

    def assign_ownership(self, user):
        self.owner = user.id
        user.budget -= self.price
        db.session.commit()

    def unassign_ownership(self, user):
        self.owner = None
        user.add_to_budget(self.price)
        db.session.commit()
