import nltk

from nltk.corpus import stopwords

from nltk.tokenize import word_tokenize

from nltk.stem import PorterStemmer, WordNetLemmatizer

import os

def createdict(location,dict):

	d=0

	sum=0

	stop=set(stopwords.words('english'))

	list1=[]

	list=[]

	os.chdir(location)

	for file in os.listdir(location):

		f=open(file,"r")

		str=f.read().lower()

		str=str.replace("<br /><br />"," ")

		str=str.replace("\n"," ")

		for w in str:

			for i in w:

				if (i>'z' or i<'a') and i!=' ':

					str=str.replace(i," ")

		list1=str.split()

		l1=len(list1)

		c=0

		#print(list1)

		while l1!=0:

			if list1[c] in stop:

				del list1[c]

				c=c-1

			c=c+1

			l1=l1-1	

		for w in list1:

			w=PorterStemmer().stem(w)

		d=d+1

		list=list+list1

		f.close()

		if(d>2500):

			break

	setA= set(list)

	for w in setA:

		dict[w]=0

	for w in list:

		dict[w]=dict[w]+1

	return len(list)	    

dictpos={}

path1="/home/harshit-mudit/Downloads/aclImdb/train/pos"

s1=createdict(path1,dictpos)

dictneg={}

path2="/home/harshit-mudit/Downloads/aclImdb/train/neg"

s2=createdict(path2,dictneg)



def accuracy(path,flag):

	cnt1=0

	cnt2=0	

	c=0

	os.chdir(path)

	for file in os.listdir(path):

		c=c+1

		f=open(file,"r")

		str=f.read()	

		prod1=1

		prod2=1

		str=str.replace("<br /><br />"," ")

		str=str.replace("\n"," ")

		for w in str:

			for i in w:

				if (i>'z' or i<'a') and i!=' ':

					str=str.replace(i," ")

		list=str.lower().split()

		for i in list:

			i=PorterStemmer().stem(i)	

		l1=len(dictpos)

		l2=len(dictneg)

		for i in list:

			if dictpos.has_key(i) == True:

					prod1=prod1*dictpos[i]*10000.0/s1

			if dictneg.has_key(i) == True:

					prod2=prod2*dictneg[i]*10000.0/s2

		if prod1*l1>prod2*l2:

			cnt1=cnt1+1

		else:

			cnt2=cnt2+1

		if c>500:

			break

	if flag == 0:

		return (cnt1*100.0/(cnt1+cnt2))##pos

	else:

		return (cnt2*100.0/(cnt1+cnt2))##neg



path3="/home/harshit-mudit/Downloads/aclImdb/test/pos"

accpos=accuracy(path3,0)

path4="/home/harshit-mudit/Downloads/aclImdb/test/neg"

accneg=accuracy(path4,1)

print(accpos,accneg)

print((accpos+accneg)/2)

//here i have trained about 2500 positive and 2500 negative reviews,and tested it in 500 positive and 500 negative reviews.
//And my accuracy for positve is 69.66% and for negative reviews it is 82.63%.


