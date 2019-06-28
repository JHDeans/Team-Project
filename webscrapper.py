import requests
from bs4 import BeautifulSoup


def title_generator(titleStories):
    titles = []	
 
    def post_formatter(titleStory):
        titleStories = str(titleStory).replace('<h2>', ' ')
        titleStories = titleStories.replace('</h2>', ' ')
        titles.append(titleStories)


    for titleStory in titleStories:
        post_formatter(titleStory)


    return titles
    	
	
def story_generator(stories_list):
    stories = []	
    def post_formatter2(story):
        story = str(story).replace('<p>', ' ')
        story = story.replace('</p>', ' ')
        stories.append(story)


    for story in stories_list:
        post_formatter2(story)


    return stories		


r = requests.get('https://www.thespoof.com/spoof-news/us/')
soup = BeautifulSoup(r.text, 'html.parser')

titleStories = soup.find_all('h2')
getStories = soup.find_all('p')

titles = title_generator(titleStories)[:-1]
stories = story_generator(getStories)[:-3]


for title in titles:
    print(title)


for story in stories:
    print(story)
