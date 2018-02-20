import re
import json

def filterUrl(fname):
	tweets = []

	# url_regex = r'(https|http)(:(\w|.|\/)+(\s|\n)?)?'
	url_regex = r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b'
	url_pattern = re.compile(url_regex)

	with open(fname,encoding="utf-8") as f:
		tweet = json.load(f)

		for value in tweet:
			if len(value["text_de"]) != 0:
				value["text_de"] = url_pattern.sub('', value["text_de"]) 

			elif len(value["text_ru"]) != 0:
				value["text_ru"] = url_pattern.sub('', value["text_ru"]) 

			elif len(value["text_en"]) != 0:
				value["text_en"] = url_pattern.sub('', value["text_en"]) 


			tweets.append(value)

	outputFile = open('new_train2.json','w')
	outputFile.write(json.dumps(tweets,ensure_ascii=False))


def main():
	filterUrl('train.json')

if __name__ == '__main__':
	main()