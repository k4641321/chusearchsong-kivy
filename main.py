import kivy
kivy.require("2.3.1")

from kivy.app import App
from search import 曲目搜索
from kivy.uix.boxlayout import BoxLayout
from loguru import logger
from kivy.clock import Clock

class root(App):

    # def search(self):
    #     结果=曲目搜索("resources\list.json","分类",None,None,0,0,"b")
    #     logger.info(结果)
    def build(self):
        logger.info("building..")
        # return BoxLayout()

if __name__ == "__main__":
    root().run()