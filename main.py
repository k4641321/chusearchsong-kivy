import kivy
kivy.require("2.3.1")

from kivy.app import App
from search import 曲目搜索
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
        """异步搜索核心逻辑（保持不变）"""
        logger.info("开始搜索...")
        曲目列表路径= "resources/list.json"
        logger.info(self.root.ids.filterBox.children[1].text)
        结果 = await 曲目搜索(曲目列表路径,None, None, None, 0, 0, "b")
        # logger.info(f"搜索结果: {结果}")

    def _run_async_via_clock(self, dt=0):
            self.loop.run_until_complete(self.search())
       

    def schedule_search_with_clock(self,):
        """供KV调用的Clock调度入口（仅触发Clock调度，不直接调用异步函数）"""
        # 用Clock调度_run_async_via_clock，dt参数是Clock自动传递的时间差，可忽略
        Clock.schedule_once(self._run_async_via_clock)
       

if __name__ == "__main__":
    # Clock.schedule_once(root.schedule_search_with_clock,1)
    root().run()