"""
Hello Skids,
Today is Your Lucky Day!

I will Let You Take Whatever You want from This Code.
If You Want To Know How i Made Any of The Functions
Or How You Can implement Them Into Your Script
Just Join The Discord and Message anyone with The Highest Role!
https://discord.gg/VHtvszBAx3

P.S I dont Recommend You Skidding!
Its a bad crime and can get you into serious trouble.
You Should Only Skid My Projects Since I allow People Todo So!

People Spend Hours Coding These Scripts Just For You!
Not To Steal The Code But For You To Use The Service.
Some People Like Oli (Another Lobbybot Owner https://partybot.net)
had to put a really alarming message for the skids because he wanted
his work to be private!
I aspire to be like Gomashio(https://github.com/gomashio1596) or pdf(https://github.com/pdf114514)
where i help people in terms of coding. Or any technical problems.
Gomashio or PDF if you see this keep up the great work <3


I Spent Alot Of Time On This Bot So if You Could Support Me By Joining I would appreciate it!
    - Pirxcy
""" 

import os
import fortnitepy
from fortnitepy.ext import commands
import requests
import json
import time
import asyncio
import base64
import BenBotAsync
import sanic
from sanic.exceptions import NotFound

app = sanic.Sanic("PirxcyLobbyBot")
pirxcy = """
██████╗ ██╗██████╗ ██╗  ██╗ ██████╗██╗   ██╗
██╔══██╗██║██╔══██╗╚██╗██╔╝██╔════╝╚██╗ ██╔╝
██████╔╝██║██████╔╝ ╚███╔╝ ██║      ╚████╔╝ 
██╔═══╝ ██║██╔══██╗ ██╔██╗ ██║       ╚██╔╝  
██║     ██║██║  ██║██╔╝ ██╗╚██████╗   ██║   
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝   ╚═╝   
"""
pdf = """
██████╗ ██████╗ ███████╗
██╔══██╗██╔══██╗██╔════╝
██████╔╝██║  ██║█████╗  
██╔═══╝ ██║  ██║██╔══╝  
██║     ██████╔╝██║     
╚═╝     ╚═════╝ ╚═╝     
"""
gomashio = """
 ██████╗  ██████╗ ███╗   ███╗ █████╗ ███████╗██╗  ██╗██╗ ██████╗ 
██╔════╝ ██╔═══██╗████╗ ████║██╔══██╗██╔════╝██║  ██║██║██╔═══██╗
██║  ███╗██║   ██║██╔████╔██║███████║███████╗███████║██║██║   ██║
██║   ██║██║   ██║██║╚██╔╝██║██╔══██║╚════██║██╔══██║██║██║   ██║
╚██████╔╝╚██████╔╝██║ ╚═╝ ██║██║  ██║███████║██║  ██║██║╚██████╔╝
 ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝ ╚═════╝ 
"""
pirxcy2 = """
 __     __       __      
|__) | |__) \_/ /  ` \ / 
|    | |  \ / \ \__,  |  
                         
"""

def intro():
  os.system('cls||clear')
  print(gomashio)
  time.sleep(1)
  os.system('cls||clear')
  print(pdf)
  time.sleep(1)
  os.system('cls||clear')
  print(pirxcy)
  time.sleep(1.3)
  os.system('cls||clear')
  print(pirxcy2)
  

loop = asyncio.get_event_loop()


def keep_alive():
    url = f'https://{os.getenv("REPL_SLUG")}.{os.getenv("REPL_OWNER")}.repl.co'
    requests.post('https://pinger.pirxcy.xyz/api/add', json={'url': url})
    print("Posted URL To PirxcyPinger!")
    
def reset_config():
    try:
        os.remove("settings.json")
        print("Removed Current Settings.json")
    except:
        print("Settings.json Not Found...\nWriting New File") 
    try:
      f = open("settings.json", "x")   
    except FileExistsError:
      print("Created Settings.json")
    print("Restoring Settings.json")
    with open("settings.json", "w") as f:
      data = requests.get("https://raw.githubusercontent.com/PirxcyFinal/PirxcyBotV2/main/settings.json").text.replace('“','"').replace('”','"')
      f.write(data)
      print("Restored Settings.json")
      f.close()

