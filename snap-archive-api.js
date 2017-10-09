"use strict";
var page = require('webpage').create(),
    system = require('system'),
    address, url, size;

url = system.args[1];
address = system.args[2];
var pageWidth = 1200;
var pageHeight = 1200;
page.viewportSize = { width: pageWidth, height: pageHeight };
page.clipRect = { top: 0, left: 0, width: pageWidth, height: pageHeight };
page.open(url, function (status) {
	if (status !== 'success') {
		console.log('Unable to load the address!');
		phantom.exit(1);
	} else {
		url = page.evaluate(function() {
			try {
				var bar = document.getElementById("wm-ipp");
				bar.parentNode.removeChild(bar);			
			}
			catch(err) {
				console.log("no clean up needed!");
			}	
			return document.location.href;
		});
		console.log(url);
		var actual_timestamp = url.split('/')[4];
		window.setTimeout(function () {
			page.render(address+'/'+actual_timestamp+'.png');
			phantom.exit();
		}, 10);
	}
});
