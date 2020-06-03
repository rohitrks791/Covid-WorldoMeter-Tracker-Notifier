import requests
import bs4
from plyer import notification
import time
import datetime
import threading

def get_corona_detail_of_world():
    
    print(f"{'/'*20} COVID-19 Coronavirus Pandemic {'/'*20}")
    print("Covid-WorldoMeter-Tracker")
    
    url="https://www.worldometers.info/coronavirus/"
    
    page=requests.get(url)
    page1=requests.get(url)
    
    soup=bs4.BeautifulSoup(page.content,"html.parser")
    soup1=bs4.BeautifulSoup(page1.content,"html.parser")
    
    world_detail=soup.find_all(class_="maincounter-number")
    active_detail=soup1.find_all(class_="panel_front")

    data=[count.get_text()for count in world_detail]
    data1=[count.get_text() for count in active_detail]
    

    ntitle="COVID-19 Coronavirus Pandemic"
    print('Coronavirus Cases:',end="")
    print(data[0].strip())
    
    print("Active Cases:",end="")
    x=data1[0]
    z=x.find("Currently")
    print(data1[0][1:z].strip())
    
    print("Deaths:",end="")
    print(data[1].strip())
    print("Recovered:",end="")
    print(data[2].strip())

    ntext=f"\n Coronavirus-Cases: {data[0].strip()}\n Active-Cases: {data1[0][1:z].strip()}\n Deaths: {data[1].strip()}\n Recovered: {data[2].strip()}"
    notifyMe(ntitle,ntext)
    


def View_by_country():
    
    print("|| Track by Country ||")
    input_country=input("Enter Country:")
    url=f"https://www.worldometers.info/coronavirus/country/" + input_country
    
    page=requests.get(url)
    page1=requests.get(url)
    
    soup=bs4.BeautifulSoup(page.content,"html.parser")
    soup1=bs4.BeautifulSoup(page1.content,"html.parser")
    
    world_detail=soup.find_all(class_="maincounter-number")
    active_detail=soup1.find_all(class_="panel_front")
    

    
    data=[count.get_text()for count in world_detail]
    data1=[count.get_text() for count in active_detail]
    

    ntitle="COVID-19 Coronavirus Pandemic"
    print('Coronavirus Cases:',end="")
    print(data[0].strip())
    

    if input_country =="india":
            print("Active Cases:",end="")
            x=data1[0]
            z=x.find("Cases")
            print(data1[0][1:z].strip())
    
    print("Deaths:",end="")
    print(data[1].strip())
    print("Recovered:",end="")
    print(data[2].strip())
 
    if input_country =="india":
             ntext=f" Coronavirus-Cases: {data[0].strip()}\n Active-Cases: {data1[0][1:z].strip()}\n Deaths: {data[1].strip()}\n Recovered: {data[2].strip()}"
    
    else:
        ntext=f"Coronavirus-Cases: {data[0].strip()}\n Deaths: {data[1].strip()}\n Recovered: {data[2].strip()}"
    notifyMe(ntitle,ntext)
      

def notifyMe(title,message):
            notification.notify(
            title=title,
            message=message,
            app_icon ="D:\\rr.ico",
            timeout=100,
            )


if __name__ == "__main__":
    get_corona_detail_of_world()
    while True:
        option=input("\nView by country[Y/N]:")
        if option.lower()=='y':
            print(f"{'='*40}")
            View_by_country()
        else:
            ntitle="COVID-19 Coronavirus Pandemic" 
            ntext='\n"We Are In This Together-\nAnd We Will Get Through This,\nTogether."'
            notifyMe(ntitle,ntext)
            break
    print(f"{'='*40}")
    print('\n"We Are In This Together-\nAnd We Will Get Through This,\nTogether."')    
    print(f"{'='*40}")
