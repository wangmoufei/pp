import scrapy


class WyySpider(scrapy.Spider):
    name = 'wyy'
    allowed_domains = ['https://music.163.com/#/user/home?id=29761590']
    start_urls = ['https://api.imjad.cn/cloudmusic/?type=playlist&id=29761590']

    def parse(self, response):
        # personal_information = response.js("document.querySelector('#j-name-wrap > i')")
        # print(personal_information)
        pass




if __name__ == '__main__':
    from scrapy import cmdline

    args = "scrapy crawl wyy".split()
    cmdline.execute(args)