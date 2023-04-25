import scrapy

class PostsSpider(scrapy.Spider):
    name="blackspyder"

    start_urls=[
        "https://thehiddenwiki.org/"

    ]

    def parse(self, response, **kwargs):
        
        page = response.url.split('/')[-1]
        fileName = 'link_database.txt'


        all_links = response.css('a::attr(href)').getall()

        onion_links_directory = [link +"\n" for link in all_links if ".onion" in link]
        with open(fileName,'w') as f:
            f.writelines(onion_links_directory)
