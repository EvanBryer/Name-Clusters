import argparse
parser = argparse.ArgumentParser(description='Name clusters from K-means by extracting most common word(s)')
parser.add_argument("-p", "--path", help="path to file of new line delimited strings.", required=True)
args = parser.parse_args()
#Text pre-processing
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
#import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D

nltk.download('stopwords')
nltk.download('wordnet')

#Cleaning the text
import string
def text_process(text):
    '''
    Takes in a string of text, then performs the following:
    1. Remove all punctuation
    2. Remove digits
    3. Remove all stopwords from included languages
   	4. Return the cleaned text as a list of words
    '''
    stemmer = WordNetLemmatizer()
    nopunc = [char for char in text if char not in string.punctuation]
    nopunc = ''.join([i for i in nopunc if not i.isdigit()])
    nopunc =  [word.lower() for word in nopunc.split() if word not in stopwords.words('english') and word not in stopwords.words('french') and word not in stopwords.words('german') 			and word not in stopwords.words('spanish') and word not in stopwords.words('italian') and word not in stopwords.words('dutch')]
    return [stemmer.lemmatize(word) for word in nopunc]

def toArr(arr):
	arr = arr.replace("\\\\n","")
	arr = arr.replace("\\n","")
	if len(arr[0:len(arr)].split("\', \'")) > 1:
		arr = arr[0:len(arr)].split("\', \'")
		for val in range(0,len(arr)):
			arr[val] = (re.sub("[^a-zA-Z0-9 -]", "", arr[val].lower()).strip())
	else:
		arr = [(re.sub("[^a-zA-Z0-9 -]", "", arr.lower()).strip())]
	return arr

with open(args.path) as f:
	for l in f:
		t = l.split("\t")[1]
		arr = toArr(t)
		group = []
		for v in arr:
			group.append(text_process(v))
		sets = map(set, group)
		words = {}
		for val in sets:
			for word in val:
				try:
					words[word] = words[word]+1
				except:
					words[word] = 1
		vals = words.values()
		high = max(vals)
		common = []
		for word in words:
			if words[word] == high:
				common.append(word)
		print(*common, "\t||\t", l)
















