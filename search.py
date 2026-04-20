
import json
import asyncio
from loguru import logger

#多构建一个歌曲的json
def 返回歌曲json(id,title,artist,genre,bpm,version,zhversion,difficulties):
    data = {
        "id": id,
        "title": title,
        "artist":artist,
        "genre": genre,
        "bpm": bpm,
        "version": version,
        "zhversion":zhversion,
        "difficulties":difficulties,
        "isappend":False,
    }
    return data
async def 曲目搜索(曲目列表路径:str,分类筛选:str,版本筛选:str,版本筛选中文名,难度筛选前:float ,难度筛选后:float ,搜索框:str):
    with open(曲目列表路径, "r", encoding="UTF-8") as f:
        曲目列表 = json.load(f)
        f.close()
    结果 = []
    if 分类筛选=="分类":
        分类筛选=None

    for i in 曲目列表["songs"]:
        if 搜索框.lower() in i["title"].lower():
            if 分类筛选 == None and i["version"] == 版本筛选:
                单首曲目 = 返回歌曲json(i["id"],i["title"],i["artist"],i["genre"],i["bpm"],i["version"],版本筛选中文名,i["difficulties"])
                结果.append(单首曲目)
            elif 分类筛选 == i["genre"] and 版本筛选 == None:
                for j in 曲目列表["versions"]:
                    if i["version"] == j["version"]:
                        单首曲目 = 返回歌曲json(i["id"],i["title"],i["artist"],i["genre"],i["bpm"],i["version"],j["title"],i["difficulties"])
                结果.append(单首曲目)
            elif 分类筛选 == i["genre"] and i["version"] == 版本筛选:
                单首曲目 = 返回歌曲json(i["id"],i["title"],i["artist"],i["genre"],i["bpm"],i["version"],版本筛选中文名,i["difficulties"])
                结果.append(单首曲目)
            elif 版本筛选 == None and 分类筛选 == None:
                for j in 曲目列表["versions"]:
                    if i["version"] == j["version"]:
                        单首曲目 = 返回歌曲json(i["id"],i["title"],i["artist"],i["genre"],i["bpm"],i["version"],j["title"],i["difficulties"])
                结果.append(单首曲目)
    #print(结果)
    结果2=[]
    for i in 结果:
        isappend=False
        if i["isappend"]==True:
            isappend=True
            continue
        if 难度筛选前==0 or 难度筛选后==0:
            continue
        for j in i["difficulties"]: 
            if 难度筛选前 <= j["level_value"] <= 难度筛选后 and isappend==False:
                isappend=True
                结果2.append(i)
        if isappend:
            i["isappend"]=True
    #print(结果2)
    if not 结果2==[]:
        结果=结果2
    logger.info(结果)
    return 结果
