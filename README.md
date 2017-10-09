This is Internet Archive crawling script written by Bardia Doosti
If you used my code please cite our paper:

@inproceedings{Doosti:2017:DSH:3091478.3091503,
 author = {Doosti, Bardia and Crandall, David J. and Su, Norman Makoto},
 title = {A Deep Study into the History of Web Design},
 booktitle = {Proceedings of the 2017 ACM on Web Science Conference},
 series = {WebSci '17},
 year = {2017},
 isbn = {978-1-4503-4896-6},
 location = {Troy, New York, USA},
 pages = {329--338},
 numpages = {10},
 url = {http://doi.acm.org/10.1145/3091478.3091503},
 doi = {10.1145/3091478.3091503},
 acmid = {3091503},
 publisher = {ACM},
 address = {New York, NY, USA},
 keywords = {convolutional neural networks, cultural analytics, deep learning, web design},
}

This website crawler is based on PhantomJS so please remember to download it from http://phantomjs.org/ and put pre-compiled phantomjs beside the render.py and snap-archive-api.js file.

The render.py lists the websites you want to crawl and sends it to phantomjs and snap-archive-api.js will save the png file using phantomjs.

Please notice that render.py crawls from 1996 to 2013 with the rate of two snapshots per month which we used in our research. You can change it to whatever which is good for you.
