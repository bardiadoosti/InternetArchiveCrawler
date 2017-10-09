import os
from urllib import urlopen
import json

# urls = ['aol.com','bloomberg.com','cisco.com','imdb.com','msn.com',\
#         'slac.stanford.edu','sun.com','whitehouse.gov','yahoo.com',\
#         'mtv.com','cnn.com','xerox.com','ibm.com','adobe.com','apple.com',\
#         'ask.com','amazon.com','indiana.edu','berkeley.edu','rollingstone.com']

#urls = ['cern.ch', 'vlib.org', 'www6.slac.stanford.edu', 'nikhef.nl/en', 'ncsa.illinois.edu', 'fnal.gov', 'sunsite.berkeley.edu', 'osu.edu', 'aliweb.com', 'Bloomberg.com', 'Chabad.org', 'ibiblio.org/Dave/#drfun.html', 'xxx.lanl.gov/archive/astro-ph', 'oreilly.com/gnn', 'heavensgate.com', 'haystack.mit.edu', 'imdb.com', 'iuma.com', 'kent.ac.uk/sac', 'sitomobile.com', 'thetech.org', 'nexor.com', 'mtv.com', #'parc.com', 'pespmc1.vub.ac.be', 'expasy.org', 'cl.cam.ac.uk/coffee/coffee.html', 'trincoll.edu/zines/tj', 'Wired.com', 'ama.org', 'amnesty.org', 'art.net', 'graffiti.org', 'fishcam.com', 'pakin.org/complaint', #'bianca.org', 'birminghamalcitycouncil.org', 'chabad.org', 'coolsiteoftheday.com', 'cyber.harvard.edu', 'cordis.com', 'economist.com', 'galaxy.com', 'ezone.org', 'epage.com', 'fvgroup.com', 'fogcam.org', #'hotwire.com', 'ibm.com', 'italiaonline.it', 'links.net', 'lawinfo.com', 'litkicks.com', 'lycos.com', 'megadeth.com', 'microsoft.com', 'museumofbadart.org', 'nineplanets.org', 'nando.net', 'netboy.com', #'netrek.org', 'Onlinetechex.com', 'Pathfinder.com', 'pizzahut.com', 'Powells.com', 'Purple.com', 'Rant.com', 'kennedy.senate.gov', 'Sex.com', 'Sighting.com', 'skepdic.com', 'steelforge.com', #'simpsonsarchive.com', 'spinnwebe.com', 'Telegraph.co.uk', 'Transdat.com', 'velonews.com', 'lis.virginia.gov', 'theuselessweb.com', 'webcrawler.com', 'wendyisdell.com', 'Whitehouse.gov', 'cs.colorado.edu/home/#mcbryan/WWWW.html', 'yahoo.com']

urls = ['iuma.com', 'kent.ac.uk/sac', 'sitomobile.com', 'thetech.org', 'nexor.com', 'mtv.com', 'parc.com', 'pespmc1.vub.ac.be', 'expasy.org', 'cl.cam.ac.uk/coffee/coffee.html', 'trincoll.edu/zines/tj', 'Wired.com', 'ama.org', 'amnesty.org', 'art.net', 'graffiti.org', 'fishcam.com', 'pakin.org/complaint', 'bianca.org', 'birminghamalcitycouncil.org', 'chabad.org', 'coolsiteoftheday.com', 'cyber.harvard.edu', 'cordis.com', 'economist.com', 'galaxy.com', 'ezone.org', 'epage.com', 'fvgroup.com', 'fogcam.org', 'hotwire.com', 'ibm.com', 'italiaonline.it', 'links.net', 'lawinfo.com', 'litkicks.com', 'lycos.com', 'megadeth.com', 'microsoft.com', 'museumofbadart.org', 'nineplanets.org', 'nando.net', 'netboy.com', 'netrek.org', 'Onlinetechex.com', 'Pathfinder.com', 'pizzahut.com', 'Powells.com', 'Purple.com', 'Rant.com', 'kennedy.senate.gov', 'Sex.com', 'Sighting.com', 'skepdic.com', 'steelforge.com', 'simpsonsarchive.com', 'spinnwebe.com', 'Telegraph.co.uk', 'Transdat.com', 'velonews.com', 'lis.virginia.gov', 'theuselessweb.com', 'webcrawler.com', 'wendyisdell.com', 'cs.colorado.edu/home/mcbryan/WWWW.html']

years = ['1996','1997','1998','1999','2000','2001','2002','2003','2004',\
         '2005','2006','2007','2008','2009','2010','2011','2012','2013']
months = ['01','02','03','04','05','06','07','08','09','10','11','12']
days = ['01','15']

for url in urls:
	for year in years:
		for month in months:
			for day in days:
                                timestamp = year+month+day
                                address = 'http://archive.org/wayback/available?url=' + url + '&timestamp=' + timestamp
                                json_res = urlopen(address).read()
                                decoded = json.loads(json_res)
                                address = str(decoded['archived_snapshots']['closest']['url'])
				cmd = './phantomjs snap-archive-api.js '+ address + ' ' + url
				print(cmd)
				os.system(cmd)
