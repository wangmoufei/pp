import scrapy


class Top250Spider(scrapy.Spider):
    name = 'top250'
    allowed_domains = ['book.douban.com']
    start_urls = ['https://book.douban.com/top250?start=0/']

    def parse(self, response):
        print(response.url)
        print(response.status)
        print(response.text)






if __name__ == '__main__':
    from scrapy import cmdline

    args = "scrapy crawl top250 -s LOG_FILE=all.log".split()
    cmdline.execute(args)

# scrapy crawl wyy --nolog不输出日志
# scrapy crawl wyy默认输出日志到窗口
# scrapy crawl wyy -s LOG_FILE=all.log #日志输出到当前目录下
