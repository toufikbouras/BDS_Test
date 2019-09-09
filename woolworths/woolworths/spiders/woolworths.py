
# coding: utf-8


from woolworths.items import WoolworthsItem
from scrapy.spiders import CrawlSpider


class WoolWorthsSpider(CrawlSpider):
    
    # identity
    name = 'wwspider'
#   allowed_domains = ['woolworths.com.au']
    start_urls = ['https://www.woolworths.com.au/shop/browse/drinks/cordials-juices-iced-teas/iced-teas',
                 ]
    custom_settings = {
    # specifies exported fields and order
    'FEED_EXPORT_FIELDS': ["Home", "Drinks", "CJIT", "IcedTeas"],
  }
#     def __init__(self):
#         self.driver = webdriver.Firefox()

#     def request(self):
#         url = 'https://www.woolworths.com.au/shop/browse/drinks/cordials-juices-iced-teas/iced-teas'
#         yield scrapy.Request(url = url, callback = self.parse)
        
    def parse(self, response):
        items = []
#         item['IcedTeas'] = link[13] 
        IcedList = response.xpath('//div[@class="tile-container tile-product"]//a[@class="shelfProductTile-descriptionLink"]/text() \
        | //div[@class="tile-container tile-bundle"]//div[@class="shelfBundleTile-title"]/text').extract()
        link = response.xpath('//ul[@class="breadcrumbs-linkList"]/li[@class="breadcrumbs-link"]//span[@ng-switch="!!link.url"]//text()').extract()

#         item['IcedTeas'] = [x.strip() for x in IcedList]
        for x in IcedList:
            item = WoolworthsItem()
            item['Home'] = link[2]
            item['Drinks'] = link[6]
            item['CJIT'] = link[10]
            item['IcedTeas'] = x.strip()

            items.append(item)
#         for value in response.xpath('//div[@class="tile-container tile-product"]//a[@class="shelfProductTile-descriptionLink"]/text() \
#         | //div[@class="tile-container tile-bundle"]//div[@class="shelfBundleTile-title"]/text').extract():

        return(items)

        



