import scrapy
from scrapy.crawler import CrawlerProcess

class ConsultKoenSpider(scrapy.Spider):
    name = "consult_koen_spider"
    # the code for your spider

    def start_requests( self ):
            urls = [ 'https://www.consult-koen.web.app' ]
            for url in urls:
                #	Yield							|	Return
                #	=========================================================================
                # 1	Yield is generally used to 		|	Return is generally used for ending
                #	convert a regular Python 		|	the execution and “returns”
                #	function into a generator. 		|	result to the caller statement.
                #	-------------------------------------------------------------------------
                # 2	It replace the return of a 		|	It exits a function and handing back
                #	function to suspend its 		|	a value to its caller.
                #	execution without destroying	|
                #	local variables.				|
                #	-------------------------------------------------------------------------
                # 3	It is used when the generator	|	It is used when a function.
                #	returns an intermediate result	|	is ready to send a value.
                #	to the caller.
                #	-------------------------------------------------------------------------
                # 4	Code written after yield 		|	Code written after return statement
                # 	statement executes in next 		|	won't be executed.
                #	function call.					|
                #	-------------------------------------------------------------------------
                # 5	It can run multiple times.		|	It only runs single time.
                # 6	'yield' functions executes 		|	Every function calls run the
                #	from the last state from where 	|	'return' function from the start.
                #	the function get paused.		|
                #	-------------------------------------------------------------------------
                yield scrapy.Request( url = url, callback = self.parse )

    def parse( self, response ):
        # simple example: write out the html
        html_file = 'consult_koen.html'
        # with open( html_file, 'wb' ) as fout:
        #     fout.write( response.body )
        links = response.css('a::attr(href)').extract()

        title = response.xpath('//h1[contains(@class,"title")]/text()')
        title_ext = title.extract_first().strip()
        ch_titles = response.css('h4.chapter__title::text')
        ch_titles_ext = [t.strip() for t in ch_titles.extract()]
        dc_dict[ title_ext ] = ch_titles_ext

        filepath = 'DC_links.csv'
        with open( filepath, 'w' ) as f:
            f.writelines( [link + '/n' for link in links] )


# Initialize the dictionary **outside** of the Spider class
dc_dict = dict()

# initiate a CrawlerProcess
process = CrawlerProcess()
# tell the process which spider to use
process.crawl(ConsultKoenSpider)
# start the crawling process
process.start()

# OUTPUT
# 2021-07-10 16:26:25 [scrapy.utils.log] INFO: Scrapy 2.5.0 started (bot: scrapybot)
# 2021-07-10 16:26:26 [scrapy.utils.log] INFO: Versions: lxml 4.6.3.0, libxml2 2.9.5, cssselect 1.1.0, parsel 1.6.0, w3lib 1.22.0, Twisted 21.2.0, Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)], pyOpenSSL 20.0.1 (OpenSSL 1.1.1k  25 Mar 2021), cryptography 3.4.7, Platform Windows-10-10.0.19043-SP0
# 2021-07-10 16:26:26 [scrapy.utils.log] DEBUG: Using reactor: twisted.internet.selectreactor.SelectReactor
# 2021-07-10 16:26:26 [scrapy.crawler] INFO: Overridden settings:
# {}
# 2021-07-10 16:26:26 [scrapy.extensions.telnet] INFO: Telnet Password: 5940d893371a9458
# 2021-07-10 16:26:26 [scrapy.middleware] INFO: Enabled extensions:
# ['scrapy.extensions.corestats.CoreStats',
#  'scrapy.extensions.telnet.TelnetConsole',
#  'scrapy.extensions.logstats.LogStats']
# 2021-07-10 16:26:27 [scrapy.middleware] INFO: Enabled downloader middlewares:
# ['scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware',
#  'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware',
#  'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware',
#  'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware',
#  'scrapy.downloadermiddlewares.retry.RetryMiddleware',
#  'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware',
#  'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware',
#  'scrapy.downloadermiddlewares.redirect.RedirectMiddleware',
#  'scrapy.downloadermiddlewares.cookies.CookiesMiddleware',
#  'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware',
#  'scrapy.downloadermiddlewares.stats.DownloaderStats']
# 2021-07-10 16:26:27 [scrapy.middleware] INFO: Enabled spider middlewares:
# ['scrapy.spidermiddlewares.httperror.HttpErrorMiddleware',
#  'scrapy.spidermiddlewares.offsite.OffsiteMiddleware',
#  'scrapy.spidermiddlewares.referer.RefererMiddleware',
#  'scrapy.spidermiddlewares.urllength.UrlLengthMiddleware',
#  'scrapy.spidermiddlewares.depth.DepthMiddleware']
# 2021-07-10 16:26:27 [scrapy.middleware] INFO: Enabled item pipelines:
# []
# 2021-07-10 16:26:27 [scrapy.core.engine] INFO: Spider opened
# 2021-07-10 16:26:27 [scrapy.extensions.logstats] INFO: Crawled 0 pages (at 0 pages/min), scraped 0 items (at 0 items/min)
# 2021-07-10 16:26:27 [scrapy.extensions.telnet] INFO: Telnet console listening on 127.0.0.1:6023
# 2021-07-10 16:26:27 [scrapy.core.downloader.tls] WARNING: Remote certificate is not valid for hostname "www.consult-koen.web.app"; VerificationError(errors=[DNSMismatch(mismatched_id=DNS_ID(hostname=b'www.consult-koen.web.app'))])
# 2021-07-10 16:26:27 [scrapy.core.engine] DEBUG: Crawled (404) <GET https://www.consult-koen.web.app> (referer: None)
# 2021-07-10 16:26:27 [scrapy.spidermiddlewares.httperror] INFO: Ignoring response <404 https://www.consult-koen.web.app>: HTTP status code is not handled or not allowed
# 2021-07-10 16:26:27 [scrapy.core.engine] INFO: Closing spider (finished)
# 2021-07-10 16:26:27 [scrapy.statscollectors] INFO: Dumping Scrapy stats:
# {'downloader/request_bytes': 224,
#  'downloader/request_count': 1,
#  'downloader/request_method_count/GET': 1,
#  'downloader/response_bytes': 11005,
#  'downloader/response_count': 1,
#  'downloader/response_status_count/404': 1,
#  'elapsed_time_seconds': 0.868,
#  'finish_reason': 'finished',
#  'finish_time': datetime.datetime(2021, 7, 10, 14, 26, 27, 983441),
#  'httperror/response_ignored_count': 1,
#  'httperror/response_ignored_status_count/404': 1,
#  'log_count/DEBUG': 1,
#  'log_count/INFO': 11,
#  'log_count/WARNING': 1,
#  'response_received_count': 1,
#  'scheduler/dequeued': 1,
#  'scheduler/dequeued/memory': 1,
#  'scheduler/enqueued': 1,
#  'scheduler/enqueued/memory': 1,
#  'start_time': datetime.datetime(2021, 7, 10, 14, 26, 27, 115441)}
# 2021-07-10 16:26:27 [scrapy.core.engine] INFO: Spider closed (finished)