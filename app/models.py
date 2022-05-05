class News:
    '''
    News class to define News Objects
    '''

    def __init__(self,content,img,url,published):
        self.content =content
        self.img = img
        self.url = url
        self.published = published



class Source:

    def __init__(self,name,url):
        self.name = name
        self.url = url