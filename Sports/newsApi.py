from newsapi import NewsApiClient
import dateutil.parser
import operator

def getNews(input_value):

    newsapi = NewsApiClient(api_key='fbfba5ccce3947d7987f287a603127c0')

    query = None

    #if(input_value != 'null' or input_value != 'newest' or input_value != 'oldest'):
    if(input_value != 'null' and input_value != 'newest' and input_value != 'oldest'):
        query = input_value
    

    all_articles = newsapi.get_top_headlines(q=query,
                                      language='en',
                                      category='sports',
                                      country='us',
                                      page_size = 100
                                      )

    articles = all_articles['articles']
    length = len(articles)
    desc =[]
    title =[]
    img =[]
    artURL = []
    source = []
    date = []
    for i in range(length):
        art = articles[i]
        title.append(art['title'])
        desc.append(art['description'])
        img.append(art['urlToImage'])
        artURL.append(art['url'])
        temp = art['source']
        source.append(temp['name'])
        temp = dateutil.parser.parse(art['publishedAt'])
        date.append(temp.strftime('%Y-%m-%d'))


    mylist = zip(title, desc, img, artURL, source, date)

    if(input_value == "newest"):
        sortedList = sorted(mylist, key = operator.itemgetter(5), reverse = True)
        mylist = sortedList
    if(input_value == "oldest"):
        sortedList = sorted(mylist, key = operator.itemgetter(5))
        mylist = sortedList

    context = {'mylist': mylist}
    return context