try:
  os.listdir("settings.json")
except FileNotFoundError:
  reset_config()
  exit(1)
except:
  None

with open('settings.json') as f:
  try:
      data = json.load(f)
  except json.decoder.JSONDecodeError:
      print('Your Settings in The Settings.json wasnt Modified Correctly\nRestoring Now!')
      reset_config()
      exit(1)


#Credit AtomicXYZ For The Code SimpleDeviceAuthHandler
#https://github.com/AtomicXYZ/EpicEndpoints/

class SimpleDeviceAuthHandler:

    def __init__(self) -> None:
        headers = {
            'content-type': "application/x-www-form-urlencoded",
            'authorization': "basic YjA3MGYyMDcyOWY4NDY5M2I1ZDYyMWM5MDRmYzViYzI6SEdAWEUmVEdDeEVKc2dUIyZfcDJdPWFSbyN+Pj0+K2M2UGhSKXpYUA==",
        }
        response = requests.request("POST","https://account-public-service-prod.ol.epicgames.com/account/api/oauth/token", data="grant_type=client_credentials", headers=headers)
        self.access_token = json.loads(response.text)['access_token']
        self.device_code = None

    def login(self):
        url2 = "https://account-public-service-prod03.ol.epicgames.com/account/api/oauth/deviceAuthorization"

        querystring2 = {"prompt":"login"}

        payload2 = "prompt=promptType"
        headers2 = {
            'content-type': "application/x-www-form-urlencoded",
            'authorization': f"bearer {self.access_token}",
            }

        response2 = requests.request("POST", url2, data=payload2, headers=headers2, params=querystring2)

        url = response2.json()['verification_uri_complete']
        self.device_code = response2.json()['device_code']

        return url

    def device_auth(self):
        device_auths = {}

        if self.device_code == None:
            return {}
        else:
            try:
                deviceCode = self.device_code
                clientToken = "NTIyOWRjZDNhYzM4NDUyMDhiNDk2NjQ5MDkyZjI1MWI6ZTNiZDJkM2UtYmY4Yy00ODU3LTllN2QtZjNkOTQ3ZDIyMGM3"
                url3 = "https://account-public-service-prod.ol.epicgames.com/account/api/oauth/token"
                payload3 = f"grant_type=device_code&device_code={deviceCode}"
                headers3 = {
                    'content-type': "application/x-www-form-urlencoded",
                    'authorization': f"basic {clientToken}",
                    }
                status = 0
                time_start = time.time()
                while(status != 200):
                    response3 = requests.request("POST", url3, data=payload3, headers=headers3)
                    status = response3.status_code
                    time_now = time.time()
                    if(time_now-time_start >= 600):
                        return {}
                    time.sleep(1)
                self.device_code = None
                data = response3.json()

                device_auths['display_name'] = data['displayName']

                account_id = data['account_id']
                access_token = data['access_token']

                url = f"https://account-public-service-prod.ol.epicgames.com/account/api/public/account/{account_id}/deviceAuth"
                headers = {
                    'content-type': "application/json",
                    'authorization': f"bearer {access_token}",
                    }
                response = requests.request("POST", url, headers=headers)
                device_details = response.json()

                device_auths['device_id'] = device_details['deviceId']
                device_auths['account_id'] = device_details['accountId']
                device_auths['secret'] = device_details['secret']

                return device_auths
            except:
                return {}

def getDisplayName(account_id, access_token):
  url = "https://account-public-service-prod.ol.epicgames.com/account/api/public/account/"

  querystring2 = {"accountId":account_id}

  headers = {
        'content-type': "application/json",
        'authorization': f"bearer {access_token}",
        }

  response = requests.request("GET", url, headers=headers,params=querystring2)

  data = json.loads(response.text)
  print(data)
  return data[0]['displayName']

