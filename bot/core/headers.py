from bot.core.agents import generate_random_user_agent

headers = {
		'Accept': '*/*',
		'Accept-Language': 'en-US,en;q=0.9,uk-UA;q=0.8,uk;q=0.7,ru;q=0.6,zh-CN;q=0.5,zh;q=0.4',
		'Connection': 'keep-alive',
		'Origin': 'https://mmbump.pro',
		'Referer': 'https://mmbump.pro/',
		'Sec-Fetch-Dest': 'empty',
		'Sec-Fetch-Mode': 'cors',
		'Sec-Fetch-Site': 'same-site',
		"User-Agent": generate_random_user_agent(),
		'sec-ch-ua': '"Chromium";v="126", "Google Chrome";v="126", "Not;A Brand";v="99"',
		'sec-ch-ua-mobile': '?1',
		'sec-ch-ua-platform': '"Android"',
}
