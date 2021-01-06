from bs4 import BeautifulSoup
import json

EP = 92
for i in range(1, EP+1):

    soup = BeautifulSoup(open('./detail_html/{}.html'.format(i)), 'html5lib')
    listing_dic ={}
    listing_dic['title'] = soup.find('h1').text.strip()
    season_title = soup.find('div', class_='bp_item bp_text_only')
    season_episode= season_title.find('div', attrs = {'class':'bp_heading'}).text.strip().split('| ')
    listing_dic['season'] = season_episode[0].replace('Season ','')
    listing_dic['episode'] = season_episode[1].replace('Episode ','')
    listing_dic['description'] = soup.find('div', attrs = {'class':'summary_text'}).text.strip()
    listing_dic['rating'] = soup.find('div', attrs = {'class':'ratingValue'}).text.strip()
    listing_dic['total_vote'] = soup.find('span', attrs = {'itemprop':"ratingCount"}).text.strip()
    article = soup.find_all('div', class_='article')
    listing_dic['airdate'] = soup.find('a', attrs = {'title':'See more release dates'}).text.strip()
    listing_dic['runtime'] = soup.find('time').text.strip()
    listing_dic['list_of_the_cast'] = soup.find('table', attrs = {'class':'cast_list'}).text.strip().replace("              ...","as").replace("            ","").replace("\n"," ").replace('                     ','').replace('Episode cast overview, first billed only:','').replace('     ','\n').replace('\n\n',' ').replace('Episode cast overview:','').replace('Episode credited cast:','').replace('   Rest of cast listed alphabetically:','')
    print(i)
    with open('./result/{}.json'.format(season_episode), 'w') as outfile:
        json.dump(listing_dic, outfile)




