import base64
import unittest

from selenium import webdriver
import time
import os

# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.options import Options

from utils.pageloadtimer import PageLoadTimer


# class TestStringMethods(unittest.TestCase):
class TestStringMethods():
    def setUp(self):
        self.driver = webdriver.Firefox()
        # self.addCleanup(self.driver.quit)
        #
        # self.results = [
        #     ('search', 2000), ('main', 96)
        # ]


    def test_fields(self):
        self.driver = webdriver.Firefox()
        self.driver.get('https://s.wuage.com/factory/search?psa=W1.a211.c1.19')
        # self.assertEqual(self.driver.title, 'Example Domain')

        for i in range(1,6):
            time.sleep(0.2)
            self.driver.save_screenshot("search"+str(i)+".png")
        #
        # plt = PageLoadTimer(self.driver)
        # expected = [x[0] for x in self.results]
        # actual = [x[0] for x in plt.get_event_times()]
        # self.assertEqual(expected, actual)

    def test_snap(self):


        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("start-maximized")
        options.add_argument("disable-infobars")
        options.add_argument("--disable-extensions")
        self.driver = webdriver.Chrome(options=options)
        # WINDOW_SIZE = 1920,1080
        # self.driver.set_window_size(WINDOW_SIZE)
        self.driver.get('https://s.wuage.com/factory/search?psa=W1.a211.c1.19')
        shots = []
        TARGET_FOLDER = r'{}.png'
        # if not os.path.isdir(os.path.dirname(TARGET_FOLDER)):
        #     os.makedirs(os.path.dirname(TARGET_FOLDER))
        # we know that the animation duration on this page is 1 sec so we will try to record as many frames as possible in 1 sec
        start_time = time.time()
        while time.time() <= start_time + 1:
            shots.append(self.driver.get_screenshot_as_png())

        # dumping all captured frames
        for i in range(len(shots)):
            with open(TARGET_FOLDER.format(i), "wb") as f:
                f.write(shots[i])
        #
        # for i in range(1, 6):
        #     time.sleep(0.2)
        #     self.driver.save_screenshot("search" + str(i) + ".png")
    def tst_snap2(self):
        TARGET_FOLDER = r'{}.png'
        WINDOW_SIZE = 1920, 1080
        ANIM_DURATION = 1
        FRAMES = 15
        BASE_SCR = """
        function load_script(){
            let ss = document.createElement("script");
            ss.src = "https://cdnjs.cloudflare.com/ajax/libs/html2canvas/0.4.1/html2canvas.js";
            ss.type = "text/javascript";
            document.getElementsByTagName("head")[0].appendChild(ss);
        };

        load_script();
        shots = [];

        window.take = function() {
          html2canvas(document.body, {
            onrendered: function (canvas) {
              shots.push(canvas);
            }
          })
        };

        window.record = function(times, sleep){
            for (let i=0; i<times; i++){
                setTimeout(window.take(), sleep*i)
                console.log("issued screenshot with sleep: " + sleep*i)
            }
        };
        """ + """ 
        document.body.setAttribute("style", "width: {width}px; height: {height}px");
        """.format(width=WINDOW_SIZE[1], height=WINDOW_SIZE[0])

        RECORD_SCR = """
        document.body.innerHTML = document.body.innerHTML
        window.record({}, {})
        """

        GRAB_SCR = """

        function getShots(){
            let retval = []
            for (let i=0; i<shots.length; i++){
                retval.push(shots[i].toDataURL("image/png"))
            }
            return retval;
        }

        return getShots()
        """

        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("start-maximized")
        options.add_argument("disable-infobars")
        options.add_argument("--disable-extensions")

        # if not os.path.isdir(os.path.dirname(TARGET_FOLDER)):
        #     os.makedirs(os.path.dirname(TARGET_FOLDER))

        # driver = webdriver.Chrome( chrome_options=options)
        driver = webdriver.PhantomJS()
        # driver = webdriver.Chrome(executable_path=r'c:\_\chromedriver.exe')
        driver.set_window_size(*WINDOW_SIZE)
        driver.get('https://s.wuage.com/factory/search?keyWord=&psa=W2.p4.c17.j9')

        driver.execute_script(BASE_SCR)
        time.sleep(3)
        driver.execute_script(RECORD_SCR.format(FRAMES, (ANIM_DURATION / FRAMES) * 100))

        shots = []
        while len(shots) < FRAMES:
            shots = driver.execute_script(GRAB_SCR)

        # dumping all captured frames
        for i in range(len(shots)):
            with open(TARGET_FOLDER.format(i), "wb") as f:
                f.write(base64.urlsafe_b64decode(shots[i].split('base64,')[1]))

        driver.quit()
if __name__ == '__main__':
    # unittest.main()
    unittest = TestStringMethods()
    unittest.tst_snap2()