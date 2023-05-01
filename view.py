import requests

#MADE WITH ♥ BY SHRUM#0002

def uwu():
    channel = input("Enter channel: ")
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US',
        'Client-Id': 'kimne78kx3ncx6brgo4mv6wki5h1ko',
        'Client-Session-Id': 'cda1771eaa8aff55',
        'Client-Version': '52171a49-ed35-40a2-843a-48bfcd4610fe',
        'Connection': 'keep-alive',
        'Content-Type': 'text/plain;charset=UTF-8',
        'Origin': 'https://www.twitch.tv',
        'Referer': 'https://www.twitch.tv/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
        'X-Device-Id': 'prHuujtFwE2eDrQj5EFBHdHDUX8kJTsG',
        'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {"operationName":"UseViewCount","variables":{"channelLogin":channel},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"00b11c9c428f79ae228f30080a06ffd8226a1f068d6f52fbc057cbde66e994c2"}}}

    response = requests.post("https://gql.twitch.tv/gql", headers=headers, json=data)
    try:
        livecount = response.json()["data"]["user"]["stream"]["viewersCount"]
        print(livecount)
    except:
        print("User is not streaming..")


uwu()
