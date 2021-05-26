from pycricbuzz import Cricbuzz
matches=Cricbuzz().matches()
Match_Ids={}
import time
import pyttsx3 as r
engine = r.init()
engine.setProperty('rate',150)
from twilio.rest import Client
account_sid = 'twilio account sid'
auth_token = 'twilio authentication token'
client = Client(account_sid, auth_token)
z="/n"
count=0
wic=0
l=[]
def message(n):
    client.messages.create(
    body=n,
    from_='whatsapp:twilio number',
    to='whatsapp:Receiver Number')
def speak(text):
    engine.say(text)
    engine.runAndWait()
def available_Live_Matches():
    speak("Turning on the cricket bot")
    print("The Live Events Are:\n")
    speak("The live events are")
    count1=0
    for i in matches:
        if i['mchstate']=='inprogress' or i['mchstate']=="innings break":
            print("-> "+i['team1']['name'],end=" vs ")
            Match_Ids[i['team1']['name'].lower()]=i['id']
            Match_Ids[i['team1']['name'].lower()]=i['id']
            print(i['team2']['name'])
            Match_Ids[i['team2']['name'].lower()]=i['id']
            Match_Ids[i['team2']['name'].lower()]=i['id']
            speak(i['team1']['name']+" versus "+i['team2']['name'])
            print()
        else:
            count1+=1
    return count1
    #print(Match_Ids)
count1=available_Live_Matches()
if count1==len(matches):
    print("There is no live matches available")
    print()
    speak("There is no live matches available")
