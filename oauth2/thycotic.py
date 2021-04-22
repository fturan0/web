import requests, urllib3, json
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://mithrandir.lotr.local/secretserver/"
proxies = {'https':'http://127.0.0.1:8080'}
creds = {'username':'ss_admin', 'password':'pass', 'grant_type':'password'}

def get_token(url,data):
	endpoint = "oauth2/token"
	res = requests.post(url + endpoint, verify = False, proxies = proxies, data = data)
	res_data = json.loads(res.text)
	return res_data['access_token']

def get_secret(url, secret_id, token):
	endpoint = "api/v1/secrets/" + str(secret_id)
	headers = {'Authorization':'Bearer ' + token}
	res = requests.get(url + endpoint, verify = False, proxies = proxies, headers = headers)
	res_data = json.loads(res.text)
	username = [i["itemValue"] for i in res_data['items'] if i["fieldName"] == "Username"][0]
	password = [i["itemValue"] for i in res_data['items'] if i["fieldName"] == "Password"][0]
	return {"username":username, "password":password}


token = get_token(url, creds)
secret = get_secret(url, 10, token)


print(json.dumps(secret, indent = 6))
