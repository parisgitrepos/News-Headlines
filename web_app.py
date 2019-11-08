from flask import Flask, render_template
from news_headlines import News_Headlines

app = Flask(__name__, template_folder='html_templates')

@app.route('/')
def index():
    news = News_Headlines()
    tech = news.tech_news()
    business = news.business_news()
    political = news.political_news()
    US_CA = news.US_CA_news()
    ME = news.ME_news()
    EU = news.EU_news()
    UK = news.UK_news()
    Asia = news.Asia_news()
    India = news.India_news()
    world = news.world_news()
    return render_template('home.html', political = political[0], political_link = political[1], tech = tech[0], tech_link = tech[1],
                    business = business[0], business_link = business[1], US_CA = US_CA[0], US_CA_link = US_CA[1], ME = ME[0],
                    ME_link = ME[1], EU = EU[0], EU_link = EU[1], UK = UK[0], UK_link = UK[1], Asia = Asia[0], Asia_link = Asia[1],
                    India = India[0], India_link = India[1], world = world[0], world_link = world[1])

app.run()