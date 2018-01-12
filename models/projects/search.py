"""
  @author Victor I. Afolabi
  A.I. engineer/researcher & Software engineer
  javafolabi@gmail.com
  
  Created on 12 January, 2018 @ 1:56 PM.
  
  Copyright © 2018. Victor. All rights reserved.
"""

# Search API (Deprecated): http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q=
# https://www.google.com/?client=safari&channel=iphone_bm&gws_rd=cr&ei=GkfAWOWPOMuqaabnrOgF#channel=iphone_bm&q=search+query&*
# https://www.google.com.ng/search?q=time&biw=1085&bih=646&source=lnms&sa=X&ved=0ahUKEwj_rZXsv8fSAhWL1BoKHaiKAFsQ_AUIBygA
import urllib.parse
import urllib.request

from bs4 import BeautifulSoup


class Search(object):
    def __init__(self):
        self.googleSearchURL = 'https://www.google.com/search?q={}&start={}'

    def search(self, query, page=1):
        """
        Parses Google for a search query.
        :param query: String to be searched.
        :param page: Page to be displayed.
        :return: dictionary. Containing titles, links, cites and descriptions.
        """
        page = int(f'{page}0')
        query = urllib.parse.quote(query)
        self.googleSearchURL = self.googleSearchURL.format(query, page)
        source = Search.getSource(self.googleSearchURL)
        soup = BeautifulSoup(source, 'lxml')
        # find all class_='g' => each result
        each_result = soup.find_all('div', class_='g')
        titles = []
        links = []
        cites = []
        descs = []
        for each in each_result:
            try:
                h3 = each.find('h3', class_='r')
                link = h3.find('a')
                cite = each.find('cite', class_='_Rm')
                desc = each.find('span', class_='st')
                ''' Get the text and link '''
                h3_text = h3.text
                link = link.get('href')
                cite = cite.text
                desc_text = desc.text
                ''' Append links and text to a list '''
                titles.append(h3_text)
                links.append(link)
                cites.append(cite)
                descs.append(desc_text)
            except:
                pass
        search_results = {'titles': titles,
                          'links': links,
                          'cites': cites,
                          'descriptions': descs}
        print(len(titles), len(links), len(cites), len(descs))
        return search_results

    @staticmethod
    def getSource(url):
        """
        Returns the source code of a webpage.
        :rtype: string
        :param url: URL to pull it's source code
        :return: string, source code of a given URL.
        """
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/56.0.2924.87 Safari/537.36'}
        try:
            request = urllib.request.Request(url, headers=headers)
            response = urllib.request.urlopen(request)
            resp = response.read()
        except Exception as e:
            raise Exception('ERROR: {}\n'.format(e))
        return str(resp)


if __name__ == '__main__':
    search = Search()
    results = search.search('preaching to the choir', 1)
    print(results)
