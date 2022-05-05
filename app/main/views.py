from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_news,get_source


@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular movie
    popular_news = get_news('bitcoin')

    title = 'Home - Welcome to The best News Review Website Online'

    return render_template('index.html', title = title, news = popular_news)


# Views
@main.route('/source')
def source():

    '''
    View news page function that returns the new details page and its data
    '''
    new = get_source()

    return render_template('source.html',source = new)

# @main.route('/search/<new_name>')
# def search(new_name):
#     '''
#     View function to display the search results
#     '''
#     new_name_list = new_name.split(" ")
#     new_name_format = "+".join(new_name_list)
#     searched_news = search_movie(new_name_format)
#     title = f'search results for {new_name}'
#     return render_template('search.html',movies = searched_movies)

# @main.route('/new/review/new/<int:id>', methods = ['GET','POST'])
# def new_review(id):
#     form = ReviewForm()
#     new = get_new(id)

#     if form.validate_on_submit():
#         title = form.title.data
#         review = form.review.data
#         new_review = Review(new.id,title,new.poster,review)
#         new_review.save_review()
#         return redirect(url_for('new',id = new.id ))

#     title = f'{new.title} review'
#     return render_template('new_review.html',title = title, review_form=form, new=new)