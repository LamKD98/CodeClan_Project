from flask import Blueprint, render_template, request, redirect, url_for
from repositories import team_repository
from repositories import league_repository
from models.team import Team

team_blueprint = Blueprint('teams', __name__)

# INDEX
# GET /books
@team_blueprint.route('/teams')
def books():
    all_teams = team_repository.select_all()
    return render_template('teams/index.html', all_teams = all_teams)

# NEW
# GET /books/new
@team_blueprint.route('/teams/new')
def new_book():
    league = league_repository.select_all()
    return render_template('books/new.html', all_leagues = league)

#CREATE
@team_blueprint.route('/teams', methods=['POST'])
def create():
    team_name = request.form['team_name']
    league_id = request.form['league_id']
    region = request.form['region']

    league = league_repository.select(league_id)
    team = Team(team_name, league, 0, 0, region)
    team_repository.save(team)
    return redirect(url_for('teams.index'))

# SHOW
# GET /books/<id>
@book_blueprint.route('/books/<id>')
def show_book(id):
    book = book_repository.select(id)
    return render_template('/books/show.html', book=book)

# EDIT
# GET /books/<id>/edit
@book_blueprint.route('/books/<id>/edit')
def edit_book(id):
    book = book_repository.select(id)
    author = author_repository.select_all()
    return render_template('books/edit.html', book=book, all_authors=author)

# UPDATE
# POST /books/<id>
@book_blueprint.route('/books/<id>', methods=['POST'])
def update_book(id):
    title = request.form['title']
    author_id = request.form['author_id']

    author = author_repository.select(author_id)
    book = Book(title, author, id)
    book_repository.update(book)

    return redirect('/books')   

# DELETE
# DELETE /tasks/<id>/delete
@book_blueprint.route('/books/<id>/delete', methods=['POST'])
def delete_book(id):
    book_repository.delete(id)
    return redirect('/books') 