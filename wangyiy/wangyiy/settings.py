# Scrapy settings for wangyiy project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'wangyiy'

SPIDER_MODULES = ['wangyiy.spiders']
NEWSPIDER_MODULE = 'wangyiy.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'wangyiy (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
    'Cookie': '_iuqxldmzr_=32; _ntes_nnid=e13a98f905c7a1e8a70bc195790e53cd,1636251908058; _ntes_nuid=e13a98f905c7a1e8a70bc195790e53cd; NMTID=00OShS0wM-GDLbfREpXpHYLgnjjsa0AAAF8-DaOWw; WEVNSM=1.0.0; WNMCID=luyyyp.1636251908271.01.0; WM_NI=9hLSd6TxBWj0sdkDah2bFJxCzQ8r59%2B7gbgvLCwriL2rquNKSYjYo3MtGHlCO5Q2HUBYq5q59z5I2NrPC8Bg1Ws%2B8jCT5bK4qKSiFkeV4c%2BfQL6oReKNEn54QEcpvQpfclE%3D; WM_TID=O9WqjTOwG0dBBQRBBUd%2BpP7QSinDFMPl; WM_NIKE=9ca17ae2e6ffcda170e2e6ee89fc46b2ada187c963b39a8aa3c15e828b9aaeb53f8dae9eb9b267919f8686b32af0fea7c3b92afbb884b4e73e98a88eb8e93cb1bca5a5e464f2be8aabfb49ba8ff893b833e9e9a983e67e909db993ec48f2aebf96cd419187a6baee398fac89a9ef498deb9fd3cb5f8287bfd6f43ffba6fbaab146b2908dd9c16df389bdccbb62818cfb83ca40b3959d8ac561a78afc84aa6e9394fa90d16f89928b8fb840939bad91f55bb4baad8dc837e2a3; MUSIC_U=e6c564d6fafcd63cf8acaec46df8dc6f5120f5c6898baae61bfc52ca67b552ea519e07624a9f0053d78b6050a17a35e705925a4e6992f61dfe3f0151024f9e31; __csrf=821c42629d6cc6690d71a2152b9ca49e; __remember_me=true; ntes_kaola_ad=1; JSESSIONID-WYYY=ER95jasPrgJmDl%2F5SCTa5YM18l5AG3V7xc3MK%2BwNokyklsojcM3gUeH3hGgnsz7g64jGenYP1rpQ3gzAbZPdD1D%2F5Ahj7JTxyZXDuBu%2B6poqe%2Fs8SuI6AF8i5lPUF6s2Mtk8Rdeq7DyfqCUbpGFsDNa%5C0BYqXd3V%2BH4FvS1X%2BC4Aj6Q%2F%3A1636255448874'

}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'wangyiy.middlewares.WangyiySpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'wangyiy.middlewares.WangyiyDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    # 'wangyiy.pipelines.WangyiyPipeline': 300,
    'wangyiy.pipelines.MysqlPipeline': 301,
}
# 数据库链接
MYSQL_HOST = '8.142.77.136'
MYSQL_DATABASE = 'wangfei'
MYSQL_USER = 'root'
MYSQL_PASS = 'root'
MYSQL_PORT = 3306
# 配置下载的图片地址
# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