def getAccessToken(clientId, secret):
    id = clientId + ":" + secret
    clientToken = base64.b64encode(bytes(id, 'utf-8'))
    clientToken = clientToken.decode("utf-8")

    url = "https://account-public-service-prod.ol.epicgames.com/account/api/oauth/token"

    payload = "grant_type=client_credentials"
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'authorization': f"basic {clientToken}",
        }

    response = requests.request("POST", url, data=payload, headers=headers)

    data = json.loads(response.text)

    access_token = data['access_token']
    expire = data['expires_in']

    return access_token

def getDeviceCode(access_token):
    url2 = "https://account-public-service-prod03.ol.epicgames.com/account/api/oauth/deviceAuthorization"

    querystring2 = {"prompt":"login"}

    payload2 = "prompt=promptType"
    headers2 = {
        'content-type': "application/x-www-form-urlencoded",
        'authorization': f"bearer {access_token}",
        }

    response2 = requests.request("POST", url2, data=payload2, headers=headers2, params=querystring2)

    data2 = json.loads(response2.text)
    print(data2)

    return data2

def deviceCodeData(deviceCode, clientId, secret):

    id = clientId + ":" + secret
    clientToken = base64.b64encode(bytes(id, 'utf-8'))
    clientToken = clientToken.decode("utf-8")

    url3 = "https://account-public-service-prod.ol.epicgames.com/account/api/oauth/token"

    payload3 = f"grant_type=device_code&device_code={deviceCode}"
    headers3 = {
        'content-type': "application/x-www-form-urlencoded",
        'authorization': f"basic {clientToken}",
        }

    response3 = requests.request("POST", url3, data=payload3, headers=headers3)

    data3 = json.loads(response3.text)

    return data3

def getDeviceAuth(access_token,account_id):
  url = f"https://account-public-service-prod.ol.epicgames.com/account/api/public/account/{account_id}/deviceAuth"

  headers = {
      'content-type': "application/json",
      'authorization': f"bearer {access_token}",
      }

  response = requests.request("POST", url, headers=headers)

  data = json.loads(response.text)

  return data

#I would Make it Async But Thats wayyy To Much Effort For Me.
#Lesson From Pirxcy Take What You Are Given With.

#Login
handler = SimpleDeviceAuthHandler() #Handler
loginurl = handler.login() #URL To Sign in With
intro()
print("Sign in With\n" + loginurl)
device_auth_details = handler.device_auth() #Script Continues Once They Have Logged in!
device = device_auth_details['device_id']
account = device_auth_details['account_id']
secret = device_auth_details['secret']
with open("settings.json", "r+") as file:
  datas = json.load(file)
  datas.update({"device_id": device})
  datas.update({"account_id": account})
  datas.update({"secret": secret})
  file.seek(0)
  json.dump(datas, file, indent=2)
  file.close()

client = commands.Bot(
	command_prefix=data['prefix'],
	auth=fortnitepy.DeviceAuth(
	device_id=device,
	account_id=account,
	secret=secret,
	ios_token="NTIyOWRjZDNhYzM4NDUyMDhiNDk2NjQ5MDkyZjI1MWI6ZTNiZDJkM2UtYmY4Yy00ODU3LTllN2QtZjNkOTQ3ZDIyMGM3"
	)
)

@app.route('/loadout')
async def b_loadout(request):
	return sanic.response.json({
			"skin": client.party.me.outfit,
			"emote": client.party.me.emote,
			"backpack": client.party.me.backpack,
			"pickaxe": client.party.me.pickaxe,
			"last_login": str(client.user.last_login),
			"party_count": str(client.party.member_count),
			"email": client.user.email,
			"user_name": client.user.display_name,
			"join_message": data['join_message'],
			"status": data['status'],
			"id": os.getenv("REPL_ID")
	})

@app.route('/status', methods=['POST'])
async def change_status(request):
	status = request.form.get('STATUS')
	with open("settings.json", "r+") as file:
			datas = json.load(file)
	for element in data:
			element.pop('status', None)
	datas.update({'status': status})
	file.seek(0)
	json.dump(datas, file, indent=2)
	id = os.getenv("REPL_ID")
	return sanic.response.redirect(f"https://lobbybot.pirxcy.xyz/custombot/{id}/commands")