else:
    print("\nWhich Match Would You Like To Watch\n")
    speak("\nWhich Match Would You Like To Watch\n")
    match=input()
    user_match_id=Match_Ids.get(match.lower())
    msg=""
    for i in matches:
        if i['mchstate']=='inprogress' or i['mchstate']=="innings break":
            if i['id']==user_match_id:
                mat=i
    for i in matches:
        if i['id']==user_match_id:
            if i['mchstate']=='inprogress' or i['mchstate']=="innings break":
                if i['mchstate']=='innings break':
                    while True:
                        if i['mchstate']=='inprogress':
                            speak("Innings started")
                            message("Innings started")
                            break
                print("\nWelcome To "+i['team1']['name']+" vs "+i['team2']['name']+" "+i['type']+" Match")
                speak("Welcome To "+i['team1']['name']+" versus "+i['team2']['name']+" "+i['type']+" Match")
                msg+="Welcome To "+i['team1']['name']+" vs "+i['team2']['name']+" "+i['type']+" Match\n\n"
                print()
                print("Toss Events")
                speak("toss event")
                msg+="Toss Events :- "
                print()
                print(i['toss'])
                speak(i['toss'])
                msg+=i['toss']+"\n\n"
                print()
                print(i['team1']['name']+" Playing XI")
                speak(i['team1']['name']+" Playing XI")
                msg+=i['team1']['name']+" Playing XI\n"
                msg+="\n"
                print()
                l=i['team1']['squad']
                p_c=1
                for j in l:
                    msg+=str(p_c)+")"+j+"\n"
                    print(str(p_c)+")"+j)
                    speak(j)
                    p_c+=1
                print()
                msg+="\n"
                print(i['team2']['name']+" Playing XI")
                speak(i['team2']['name']+" Playing XI")
                msg+=i['team2']['name']+" Playing XI\n"
                msg+="\n"
                print()
                l=i['team2']['squad']
                p_c=1
                for j in l:
                    msg+=str(p_c)+")"+j+"\n"
                    print(str(p_c)+")"+j)
                    speak(j)
                    p_c+=1
                print()
                message(msg)
    for i in matches:
        if i['id']==user_match_id:
            if i['mchstate']=='inprogress' or i['mchstate']=="innings break":
                if i['mchstate']=='innings break':
                    while True:
                        if i['mchstate']=='inprogress':
                            speak("Innings started")
                            message("Innings started")
                            l=[]
                            break
                while True:
                    try:
                        c=Cricbuzz().livescore(i['id'])
                        if len(c)!=0:
                            c=Cricbuzz().livescore(i['id'])
                            com=Cricbuzz().commentary(i['id'])
                            a=com['commentary'][0]['comm']
                            if "<b>" in a:
                                com=a.replace("<b>","")
                                a=com
                            if "</b>" in a:
                                com=a.replace("</b>","")
                                a=com
                            if z[0] in a:
                                com=a.replace(z[0]," for ")
                                a=com
                            if "Ovs" in a:
                                com=a.replace("Ovs"," overs")
                                a=com
                            if " b " in a:
                                com=a.replace(" b "," Bowled by ")
                                a=com
                            if " c " in a:
                                com=a.replace(" c "," Caught by ")
                                a=com
                            score_details=c['batting']['score']
                            if score_details[len(score_details)-1]['wickets']=='10':
                                wic+=1
                                break
                            if score_details[len(score_details)-1]['overs'] not in l:
                                string=str(float(score_details[len(score_details)-1]['overs']))
                                if string[-1]=='0':
                                    batsman_details=c['batting']['batsman']
                                    cur=i['status'].replace("(","")
                                    cur=cur.replace(")","")
                                    client.messages.create(
                                    body=c['batting']['team']+" "+score_details[len(score_details)-1]['runs']+"/"+score_details[len(score_details)-1]['wickets']+"   "+score_details[len(score_details)-1]['overs']+" Overs"+"\n\n"+batsman_details[0]['name']+" "+batsman_details[0]['runs']+" ("+batsman_details[0]['balls']+")*\n"+batsman_details[1]['name']+" "+batsman_details[1]['runs']+" ("+batsman_details[1]['balls']+")"+"\n\n"+cur,
                                    from_='whatsapp:Twilio Number',
                                    to='whatsapp:Receiver Number')
                                l.append(score_details[len(score_details)-1]['overs'])
                                print(c['batting']['team'],end=" ")
                                score_details=c['batting']['score']
                                print(score_details[len(score_details)-1]['runs']+"/"+score_details[len(score_details)-1]['wickets'],score_details[len(score_details)-1]['overs']+" Overs")
                                speak("at the end of "+score_details[len(score_details)-1]['overs']+" overs"+c['batting']['team']+" "+score_details[len(score_details)-1]['runs']+" for "+score_details[len(score_details)-1]['wickets']+" in "+score_details[len(score_details)-1]['overs']+" Overs")
                                print()
                                a=a.replace("  "," ")
                                try:
                                    c1=a.split(",")
                                    if len(c)>1:
                                        print(c1[0],c1[1])
                                        speak(c1[0]+c1[1])
                                    if c1[1]==" FOUR" or c1[1]=="FOUR":
                                        message(c1[0]+c1[1]+"\n\n"+batsman_details[0]['name']+batsman_details[0]['runs']+" ("+batsman_details[0]['balls']+")*"+"\n"+batsman_details[1]['name']+batsman_details[1]['runs']+" ("+batsman_details[1]['balls']+")")
                                    elif c1[1]==" SIX" or c1[1]=="SIX":
                                        message(c1[0]+c1[1]+"\n\n"+batsman_details[0]['name']+batsman_details[0]['runs']+" ("+batsman_details[0]['balls']+")*"+"\n"+batsman_details[1]['name']+batsman_details[1]['runs']+" ("+batsman_details[1]['balls']+")")
                                    else:
                                        print("",end="")
                                    print()      
                                except:
                                    print("",end="")
                                batsman_details=c['batting']['batsman']
                                print(batsman_details[0]['name'],batsman_details[0]['runs']+" ("+batsman_details[0]['balls']+")*                     ",end=" ")
                                print(batsman_details[1]['name'],batsman_details[1]['runs']+" ("+batsman_details[1]['balls']+")")
                                print()
                        if mat['mchstate']!='inprogress' and mat['mchstate']!="innings break":
                            break
                    except:
                        if mat['mchstate']!='inprogress' and mat['mchstate']!="innings break":
                            break
                        elif score_details[len(score_details)-1]['overs'] not in l:
                            print("\nwicket")
                            speak("Wicket")
                            l.append(score_details[len(score_details)-1]['overs'])
                            message("wicket\n\n"+c['batting']['team']+" "+score_details[len(score_details)-1]['runs']+"/"+score_details[len(score_details)-1]['wickets']+"   "+score_details[len(score_details)-1]['overs']+" Overs")
                            print()
                            time.sleep(6)
                        else:
                            print("",end="")
                    time.sleep(5)
        else:
            if wic==1:
                break
            else:
                count+=1
if count==len(matches)-1:
    print(mat['status'])
    speak(mat['status'])
    message(mat['status'])
    print()
