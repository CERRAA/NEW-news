import urllib.request,json
from .models import News,Source


# Getting api key
# Getting the movie base url
base_url = None
NEWS_API_BASE_URL ='https://newsapi.org/v2/everything?q={}&apiKey=da6eaf7a0f56440ea2c0cff6cad32b2d'

def configure_request(app):
    global base_url
    base_url = app.config['NEWS_API_BASE_URL']



def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = NEWS_API_BASE_URL.format(category)

    with urllib.request.urlopen(get_news_url) as url:
        get_new_data = url.read()
        get_news_response = json.loads(get_new_data)

        news_results = None

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_results(news_results_list)


    return news_results

def process_results(news_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain new details

    Returns :
        new_results: A list of new objects
    '''
    news_results = []
    for news_item in news_list:
        content = news_item.get('content')
        img = news_item.get('urlToImage')
        url = news_item.get('url')
        published = news_item.get('publishedAt')

        news_object = News(content,img,url,published)
        news_results.append(news_object)

    return news_results

def get_source():
    '''
    Function that gets the json response to our url request
    '''
    SOURCE_API_BASE_URL = 'https://newsapi.org/v2/top-headlines/sources?apiKey=da6eaf7a0f56440ea2c0cff6cad32b2d'

    with urllib.request.urlopen(SOURCE_API_BASE_URL) as url:
        get_new_data = url.read()
        get_news_response = json.loads(get_new_data)

        news_results = None

        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results = process_source(news_results_list)


    return news_results

def process_source(source_list):
  
    news_results = []
    for source_item in source_list:
        name = source_item.get('name')
        url = source_item.get('url')
    
        news_object = Source(name,url)
        news_results.append(news_object)

    return news_results


