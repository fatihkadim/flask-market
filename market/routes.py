from sqlite3 import IntegrityError
from market import app ,db
from flask import render_template,redirect,url_for,flash ,request,get_flashed_messages
from market.models import Item,User
from market.forms import RegisterForm,LoginForm,PurchaseItemForm,SellForm
from flask_login import login_user,logout_user ,login_required,current_user

@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")

@app.route("/market",  methods=['GET','POST'])
@login_required
def market_page():
    purchase_form = PurchaseItemForm()
    sell_form = SellForm()
    if request.method == "POST":
        purchased_item =request.form.get('purchased_item')
        p_item_object = Item.query.filter_by(name=purchased_item).first()

        if p_item_object:
            if current_user.can_purchase(p_item_object):
                p_item_object.assign_ownership(current_user)
                flash(message=f"Congratulations. You purchased {p_item_object.name} for {p_item_object.price}$",category="success")
            else:
                flash(message="Not enough balance",category="danger")

        owned_item = request.form.get('owned_item')
        print("OWNED ITEM:", owned_item)
        o_item_object = Item.query.filter_by(name=owned_item).first()
        if o_item_object:
            if o_item_object in current_user.items:
                o_item_object.unassign_ownership(current_user)
                flash(message=f"You successfully sold {o_item_object.name} and received {o_item_object.price}$!", category="success")
            else:
                flash(message="You cannot sell an item you don't own!", category="danger")
        return  redirect(url_for('market_page'))

    if request.method == "GET":
        items = Item.query.filter_by(owner = None)
        owned_items = Item.query.filter_by(owner=current_user.id)
        return render_template("market.html",items=items,purchase_form=purchase_form,owned_items=owned_items,sell_form=sell_form)

@app.route("/register",methods=['GET','POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email_address = form.email_address.data,
                              password=form.password1.data)
        db.session.add(user_to_create)

        try:
            db.session.commit()
            login_user(user_to_create)
            flash(message=f"User successfully created! You are now logged in as {user_to_create.username}.",category="success")
            return redirect(url_for('market_page'))
        except IntegrityError:
            db.session.rollback()
            flash(message="This email is already registered. Please try another email.", category="danger")

        return redirect(url_for('market_page'))

    if form.errors != {}: # if there are errors from the validations
        for err_msg in form.errors.values():
            flash(message=f'There was an error with creating a user: {err_msg}',category="danger")

    return render_template("register.html",form=form)

@app.route("/login",methods=['GET','POST'])
def login_page():
    form = LoginForm()

    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username = form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(
                attempted_password=form.password.data
        ):
            login_user(attempted_user)
            flash(message=f"Successfully logged in as {attempted_user.username}",category='success')
            return redirect(url_for('market_page'))

        else:
            flash(message="Username and password dont match. Please try again.",category='danger')
    return render_template("login.html",form = form)

@app.route("/logout")
def logout_page():
    logout_user()
    flash(message='You have been logged out.',category='info')
    return redirect(url_for('home_page'))
