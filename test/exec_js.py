#-*- coding: utf-8 -*-
# ------ wuage.com testing team ---------
# __author__ : jianxing.wei@wuage.com
from selenium import webdriver
import time

# 读取JS代码，这里保存在test.js文件中
def get_script():
    with open('./lcp.js', encoding='utf-8') as f:
        js_script = f.read()
        return js_script

# 主函数
def main():
    # 启动chrome，这都是selenium标准用法，不清楚请百度
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    browser = webdriver.Chrome(options=chrome_options)
    mainUrl = 'http://www.wuage.com'
    browser.get(mainUrl)

    # 异步执行JS代码并获取结果，同时记录前后时间
    start_time = time.time()
    results = browser.execute_async_script(get_script())
    end_time = time.time()

    # 打印结果，并显示结果的类型
    # print('执行结果：', results)
    for entry in results:
        print(f"entry size is : ", len(entry))
        print(entry)
    print('结果类型：', type(results))

    # 打印开始和结束时间，以及总时长
    print('运行时长：', end_time - start_time)
    browser.quit()

if __name__ == '__main__':
    main()

