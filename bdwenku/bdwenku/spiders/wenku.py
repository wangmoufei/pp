import scrapy


class WenkuSpider(scrapy.Spider):
    name = 'wenku'
    allowed_domains = ['wenku.baidu.com']
    start_urls = ['https://wenku.baidu.com/search?word=python&pn=1']

    def parse(self, response):
        print("Hello Scrapy")
        # print(response.url)
        # print(response.status)
        alist = response.selector.css("dl dt a.tiaoquan")
        print(len(alist))
        for a in alist:
            print(a.css("::attr(title)").get())
        yield


if __name__ == '__main__':
    from scrapy import cmdline

    args = "scrapy crawl wenku".split()
    cmdline.execute(args)
