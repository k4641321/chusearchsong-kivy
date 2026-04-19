import kivy
kivy.require("2.3.1")

from kivy.app import App
from search import 曲目搜索
from kivy.uix.boxlayout import BoxLayout
from loguru import logger
from kivy.clock import Clock
import asyncio

class root(App):

    def build(self):
        logger.info("building..")
        # 确保返回 KV 文件中定义的根组件
        # 如果 KV 文件名是 root.kv，Kivy 会自动加载，这里不需要手动 return BoxLayout()
        
    async def do_search(self):
        """执行实际的异步搜索任务"""
        try:
            # 假设 曲目搜索 是一个 async 函数
            结果 = await 曲目搜索("resources/list.json", "分类", None, None, 0, 0, "b")
            logger.info(f"搜索结果: {结果}")
        except Exception as e:
            logger.error(f"搜索出错: {e}")

    def search(self):
        """由按钮触发的同步入口，负责调度异步任务"""
        logger.info("开始搜索...")
        # 使用 Clock 调度异步任务，避免阻塞 UI
        Clock.schedule_once(lambda dt: asyncio.ensure_future(self.do_search()), 0)

if __name__ == "__main__":
    root().run()