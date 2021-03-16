"""
    参考标准：
    https://www.w3.org/TR/navigation-timing/
    https://developer.mozilla.org/en-US/docs/Web/API/Navigation_timing_API
    https://techblog.constantcontact.com/software-development/measure-page-load-times-using-the-user-timing-api/
"""
import asyncio
import collections
import textwrap
from time import sleep
import json
from selenium import webdriver

import multiprocessing
class PageLoadTimer:

    def __init__(self, driver):
        """
            takes:
                'driver': webdriver instance from selenium.
        """
        self.driver = driver

        self.jscript = textwrap.dedent("""
            var performance = window.performance || {};
            var timings = performance.timing || {};
            return timings;
            """)
    #通过js获取各个事件的时间戳
    def inject_timing_js(self):
        timings = self.driver.execute_script(self.jscript)
        return timings

    def caculate_timing_frontend(self,url):
        self.driver.get(url)

        sleep(6)
        navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
        responseStart = driver.execute_script("return window.performance.timing.responseStart")
        domComplete = driver.execute_script("return window.performance.timing.loadEventEnd")

        backendPerformance = responseStart - navigationStart
        frontendPerformance = domComplete - navigationStart

        print("Back End: %s" % backendPerformance)
        print("Front End: %s" % frontendPerformance)

    async def monitor_performance(self):
        # timeLineEnties = []

        import time
        for i in [0.1 ,0.3, 0.5,0.7, 0.9,1.2, 1.5, 1.8, 2.2]:
            millis_start = int(round(time.time() * 1000))
            driver.execute_script("document.location.reload()")
            consume = int(round(time.time() * 1000)) - millis_start
            print(f"relocd time is : ",consume)
            sleep(i)
            print(f"intervel time is : {0}",i)
            entries = driver.execute_script("return window.performance.getEntries()")
            # entries = driver.execute_async_script("return window.performance.getEntries()")

            print(len(entries))

            print(entries)
    async def getUrl(self,loop, url):
        import time
        for i in range(0,loop):

            millis_start = int(round(time.time() * 1000))
            self.driver.get(url)
            consume = int(round(time.time() * 1000)) - millis_start
            print(consume)
        # self.driver.refresh()
    async def getEntrites(self, url):
        await asyncio.gather(
            # self.monitor_performance(),
            self.getUrl(1,url),
            self.monitor_performance(),


        )
        # timeLineEnties = []
        # await self.monitor_performance()
        # self.driver.get(url)

        # for i in range(1,10):
        #     sleep(0.2)
        #     entries = driver.execute_script("return window.performance.getEntries()")
        #     timeLineEnties.append(entries)
        # for entry in timeLineEnties:
        #     print(entry)
        #     # jb_entry = json.loads(entries,encoding='utf-8')
        #     print(len(entries))



    def get_event_times(self):

        """

        :return: W3C timing API 返回性能Event列表
        """
        timings = self.inject_timing_js()
        #排除其它非时间戳类型值和0的干扰
        good_values = [epoch for epoch in timings.values() if epoch != 0 and isinstance(epoch, int)]
        # w3c 定义时间
        ordered_events = ('navigationStart', 'fetchStart', 'domainLookupStart',
                          'domainLookupEnd', 'connectStart', 'connectEnd',
                          'secureConnectionStart', 'requestStart',
                          'responseStart', 'responseEnd', 'domLoading',
                          'domInteractive', 'domContentLoadedEventStart',
                          'domContentLoadedEventEnd', 'domComplete',
                          'loadEventStart', 'loadEventEnd'
                          )
        startTime = min(good_values)
        event_times = ((event, timings[event] - startTime)
                       for event in ordered_events if event in timings)
        return collections.OrderedDict(event_times)

    def get_onLoadTime(self, url):
        self.driver.get(url)
        timings = self.inject_timing_js()
        # 排除其它非时间戳类型值和0的干扰
        good_values = [epoch for epoch in timings.values() if epoch != 0 and isinstance(epoch, int)]
        # w3c 定义时间
        ordered_events = ('navigationStart',  'loadEventEnd'
                          )
        startTime = min(good_values)
        event_times = ((event, timings[event] - startTime)
                       for event in ordered_events if event in timings)
        dict=collections.OrderedDict(event_times)
        print("onload time: "+str(dict["loadEventEnd"]))
        return dict["loadEventEnd"]



    def process_geturl(self):

        import time
        print(f"request url at : ",time.time())
        url = 'https://www.wuage.com/?psa=W1.a211.c1.2'
        millis_start = int(round(time.time() * 1000))
        self.driver.get(url)
        consume = int(round(time.time() * 1000)) - millis_start
        print(f"get url consume : ",consume)

    def process_getperf(self):

        import time
        sleeped = 0.0
        perfbegin = int(round(time.time() * 1000))
        for i in range(5):
            # millis_start = int(round(time.time() * 1000))
            # driver.execute_script("document.location.reload()")
            # consume = int(round(time.time() * 1000)) - millis_start
            # print(f"relocd time is : ", consume)
            sleep(i/10)
            # print(f"execute script at : ",time.time())
            print(f"intervel time is : ", i)
            millis_start = int(round(time.time() * 1000))
            entries = driver.execute_script("return window.performance.getEntries()")
            # entries = driver.execute_async_script("return window.performance.getEntries()")
            millis_end = int(round(time.time() * 1000))
            consume = millis_end - millis_start
            print(f"execute script time is : ", consume)
            sleeped =  millis_end - perfbegin
            print(f"have sleeped : ",sleeped)
            print(len(entries))

            # print(entries)
        # sleep(3)
        # entries = driver.execute_script("return window.performance.getEntries()")
        # print(f"entries number is : ", len(entries))
        # print(len(entries))

if __name__ == '__main__':



    url = 'https://go.wuage.com/?psa=W1.a211.c1.3'
    urlhome = 'https://www.wuage.com/?psa=W1.a211.c1.2'

    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--incognito')  # 隐身模式（无痕模式）

    mobile_emulation = {"deviceName": "Nexus 5"}

    chrome_options = webdriver.ChromeOptions()

    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)


    driver = webdriver.Chrome(options=chrome_options)
    # driver.
    # driver.implicitly_wait(10)
    # driver.refresh()
    driver.get("https://m.wuage.com/#/home")
    sleep(9)

    # timer = PageLoadTimer(driver)
    # timer.caculate_timing_frontend(url)
    # timer.get_onLoadTime()
    # asyncio.run(timer.getEntrites(urlhome))
    # timer.getEntrites(urlhome)
    # p1 = multiprocessing.Process(target=timer.process_geturl)
    # p2 = multiprocessing.Process(target=timer.process_getperf)
    #
    # p1.start()
    # p2.start()
    #
    # p1.join()
    # p2.join()
    # timer.get_onLoadTime(url)
    # print(timer.get_event_times().__str__())
    driver.close()
