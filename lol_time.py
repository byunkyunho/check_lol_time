import requests
from bs4 import BeautifulSoup
import datetime
import pyautogui

while True:
    all_time = [0,0,0]
    today = int(datetime.datetime.now().strftime('%d'))
    game_list = []
    today_game_list = []
    time_list = []
    player = pyautogui.prompt(text="소환사를 입력하세요.", title="오롤몇")
    if player == None or "":
        break
    first_parse = BeautifulSoup(requests.get("https://www.op.gg/summoner/userName={}".format(player.strip())).text, "html.parser").find("div", class_="GameItemList")
    if first_parse == None:
        pyautogui.alert(text="존재하지 않는 소환사입니다.", button="확인")
    else:
        game_list = first_parse.find_all("div", class_ = "GameItemWrap")
        for game in game_list:
            if today == int(game.find('span', class_="_timeago _timeCount").text.split(" ")[0].split("-")[2]):
                game_time = game.find("div", class_="GameLength").text.split(" ")
                time_list.append([int(game_time[0].split("m")[0]), int(game_time[1].split("s")[0])])

        for time in time_list:
            all_time[1] += time[0]
            all_time[2] += time[1]

        all_time[1] += all_time[2] // 60
        all_time[0] = all_time[1] // 60 
        all_time[2] = all_time[2] % 60
        all_time[1] = all_time[1] % 60
        if all_time == [0,0,0]:
            pyautogui.alert(text="\n오늘 게임을 하지 않았습니다.\n".format(all_time[0], all_time[1], all_time[2]), button="확인")
        else:
            pyautogui.alert(text="\n오늘 {}시간 {}분 {}초동안 게임을 했습니다.\n".format(all_time[0], all_time[1], all_time[2]), button="확인")
    