@app.route('/join_message', methods=['POST'])
async def change_join_message(request):
	status = request.form.get('JOIN_MESSAGE')
	with open("settings.json", "r+") as file:
			datas = json.load(file)
	for element in data:
			element.pop('join_message', None)
	datas.update({'join_message': status})
	file.seek(0)
	json.dump(datas, file, indent=2)
	id = os.getenv("REPL_ID")
	return sanic.response.redirect(f"https://lobbybot.pirxcy.xyz/custombot/{id}/commands")


@app.route('/skin', methods=['POST'])
async def skin(request):
	id = os.getenv("REPL_ID")
	item = request.form.get('OUTFIT')
	try:
			cosmetic = await BenBotAsync.get_cosmetic(
			lang="en",
			searchLang="en",
			matchMethod="contains",                
			name=item,
			backendType="AthenaCharacter"
			)
	except:
			return sanic.response.redirect(f"https://lobbybot.pirxcy.xyz/custombot/{id}/commands")
	await client.party.me.set_outfit(asset=cosmetic.id)
	return sanic.response.redirect(f"https://lobbybot.pirxcy.xyz/custombot/{id}/commands")


@app.route('/emote', methods=['POST'])
async def emote(request):
		id = os.getenv("REPL_ID")
		item = request.form.get('EMOTE')
		try:
				cosmetic = await BenBotAsync.get_cosmetic(
						lang="en",
						searchLang="en",
						matchMethod="contains",
						name=item,
						backendType="AthenaDance"
				)
				await client.party.me.clear_emote()
				await client.party.me.set_emote(asset=cosmetic.id)
				return sanic.response.redirect(f"https://lobbybot.pirxcy.xyz/custombot/{id}/commands")
		except:
				return sanic.response.redirect(f"https://lobbybot.pirxcy.xyz/custombot/{id}/commands")
						
@app.route('/eid', methods=['POST'])
async def eid(request):
		id = os.getenv("REPL_ID")
		item = request.form.get('EMOTE')
		await client.party.me.clear_emote()
		await client.party.me.set_emote(asset=item)
		return sanic.response.redirect(f"https://lobbybot.pirxcy.xyz/custombot/{id}/commands")


@app.route('/cid', methods=['POST'])
async def cid(request):
		id = os.getenv("REPL_ID")
		item = request.form.get('OUTFIT')
		await client.party.me.clear_emote()
		await client.party.me.set_outfit(asset=item)
		return sanic.response.redirect(f"https://lobbybot.pirxcy.xyz/custombot/{id}/commands")

@app.route('/pickaxe', methods=['POST'])
async def pickaxe(request):
		id = os.getenv("REPL_ID")
		item = request.form.get('PICKAXE')
		try:
				cosmetic = await BenBotAsync.get_cosmetic(
						lang="en",
						searchLang="en",
						matchMethod="contains",
						name=item,
						backendType="AthenaPickaxe"
				)
				await client.party.me.set_pickaxe(asset=cosmetic.id)
				return sanic.response.redirect(f"https://lobbybot.pirxcy.xyz/custombot/{id}/commands")
		except:            
				return sanic.response.redirect(f"https://lobbybot.pirxcy.xyz/custombot/{id}/commands")        
								
@app.route('/backpack', methods=['POST'])
async def backpack(request):
	id = os.getenv("REPL_ID")
	item = request.form.get('BACKPACK')
	try:
			cosmetic = await BenBotAsync.get_cosmetic(
					lang="en",
					searchLang="en",
					matchMethod="contains",
					name=item,
					backendType="AthenaBackpack"
			)
			await client.party.me.set_pickaxe(asset=cosmetic.id)
			return sanic.response.redirect(f"https://lobbybot.pirxcy.xyz/custombot/{id}/commands")        
	except:
			return sanic.response.redirect(f"https://lobbybot.pirxcy.xyz/custombot/{id}/commands")
						

@app.route('/level', methods=['POST'])
async def level(request):
	id = os.getenv("REPL_ID")
	try:
		level = int(request.form.get('LEVEL'))
	except:
		return sanic.response.redirect(f"https://lobbybot.pirxcy.xyz/custombot/{id}/commands")
	await client.party.me.set_banner(season_level=level)
	return sanic.response.redirect(f"https://lobbybot.pirxcy.xyz/custombot/{id}/commands")

