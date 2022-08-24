import asyncio
from rubika import Client, methods, models, handlers, exceptions
import time
from random import choice as ch
import os.path
import logging
from re import findall
import sqlite3
from requests import get
import json
logging.basicConfig(level=logging.ERROR)

admins  = "CipherX"
Channel = "Yes_GNG"
status  = []
mute    = []

db = sqlite3.connect("CipherX.db")

mycursor = db.cursor()


async def main():
    async with Client(session="SATAN-LORD") as client:
        @client.on(handlers.MessageUpdates(models.raw_text))
        async def DIGI(event):
            me = await client.get_me()
            me_guid = me.user.user_guid
            admin = await client(methods.extras.GetObjectByUsername(username=admins))

            if os.path.exists("BOT"):
                mode = open("BOT").read()
            else:
                mode = "off"
            if mode == "on":
                if event.raw_text.startswith("ساعت") and event.type == "Group":
                    try:
                        url = json.loads(get(f"http://api.codebazan.ir/time-date/?json=en").text)
                        await event.reply(f"ساعت : {url['result']['time']}")
                    except:
                        pass
                if event.raw_text.startswith("جوک") and event.type == "Group":
                    try:
                        url = get("https://api.codebazan.ir/jok/").text
                        await event.reply(url)
                    except:
                        pass
                if event.raw_text.startswith("تاریخ") and event.type == "Group":
                    try:
                        url = json.loads(get(f"http://api.codebazan.ir/time-date/?json=en").text)
                        await event.reply(f"""
• 𝔗𝔦𝔐𝔢𝔖 𝔇𝔞𝔗𝔢 •

ساعت : {url['result']['time']}
تاریخ : {url['result']['date']}
فصل : {url['result']['fasl']}
ماه : {url['result']['mahname']}
روز : {url['result']['weekname']}

                    """)
                    except:
                        pass
                if event.raw_text.startswith("بیو") and event.type == "Group":
                    try:
                        url = get("https://api.codebazan.ir/bio/").text
                        await event.reply(url)
                    except:
                        pass
                if event.raw_text.startswith("/run") and event.type == "Group":
                    try:
                        count = status.count(event.object_guid)
                        if count == 1:
                                await event.reply("ربـات قـبلـا در ایـن گـروه فـعـال شـده اسـت •❌")
                        elif count == 0:
                            status.append(event.object_guid)
                            await event.reply("🔥 ربـات بـامـوفـقـیت در گـروه **فعال** شـد 🔥\n\n❌ مهم :\n• دقـت داشـتـه باشـید این ربـات رایگـان اسـت و فـقـط لـینـک پـاک مـیکـنـد •\n• برای دیدن دستورات سرگرمی دستور (سرگرمی) رو ارسال کنید •\n\n🔥👻 بـرای تـهـیـه ربـات حـرفـه ای و پـرسـرعـت بـه ایـدی زیـر مراجـعـه فـرمـایید :\n@CipherX")
                    except:
                        pass

                if event.object_guid in status:
                    try:

                        if event.find_keys(keys=['forwarded_from']):
                            try:
                                await event.delete_messages()
                            except:
                                pass
                        if event.raw_text.startswith("https://") or event.raw_text.startswith("http://"):
                            try:
                                await event.delete_messages()
                            except:
                                pass
                        za_1 = findall(r"https://rubika.ir/joing/\w{32}",event.raw_text)
                        za_2 = findall(r"https://rubika.ir/joinc/\w{32}",event.raw_text)
                        if za_1:
                            try:
                                await event.delete_messages()
                            except:
                                pass
                        if za_2:
                            try:
                                await event.delete_messages()
                            except:
                                pass
                    except:
                        pass

                if event.raw_text.startswith("/answer") and event.type == "Group":
                    try:
                        command = event.raw_text.replace("/answer", "").strip()
                        MyA = command.split(":")
                        mycursor.execute('INSERT INTO Answer (object_guid, matn, javab) VALUES (?, ?, ?)', (event.object_guid, MyA[0], MyA[1]))
                        db.commit()
                        await event.reply(f'• متن جدید با موفقیت افزوده شد •\nمتن :‌ {MyA[0]}\nجواب : {MyA[1]}')
                    except:
                        pass
                data_Answer = db.execute('SELECT * FROM Answer').fetchall()
                for OyA in data_Answer:
                    if event.raw_text == OyA[1] and event.object_guid in OyA[0]:
                        if event.type == "Group":
                            await event.reply(OyA[2])

                if event.raw_text.startswith("تنظیم لقب") and event.type == "Group":
                    try:
                        command = event.raw_text.replace("تنظیم لقب","").strip()
                        us = await client(methods.messages.GetMessagesByID(event.object_guid,message_ids=event.message.reply_to_message_id))
                        mycursor.execute('INSERT INTO Lghab (object_guid, object_target, matn) VALUES (?, ?, ?)', (event.object_guid, us.messages[0].author_object_guid, command))
                        db.commit()
                        await event.reply(f'لقب افزوده شد 🔥\nلقب : {command}')
                    except:
                        pass
                data_Lhgab = db.execute('SELECT * FROM Lghab').fetchall()
                for LgA in data_Lhgab:
                    if event.raw_text.startswith("بای") and event.message.author_object_guid in LgA[1]:
                        if event.type == "Group" and event.object_guid in LgA[0]:
                            await event.reply(f"بای {LgA[2]}")
                    if event.raw_text.startswith("خدافط") and event.message.author_object_guid in LgA[1]:
                        if event.type == "Group" and event.object_guid in LgA[0]:
                            await event.reply(f"خدافظ {LgA[2]}")
                    if event.raw_text.startswith("سلام") and event.message.author_object_guid in LgA[1]:
                        if event.type == "Group" and event.object_guid in LgA[0]:
                            await event.reply(f"سلام {LgA[2]}")
                    if event.raw_text.startswith("من اومدم") and event.message.author_object_guid in LgA[1]:
                        if event.type == "Group" and event.object_guid in LgA[0]:
                            await event.reply(f"خوش اومدی {LgA[2]}")
                    if event.raw_text.startswith("خوبی") and event.message.author_object_guid in LgA[1]:
                        if event.type == "Group" and event.object_guid in LgA[0]:
                            await event.reply(f"ت خوبی {LgA[2]}")
                    if event.raw_text.startswith("چخبر") and event.message.author_object_guid in LgA[1]:
                        if event.type == "Group" and event.object_guid in LgA[0]:
                            await event.reply(f"سلامتیت {LgA[2]}")
                    if event.raw_text.startswith("سلامتی") and event.message.author_object_guid in LgA[1]:
                        if event.type == "Group" and event.object_guid in LgA[0]:
                            await event.reply(f"سلامت باشی {LgA[2]}")
                    if event.raw_text.startswith("چطوری") and event.message.author_object_guid in LgA[1]:
                        if event.type == "Group" and event.object_guid in LgA[0]:
                            await event.reply(f"خوبم ت خوبی {LgA[2]}")
                    if event.raw_text.startswith("حصلم سرفته") and event.message.author_object_guid in LgA[1]:
                        if event.type == "Group" and event.object_guid in LgA[0]:
                            await event.reply(f"چرا  {LgA[2]}")
                    if event.raw_text.startswith("حسلم سرفته") and event.message.author_object_guid in LgA[1]:
                        if event.type == "Group" and event.object_guid in LgA[0]:
                            await event.reply(f"چرا  {LgA[2]}")
                    if event.raw_text.startswith("هعی") and event.message.author_object_guid in LgA[1]:
                        if event.type == "Group" and event.object_guid in LgA[0]:
                            await event.reply(f"نکش  {LgA[2]}")
                    if event.raw_text.startswith("من برم") and event.message.author_object_guid in LgA[1]:
                        if event.type == "Group" and event.object_guid in LgA[0]:
                            await event.reply(f"برو بسلامت  {LgA[2]}")


                if event.raw_text.startswith("حذف لقب") and event.type == "Group":
                    try:
                        command = event.raw_text.replace("حذف لقب","").strip()
                        us = await client(methods.messages.GetMessagesByID(event.object_guid,message_ids=event.message.reply_to_message_id))
                        mycursor.execute('DELETE from Lghab WHERE object_target = "%s" ' %us.messages[0].author_object_guid)
                        db.commit()
                        await event.reply(f'لقب با موفقیت حذف شد 🔥')
                    except:
                        pass
                if event.raw_text.startswith("/delanswer") and event.type == "Group":
                    try:
                        command = event.raw_text.replace("/delanswer", "").strip()
                        mycursor.execute(f'DELETE from Answer WHERE matn = "%s" ' %command)
                        db.commit()
                        await event.reply(f'• متن شما با موفقیت حذف شد •\nمتن : {command}')
                    except:
                        pass
                if event.raw_text.startswith("سرگرمی") and event.type == "Group":
                    try:
                        await event.reply(f"""
دستورات سرگرمی :

• کی با کی رل میزنه 👻✨

• کی منو دوست داره 👻✨

• کی با من رل میزنه 👻✨

• بیو 👻✨

• جوک 👻✨

• ساعت 👻✨

• تاریخ 👻✨



تنظیم لقب 🔥

• روی فرد مورد نظر ریپلی کنید و مانند دستور زیر عمل کنید •


تنظیم لقب [ لقب ] •



حذف لقب 🔥

• روی فرد مورد نظر ریپلی کنید و مانند دستور زیر عمل کنید •


حذف لقب •



افزودن متن به ربات 🔥

• مانند دستور زیر عمل کنید •

• /answer CIPHER-X:Salam CiperX


جای CIPHER-X متنی که میخواهید کاربر میخواهد بگد

و جای Salam CipherX جواب خود را بنویسید



حذف متن 🔥

• مانند دستور زیر عمل کنید •

• /delanswer CIPHER-X

جای CIPHER-X متنی که میخواهید پاک شود رو بزارید

متنی که قبلا اضافه کردید




**RUBIKA**

@CipherX
                """)
                    except:
                        pass
                if event.raw_text.startswith("/ban")and event.type == "Group":
                    acsess = await client(methods.groups.GetGroupAdminMembers(group_guid= event.object_guid ,start_id=None))
                    for admins_group in acsess.in_chat_members:
                        if event.message.author_object_guid in admins_group.member_guid:
                            command = event.raw_text.replace("/ban","").strip()
                            ids = command.replace("@","").strip()
                            usernames = await client(methods.extras.GetObjectByUsername(username=ids))
                            await client(methods.groups.BanGroupMember(event.object_guid,ids.user.user_guid))
                            await event.send_message(event.object_guid,message=f'🔥 کاربر {usernames.user.first_name} \n• از گروه بن شد •')

                if event.raw_text.startswith("/lock")and event.type == "Group":
                    acsess = await client(methods.groups.GetGroupAdminMembers(group_guid= event.object_guid ,start_id=None))
                    for admins_group in acsess.in_chat_members:
                        if event.message.author_object_guid in admins_group.member_guid:
                            await client(methods.groups.SetGroupDefaultAccess(event.objec_guid,access_list=None))
                            await client.send_message("🔥 گروه قفل شد 🔥")

                if event.raw_text.startswith("/unlock")and event.type == "Group":
                    acsess = await client(methods.groups.GetGroupAdminMembers(group_guid= event.object_guid ,start_id=None))
                    for admins_group in acsess.in_chat_members:
                        if event.message.author_object_guid in admins_group.member_guid:
                            await client(methods.groups.SetGroupDefaultAccess(event.objec_guid,access_list=["AddMember","SendMessages"]))
                            await client.send_message("🔥 گروه باز شد 🔥")

                if event.raw_text.startswith("/mute")and event.type == "Group":
                    acsess = await client(methods.groups.GetGroupAdminMembers(group_guid= event.object_guid ,start_id=None))
                    for admins_group in acsess.in_chat_members:
                        if event.message.author_object_guid in admins_group.member_guid:
                            command = event.raw_text.replace("/mute","").strip()
                            ids = command.replace("@","").strip()
                            usernames = await client(methods.extras.GetObjectByUsername(username=ids))
                            mutecount = mute.count(usernames.user.user_guid)
                            if mutecount == 1:
                                await event.reply(f"❌ کاربر {usernames.user.first_name}\n• قبلا میوت بود •")
                            elif mutecount == 0:
                                mute.append(usernames.user.user_guid)
                                await client.send_message(event.object_guid,message=f'🔥 کاربر {usernames.user.first_name}\n• میوت شد •')

                if event.raw_text.startswith("/unmute")and event.type == "Group":
                    acsess = await client(methods.groups.GetGroupAdminMembers(group_guid= event.object_guid ,start_id=None))
                    for admins_group in acsess.in_chat_members:
                        if event.message.author_object_guid in admins_group.member_guid:
                            command = event.raw_text.replace("/umute","").strip()
                            ids = command.replace("@","").strip()
                            usernames = await client(methods.extras.GetObjectByUsername(username=ids))
                            mute.remove(usernames.user.user_guid)
                            await client.send_message(event.object_guid,message=f'🔥 کاربر {usernames.user.first_name}\n• حذف میوت شد •')
                if event.raw_text.startswith("ربات") or event.raw_text.startswith("بات"):
                    try:
                        print(f"\033[32m{event.object_guid} | \033[37m {event.raw_text}")
                        await event.reply(ch(['جونم ? ', 'بفرما', 'جون دلم؟‌', 'بگو', 'چی میخوای؟', 'زود بگو کارتو', 'خستم کردی دگ چیه ؟','هوم؟','چیه نفصم ؟','جوندلم خشگله','چیههههههه؟','نمودی مارو بگو','هن ؟','هوف باز ت اومدی']))
                    except:
                        pass
                if event.message.author_object_guid in mute:
                    try:
                        await event.delete_messages()
                    except:
                        pass
                if event.raw_text.startswith("کی با کی رل میزنه") or event.raw_text.startswith("کی با کی رل میزنع"):
                    try:
                        if event.type == "Group":
                            dialogs = await client(methods.groups.GetGroupAllMembers(group_guid= event.object_guid ,search_text=None, start_id=None))
                            for i in range(2):
                                random = ch(dialogs.in_chat_members)
                                random1 = ch(dialogs.in_chat_members)
                                name = random.first_name
                                name1 = random1.first_name
                            if name == name1:
                                await event.delete_messages()
                            else:
                                await event.reply(f"""
این [ {name}]({random.member_guid})

با این [ {name1}]({random1.member_guid})

رل میزنه ❤️🗿
                            """)
                    except:
                        pass
                if event.raw_text.startswith("کی با من رل میزنه") or event.raw_text.startswith("کی با من رل میزنع"):
                    try:
                        if event.type == "Group":
                            dialogs = await client(methods.groups.GetGroupAllMembers(group_guid= event.object_guid ,search_text=None, start_id=None))
                            random = ch(dialogs.in_chat_members)
                            name = random.first_name
                            await event.reply(f"این [ {name}]({random.member_guid}) باهات رل میزنه ❤️✨")
                    except:
                        pass
                if event.raw_text.startswith("کی منو دوست داره") or event.raw_text.startswith("با منو دوست دارع"):
                    try:
                        if event.type == "Group":
                            dialogs = await client(methods.groups.GetGroupAllMembers(group_guid= event.object_guid ,search_text=None, start_id=None))
                            random = ch(dialogs.in_chat_members)
                            name = random.first_name
                            await event.reply(f"این [ {name}]({random.member_guid}) دوست داره ❤️✨")
                    except:
                        pass
                if event.raw_text and event.type == "User" and not event.message.author_object_guid == admin.user.user_guid:
                    if event.raw_text == "/start" and not event.message.author_object_guid == admin.user.user_guid:
                        try:
                            await client.send_message(event.object_guid,file_inline="bot.png",message=f"""
ســـلام کاربـــر گرامـــی👋🏻🌹

بـه ربــات 𝖨𝖮 𝖣𝖨𝖦𝖨 خـوش آمـدید

بـرای افـزودن ربــات بـه گـروه خـود از دسـتـور

/help

اسـتـفـاده کنـیـد

مـوفـق بــاشـید ✌️
            """)
                        except:
                            pass
                    elif event.raw_text == "/help":
                        await client.send_message(event.object_guid,message=f"""
بـرای عـضو شـدن ربــات بـه گـروهـتـون از دسـتور جـویـن اسـتفـاده کـنـید 🔥

مـانـنـد‌:

/join لـینـک گـروه 👻


🔰 پـشـتـیـبـانـی:

**RUBIKA** 👇🏻\n@CipherX

                                """)
                    elif event.raw_text.startswith("/join"):
                        try:
                            link = findall(r"https://rubika.ir/joing/\w{32}",event.raw_text)
                            if link:
                                for i in link:
                                    global Check_Join
                                    Check_Join = await client(methods.groups.GroupPreviewByJoinLink(link=i))

                                    if Check_Join.has_joined == True:
                                        await event.reply("درحـال حـاضـر تـو گـروه هـسـتـم ❤️😐")
                                    if Check_Join.has_joined == False:
                                        group = await client(methods.groups.JoinGroup(link=i))
                                        await client.send_message(event.object_guid,message=f"""
ربـات بـا موفـقیت عـضـو گـروه {group.group.group_title} شـد 🔥👇🏻


بـرای اجـرای درسـت ربـات ان را ادمـین کنـید •

بـرای اطـلاع از وضـعیت ربـات •

•‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍ ‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌کانال رو چک کنیـב  • 🔥👻

🔰 @Yes_GNG


• مـشکـلی بـود پـی وی بگید 🗿❤️

**RUBIKA** 👇🏻

@CipherX
                                        """)
                                        await client.send_message(group.group.group_guid,message=f"""
ربـات بـامـوفـقـیت در گـروه {group.group.group_title} عـضـو شـد 🔥👇🏻


بـرای اجـرای ربـات دسـتـور 🔰

• /run  ‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌

رو ارسـال کـنـید •

برای دیدن لیست سرگرمی ها 🔰

• سرگرمی



❌ نکته :

• ادمینم نکنی نمیتونم جواب بدم •




• موفق باشید 𝗖𝗜𝗣𝗛𝗘𝗥-𝙓 🔥👻
""")
                        except:
                            pass
                    else:
                        await client.send_message(event.object_guid,file_inline="start.jpg",message=f"""
 🔥👻 دوسـت داری گـروهـت یـه ربـات هـوشـمنـد داشـتـه بـاشـه ؟\n\n• اونـم بـه صـورت کامـلا رایـگـان •\nرو پیام زیر کلیک کن\n• /start  \nبـرای هـمـایـت از مـا و دریـافـت وضـعـیـت ربـات
در کـانـال زیـر جـویـن شـویـد\n\n• @{Channel}\n\n🔰 پـشـتـیـبـانـی:\n**RUBIKA** 👇🏻\n@CipherX

                            """)
            else:
                pass

            if event.raw_text.startswith(".bot") and event.type == "User":
                if event.message.author_object_guid in admin.user.user_guid:
                    try:
                        CyA = event.raw_text.replace(".bot","").strip()
                        if CyA == "on":
                            await event.reply("ادمین بات شناسایی شد ✅\n\n• ربات روشن شد •")
                            open("BOT","w").write("on")
                        elif CyA == "off":
                            await event.reply("ادمین بات شناسایی شد ✅\n\n• ربات خاموش شد •")
                            open("BOT","w").write("off")
                            dialogs = await client(methods.chats.GetChats(start_id=None))
                            if dialogs.chats:
                                for index, dialog in enumerate(dialogs.chats, start=1):
                                    if methods.groups.SendMessages in dialog.access:
                                        await client.send_message(dialog.object_guid,message=f"[ربات در دست تعمیر است ....]({me_guid})")
                        else:
                            await event.reply("لطفا دستور رو درست وارد کنید ❌")
                    except:
                        pass
                else:
                    await client.send_message(event.object_guid,message="شما به عنوان ادمین ربات شناسایی نشدید ❌")

            elif event.raw_text == "امار" and event.type == "User":
                if event.message.author_object_guid in admin.user.user_guid:
                    try:
                        tedad = len(status)
                        await event.reply(f"""🔰 امار فعلی ربات :‌ {tedad}""")
                    except:
                        pass

        await client.run_until_disconnected()

asyncio.run(main())
