
import json
import asyncio
from loguru import logger
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

版本号对照={
    "CHUNITHM":10000,
    "CHUNITHM PLUS":10500,
    "CHUNITHM AIR":11000,
    "CHUNITHM AIR PLUS":11500,
    "CHUNITHM STAR":12000,
    "CHUNITHM STAR PLUS":12500,
    "CHUNITHM AMAZON":13000,
    "CHUNITHM AMAZON PLUS":13500,
    "CHUNITHM CRYSTAL":14000,
    "CHUNITHM CRYSTAL PLUS":14500,
    "CHUNITHM PARADISE":15000,
    "CHUNITHM PARADISE LOST":15500,
    "CHUNITHM NEW":20000,
    "CHUNITHM NEW PLUS":20500,
    "CHUNITHM SUN":21000,
    "CHUNITHM SUN PLUS":21500,
    "CHUNITHM LUMINOUS":22000,
    "CHUNITHM LUMINOUS PLUS":22500,
    "CHUNITHM VERSE":23000,
    "全部版本":None,
    "版本":None 

}
#多构建一个歌曲的json
def 返回歌曲json(id,title,artist,genre,bpm,version_value,version,difficulties):
    data = {
        "id": id,
        "title": title,
        "artist":artist,
        "genre": genre,
        "bpm": bpm,
        "version_value": version_value,
        "version":version,
        "difficulties":difficulties,
        "isappend":False,
    }
    return data
async def 曲目搜索(曲目列表路径:str,分类筛选:str,版本筛选:str,难度下限:str ,难度上限:str ,搜索框:str):
    print(分类筛选,'1',版本筛选,'1',难度下限,'1',难度上限,'1',搜索框)
    with open(曲目列表路径, "r", encoding="UTF-8") as f:
        曲目列表 = json.load(f)
        f.close()

    if 分类筛选=="流派" or 分类筛选=='全部流派':
        分类筛选=None

    if 版本筛选=="版本" or 版本筛选=='全部版本':
        版本筛选值=None 
    else:   
        版本筛选值=版本号对照[版本筛选]

    if 难度下限=="难度下限":
        难度下限=0
    else:
        难度下限=float(难度下限)

    if 难度上限=="难度上限":
        难度上限=0
    else:
        难度上限=float(难度上限)

    print(分类筛选,'1',版本筛选值,'1',难度下限,'1',难度上限,'1',搜索框)

    #正式检索
    结果 = []

    for i in 曲目列表["songs"]:
        #初步筛选标题
        if 搜索框.lower() in i["title"].lower():
            for j in 曲目列表["versions"]:
                if i["version"] == j["version"]:
                    单首曲目 = 返回歌曲json(i["id"],i["title"],i["artist"],i["genre"],i["bpm"],i["version"],j["title"],i["difficulties"])
                    结果.append(单首曲目)
    # logger.info(结果)

    #筛选分类
        
    if 分类筛选 == None:
        logger.info('跳过分类')
    else:
        结果2 = []
        for i in 结果:
            if 分类筛选==i["genre"]:  
                结果2.append(i)
        结果=结果2
        logger.info(结果2)    

    #筛选版本
    if 版本筛选值==None:
        logger.info('跳过版本')
    else:
        结果3 = []
        for i in 结果:
            if 版本筛选值==i["version_value"]:  
                结果3.append(i)
        结果=结果3
        logger.info(结果3)

    #难度筛选
    if 难度下限==0 and 难度上限==0:
        logger.info('跳过难度')
    else:
        结果4 = []
        for i in 结果:
            isappend=False
            if i["isappend"]==True:
                isappend=True
                continue
            if 难度下限==0 or 难度上限==0:
                continue
            for j in i["difficulties"]: 
                if 难度下限 <= j["level_value"] <= 难度上限 and isappend==False:
                    isappend=True
                    结果4.append(i)
            if isappend:
                i["isappend"]=True
        结果=结果4
        logger.info(结果4)
    
    logger.info(结果)
        # if 搜索框.lower() in i["title"].lower():
        #     if 分类筛选 == None and i["version"] == 版本筛选值:
        #         单首曲目 = 返回歌曲json(i["id"],i["title"],i["artist"],i["genre"],i["bpm"],i["version"],版本筛选,i["difficulties"])
        #         结果.append(单首曲目)
        #     elif 分类筛选 == i["genre"] and 版本筛选 == None:
        #         for j in 曲目列表["versions"]:
        #             if i["version"] == j["version"]:
        #                 单首曲目 = 返回歌曲json(i["id"],i["title"],i["artist"],i["genre"],i["bpm"],i["version"],j["title"],i["difficulties"])
        #         结果.append(单首曲目)
        #     elif 分类筛选 == i["genre"] and i["version"] == 版本筛选值:
        #         单首曲目 = 返回歌曲json(i["id"],i["title"],i["artist"],i["genre"],i["bpm"],i["version"],版本筛选,i["difficulties"])
        #         结果.append(单首曲目)
        #     elif 版本筛选 == None and 分类筛选 == None:
        #         for j in 曲目列表["versions"]:
        #             if i["version"] == j["version"]:
        #                 单首曲目 = 返回歌曲json(i["id"],i["title"],i["artist"],i["genre"],i["bpm"],i["version"],j["title"],i["difficulties"])
        #         结果.append(单首曲目)
            # else:
            #     for j in 曲目列表["versions"]:
            #         if i["version"] == j["version"]:
            #             单首曲目 = 返回歌曲json(i["id"],i["title"],i["artist"],i["genre"],i["bpm"],i["version"],j["title"],i["difficulties"])
            #     结果.append(单首曲目)
    # print(结果)
    # 结果2=[]
    # for i in 结果:
    #     isappend=False
    #     if i["isappend"]==True:
    #         isappend=True
    #         continue
    #     if 难度下限==0 or 难度上限==0:
    #         continue
    #     for j in i["difficulties"]: 
    #         if 难度下限 <= j["level_value"] <= 难度上限 and isappend==False:
    #             isappend=True
    #             结果2.append(i)
    #     if isappend:
    #         i["isappend"]=True
    # #print(结果2)
    # if not 结果2==[]:
    #     结果=结果2
    # logger.info(结果)
    return 结果

async def 结果容器创建(结果):
    滚动条=ScrollView(size_hint=(1,1),bar_pos_y='right',size=(Window.width,Window.height),scroll_wheel_distance=100)
    结果容器=BoxLayout(orientation="vertical",size_hint_y=None)
    结果容器.bind(minimum_height=结果容器.setter('height'))
    for i in 结果:
        # 单曲容器=BoxLayout(orientation="horizontal",size_hint_y=None,height=40)
        
        单曲标签=Label(
            text=f"{i['id']}  -  {i['title']}    {i['genre']}  -  {i['version']}",
            font_name="simhei.ttf",
            size_hint_y=None,
            height=40,
            halign="center",
            valign="middle",
            )
        单曲标签.id=i['id']
        单曲标签.bind(size=单曲标签.setter('text_size'))
        # 单曲容器.add_widget(单曲标签)
        结果容器.add_widget(单曲标签)
    滚动条.add_widget(结果容器)
    return 滚动条