@client.event
async def event_ready():
	await app.create_server(
			host='0.0.0.0',
			port=80,
			return_asyncio_server=True,
			debug=True,
			backlog=100
	)
	print("Connecting To Pinger")
	keep_alive()
	print("Connected")
	if data['status']:
			await client.set_presence(data['status']) 
	print(f'Launched {client.user.display_name}\nConnecting To Dashboard')
	print('Connected To Dash')

@client.event
async def event_friend_request(request):
	await request.accept()

@client.event
async def event_party_member_join(member):
	if data['join_message']:
		await client.party.send(data['join_message'])

#commands
		
@client.command()
async def skin(ctx, *, item = None):
	if item is None:
		i = data['prefix']
		await ctx.send(f'No skin was given, try: {i}skin IKONIK')
	else:
		try:
			cosmetic = await BenBotAsync.get_cosmetic(
					lang="en",
					searchLang="en",
					matchMethod="contains",                
					name=item,
					backendType="AthenaCharacter"
				)
			await client.party.me.set_outfit(asset=cosmetic.id)
			await ctx.send(f'Skin set to: {cosmetic.name}')
		except BenBotAsync.exceptions.NotFound:
			await ctx.send(f'Could not find a skin named: {item}')

@client.command()
async def emote(ctx, *, item = None):
		if item is None:
				i = data['prefix']
				await ctx.send(f'Invalid Item\nTry:\n {i}emote floss')
		else:
				try:
						cosmetic = await BenBotAsync.get_cosmetic(
								lang="en",
								searchLang="en",
								matchMethod="contains",
								name=item,
								backendType="AthenaDance"
						)
						await client.party.me.clear_emote()
						await client.party.me.set_emote(asset=cosmetic.id)
						await ctx.send(f'Dance set to: {cosmetic.name}')
				except BenBotAsync.exceptions.NotFound:
						await ctx.send(f'Could not find a Dance named: {item}')
						
@client.command()
async def pickaxe(ctx, *, item = None):
		if item is None:
				i = data['prefix']
				await ctx.send(f'Invalid Item\nTry:\n{i}pickaxe Default Pickaxe')
		else:
				try:
						cosmetic = await BenBotAsync.get_cosmetic(
								lang="en",
								searchLang="en",
								matchMethod="contains",
								name=item,
								backendType="AthenaPickaxe"
						)
						await client.party.me.set_pickaxe(asset=cosmetic.id)
						await ctx.send(f'Axe set to: {cosmetic.name}')
				except BenBotAsync.exceptions.NotFound:
						await ctx.send(f'Could not find a Axe named: {item}')            
								
@client.command()
async def backpack(ctx, *, item = None):
		if item is None:
				i = data['prefix']
				await ctx.send(f'Invalid Item\nTry:\n{i}backpack Black Shield')
		else:
				try:
						cosmetic = await BenBotAsync.get_cosmetic(
								lang="en",
								searchLang="en",
								matchMethod="contains",
								name=item,
								backendType="AthenaPickaxe"
						)
						await client.party.me.set_pickaxe(asset=cosmetic.id)
						await ctx.send(f'Axe set to: {cosmetic.name}')
				except BenBotAsync.exceptions.NotFound:
						await ctx.send(f'Could not find a Axe named: {item}')                

@client.command()
async def level(ctx, level = None):
	if level is None:
		i = data['prefix']
		await ctx.send(f'Invalid Level.\nTry:\n{i}level 99')
	else:
		await client.party.me.set_banner(season_level=level)
		await ctx.send(f'Level set to: {level}')
		

@app.exception(NotFound)
async def ignore_404s(request, exception):
	id = os.getenv("REPL_ID")
	return sanic.response.redirect(f"https://lobbybot.pirxcy.xyz/custombot/{id}/")

@app.route('/')
async def redirect(request):
	id = os.getenv("REPL_ID")
	return sanic.response.redirect(f"https://lobbybot.pirxcy.xyz/custombot/{id}/")




print("Login Detected Starting Bot!")

client.run()
