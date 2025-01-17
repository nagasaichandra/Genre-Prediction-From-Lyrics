from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from GenrePrediction import prediction
from GenrePrediction import similar
from GenrePrediction import Model
from GenrePrediction import Data


import joblib

from string import punctuation
import nltk
from nltk import FreqDist
import math
from nltk.corpus import stopwords 
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')
from nltk import word_tokenize, pos_tag
decide=[]
genred=input()








def index(request):
    return render(request, 'index.html', {})
def new_page(request):
	import joblib
	data = request.GET["fulltextarea"]
	load_model_dir = 'GenrePrediction/Model/genrePredict.pkl'
	clf = joblib.load(load_model_dir)
	genred=prediction.predict_a_song(data,clf)
	lylen={'Pop': 205.63510562964711, 'Hip-Hop': 430.9917806870755, 'Rock': 166.65387815280923, 'Metal': 150.58008247618145, 'Country': 163.48524412855377, 'Jazz': 154.45732854455275, 'Electronic': 174.99855468122692, 'Folk': 170.92400218698742, 'R&B': 193.1815572299964, 'Indie': 172.19304347826088}
	lyuniqlen={'Pop': 98.01085801959164, 'Hip-Hop': 225.17270400629982, 'Rock': 89.09069559264915, 'Metal': 91.11015784234725, 'Country': 89.52364029666255, 'Jazz': 82.51633316230546, 'Electronic': 82.18387666613137, 'Folk': 95.8529250956807, 'R&B': 96.3362038033728, 'Indie': 90.6751304347826}
	lineuniqlen={'Pop': 2.461601849656154, 'Hip-Hop': 3.485599896385689, 'Rock': 2.888647701779367, 'Metal': 3.0881449932442093, 'Country': 3.614228681928763, 'Jazz': 2.868311851992771, 'Electronic': 2.3472491686733172, 'Folk': 3.1174315841883455, 'R&B': 2.740270874371039, 'Indie': 2.908426583959033}
	punctdict={'Pop': 37.18836303552461, 'Hip-Hop': 90.79609213505266, 'Rock': 28.2465062397978, 'Metal': 23.048442906574394, 'Country': 23.018309641532756, 'Jazz': 28.800410466906104, 'Electronic': 31.59723783523366, 'Folk': 28.571350464734827, 'R&B': 40.28274129888769, 'Indie': 26.928695652173914}
	linelendict={'Pop': 5.164649780649751, 'Hip-Hop': 6.671611964405437, 'Rock': 5.403531074893207, 'Metal': 5.1038560221326446, 'Country': 6.6001902563782675, 'Jazz': 5.369019309426425, 'Electronic': 4.998124068340787, 'Folk': 5.558973629461031, 'R&B': 5.495024444013513, 'Indie': 5.523133221023507}
	linenum={'Pop': 39.81588575475038, 'Hip-Hop': 64.60084654001378, 'Rock': 30.841661839818862, 'Metal': 29.503199507038914, 'Country': 24.769777503090236, 'Jazz': 28.768257225927826, 'Electronic': 35.01284727798298, 'Folk': 30.747402952433024, 'R&B': 35.15572299964119, 'Indie': 31.176695652173912}
	linecommon={'Pop': [('love', 67237), ('know', 50857), ('like', 41713), ('baby', 31224), ('want', 26806), ('never', 26200), ('time', 26005), ('yeah', 22954), ('come', 22039), ('make', 21258), ('heart', 19881), ('feel', 19672), ('take', 19040), ('need', 18480), ('could', 17556), ('back', 16774), ('life', 16340), ('away', 15861), ('girl', 15339), ('right', 15321), ('tell', 14965), ('night', 14137), ('give', 14131), ("'cause", 13872), ('world', 12595), ('think', 12098), ('would', 11990), ('keep', 11513), ('good', 11461), ('chorus', 11020), ('every', 10891), ('eyes', 10409), ('always', 10249), ('still', 9831), ('little', 9345), ('around', 9332), ('ever', 9306), ('find', 9197), ('look', 8900), ('mind', 8797), ('cause', 8671), ('nothing', 8646), ('said', 8604), ('hold', 8325), ('long', 8196), ('tonight', 8045), ('things', 7967), ('everything', 7877), ('really', 7863), ('better', 7696)], 'Hip-Hop': [('like', 80352), ('know', 50080), ('nigga', 34720), ('shit', 29658), ('back', 25915), ('yeah', 25866), ('love', 24981), ('make', 23772), ('niggas', 23733), ('fuck', 22815), ('come', 21043), ('want', 20974), ('never', 20621), ('time', 20431), ('baby', 19484), ('bitch', 18677), ('cause', 18351), ('take', 18204), ('right', 16996), ('girl', 16677), ('money', 16102), ('chorus', 15552), ('keep', 15269), ('tell', 15247), ('life', 14841), ('need', 13920), ("'cause", 13374), ('give', 13020), ('could', 12618), ('still', 12312), ('real', 11418), ('think', 11352), ('feel', 11182), ('look', 10560), ('good', 9921), ('verse', 9710), ('said', 9607), ('even', 9568), ("y'all", 9439), ('around', 9273), ('call', 9193), ('better', 9160), ('every', 8840), ('would', 8825), ('game', 8729), ('stop', 8511), ('world', 8284), ('little', 8215), ('really', 7993), ('mind', 7839)], 'Rock': [('know', 98756), ('love', 89197), ('like', 82384), ('time', 66115), ('never', 61117), ('want', 51376), ('come', 46869), ('away', 44433), ('take', 44359), ('back', 43154), ('yeah', 40922), ('could', 40903), ('make', 39018), ('life', 38516), ('feel', 36742), ('baby', 36638), ('right', 32089), ('night', 32072), ('heart', 30681), ('world', 30379), ('need', 30219), ('tell', 29596), ('well', 28869), ('think', 28129), ('would', 27681), ('eyes', 27052), ('said', 26385), ('little', 25521), ('around', 24917), ('still', 24708), ('give', 24579), ('find', 23792), ('long', 23735), ('good', 23705), ('nothing', 23264), ("'cause", 23114), ('every', 22378), ('always', 22335), ('look', 22247), ('mind', 22026), ('keep', 21969), ('home', 21455), ('things', 20755), ('ever', 20078), ('girl', 19556), ('gone', 18974), ('everything', 18491), ('something', 18223), ('alone', 17574), ('chorus', 17190)], 'Metal': [('life', 13480), ('time', 12251), ('never', 11360), ('like', 11049), ('know', 9919), ('world', 8184), ('away', 7907), ('eyes', 7769), ('take', 7441), ('come', 7146), ('love', 6849), ('feel', 6694), ('back', 6425), ('blood', 6410), ('death', 6270), ('night', 5927), ('mind', 5624), ('pain', 5619), ('want', 5532), ('heart', 5239), ('make', 5233), ('soul', 5190), ('dead', 5089), ('light', 5045), ('still', 4972), ('inside', 4870), ('nothing', 4862), ('could', 4295), ('live', 4123), ('face', 4020), ('lost', 3939), ('black', 3805), ('left', 3801), ('right', 3794), ('fear', 3764), ('fire', 3736), ('dark', 3727), ('need', 3718), ('give', 3695), ('find', 3688), ('every', 3650), ('last', 3585), ('fall', 3573), ('hell', 3531), ('chorus', 3494), ('hear', 3454), ('lies', 3450), ('hate', 3422), ('look', 3413), ('would', 3390)], 'Country': [('love', 18660), ('know', 11619), ('like', 11493), ('time', 8517), ('never', 7830), ('back', 6973), ('heart', 6676), ('could', 6287), ('little', 6176), ('come', 5776), ('well', 5307), ('night', 5255), ('baby', 5233), ('take', 5030), ('home', 4743), ('long', 4737), ('away', 4642), ('make', 4611), ('would', 4516), ('life', 4506), ('right', 4441), ('want', 4409), ('good', 4328), ('said', 4269), ('still', 4156), ('every', 3886), ('gone', 3859), ('yeah', 3859), ('tell', 3831), ('ever', 3817), ('world', 3669), ('around', 3571), ('always', 3488), ('think', 3465), ('girl', 3230), ('mind', 3141), ("'cause", 3124), ('eyes', 3124), ('find', 3028), ('keep', 2958), ('feel', 2952), ('need', 2942), ('chorus', 2923), ('look', 2724), ('give', 2687), ('things', 2666), ('much', 2649), ('left', 2532), ('hold', 2496), ('cause', 2402)], 'Jazz': [('love', 10460), ('know', 5389), ('like', 4392), ('baby', 3838), ('never', 3015), ('come', 2963), ('time', 2948), ('heart', 2817), ('want', 2451), ('make', 2288), ('could', 2091), ('night', 2088), ('tell', 1976), ('take', 1936), ('back', 1922), ('away', 1869), ('little', 1824), ('would', 1783), ('life', 1756), ('good', 1732), ('right', 1704), ('yeah', 1673), ('feel', 1624), ('need', 1617), ('well', 1611), ('long', 1528), ('give', 1511), ('world', 1483), ('keep', 1428), ('said', 1405), ('every', 1400), ('always', 1335), ("'cause", 1332), ('home', 1321), ('eyes', 1318), ('around', 1304), ('find', 1253), ('think', 1234), ('still', 1187), ('hear', 1180), ('girl', 1150), ('ever', 1090), ('things', 1088), ('gone', 1079), ('sweet', 1027), ('look', 1023), ('dream', 1020), ('true', 1011), ('thing', 1006), ('much', 993)], 'Electronic': [('love', 8808), ('know', 6809), ('like', 6147), ('come', 4643), ('want', 4345), ('time', 4230), ('feel', 4071), ('never', 3954), ('take', 3385), ('make', 3373), ('baby', 3259), ('yeah', 3216), ('back', 2901), ('life', 2858), ('need', 2799), ('away', 2766), ('night', 2628), ('world', 2595), ('right', 2548), ('give', 2519), ('could', 2497), ('heart', 2320), ('tell', 2168), ('keep', 1889), ('good', 1853), ('around', 1806), ('girl', 1777), ('eyes', 1772), ('think', 1717), ("'cause", 1683), ('mind', 1679), ('hold', 1627), ('stop', 1619), ('every', 1593), ('find', 1591), ('nothing', 1578), ('still', 1567), ('look', 1527), ('something', 1466), ('always', 1447), ('would', 1446), ('tonight', 1444), ('little', 1425), ('light', 1421), ('ever', 1366), ('cause', 1291), ('hear', 1276), ('better', 1204), ('things', 1182), ('chorus', 1181)], 'Folk': [('love', 1543), ('like', 1271), ('know', 1104), ('never', 934), ('time', 885), ('come', 759), ('away', 750), ('heart', 641), ('back', 591), ('night', 586), ('could', 576), ('would', 542), ('take', 513), ('want', 500), ('well', 490), ('life', 489), ('home', 476), ('world', 462), ('long', 452), ('still', 442), ('make', 427), ('little', 417), ('feel', 416), ('said', 406), ('eyes', 402), ('chorus', 400), ('find', 397), ('right', 395), ('around', 381), ('every', 376), ('need', 373), ('tell', 371), ('think', 366), ('baby', 354), ('good', 350), ('hear', 341), ('sing', 339), ("'cause", 330), ('yeah', 318), ('keep', 315), ('ever', 314), ('light', 305), ('song', 299), ('give', 289), ('gone', 283), ('mind', 280), ('nothing', 279), ('look', 275), ('head', 273), ('always', 271)], 'R&B': [('love', 5787), ('baby', 4364), ('know', 4333), ('like', 2943), ('want', 2639), ('yeah', 2460), ('time', 2357), ('never', 2076), ('make', 1925), ('girl', 1857), ('come', 1851), ('back', 1769), ('take', 1634), ('need', 1498), ('right', 1453), ('could', 1415), ('tell', 1396), ('life', 1386), ('heart', 1385), ('feel', 1297), ('away', 1204), ("'cause", 1203), ('night', 1200), ('think', 1192), ('give', 1146), ('good', 1142), ('world', 1061), ('keep', 1031), ('every', 1008), ('little', 993), ('would', 989), ('said', 945), ('well', 914), ('long', 873), ('look', 827), ('around', 827), ('ever', 814), ('mind', 811), ('chorus', 800), ('eyes', 793), ('home', 775), ('things', 759), ('always', 742), ('still', 738), ('thing', 720), ('much', 719), ('find', 659), ('nothing', 658), ('everything', 655), ('hold', 648)], 'Indie': [('know', 3437), ('love', 2999), ('like', 2707), ('time', 1872), ('never', 1691), ('come', 1609), ('want', 1431), ('could', 1423), ('take', 1322), ('back', 1266), ('away', 1184), ('feel', 1123), ('make', 1101), ('would', 1041), ('heart', 1032), ('life', 945), ('still', 929), ('home', 918), ('said', 901), ('think', 899), ('need', 878), ('night', 872), ('right', 849), ('well', 840), ('tell', 835), ('yeah', 823), ('around', 812), ('eyes', 807), ('world', 792), ('long', 788), ('little', 778), ('always', 777), ('keep', 775), ('good', 765), ('find', 762), ('mind', 736), ('every', 718), ('something', 712), ('nothing', 709), ('ever', 677), ("'cause", 665), ('light', 653), ('things', 645), ('give', 638), ('look', 614), ('hold', 612), ('head', 598), ('girl', 596), ('baby', 588), ('everything', 587)]}
	lypro={'Pop': [40.98781423344742, 14.813141744364453, 53.590876903103975, 67.28514103623274], 'Hip-Hop': [70.80642779801161, 33.14228762673491, 99.49921252091741, 153.58544148046067], 'Rock': [31.855689537149175, 11.438365541572324, 44.06585224580064, 48.83174135116634], 'Metal': [22.750817651798833, 11.07252215954875, 35.525524956154904, 54.091340000948], 'Country': [31.359548825710753, 11.060800370828183, 41.525957972805934, 42.74049752781212], 'Jazz': [28.926971096288696, 11.253805370275355, 39.18966991619634, 48.032666324610915], 'Electronic': [34.26079974305444, 12.854665167817569, 46.227236229323914, 55.32872972538944], 'Folk': [26.39420448332422, 13.032804811372335, 38.486604702022966, 59.46145434663751], 'R&B': [43.04305705059203, 12.609616074632221, 54.72515249372085, 50.03982777179763], 'Indie': [33.35930434782609, 11.220521739130435, 45.84, 48.456]}

	output=' '
	text=data
	words=len(str(text).split(' '))
	uniq_words=len(set(str(text).split(' ')))
	line=len(str(text).split('\n'))
	uniq_words_line=len(set(str(text).split(' ')))/line
	punc=len([w for w in text if w in punctuation])
	words_line=words/line
	val=len([word for word,pos in pos_tag(word_tokenize(text)) if pos.startswith('PRP')])
	val1=len([word for word,pos in pos_tag(word_tokenize(text)) if pos.startswith('JJ')])
	val2=len([word for word,pos in pos_tag(word_tokenize(text)) if pos.startswith('VB')])
	val3=len([word for word,pos in pos_tag(word_tokenize(text)) if pos.startswith('NN')])
	v=[val,val1,val2,val3]
	stop_words = set(stopwords.words('english')) 
	text=text.lower()
	tockstop=word_tokenize(text)
	tock=[w for w in tockstop if not w in stop_words and len(w)>3]
	fd=nltk.FreqDist(tock)
	common=fd.most_common(10)
	
	if abs(words-lylen[genred]) == min([ abs(lylen[i]-words) for i in lylen.keys()] ):
		output=output+' The no of words is '+str(words)+ ' which is closer to the average word length of genre ' + str(genred)+'. '
	if abs(uniq_words-lyuniqlen[genred]) == min([abs(uniq_words-lyuniqlen[i]) for i in lyuniqlen.keys()] ):
		output=output+' The total no of unique words is '+str(uniq_words)+ ' which is closer to the average word length of genre ' + str(genred)+'. '
	if abs(uniq_words_line-lineuniqlen[genred]) == min([abs(uniq_words_line-lineuniqlen[i]) for i in lineuniqlen.keys()] ):
		output=output+' The total no of unique words per line is '+str(uniq_words_line)+ ' which is closer to the average word length of genre ' + str(genred)+'. '
	if abs(punc-punctdict[genred]) == min([punc-punctdict[i] for i in punctdict.keys()]):
		output=output+' The no of punctuations is '+str(round(punc))+ ' which is closer to the average punctuation length of genre ' + str(genred)+'. '
	if abs(words_line-linelendict[genred]) == min([words_line-linelendict[i] for i in linelendict.keys()] ):
		output=output+' The avergae words per line '+str(round(words_line))+ ' which is closer to the average words length per line of genre ' + str(genred)+'. '
	if abs(line-linenum[genred]) == min([line-linenum[i] for i in linenum.keys()] ):
		output=output+' The no of lines is '+str(line)+ ' which is closer to the average no of lines of genre ' + str(genred)+'. '
	for i in range(0,4):
		name=['pronous','adjective','verb','Noun']
		if abs(v[i]-lypro[genred][i]) == min([ abs(lypro[j][i]-v[i]) for j in lylen.keys()] ):
			output=output+' The no of '+ str(name[i])+ ' is '+str(v[i])+ ' which is closer to the average '+ str(name[i])+  ' length of genre ' + str(genred)+'. '
	f=False
	for val in common:
		for val1 in linecommon[genred]:
			if val[0]==val1[0]:
				output=output+str(val[0])+','
				f=True
	if f is True:
		output=output+' are found in the most common 50 words in the genre ' + str(genred)+'. '
	songs=similar.similar_songs(data)
	return render(request, 'newpage.html', {'data':genred,'output':output,'songs':songs})