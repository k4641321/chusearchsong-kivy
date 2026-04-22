import kivy
kivy.require("2.3.1")

from kivy.app import App
from search import 曲目搜索,结果容器创建
from loguru import logger
from kivy.clock import Clock
import asyncio
from kivy.lang import Builder


class root(App):

    def build(self):
        logger.info("building..")
        try:
            self.loop=asyncio.get_event_loop()
        except RuntimeError:
            self.loop = asyncio.new_event_loop()
            asyncio.set_event_loop(self.loop)
        return Builder.load_file("root.kv")
    async def search(self):
        logger.info("开始搜索...")
        曲目列表路径 = "resources/list.json"
        
        genre = self.root.ids.genreSpinner.text
        version = self.root.ids.versionSpinner.text
        diff_min = self.root.ids.diffminSpinner.text
        diff_max = self.root.ids.diffmaxSpinner.text
        search_text = self.root.ids.searchinput.text or ""
        logger.info(f"搜索参数: {genre} {version} {diff_min} {diff_max} {search_text}")
        # try:
        self.root.ids.resultbox.clear_widgets()
        结果 = await 曲目搜索(
            曲目列表路径,
            genre,
            version,
            diff_min,
            diff_max,
            search_text
        )
        结果容器= await 结果容器创建(结果)
        # logger.info(结果)
        self.root.ids.resultbox.add_widget(结果容器)
        # except Exception as e:
        #     logger.error(f"搜索过程出错: {e}",exc_info=True)
        #     # 显示错误信息到 UI

    def _run_async_via_clock(self, dt=0):
            self.loop.run_until_complete(self.search())
       

    def schedule_search_with_clock(self):
        """供KV调用的Clock调度入口（仅触发Clock调度，不直接调用异步函数）"""
        # 用Clock调度_run_async_via_clock，dt参数是Clock自动传递的时间差，可忽略
        Clock.schedule_once(self._run_async_via_clock)
       

if __name__ == "__main__":
    # Clock.schedule_once(root.schedule_search_with_clock,1)
    root().run()