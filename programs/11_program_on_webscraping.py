"""
Program on webscraping using beautifulsoup4 library
Here I am using 2 libraries. - urllib library and beautifulsoup4
Documentation:
    https://pypi.org/project/beautifulsoup4/     # using beautifulsoup , i cannot directory pass the url
    https://docs.python.org/3/library/urllib.request.html # to get the url, i need to use urllib library.
    https://www.crummy.com/software/BeautifulSoup/bs4/doc/
    https://www.crummy.com/software/BeautifulSoup/bs4/doc/

for parsing html, xml we use beautifulsoup4 library.
"""

print("Get data from website and print")
print("-"*20)
# ----------------

try:
    import urllib.request as mylib
    #my_website_handle = mylib.urlopen("https://www.python.org") # if this is locked, then we can use below url
    my_website_handle = mylib.urlopen("https://www.crummy.com/software/BeautifulSoup/bs4/doc/")
    my_website_data = my_website_handle.read()
    print(my_website_data)
    my_website_handle.close()
except Exception as e:
    print("Not able to get data from website")
    print("Reason: ", e, end="\n\n")

print("#"*40, end="\n\n")
#########################

print("Create object of BeautifulSoup class with website data")
print("-"*20)
# ----------------

from bs4 import BeautifulSoup
soup = BeautifulSoup(my_website_data, "html.parser")
print(soup)

print("#"*40, end="\n\n")
#########################

print("Neatly display the html content")
print("-"*20)
# ----------------

print(soup.prettify())

print("#"*40, end="\n\n")
#########################

print("Only head tag")
print("-"*20)
# ----------------

head_tag = soup.head
print(head_tag)

print("#"*40, end="\n\n")
#########################

print("Only Body tag")
print("-"*20)
# ----------------

head_tag = soup.body
print(head_tag)

print("#"*40, end="\n\n")
#########################

print("1st title tag in entire website content")
print("-"*20)
# ----------------

title_tag = soup.title
print("title_tag:", title_tag) # <title>Welcome to Python.org</title>

title_tag_content = soup.title.text
print("title_tag_content:", title_tag_content) # Welcome to Python.org
print("type of title_tag_content:", type(title_tag_content))  #

print("#"*40, end="\n\n")
#########################

print("1st title tag inside head-tag")
print("-"*20)
# ----------------

title_tag = soup.head.title
print("title_tag:", title_tag) # <title>Welcome to Python.org</title>

title_tag_content = soup.head.title.text
print("title_tag_content:", title_tag_content) # Welcome to Python.org
print("type of title_tag_content:", type(title_tag_content))

print("#"*40, end="\n\n")
#########################

print("Content of title tag")
print("-"*20)
# ----------------

title_tag_content = soup.head.title.text
print("title_tag_content:", title_tag_content) # Welcome to Python.org
print("type of title_tag_content:", type(title_tag_content))

print("#"*40, end="\n\n")
#########################

print("1st link tag in entire website content")
print("-"*20)
# ----------------

print(soup.link) # <link rel="prefetch" href="//ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js">

print("#"*40, end="\n\n")
#########################

print("1st link tag inside head tag")
print("-"*20)
# ----------------

print(soup.head.link) # <link rel="prefetch" href="//ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js">

print("#"*40, end="\n\n")
#########################

print("1st link tag and its attributes")
print("-"*20)
# ----------------

print("1st link tag:", soup.head.link) # <link rel="prefetch" href="//ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js">

rel_value = soup.head.link.get("rel") # "prefetch"
print("Attribute 'rel': ", rel_value)    # we will get data in string only
print("type of Attribute 'rel' value: ", type(rel_value)) # we will get data in string only

href_value = soup.head.link.get("href")
print("Attribute 'href': ", href_value) # we will get data in string only
print("type of Attribute 'href' value: ", type(href_value)) # we will get data in string only

print("#"*40, end="\n\n")
#########################

print("All link tags present inside head-tag")
print("-"*20)
# ----------------

all_link_tags = soup.head.find_all(href=True) # Where href attribute should be present
print(all_link_tags)

print("#"*40, end="\n\n")
#########################

print("All href tags present inside each link-tag")
print("-"*20)
# ----------------

for each_link_tag in all_link_tags:
    print("Tag:", each_link_tag)
    print("URL:", each_link_tag.get("href"))

print("#"*40, end="\n\n")
#########################

print("All paragraph tags")
print("-"*20)
# ----------------

all_paragraph_tags = soup.find_all("p")
print(all_paragraph_tags)
# Ex: [<p>some text</p>,    <p>some text</p>,   <p>some text</p>,  etc ]

print("#"*40, end="\n\n")
#########################


print("all paragraphs content")
print("-"*20)
# ----------------

L = [10, 20, 30, 40, 50]
M = [i*i    for i in L] # Oneliner : Called Comprehensions

# Ex: [<p>some text</p>,    <p>some text</p>,   <p>some text</p>,  etc ]
all_paragraph_contents = [each_paragraph_tag.text       for each_paragraph_tag in all_paragraph_tags]
print(all_paragraph_contents)
# ["pargraph-1 content", "pargraph-2 content", "pargraph-3 content", ]

print("#"*40, end="\n\n")
#########################

print("All anchor(<a>) tag")
print("-"*20)
# ----------------

all_anchor_tags = soup.find_all("a")
print(all_anchor_tags)
# [<a href=''> </a>, <a href=''> </a>, <a href=''> </a>, <a href=''> </a>, ]

print("#"*40, end="\n\n")
#########################

print("All URLS")
print("-"*20)
# ----------------

# [<a href=''> </a>, <a href=''> </a>, <a href=''> </a>, <a href=''> </a>, ]
all_urls = [each_anchor_tag.get("href")     for each_anchor_tag in all_anchor_tags]
# This oneliner is called comprehension
print(all_urls)
# ["url-1", "url-2", "url3"]

print("#"*40, end="\n\n")
#########################

print("Cleanup All URLS")
print("-"*20)
# ----------------

cleaned_urls = [each_url   for each_url in all_urls  if each_url.startswith("http")]
print(cleaned_urls)

print("#"*40, end="\n\n")
#########################

print("Create dictionary with all urls and paragraphs")
print("-"*20)
# ----------------

my_webscrape_dictionary = {
    "website_title": title_tag_content,
    "all_urls": cleaned_urls,
    "all_paragraphs": all_paragraph_contents}
print(my_webscrape_dictionary)

print("#"*40, end="\n\n")
#########################

print("Write to web_scrape_report.json file")
print("-"*20)
# ----------------

my_json_file_handle = open(file="web_scrape_report.json", mode="w")

import json
json.dump(my_webscrape_dictionary, my_json_file_handle)

my_json_file_handle.close()

print("Created web_scrape_report.json file")

print("#"*40, end="\n\n")
#########################


"""
Output of above program


--------------------
b'<!doctype html>\n<!--[if lt IE 7]>   <html class="no-js ie6 lt-ie7 lt-ie8 lt-ie9">   <![endif]-->\n<!--[if IE 7]>      <html class="no-js ie7 lt-ie8 lt-ie9">          <![endif]-->\n<!--[if IE 8]>      <html class="no-js ie8 lt-ie9">                 <![endif]-->\n<!--[if gt IE 8]><!--><html class="no-js" lang="en" dir="ltr">  <!--<![endif]-->\n\n<head>\n    <script defer data-domain="python.org" src="https://analytics.python.org/js/script.outbound-links.js"></script>\n\n    <meta charset="utf-8">\n    <meta http-equiv="X-UA-Compatible" content="IE=edge">\n\n    <link rel="prefetch" href="//ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js">\n    <link rel="prefetch" href="//ajax.googleapis.com/ajax/libs/jqueryui/1.12.1/jquery-ui.min.js">\n\n    <meta name="application-name" content="Python.org">\n    <meta name="msapplication-tooltip" content="The official home of the Python Programming Language">\n    <meta name="apple-mobile-web-app-title" content="Python.org">\n    <meta name="apple-mobile-web-app-capable" content="yes">\n    <meta name="apple-mobile-web-app-status-bar-style" content="black">\n\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <meta name="HandheldFriendly" content="True">\n    <meta name="format-detection" content="telephone=no">\n    <meta http-equiv="cleartype" content="on">\n    <meta http-equiv="imagetoolbar" content="false">\n\n    <script async\n            src="https://media.ethicalads.io/media/client/v1.4.0/ethicalads.min.js"\n            integrity="sha256-U3hKDidudIaxBDEzwGJApJgPEf2mWk6cfMWghrAa6i0= sha384-UcmsCqcNRSLW/dV3Lo1oCi2/VaurXbib6p4HyUEOeIa/4OpsrnucrugAefzVZJfI sha512-q4t1L4xEjGV2R4hzqCa41P8jrgFUS8xTb8rdNv4FGvw7FpydVj/kkxBJHOiaoxHa8olCcx1Slk9K+3sNbsM4ug=="\n            crossorigin="anonymous"\n    ></script>\n    <script src="/static/js/libs/modernizr.js"></script>\n\n    <link href="/static/stylesheets/style.08a078d0aa02.css" rel="stylesheet" type="text/css" media="all" title="default" />\n    <link href="/static/stylesheets/mq.98d6092b2ada.css" rel="stylesheet" type="text/css" media="not print, braille, embossed, speech, tty" />\n    <link href="/static/stylesheets/no-mq.bf0c425cdb73.css" rel="stylesheet" type="text/css" media="screen" />\n    \n\n    <!--[if (lte IE 8)&(!IEMobile)]>\n    <link href="/static/stylesheets/no-mq.bf0c425cdb73.css" rel="stylesheet" type="text/css" media="screen" />\n    \n    \n    <![endif]-->\n    <link rel="stylesheet" href="//ajax.googleapis.com/ajax/libs/jqueryui/1.12.1/themes/smoothness/jquery-ui.css">\n\n    \n    <link rel="icon" type="image/x-icon" href="/static/favicon.ico">\n    <link rel="apple-touch-icon-precomposed" sizes="144x144" href="/static/apple-touch-icon-144x144-precomposed.png">\n    <link rel="apple-touch-icon-precomposed" sizes="114x114" href="/static/apple-touch-icon-114x114-precomposed.png">\n    <link rel="apple-touch-icon-precomposed" sizes="72x72" href="/static/apple-touch-icon-72x72-precomposed.png">\n    <link rel="apple-touch-icon-precomposed" href="/static/apple-touch-icon-precomposed.png">\n    <link rel="apple-touch-icon" href="/static/apple-touch-icon-precomposed.png">\n\n    \n    <meta name="msapplication-TileImage" content="/static/metro-icon-144x144.png"><!-- white shape -->\n    <meta name="msapplication-TileColor" content="#3673a5"><!-- python blue -->\n    <meta name="msapplication-navbutton-color" content="#3673a5">\n\n    <title>Welcome to Python.org</title>\n\n    <meta name="description" content="The official home of the Python Programming Language">\n    <meta name="keywords" content="Python programming language object oriented web free open source software license documentation download community">\n\n    \n    <meta property="og:type" content="website">\n    <meta property="og:site_name" content="Python.org">\n    <meta property="og:title" content="Welcome to Python.org">\n    <meta property="og:description" content="The official home of the Python Programming Language">\n    \n    <meta property="og:image" content="https://www.python.org/static/opengraph-icon-200x200.png">\n    <meta property="og:image:secure_url" content="https://www.python.org/static/opengraph-icon-200x200.png">\n    \n    <meta property="og:url" content="https://www.python.org/">\n\n    <link rel="author" href="/humans.txt">\n\n    <link rel="alternate" type="application/rss+xml" title="Python Enhancement Proposals"\n          href="https://peps.python.org/peps.rss">\n    <link rel="alternate" type="application/rss+xml" title="Python Job Opportunities"\n          href="https://www.python.org/jobs/feed/rss/">\n    <link rel="alternate" type="application/rss+xml" title="Python Software Foundation News"\n          href="https://feeds.feedburner.com/PythonSoftwareFoundationNews">\n    <link rel="alternate" type="application/rss+xml" title="Python Insider"\n          href="https://feeds.feedburner.com/PythonInsider">\n   <link rel="alternate" type="application/rss+xml" title="Python Releases"\n         href="https://www.python.org/downloads/feed.rss">\n\n    \n\n    \n    <script type="application/ld+json">\n     {\n       "@context": "https://schema.org",\n       "@type": "WebSite",\n       "url": "https://www.python.org/",\n       "potentialAction": {\n         "@type": "SearchAction",\n         "target": "https://www.python.org/search/?q={search_term_string}",\n         "query-input": "required name=search_term_string"\n       }\n     }\n    </script>\n\n    \n    <script type="text/javascript">\n    var _gaq = _gaq || [];\n    _gaq.push([\'_setAccount\', \'UA-39055973-1\']);\n    _gaq.push([\'_trackPageview\']);\n\n    (function() {\n        var ga = document.createElement(\'script\'); ga.type = \'text/javascript\'; ga.async = true;\n        ga.src = (\'https:\' == document.location.protocol ? \'https://ssl\' : \'http://www\') + \'.google-analytics.com/ga.js\';\n        var s = document.getElementsByTagName(\'script\')[0]; s.parentNode.insertBefore(ga, s);\n    })();\n    </script>\n    \n</head>\n\n<body class="python home" id="homepage">\n\n    <div id="touchnav-wrapper">\n\n        <div id="nojs" class="do-not-print">\n            <p><strong>Notice:</strong> While JavaScript is not essential for this website, your interaction with the content will be limited. Please turn JavaScript on for the full experience. </p>\n        </div>\n\n        <!--[if lte IE 8]>\n        <div id="oldie-warning" class="do-not-print">\n            <p>\n                <strong>Notice:</strong> Your browser is <em>ancient</em>. Please\n                <a href="http://browsehappy.com/">upgrade to a different browser</a> to experience a better web.\n            </p>\n        </div>\n        <![endif]-->\n\n        <!-- Sister Site Links -->\n        <div id="top" class="top-bar do-not-print">\n\n            <nav class="meta-navigation container" role="navigation">\n\n                \n                <div class="skip-link screen-reader-text">\n                    <a href="#content" title="Skip to content">Skip to content</a>\n                </div>\n\n                \n                <a id="close-python-network" class="jump-link" href="#python-network" aria-hidden="true">\n                    <span aria-hidden="true" class="icon-arrow-down"><span>&#9660;</span></span> Close\n                </a>\n\n                \n\n<ul class="menu" role="tree">\n    \n    <li class="python-meta current_item selectedcurrent_branch selected">\n        <a href="/" title="The Python Programming Language" class="current_item selectedcurrent_branch selected">Python</a>\n    </li>\n    \n    <li class="psf-meta ">\n        <a href="https://www.python.org/psf/" title="The Python Software Foundation" >PSF</a>\n    </li>\n    \n    <li class="docs-meta ">\n        <a href="https://docs.python.org" title="Python Documentation" >Docs</a>\n    </li>\n    \n    <li class="pypi-meta ">\n        <a href="https://pypi.org/" title="Python Package Index" >PyPI</a>\n    </li>\n    \n    <li class="jobs-meta ">\n        <a href="/jobs/" title="Python Job Board" >Jobs</a>\n    </li>\n    \n    <li class="shop-meta ">\n        <a href="/community/"  >Community</a>\n    </li>\n    \n</ul>\n\n\n                <a id="python-network" class="jump-link" href="#top" aria-hidden="true">\n                    <span aria-hidden="true" class="icon-arrow-up"><span>&#9650;</span></span> The Python Network\n                </a>\n\n            </nav>\n\n        </div>\n\n        <!-- Header elements -->\n        <header class="main-header" role="banner">\n            <div class="container">\n\n                <h1 class="site-headline">\n                    <a href="/"><img class="python-logo" src="/static/img/python-logo.png" alt="python&trade;"></a>\n                </h1>\n\n                <div class="options-bar-container do-not-print">\n                    <a href="https://psfmember.org/civicrm/contribute/transact?reset=1&id=2" class="donate-button">Donate</a>\n                    <div class="options-bar">\n                        \n                        <a id="site-map-link" class="jump-to-menu" href="#site-map"><span class="menu-icon">&equiv;</span> Menu</a><form class="search-the-site" action="/search/" method="get">\n                            <fieldset title="Search Python.org">\n\n                                <span aria-hidden="true" class="icon-search"></span>\n\n                                <label class="screen-reader-text" for="id-search-field">Search This Site</label>\n                                <input id="id-search-field" name="q" type="search" role="textbox" class="search-field" placeholder="Search" value="" tabindex="1">\n\n                                <button type="submit" name="submit" id="submit" class="search-button" title="Submit this Search" tabindex="3">\n                                    GO\n                                </button>\n\n                                \n                                <!--[if IE]><input type="text" style="display: none;" disabled="disabled" size="1" tabindex="4"><![endif]-->\n\n                            </fieldset>\n                        </form><span class="breaker"></span><div class="adjust-font-size" aria-hidden="true">\n                            <ul class="navigation menu" aria-label="Adjust Text Size on Page">\n                                <li class="tier-1 last" aria-haspopup="true">\n                                    <a href="#" class="action-trigger"><strong><small>A</small> A</strong></a>\n                                    <ul class="subnav menu">\n                                        <li class="tier-2 element-1" role="treeitem"><a class="text-shrink" title="Make Text Smaller" href="javascript:;">Smaller</a></li>\n                                        <li class="tier-2 element-2" role="treeitem"><a class="text-grow" title="Make Text Larger" href="javascript:;">Larger</a></li>\n                                        <li class="tier-2 element-3" role="treeitem"><a class="text-reset" title="Reset any font size changes I have made" href="javascript:;">Reset</a></li>\n                                    </ul>\n                                </li>\n                            </ul>\n                        </div><div class="winkwink-nudgenudge">\n                            <ul class="navigation menu" aria-label="Social Media Navigation">\n                                <li class="tier-1 last" aria-haspopup="true">\n                                    <a href="#" class="action-trigger">Socialize</a>\n                                    <ul class="subnav menu">\n                                        <li class="tier-2 element-1" role="treeitem"><a href="https://www.linkedin.com/company/python-software-foundation/"><i aria-hidden="true" class="fa fa-linkedin-square"></i>LinkedIn</a></li>\n                                        <li class="tier-2 element-2" role="treeitem"><a href="https://fosstodon.org/@ThePSF"><span aria-hidden="true" class="icon-mastodon"></span>Mastodon</a></li>\n                                        <li class="tier-2 element-3" role="treeitem"><a href="/community/irc/"><span aria-hidden="true" class="icon-freenode"></span>Chat on IRC</a></li>\n                                        <li class="tier-2 element-4" role="treeitem"><a href="https://twitter.com/ThePSF"><span aria-hidden="true" class="icon-twitter"></span>Twitter</a></li>\n                                    </ul>\n                                </li>\n                            </ul>\n                        </div>\n                        <span data-html-include="/authenticated"></span>\n                    </div><!-- end options-bar -->\n                </div>\n\n                <nav id="mainnav" class="python-navigation main-navigation do-not-print" role="navigation">\n                    \n                        \n<ul class="navigation menu" role="menubar" aria-label="Main Navigation">\n  \n    \n    \n    <li id="about" class="tier-1 element-1  " aria-haspopup="true">\n        <a href="/about/" title="" class="">About</a>\n        \n            \n\n<ul class="subnav menu" role="menu" aria-hidden="true">\n    \n        <li class="tier-2 element-1" role="treeitem"><a href="/about/apps/" title="">Applications</a></li>\n    \n        <li class="tier-2 element-2" role="treeitem"><a href="/about/quotes/" title="">Quotes</a></li>\n    \n        <li class="tier-2 element-3" role="treeitem"><a href="/about/gettingstarted/" title="">Getting Started</a></li>\n    \n        <li class="tier-2 element-4" role="treeitem"><a href="/about/help/" title="">Help</a></li>\n    \n        <li class="tier-2 element-5" role="treeitem"><a href="http://brochure.getpython.info/" title="">Python Brochure</a></li>\n    \n</ul>\n\n        \n    </li>\n    \n    \n    \n    <li id="downloads" class="tier-1 element-2  " aria-haspopup="true">\n        <a href="/downloads/" title="" class="">Downloads</a>\n        \n            \n\n<ul class="subnav menu" role="menu" aria-hidden="true">\n    \n        <li class="tier-2 element-1" role="treeitem"><a href="/downloads/" title="">All releases</a></li>\n    \n        <li class="tier-2 element-2" role="treeitem"><a href="/downloads/source/" title="">Source code</a></li>\n    \n        <li class="tier-2 element-3" role="treeitem"><a href="/downloads/windows/" title="">Windows</a></li>\n    \n        <li class="tier-2 element-4" role="treeitem"><a href="/downloads/macos/" title="">macOS</a></li>\n    \n        <li class="tier-2 element-5" role="treeitem"><a href="/download/other/" title="">Other Platforms</a></li>\n    \n        <li class="tier-2 element-6" role="treeitem"><a href="https://docs.python.org/3/license.html" title="">License</a></li>\n    \n        <li class="tier-2 element-7" role="treeitem"><a href="/download/alternatives" title="">Alternative Implementations</a></li>\n    \n</ul>\n\n        \n    </li>\n    \n    \n    \n    <li id="documentation" class="tier-1 element-3  " aria-haspopup="true">\n        <a href="/doc/" title="" class="">Documentation</a>\n        \n            \n\n<ul class="subnav menu" role="menu" aria-hidden="true">\n    \n        <li class="tier-2 element-1" role="treeitem"><a href="/doc/" title="">Docs</a></li>\n    \n        <li class="tier-2 element-2" role="treeitem"><a href="/doc/av" title="">Audio/Visual Talks</a></li>\n    \n        <li class="tier-2 element-3" role="treeitem"><a href="https://wiki.python.org/moin/BeginnersGuide" title="">Beginner&#x27;s Guide</a></li>\n    \n        <li class="tier-2 element-4" role="treeitem"><a href="https://devguide.python.org/" title="">Developer&#x27;s Guide</a></li>\n    \n        <li class="tier-2 element-5" role="treeitem"><a href="https://docs.python.org/faq/" title="">FAQ</a></li>\n    \n        <li class="tier-2 element-6" role="treeitem"><a href="http://wiki.python.org/moin/Languages" title="">Non-English Docs</a></li>\n    \n        <li class="tier-2 element-7" role="treeitem"><a href="https://peps.python.org" title="">PEP Index</a></li>\n    \n        <li class="tier-2 element-8" role="treeitem"><a href="https://wiki.python.org/moin/PythonBooks" title="">Python Books</a></li>\n    \n        <li class="tier-2 element-9" role="treeitem"><a href="/doc/essays/" title="">Python Essays</a></li>\n    \n</ul>\n\n        \n    </li>\n    \n    \n    \n    <li id="community" class="tier-1 element-4  " aria-haspopup="true">\n        <a href="/community/" title="" class="">Community</a>\n        \n            \n\n<ul class="subnav menu" role="menu" aria-hidden="true">\n    \n        <li class="tier-2 element-1" role="treeitem"><a href="/community/diversity/" title="">Diversity</a></li>\n    \n        <li class="tier-2 element-2" role="treeitem"><a href="/community/lists/" title="">Mailing Lists</a></li>\n    \n        <li class="tier-2 element-3" role="treeitem"><a href="/community/irc/" title="">IRC</a></li>\n    \n        <li class="tier-2 element-4" role="treeitem"><a href="/community/forums/" title="">Forums</a></li>\n    \n        <li class="tier-2 element-5" role="treeitem"><a href="/psf/annual-report/2024/" title="">PSF Annual Impact Report</a></li>\n    \n        <li class="tier-2 element-6" role="treeitem"><a href="/community/workshops/" title="">Python Conferences</a></li>\n    \n        <li class="tier-2 element-7" role="treeitem"><a href="/community/sigs/" title="">Special Interest Groups</a></li>\n    \n        <li class="tier-2 element-8" role="treeitem"><a href="/community/logos/" title="">Python Logo</a></li>\n    \n        <li class="tier-2 element-9" role="treeitem"><a href="https://wiki.python.org/moin/" title="">Python Wiki</a></li>\n    \n        <li class="tier-2 element-10" role="treeitem"><a href="/psf/conduct/" title="">Code of Conduct</a></li>\n    \n        <li class="tier-2 element-11" role="treeitem"><a href="/community/awards" title="">Community Awards</a></li>\n    \n        <li class="tier-2 element-12" role="treeitem"><a href="/psf/get-involved/" title="">Get Involved</a></li>\n    \n        <li class="tier-2 element-13" role="treeitem"><a href="/psf/community-stories/" title="">Shared Stories</a></li>\n    \n</ul>\n\n        \n    </li>\n    \n    \n    \n    <li id="success-stories" class="tier-1 element-5  " aria-haspopup="true">\n        <a href="/success-stories/" title="success-stories" class="">Success Stories</a>\n        \n            \n\n<ul class="subnav menu" role="menu" aria-hidden="true">\n    \n        <li class="tier-2 element-1" role="treeitem"><a href="/success-stories/category/arts/" title="">Arts</a></li>\n    \n        <li class="tier-2 element-2" role="treeitem"><a href="/success-stories/category/business/" title="">Business</a></li>\n    \n        <li class="tier-2 element-3" role="treeitem"><a href="/success-stories/category/education/" title="">Education</a></li>\n    \n        <li class="tier-2 element-4" role="treeitem"><a href="/success-stories/category/engineering/" title="">Engineering</a></li>\n    \n        <li class="tier-2 element-5" role="treeitem"><a href="/success-stories/category/government/" title="">Government</a></li>\n    \n        <li class="tier-2 element-6" role="treeitem"><a href="/success-stories/category/scientific/" title="">Scientific</a></li>\n    \n        <li class="tier-2 element-7" role="treeitem"><a href="/success-stories/category/software-development/" title="">Software Development</a></li>\n    \n</ul>\n\n        \n    </li>\n    \n    \n    \n    <li id="news" class="tier-1 element-6  " aria-haspopup="true">\n        <a href="/blogs/" title="News from around the Python world" class="">News</a>\n        \n            \n\n<ul class="subnav menu" role="menu" aria-hidden="true">\n    \n        <li class="tier-2 element-1" role="treeitem"><a href="/blogs/" title="Python Insider Blog Posts">Python News</a></li>\n    \n        <li class="tier-2 element-2" role="treeitem"><a href="/psf/newsletter/" title="Python Software Foundation Newsletter">PSF Newsletter</a></li>\n    \n        <li class="tier-2 element-3" role="treeitem"><a href="http://pyfound.blogspot.com/" title="PSF Blog">PSF News</a></li>\n    \n        <li class="tier-2 element-4" role="treeitem"><a href="http://pycon.blogspot.com/" title="PyCon Blog">PyCon US News</a></li>\n    \n        <li class="tier-2 element-5" role="treeitem"><a href="http://planetpython.org/" title="Planet Python">News from the Community</a></li>\n    \n</ul>\n\n        \n    </li>\n    \n    \n    \n    <li id="events" class="tier-1 element-7  " aria-haspopup="true">\n        <a href="/events/" title="" class="">Events</a>\n        \n            \n\n<ul class="subnav menu" role="menu" aria-hidden="true">\n    \n        <li class="tier-2 element-1" role="treeitem"><a href="/events/python-events/" title="">Python Events</a></li>\n    \n        <li class="tier-2 element-2" role="treeitem"><a href="/events/python-user-group/" title="">User Group Events</a></li>\n    \n        <li class="tier-2 element-3" role="treeitem"><a href="/events/python-events/past/" title="">Python Events Archive</a></li>\n    \n        <li class="tier-2 element-4" role="treeitem"><a href="/events/python-user-group/past/" title="">User Group Events Archive</a></li>\n    \n        <li class="tier-2 element-5" role="treeitem"><a href="https://wiki.python.org/moin/PythonEventsCalendar#Submitting_an_Event" title="">Submit an Event</a></li>\n    \n</ul>\n\n        \n    </li>\n    \n    \n    \n    \n  \n</ul>\n\n                    \n                </nav>\n\n                <div class="header-banner "> <!-- for optional "do-not-print" class -->\n                    \n        <div id="dive-into-python" class="flex-slideshow slideshow">\n\n            <ul class="launch-shell menu" id="launch-shell">\n                <li>\n                    <a class="button prompt" id="start-shell" data-shell-container="#dive-into-python" href="/shell/">&gt;_\n                        <span class="message">Launch Interactive Shell</span>\n                    </a>\n                </li>\n            </ul>\n\n            <ul class="slides menu">\n                \n                <li>\n                    <div class="slide-code"><pre><code><span class="comment"># Python 3: Fibonacci series up to n</span>\r\n>>> def fib(n):\r\n>>>     a, b = 0, 1\r\n>>>     while a &lt; n:\r\n>>>         print(a, end=\' \')\r\n>>>         a, b = b, a+b\r\n>>>     print()\r\n>>> fib(1000)\r\n<span class="output">0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987</span></code></pre></div>\n                    <div class="slide-copy"><h1>Functions Defined</h1>\r\n<p>The core of extensible programming is defining functions. Python allows mandatory and optional arguments, keyword arguments, and even arbitrary argument lists. <a href="//docs.python.org/3/tutorial/controlflow.html#defining-functions">More about defining functions in Python&nbsp;3</a></p></div>\n                </li>\n                \n                <li>\n                    <div class="slide-code"><pre><code><span class="comment"># Python 3: List comprehensions</span>\r\n>>> fruits = [\'Banana\', \'Apple\', \'Lime\']\r\n>>> loud_fruits = [fruit.upper() for fruit in fruits]\r\n>>> print(loud_fruits)\r\n<span class="output">[\'BANANA\', \'APPLE\', \'LIME\']</span>\r\n\r\n<span class="comment"># List and the enumerate function</span>\r\n>>> list(enumerate(fruits))\r\n<span class="output">[(0, \'Banana\'), (1, \'Apple\'), (2, \'Lime\')]</span></code></pre></div>\n                    <div class="slide-copy"><h1>Compound Data Types</h1>\r\n<p>Lists (known as arrays in other languages) are one of the compound data types that Python understands. Lists can be indexed, sliced and manipulated with other built-in functions. <a href="//docs.python.org/3/tutorial/introduction.html#lists">More about lists in Python&nbsp;3</a></p></div>\n                </li>\n                \n                <li>\n                    <div class="slide-code"><pre><code><span class="comment"># Python 3: Simple arithmetic</span>\r\n>>> 1 / 2\r\n<span class="output">0.5</span>\r\n>>> 2 ** 3\r\n<span class="output">8</span>\r\n>>> 17 / 3  <span class="comment"># classic division returns a float</span>\r\n<span class="output">5.666666666666667</span>\r\n>>> 17 // 3  <span class="comment"># floor division</span>\r\n<span class="output">5</span></code></pre></div>\n                    <div class="slide-copy"><h1>Intuitive Interpretation</h1>\r\n<p>Calculations are simple with Python, and expression syntax is straightforward: the operators <code>+</code>, <code>-</code>, <code>*</code> and <code>/</code> work as expected; parentheses <code>()</code> can be used for grouping. <a href="http://docs.python.org/3/tutorial/introduction.html#using-python-as-a-calculator">More about simple math functions in Python&nbsp;3</a>.</p></div>\n                </li>\n                \n                <li>\n                    <div class="slide-code"><pre><code><span class="comment"># For loop on a list</span>\r\n>>> numbers = [2, 4, 6, 8]\r\n>>> product = 1\r\n>>> for number in numbers:\r\n...    product = product * number\r\n... \r\n>>> print(\'The product is:\', product)\r\n<span class="output">The product is: 384</span></code></pre></div>\n                    <div class="slide-copy"><h1>All the Flow You&rsquo;d Expect</h1>\r\n<p>Python knows the usual control flow statements that other languages speak &mdash; <code>if</code>, <code>for</code>, <code>while</code> and <code>range</code> &mdash; with some of its own twists, of course. <a href="//docs.python.org/3/tutorial/controlflow.html">More control flow tools in Python&nbsp;3</a></p></div>\n                </li>\n                \n                <li>\n                    <div class="slide-code"><pre><code><span class="comment"># Simple output (with Unicode)</span>\r\n>>> print("Hello, I\'m Python!")\r\n<span class="output">Hello, I\'m Python!</span>\r\n<span class="comment"># Input, assignment</span>\r\n>>> name = input(\'What is your name?\\n\')\r\n<span class="output">What is your name?\r\nPython</span>\r\n>>> print(f\'Hi, {name}.\')\r\n<span class="output">Hi, Python.</span></code>\r\n</pre></div>\n                    <div class="slide-copy"><h1>Quick &amp; Easy to Learn</h1>\r\n<p>Experienced programmers in any other language can pick up Python very quickly, and beginners find the clean syntax and indentation structure easy to learn. <a href="//docs.python.org/3/tutorial/">Whet your appetite</a> with our Python&nbsp;3 overview.</p></div>\n                </li>\n                \n            </ul>\n        </div>\n\n\n                </div>\n\n                \n        <div class="introduction">\n            <p>Python is a programming language that lets you work quickly <span class="breaker"></span>and integrate systems more effectively. <a class="readmore" href="/doc/">Learn More</a></p>\n        </div>\n\n\n             </div><!-- end .container -->\n        </header>\n\n        <div id="content" class="content-wrapper">\n            <!-- Main Content Column -->\n            <div class="container">\n\n                <section class="main-content " role="main">\n\n                    \n                    \n\n                    \n\n                    \n\n                \n\n                <div class="row">\n\n                    <div class="small-widget get-started-widget">\n                        <h2 class="widget-title"><span aria-hidden="true" class="icon-get-started"></span>Get Started</h2>\r\n<p>Whether you\'re new to programming or an experienced developer, it\'s easy to learn and use Python.</p>\r\n<p><a href="/about/gettingstarted/">Start with our Beginner&rsquo;s Guide</a></p>\n                    </div>\n\n                    <div class="small-widget download-widget">\n                        <h2 class="widget-title"><span aria-hidden="true" class="icon-download"></span>Download</h2>\n<p>Python source code and installers are available for download for all versions!</p>\n<p>Latest: <a href="/downloads/release/python-3135/">Python 3.13.5</a></p>\n                    </div>\n\n                    <div class="small-widget documentation-widget">\n                        <h2 class="widget-title"><span aria-hidden="true" class="icon-documentation"></span>Docs</h2>\r\n<p>Documentation for Python\'s standard library, along with tutorials and guides, are available online.</p>\r\n<p><a href="https://docs.python.org">docs.python.org</a></p>\n                    </div>\n\n                    <div class="small-widget jobs-widget last">\n                        <h2 class="widget-title"><span aria-hidden="true" class="icon-jobs"></span>Jobs</h2>\r\n<p>Looking for work or have a Python related position that you\'re trying to hire for? Our <strong>relaunched community-run job board</strong> is the place to go.</p>\r\n<p><a href="//jobs.python.org">jobs.python.org</a></p>\n                    </div>\n\n                </div>\n\n                <div class="list-widgets row">\n\n                    <div class="medium-widget blog-widget">\n                        \n                        <div class="shrubbery">\n                        \n                            <h2 class="widget-title"><span aria-hidden="true" class="icon-news"></span>Latest News</h2>\n                            <p class="give-me-more"><a href="https://blog.python.org" title="More News">More</a></p>\n                            \n                            <ul class="menu">\n                                \n                                \n                                <li>\n<time datetime="2025-07-24T13:55:00.000003+00:00"><span class="say-no-more">2025-</span>07-24</time>\n <a href="https://pyfound.blogspot.com/2025/07/psf-board-nominations-opening-july-29th.html">PSF Board Election Nominations Opening July 29th</a></li>\n                                \n                                <li>\n<time datetime="2025-07-22T19:47:00.000001+00:00"><span class="say-no-more">2025-</span>07-22</time>\n <a href="https://pythoninsider.blogspot.com/2025/07/python-314-release-candidate-1-is-go.html">Python 3.14 release candidate 1 is go!</a></li>\n                                \n                                <li>\n<time datetime="2025-07-16T12:43:00.000002+00:00"><span class="say-no-more">2025-</span>07-16</time>\n <a href="https://pyfound.blogspot.com/2025/07/affirm-your-psf-membership-voting-status.html">Affirm Your PSF Membership Voting Status</a></li>\n                                \n                                <li>\n<time datetime="2025-07-09T01:00:00.000002+00:00"><span class="say-no-more">2025-</span>07-09</time>\n <a href="https://mailchi.mp/python/python-software-foundation-july-2024-newsletter-19880429">PSF News: PyPI Orgs, Board Election, &amp; Yearly Reports</a></li>\n                                \n                                <li>\n<time datetime="2025-07-08T15:21:00.000001+00:00"><span class="say-no-more">2025-</span>07-08</time>\n <a href="https://pyfound.blogspot.com/2025/07/notice-of-python-software-foundation.html">Notice of Python Software Foundation Bylaws Change - Effective July 23, 2025</a></li>\n                                \n                            </ul>\n                        </div><!-- end .shrubbery -->\n\n                    </div>\n\n                    <div class="medium-widget event-widget last">\n                        \n                        <div class="shrubbery">\n                        \n                            <h2 class="widget-title"><span aria-hidden="true" class="icon-calendar"></span>Upcoming Events</h2>\n                            <p class="give-me-more"><a href="/events/calendars/" title="More Events">More</a></p>\n                            \n                            <ul class="menu">\n                                \n                                \n                                \n                                <li>\n<time datetime="2025-08-08T00:00:00+00:00"><span class="say-no-more">2025-</span>08-08</time>\n <a href="/events/python-user-group/2081/">Buea - Creating Python Communities and outreach</a></li>\n                                \n                                \n                                \n                                <li>\n<time datetime="2025-08-11T00:00:00+00:00"><span class="say-no-more">2025-</span>08-11</time>\n <a href="/events/python-events/2011/">DjangoCon Africa 2025</a></li>\n                                \n                                \n                                \n                                <li>\n<time datetime="2025-08-13T00:00:00+00:00"><span class="say-no-more">2025-</span>08-13</time>\n <a href="/events/python-events/2077/">PyCon Somalia 2025</a></li>\n                                \n                                \n                                \n                                <li>\n<time datetime="2025-08-15T00:00:00+00:00"><span class="say-no-more">2025-</span>08-15</time>\n <a href="/events/python-events/1973/">PyCon Korea 2025</a></li>\n                                \n                                \n                                \n                                <li>\n<time datetime="2025-08-18T00:00:00+00:00"><span class="say-no-more">2025-</span>08-18</time>\n <a href="/events/python-events/1971/">EuroSciPy 2025</a></li>\n                                \n                                \n                            </ul>\n                        </div>\n\n                    </div>\n\n                </div>\n\n                <div class="row">\n\n                    <div class="medium-widget success-stories-widget">\n                        \n\n\n\n                        <div class="shrubbery">\n                            \n\n                            <h2 class="widget-title"><span aria-hidden="true" class="icon-success-stories"></span>Success Stories</h2>\n                            <p class="give-me-more"><a href="/success-stories/" title="More Success Stories">More</a></p>\n\n                            \n                            <div class="success-story-item" id="success-story-932">\n\n                            <blockquote>\n                                <a href="/success-stories/abridging-clinical-conversations-using-python/">Python powers major aspects of Abridge\xe2\x80\x99s ML lifecycle, including data annotation,  research and experimentation, and ML model deployment to production.</a>\n                            </blockquote>\n\n                            <table cellpadding="0" cellspacing="0" border="0" width="100%" class="quote-from">\n                                <tbody>\n                                    <tr>\n                                        \n                                        <td><p><a href="/success-stories/abridging-clinical-conversations-using-python/">Abridging clinical conversations using Python</a> <em>by Nimshi Venkat and Sandeep Konam</em></p></td>\n                                    </tr>\n                                </tbody>\n                            </table>\n                            </div>\n                            \n\n                        </div><!-- end .shrubbery -->\n\n                    </div>\n\n                    <div class="medium-widget applications-widget last">\n                        <div class="shrubbery">\n                            <h2 class="widget-title"><span aria-hidden="true" class="icon-python"></span>Use Python for&hellip;</h2>\r\n<p class="give-me-more"><a href="/about/apps" title="More Applications">More</a></p>\r\n\r\n<ul class="menu">\r\n    <li><b>Web Development</b>:\r\n        <span class="tag-wrapper"><a class="tag" href="http://www.djangoproject.com/">Django</a>, <a class="tag" href="http://www.pylonsproject.org/">Pyramid</a>, <a class="tag" href="http://bottlepy.org">Bottle</a>, <a class="tag" href="http://tornadoweb.org">Tornado</a>, <a href="http://flask.pocoo.org/" class="tag">Flask</a>, <a class="tag" href="http://www.web2py.com/">web2py</a></span></li>\r\n    <li><b>GUI Development</b>:\r\n        <span class="tag-wrapper"><a class="tag" href="http://wiki.python.org/moin/TkInter">tkInter</a>, <a class="tag" href="https://wiki.gnome.org/Projects/PyGObject">PyGObject</a>, <a class="tag" href="http://www.riverbankcomputing.co.uk/software/pyqt/intro">PyQt</a>, <a class="tag" href="https://wiki.qt.io/PySide">PySide</a>, <a class="tag" href="https://kivy.org/">Kivy</a>, <a class="tag" href="http://www.wxpython.org/">wxPython</a>, <a class="tag" href="https://dearpygui.readthedocs.io/en/latest/">DearPyGui</a></span></li>\r\n    <li><b>Scientific and Numeric</b>:\r\n        <span class="tag-wrapper">\r\n<a class="tag" href="http://www.scipy.org">SciPy</a>, <a class="tag" href="http://pandas.pydata.org/">Pandas</a>, <a href="http://ipython.org" class="tag">IPython</a></span></li>\r\n    <li><b>Software Development</b>:\r\n        <span class="tag-wrapper"><a class="tag" href="http://buildbot.net/">Buildbot</a>, <a class="tag" href="http://trac.edgewall.org/">Trac</a>, <a class="tag" href="http://roundup.sourceforge.net/">Roundup</a></span></li>\r\n    <li><b>System Administration</b>:\r\n        <span class="tag-wrapper"><a class="tag" href="http://www.ansible.com">Ansible</a>, <a class="tag" href="https://saltproject.io">Salt</a>, <a class="tag" href="https://www.openstack.org">OpenStack</a>, <a class="tag" href="https://xon.sh">xonsh</a></span></li>\r\n</ul>\n                        </div><!-- end .shrubbery -->\n                    </div>\n\n                </div>\n\n                                <div class="psf-widget">\n\n                    <div class="python-logo"></div>\n                    \n                    <h2 class="widget-title">\r\n    <span class="prompt">&gt;&gt;&gt;</span> <a href="/psf/">Python Software Foundation</a>\r\n</h2>\r\n<p>The mission of the Python Software Foundation is to promote, protect, and advance the Python programming language, and to support and facilitate the growth of a diverse and international community of Python programmers. <a class="readmore" href="/psf/">Learn more</a> </p>\r\n<p class="click-these">\r\n    <a class="button" href="/psf/membership/">Become a Member</a>\r\n    <a class="button" href="/psf/donations/">Donate to the PSF</a>\r\n</p>\n                </div>\n\n\n\n\n                </section>\n\n                \n                \n\n                \n                \n\n\n            </div><!-- end .container -->\n        </div><!-- end #content .content-wrapper -->\n\n        <!-- Footer and social media list -->\n        \n        <footer id="site-map" class="main-footer" role="contentinfo">\n            <div class="main-footer-links">\n                <div class="container">\n\n                    \n                    <a id="back-to-top-1" class="jump-link" href="#python-network"><span aria-hidden="true" class="icon-arrow-up"><span>&#9650;</span></span> Back to Top</a>\n\n                    \n\n<ul class="sitemap navigation menu do-not-print" role="tree" id="container">\n    \n    <li class="tier-1 element-1">\n        <a href="/about/" >About</a>\n        \n            \n\n<ul class="subnav menu">\n    \n        <li class="tier-2 element-1" role="treeitem"><a href="/about/apps/" title="">Applications</a></li>\n    \n        <li class="tier-2 element-2" role="treeitem"><a href="/about/quotes/" title="">Quotes</a></li>\n    \n        <li class="tier-2 element-3" role="treeitem"><a href="/about/gettingstarted/" title="">Getting Started</a></li>\n    \n        <li class="tier-2 element-4" role="treeitem"><a href="/about/help/" title="">Help</a></li>\n    \n        <li class="tier-2 element-5" role="treeitem"><a href="http://brochure.getpython.info/" title="">Python Brochure</a></li>\n    \n</ul>\n\n        \n    </li>\n    \n    <li class="tier-1 element-2">\n        <a href="/downloads/" >Downloads</a>\n        \n            \n\n<ul class="subnav menu">\n    \n        <li class="tier-2 element-1" role="treeitem"><a href="/downloads/" title="">All releases</a></li>\n    \n        <li class="tier-2 element-2" role="treeitem"><a href="/downloads/source/" title="">Source code</a></li>\n    \n        <li class="tier-2 element-3" role="treeitem"><a href="/downloads/windows/" title="">Windows</a></li>\n    \n        <li class="tier-2 element-4" role="treeitem"><a href="/downloads/macos/" title="">macOS</a></li>\n    \n        <li class="tier-2 element-5" role="treeitem"><a href="/download/other/" title="">Other Platforms</a></li>\n    \n        <li class="tier-2 element-6" role="treeitem"><a href="https://docs.python.org/3/license.html" title="">License</a></li>\n    \n        <li class="tier-2 element-7" role="treeitem"><a href="/download/alternatives" title="">Alternative Implementations</a></li>\n    \n</ul>\n\n        \n    </li>\n    \n    <li class="tier-1 element-3">\n        <a href="/doc/" >Documentation</a>\n        \n            \n\n<ul class="subnav menu">\n    \n        <li class="tier-2 element-1" role="treeitem"><a href="/doc/" title="">Docs</a></li>\n    \n        <li class="tier-2 element-2" role="treeitem"><a href="/doc/av" title="">Audio/Visual Talks</a></li>\n    \n        <li class="tier-2 element-3" role="treeitem"><a href="https://wiki.python.org/moin/BeginnersGuide" title="">Beginner&#x27;s Guide</a></li>\n    \n        <li class="tier-2 element-4" role="treeitem"><a href="https://devguide.python.org/" title="">Developer&#x27;s Guide</a></li>\n    \n        <li class="tier-2 element-5" role="treeitem"><a href="https://docs.python.org/faq/" title="">FAQ</a></li>\n    \n        <li class="tier-2 element-6" role="treeitem"><a href="http://wiki.python.org/moin/Languages" title="">Non-English Docs</a></li>\n    \n        <li class="tier-2 element-7" role="treeitem"><a href="https://peps.python.org" title="">PEP Index</a></li>\n    \n        <li class="tier-2 element-8" role="treeitem"><a href="https://wiki.python.org/moin/PythonBooks" title="">Python Books</a></li>\n    \n        <li class="tier-2 element-9" role="treeitem"><a href="/doc/essays/" title="">Python Essays</a></li>\n    \n</ul>\n\n        \n    </li>\n    \n    <li class="tier-1 element-4">\n        <a href="/community/" >Community</a>\n        \n            \n\n<ul class="subnav menu">\n    \n        <li class="tier-2 element-1" role="treeitem"><a href="/community/diversity/" title="">Diversity</a></li>\n    \n        <li class="tier-2 element-2" role="treeitem"><a href="/community/lists/" title="">Mailing Lists</a></li>\n    \n        <li class="tier-2 element-3" role="treeitem"><a href="/community/irc/" title="">IRC</a></li>\n    \n        <li class="tier-2 element-4" role="treeitem"><a href="/community/forums/" title="">Forums</a></li>\n    \n        <li class="tier-2 element-5" role="treeitem"><a href="/psf/annual-report/2024/" title="">PSF Annual Impact Report</a></li>\n    \n        <li class="tier-2 element-6" role="treeitem"><a href="/community/workshops/" title="">Python Conferences</a></li>\n    \n        <li class="tier-2 element-7" role="treeitem"><a href="/community/sigs/" title="">Special Interest Groups</a></li>\n    \n        <li class="tier-2 element-8" role="treeitem"><a href="/community/logos/" title="">Python Logo</a></li>\n    \n        <li class="tier-2 element-9" role="treeitem"><a href="https://wiki.python.org/moin/" title="">Python Wiki</a></li>\n    \n        <li class="tier-2 element-10" role="treeitem"><a href="/psf/conduct/" title="">Code of Conduct</a></li>\n    \n        <li class="tier-2 element-11" role="treeitem"><a href="/community/awards" title="">Community Awards</a></li>\n    \n        <li class="tier-2 element-12" role="treeitem"><a href="/psf/get-involved/" title="">Get Involved</a></li>\n    \n        <li class="tier-2 element-13" role="treeitem"><a href="/psf/community-stories/" title="">Shared Stories</a></li>\n    \n</ul>\n\n        \n    </li>\n    \n    <li class="tier-1 element-5">\n        <a href="/success-stories/" title="success-stories">Success Stories</a>\n        \n            \n\n<ul class="subnav menu">\n    \n        <li class="tier-2 element-1" role="treeitem"><a href="/success-stories/category/arts/" title="">Arts</a></li>\n    \n        <li class="tier-2 element-2" role="treeitem"><a href="/success-stories/category/business/" title="">Business</a></li>\n    \n        <li class="tier-2 element-3" role="treeitem"><a href="/success-stories/category/education/" title="">Education</a></li>\n    \n        <li class="tier-2 element-4" role="treeitem"><a href="/success-stories/category/engineering/" title="">Engineering</a></li>\n    \n        <li class="tier-2 element-5" role="treeitem"><a href="/success-stories/category/government/" title="">Government</a></li>\n    \n        <li class="tier-2 element-6" role="treeitem"><a href="/success-stories/category/scientific/" title="">Scientific</a></li>\n    \n        <li class="tier-2 element-7" role="treeitem"><a href="/success-stories/category/software-development/" title="">Software Development</a></li>\n    \n</ul>\n\n        \n    </li>\n    \n    <li class="tier-1 element-6">\n        <a href="/blogs/" title="News from around the Python world">News</a>\n        \n            \n\n<ul class="subnav menu">\n    \n        <li class="tier-2 element-1" role="treeitem"><a href="/blogs/" title="Python Insider Blog Posts">Python News</a></li>\n    \n        <li class="tier-2 element-2" role="treeitem"><a href="/psf/newsletter/" title="Python Software Foundation Newsletter">PSF Newsletter</a></li>\n    \n        <li class="tier-2 element-3" role="treeitem"><a href="http://pyfound.blogspot.com/" title="PSF Blog">PSF News</a></li>\n    \n        <li class="tier-2 element-4" role="treeitem"><a href="http://pycon.blogspot.com/" title="PyCon Blog">PyCon US News</a></li>\n    \n        <li class="tier-2 element-5" role="treeitem"><a href="http://planetpython.org/" title="Planet Python">News from the Community</a></li>\n    \n</ul>\n\n        \n    </li>\n    \n    <li class="tier-1 element-7">\n        <a href="/events/" >Events</a>\n        \n            \n\n<ul class="subnav menu">\n    \n        <li class="tier-2 element-1" role="treeitem"><a href="/events/python-events/" title="">Python Events</a></li>\n    \n        <li class="tier-2 element-2" role="treeitem"><a href="/events/python-user-group/" title="">User Group Events</a></li>\n    \n        <li class="tier-2 element-3" role="treeitem"><a href="/events/python-events/past/" title="">Python Events Archive</a></li>\n    \n        <li class="tier-2 element-4" role="treeitem"><a href="/events/python-user-group/past/" title="">User Group Events Archive</a></li>\n    \n        <li class="tier-2 element-5" role="treeitem"><a href="https://wiki.python.org/moin/PythonEventsCalendar#Submitting_an_Event" title="">Submit an Event</a></li>\n    \n</ul>\n\n        \n    </li>\n    \n    <li class="tier-1 element-8">\n        <a href="/dev/" >Contributing</a>\n        \n            \n\n<ul class="subnav menu">\n    \n        <li class="tier-2 element-1" role="treeitem"><a href="https://devguide.python.org/" title="">Developer&#x27;s Guide</a></li>\n    \n        <li class="tier-2 element-2" role="treeitem"><a href="https://github.com/python/cpython/issues" title="">Issue Tracker</a></li>\n    \n        <li class="tier-2 element-3" role="treeitem"><a href="https://mail.python.org/mailman/listinfo/python-dev" title="">python-dev list</a></li>\n    \n        <li class="tier-2 element-4" role="treeitem"><a href="/dev/core-mentorship/" title="">Core Mentorship</a></li>\n    \n        <li class="tier-2 element-5" role="treeitem"><a href="/dev/security/" title="">Report a Security Issue</a></li>\n    \n</ul>\n\n        \n    </li>\n    \n</ul>\n\n\n                    <a id="back-to-top-2" class="jump-link" href="#python-network"><span aria-hidden="true" class="icon-arrow-up"><span>&#9650;</span></span> Back to Top</a>\n                    \n\n                </div><!-- end .container -->\n            </div> <!-- end .main-footer-links -->\n\n            <div class="site-base">\n                <div class="container">\n                    \n                    <ul class="footer-links navigation menu do-not-print" role="tree">\n                        <li class="tier-1 element-1"><a href="/about/help/">Help &amp; <span class="say-no-more">General</span> Contact</a></li>\n                        <li class="tier-1 element-2"><a href="/community/diversity/">Diversity <span class="say-no-more">Initiatives</span></a></li>\n                        <li class="tier-1 element-3"><a href="https://github.com/python/pythondotorg/issues">Submit Website Bug</a></li>\n                        <li class="tier-1 element-4">\n                            <a href="https://status.python.org/">Status <span class="python-status-indicator-default" id="python-status-indicator"></span></a>\n                        </li>\n                    </ul>\n\n                    <div class="copyright">\n                        <p><small>\n                            <span class="pre">Copyright &copy;2001-2025.</span>\n                            &nbsp;<span class="pre"><a href="/psf-landing/">Python Software Foundation</a></span>\n                            &nbsp;<span class="pre"><a href="/about/legal/">Legal Statements</a></span>\n                            &nbsp;<span class="pre"><a href="https://policies.python.org/python.org/Privacy-Notice/">Privacy Notice</a></span>\n                            <!--&nbsp;<span class="pre"><a href="/psf/community-infrastructure">Powered by PSF Community Infrastructure</a></span>-->\n                        </small></p>\n                    </div>\n\n                </div><!-- end .container -->\n            </div><!-- end .site-base -->\n\n        </footer>\n        \n\n    </div><!-- end #touchnav-wrapper -->\n\n    \n    <script src="//ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js"></script>\n    <script>window.jQuery || document.write(\'<script src="/static/js/libs/jquery-1.8.2.min.js"><\\/script>\')</script>\n    <script src="//ajax.googleapis.com/ajax/libs/jqueryui/1.12.1/jquery-ui.min.js"></script>\n    <script>window.jQuery || document.write(\'<script src="/static/js/libs/jquery-ui-1.12.1.min.js"><\\/script>\')</script>\n\n    <script src="/static/js/libs/masonry.pkgd.min.js"></script>\n    <script src="/static/js/libs/html-includes.js"></script>\n\n    <script type="text/javascript" src="/static/js/main-min.ef82c06437cf.js" charset="utf-8"></script>\n    \n\n    <!--[if lte IE 7]>\n    <script type="text/javascript" src="/static/js/plugins/IE8-min.8af6e26c7a3b.js" charset="utf-8"></script>\n    \n    \n    <![endif]-->\n\n    <!--[if lte IE 8]>\n    <script type="text/javascript" src="/static/js/plugins/getComputedStyle-min.d41d8cd98f00.js" charset="utf-8"></script>\n    \n    \n    <![endif]-->\n\n    \n\n    \n    \n\n</body>\n</html>\n'
########################################

Create object of BeautifulSoup class with website data
--------------------
<!DOCTYPE html>

<!--[if lt IE 7]>   <html class="no-js ie6 lt-ie7 lt-ie8 lt-ie9">   <![endif]-->
<!--[if IE 7]>      <html class="no-js ie7 lt-ie8 lt-ie9">          <![endif]-->
<!--[if IE 8]>      <html class="no-js ie8 lt-ie9">                 <![endif]-->
<!--[if gt IE 8]><!--><html class="no-js" dir="ltr" lang="en"> <!--<![endif]-->
<head>
<script data-domain="python.org" defer="" src="https://analytics.python.org/js/script.outbound-links.js"></script>
<meta charset="utf-8"/>
<meta content="IE=edge" http-equiv="X-UA-Compatible"/>
<link href="//ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js" rel="prefetch"/>
<link href="//ajax.googleapis.com/ajax/libs/jqueryui/1.12.1/jquery-ui.min.js" rel="prefetch"/>
<meta content="Python.org" name="application-name"/>
<meta content="The official home of the Python Programming Language" name="msapplication-tooltip"/>
<meta content="Python.org" name="apple-mobile-web-app-title"/>
<meta content="yes" name="apple-mobile-web-app-capable"/>
<meta content="black" name="apple-mobile-web-app-status-bar-style"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<meta content="True" name="HandheldFriendly"/>
<meta content="telephone=no" name="format-detection"/>
<meta content="on" http-equiv="cleartype"/>
<meta content="false" http-equiv="imagetoolbar"/>
<script async="" crossorigin="anonymous" integrity="sha256-U3hKDidudIaxBDEzwGJApJgPEf2mWk6cfMWghrAa6i0= sha384-UcmsCqcNRSLW/dV3Lo1oCi2/VaurXbib6p4HyUEOeIa/4OpsrnucrugAefzVZJfI sha512-q4t1L4xEjGV2R4hzqCa41P8jrgFUS8xTb8rdNv4FGvw7FpydVj/kkxBJHOiaoxHa8olCcx1Slk9K+3sNbsM4ug==" src="https://media.ethicalads.io/media/client/v1.4.0/ethicalads.min.js"></script>
<script src="/static/js/libs/modernizr.js"></script>
<link href="/static/stylesheets/style.08a078d0aa02.css" media="all" rel="stylesheet" title="default" type="text/css">
<link href="/static/stylesheets/mq.98d6092b2ada.css" media="not print, braille, embossed, speech, tty" rel="stylesheet" type="text/css">
<link href="/static/stylesheets/no-mq.bf0c425cdb73.css" media="screen" rel="stylesheet" type="text/css"/>
<!--[if (lte IE 8)&(!IEMobile)]>
    <link href="/static/stylesheets/no-mq.bf0c425cdb73.css" rel="stylesheet" type="text/css" media="screen" />
    
    
    <![endif]-->
<link href="//ajax.googleapis.com/ajax/libs/jqueryui/1.12.1/themes/smoothness/jquery-ui.css" rel="stylesheet"/>
<link href="/static/favicon.ico" rel="icon" type="image/x-icon"/>
<link href="/static/apple-touch-icon-144x144-precomposed.png" rel="apple-touch-icon-precomposed" sizes="144x144"/>
<link href="/static/apple-touch-icon-114x114-precomposed.png" rel="apple-touch-icon-precomposed" sizes="114x114"/>
<link href="/static/apple-touch-icon-72x72-precomposed.png" rel="apple-touch-icon-precomposed" sizes="72x72"/>
<link href="/static/apple-touch-icon-precomposed.png" rel="apple-touch-icon-precomposed"/>
<link href="/static/apple-touch-icon-precomposed.png" rel="apple-touch-icon"/>
<meta content="/static/metro-icon-144x144.png" name="msapplication-TileImage"/><!-- white shape -->
<meta content="#3673a5" name="msapplication-TileColor"/><!-- python blue -->
<meta content="#3673a5" name="msapplication-navbutton-color"/>
<title>Welcome to Python.org</title>
<meta content="The official home of the Python Programming Language" name="description"/>
<meta content="Python programming language object oriented web free open source software license documentation download community" name="keywords"/>
<meta content="website" property="og:type"/>
<meta content="Python.org" property="og:site_name"/>
<meta content="Welcome to Python.org" property="og:title"/>
<meta content="The official home of the Python Programming Language" property="og:description"/>
<meta content="https://www.python.org/static/opengraph-icon-200x200.png" property="og:image"/>
<meta content="https://www.python.org/static/opengraph-icon-200x200.png" property="og:image:secure_url"/>
<meta content="https://www.python.org/" property="og:url"/>
<link href="/humans.txt" rel="author"/>
<link href="https://peps.python.org/peps.rss" rel="alternate" title="Python Enhancement Proposals" type="application/rss+xml"/>
<link href="https://www.python.org/jobs/feed/rss/" rel="alternate" title="Python Job Opportunities" type="application/rss+xml"/>
<link href="https://feeds.feedburner.com/PythonSoftwareFoundationNews" rel="alternate" title="Python Software Foundation News" type="application/rss+xml"/>
<link href="https://feeds.feedburner.com/PythonInsider" rel="alternate" title="Python Insider" type="application/rss+xml"/>
<link href="https://www.python.org/downloads/feed.rss" rel="alternate" title="Python Releases" type="application/rss+xml"/>
<script type="application/ld+json">
     {
       "@context": "https://schema.org",
       "@type": "WebSite",
       "url": "https://www.python.org/",
       "potentialAction": {
         "@type": "SearchAction",
         "target": "https://www.python.org/search/?q={search_term_string}",
         "query-input": "required name=search_term_string"
       }
     }
    </script>
<script type="text/javascript">
    var _gaq = _gaq || [];
    _gaq.push(['_setAccount', 'UA-39055973-1']);
    _gaq.push(['_trackPageview']);

    (function() {
        var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
        ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
        var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
    })();
    </script>
</link></link></head>
<body class="python home" id="homepage">
<div id="touchnav-wrapper">
<div class="do-not-print" id="nojs">
<p><strong>Notice:</strong> While JavaScript is not essential for this website, your interaction with the content will be limited. Please turn JavaScript on for the full experience. </p>
</div>
<!--[if lte IE 8]>
        <div id="oldie-warning" class="do-not-print">
            <p>
                <strong>Notice:</strong> Your browser is <em>ancient</em>. Please
                <a href="http://browsehappy.com/">upgrade to a different browser</a> to experience a better web.
            </p>
        </div>
        <![endif]-->
<!-- Sister Site Links -->
<div class="top-bar do-not-print" id="top">
<nav class="meta-navigation container" role="navigation">
<div class="skip-link screen-reader-text">
<a href="#content" title="Skip to content">Skip to content</a>
</div>
<a aria-hidden="true" class="jump-link" href="#python-network" id="close-python-network">
<span aria-hidden="true" class="icon-arrow-down"><span>▼</span></span> Close
                </a>
<ul class="menu" role="tree">
<li class="python-meta current_item selectedcurrent_branch selected">
<a class="current_item selectedcurrent_branch selected" href="/" title="The Python Programming Language">Python</a>
</li>
<li class="psf-meta">
<a href="https://www.python.org/psf/" title="The Python Software Foundation">PSF</a>
</li>
<li class="docs-meta">
<a href="https://docs.python.org" title="Python Documentation">Docs</a>
</li>
<li class="pypi-meta">
<a href="https://pypi.org/" title="Python Package Index">PyPI</a>
</li>
<li class="jobs-meta">
<a href="/jobs/" title="Python Job Board">Jobs</a>
</li>
<li class="shop-meta">
<a href="/community/">Community</a>
</li>
</ul>
<a aria-hidden="true" class="jump-link" href="#top" id="python-network">
<span aria-hidden="true" class="icon-arrow-up"><span>▲</span></span> The Python Network
                </a>
</nav>
</div>
<!-- Header elements -->
<header class="main-header" role="banner">
<div class="container">
<h1 class="site-headline">
<a href="/"><img alt="python™" class="python-logo" src="/static/img/python-logo.png"/></a>
</h1>
<div class="options-bar-container do-not-print">
<a class="donate-button" href="https://psfmember.org/civicrm/contribute/transact?reset=1&amp;id=2">Donate</a>
<div class="options-bar">
<a class="jump-to-menu" href="#site-map" id="site-map-link"><span class="menu-icon">≡</span> Menu</a><form action="/search/" class="search-the-site" method="get">
<fieldset title="Search Python.org">
<span aria-hidden="true" class="icon-search"></span>
<label class="screen-reader-text" for="id-search-field">Search This Site</label>
<input class="search-field" id="id-search-field" name="q" placeholder="Search" role="textbox" tabindex="1" type="search" value=""/>
<button class="search-button" id="submit" name="submit" tabindex="3" title="Submit this Search" type="submit">
                                    GO
                                </button>
<!--[if IE]><input type="text" style="display: none;" disabled="disabled" size="1" tabindex="4"><![endif]-->
</fieldset>
</form><span class="breaker"></span><div aria-hidden="true" class="adjust-font-size">
<ul aria-label="Adjust Text Size on Page" class="navigation menu">
<li aria-haspopup="true" class="tier-1 last">
<a class="action-trigger" href="#"><strong><small>A</small> A</strong></a>
<ul class="subnav menu">
<li class="tier-2 element-1" role="treeitem"><a class="text-shrink" href="javascript:;" title="Make Text Smaller">Smaller</a></li>
<li class="tier-2 element-2" role="treeitem"><a class="text-grow" href="javascript:;" title="Make Text Larger">Larger</a></li>
<li class="tier-2 element-3" role="treeitem"><a class="text-reset" href="javascript:;" title="Reset any font size changes I have made">Reset</a></li>
</ul>
</li>
</ul>
</div><div class="winkwink-nudgenudge">
<ul aria-label="Social Media Navigation" class="navigation menu">
<li aria-haspopup="true" class="tier-1 last">
<a class="action-trigger" href="#">Socialize</a>
<ul class="subnav menu">
<li class="tier-2 element-1" role="treeitem"><a href="https://www.linkedin.com/company/python-software-foundation/"><i aria-hidden="true" class="fa fa-linkedin-square"></i>LinkedIn</a></li>
<li class="tier-2 element-2" role="treeitem"><a href="https://fosstodon.org/@ThePSF"><span aria-hidden="true" class="icon-mastodon"></span>Mastodon</a></li>
<li class="tier-2 element-3" role="treeitem"><a href="/community/irc/"><span aria-hidden="true" class="icon-freenode"></span>Chat on IRC</a></li>
<li class="tier-2 element-4" role="treeitem"><a href="https://twitter.com/ThePSF"><span aria-hidden="true" class="icon-twitter"></span>Twitter</a></li>
</ul>
</li>
</ul>
</div>
<span data-html-include="/authenticated"></span>
</div><!-- end options-bar -->
</div>
<nav class="python-navigation main-navigation do-not-print" id="mainnav" role="navigation">
<ul aria-label="Main Navigation" class="navigation menu" role="menubar">
<li aria-haspopup="true" class="tier-1 element-1" id="about">
<a class="" href="/about/" title="">About</a>
<ul aria-hidden="true" class="subnav menu" role="menu">
<li class="tier-2 element-1" role="treeitem"><a href="/about/apps/" title="">Applications</a></li>
<li class="tier-2 element-2" role="treeitem"><a href="/about/quotes/" title="">Quotes</a></li>
<li class="tier-2 element-3" role="treeitem"><a href="/about/gettingstarted/" title="">Getting Started</a></li>
<li class="tier-2 element-4" role="treeitem"><a href="/about/help/" title="">Help</a></li>
<li class="tier-2 element-5" role="treeitem"><a href="http://brochure.getpython.info/" title="">Python Brochure</a></li>
</ul>
</li>
<li aria-haspopup="true" class="tier-1 element-2" id="downloads">
<a class="" href="/downloads/" title="">Downloads</a>
<ul aria-hidden="true" class="subnav menu" role="menu">
<li class="tier-2 element-1" role="treeitem"><a href="/downloads/" title="">All releases</a></li>
<li class="tier-2 element-2" role="treeitem"><a href="/downloads/source/" title="">Source code</a></li>
<li class="tier-2 element-3" role="treeitem"><a href="/downloads/windows/" title="">Windows</a></li>
<li class="tier-2 element-4" role="treeitem"><a href="/downloads/macos/" title="">macOS</a></li>
<li class="tier-2 element-5" role="treeitem"><a href="/download/other/" title="">Other Platforms</a></li>
<li class="tier-2 element-6" role="treeitem"><a href="https://docs.python.org/3/license.html" title="">License</a></li>
<li class="tier-2 element-7" role="treeitem"><a href="/download/alternatives" title="">Alternative Implementations</a></li>
</ul>
</li>
<li aria-haspopup="true" class="tier-1 element-3" id="documentation">
<a class="" href="/doc/" title="">Documentation</a>
<ul aria-hidden="true" class="subnav menu" role="menu">
<li class="tier-2 element-1" role="treeitem"><a href="/doc/" title="">Docs</a></li>
<li class="tier-2 element-2" role="treeitem"><a href="/doc/av" title="">Audio/Visual Talks</a></li>
<li class="tier-2 element-3" role="treeitem"><a href="https://wiki.python.org/moin/BeginnersGuide" title="">Beginner's Guide</a></li>
<li class="tier-2 element-4" role="treeitem"><a href="https://devguide.python.org/" title="">Developer's Guide</a></li>
<li class="tier-2 element-5" role="treeitem"><a href="https://docs.python.org/faq/" title="">FAQ</a></li>
<li class="tier-2 element-6" role="treeitem"><a href="http://wiki.python.org/moin/Languages" title="">Non-English Docs</a></li>
<li class="tier-2 element-7" role="treeitem"><a href="https://peps.python.org" title="">PEP Index</a></li>
<li class="tier-2 element-8" role="treeitem"><a href="https://wiki.python.org/moin/PythonBooks" title="">Python Books</a></li>
<li class="tier-2 element-9" role="treeitem"><a href="/doc/essays/" title="">Python Essays</a></li>
</ul>
</li>
<li aria-haspopup="true" class="tier-1 element-4" id="community">
<a class="" href="/community/" title="">Community</a>
<ul aria-hidden="true" class="subnav menu" role="menu">
<li class="tier-2 element-1" role="treeitem"><a href="/community/diversity/" title="">Diversity</a></li>
<li class="tier-2 element-2" role="treeitem"><a href="/community/lists/" title="">Mailing Lists</a></li>
<li class="tier-2 element-3" role="treeitem"><a href="/community/irc/" title="">IRC</a></li>
<li class="tier-2 element-4" role="treeitem"><a href="/community/forums/" title="">Forums</a></li>
<li class="tier-2 element-5" role="treeitem"><a href="/psf/annual-report/2024/" title="">PSF Annual Impact Report</a></li>
<li class="tier-2 element-6" role="treeitem"><a href="/community/workshops/" title="">Python Conferences</a></li>
<li class="tier-2 element-7" role="treeitem"><a href="/community/sigs/" title="">Special Interest Groups</a></li>
<li class="tier-2 element-8" role="treeitem"><a href="/community/logos/" title="">Python Logo</a></li>
<li class="tier-2 element-9" role="treeitem"><a href="https://wiki.python.org/moin/" title="">Python Wiki</a></li>
<li class="tier-2 element-10" role="treeitem"><a href="/psf/conduct/" title="">Code of Conduct</a></li>
<li class="tier-2 element-11" role="treeitem"><a href="/community/awards" title="">Community Awards</a></li>
<li class="tier-2 element-12" role="treeitem"><a href="/psf/get-involved/" title="">Get Involved</a></li>
<li class="tier-2 element-13" role="treeitem"><a href="/psf/community-stories/" title="">Shared Stories</a></li>
</ul>
</li>
<li aria-haspopup="true" class="tier-1 element-5" id="success-stories">
<a class="" href="/success-stories/" title="success-stories">Success Stories</a>
<ul aria-hidden="true" class="subnav menu" role="menu">
<li class="tier-2 element-1" role="treeitem"><a href="/success-stories/category/arts/" title="">Arts</a></li>
<li class="tier-2 element-2" role="treeitem"><a href="/success-stories/category/business/" title="">Business</a></li>
<li class="tier-2 element-3" role="treeitem"><a href="/success-stories/category/education/" title="">Education</a></li>
<li class="tier-2 element-4" role="treeitem"><a href="/success-stories/category/engineering/" title="">Engineering</a></li>
<li class="tier-2 element-5" role="treeitem"><a href="/success-stories/category/government/" title="">Government</a></li>
<li class="tier-2 element-6" role="treeitem"><a href="/success-stories/category/scientific/" title="">Scientific</a></li>
<li class="tier-2 element-7" role="treeitem"><a href="/success-stories/category/software-development/" title="">Software Development</a></li>
</ul>
</li>
<li aria-haspopup="true" class="tier-1 element-6" id="news">
<a class="" href="/blogs/" title="News from around the Python world">News</a>
<ul aria-hidden="true" class="subnav menu" role="menu">
<li class="tier-2 element-1" role="treeitem"><a href="/blogs/" title="Python Insider Blog Posts">Python News</a></li>
<li class="tier-2 element-2" role="treeitem"><a href="/psf/newsletter/" title="Python Software Foundation Newsletter">PSF Newsletter</a></li>
<li class="tier-2 element-3" role="treeitem"><a href="http://pyfound.blogspot.com/" title="PSF Blog">PSF News</a></li>
<li class="tier-2 element-4" role="treeitem"><a href="http://pycon.blogspot.com/" title="PyCon Blog">PyCon US News</a></li>
<li class="tier-2 element-5" role="treeitem"><a href="http://planetpython.org/" title="Planet Python">News from the Community</a></li>
</ul>
</li>
<li aria-haspopup="true" class="tier-1 element-7" id="events">
<a class="" href="/events/" title="">Events</a>
<ul aria-hidden="true" class="subnav menu" role="menu">
<li class="tier-2 element-1" role="treeitem"><a href="/events/python-events/" title="">Python Events</a></li>
<li class="tier-2 element-2" role="treeitem"><a href="/events/python-user-group/" title="">User Group Events</a></li>
<li class="tier-2 element-3" role="treeitem"><a href="/events/python-events/past/" title="">Python Events Archive</a></li>
<li class="tier-2 element-4" role="treeitem"><a href="/events/python-user-group/past/" title="">User Group Events Archive</a></li>
<li class="tier-2 element-5" role="treeitem"><a href="https://wiki.python.org/moin/PythonEventsCalendar#Submitting_an_Event" title="">Submit an Event</a></li>
</ul>
</li>
</ul>
</nav>
<div class="header-banner"> <!-- for optional "do-not-print" class -->
<div class="flex-slideshow slideshow" id="dive-into-python">
<ul class="launch-shell menu" id="launch-shell">
<li>
<a class="button prompt" data-shell-container="#dive-into-python" href="/shell/" id="start-shell">&gt;_
                        <span class="message">Launch Interactive Shell</span>
</a>
</li>
</ul>
<ul class="slides menu">
<li>
<div class="slide-code"><pre><code><span class="comment"># Python 3: Fibonacci series up to n</span>
&gt;&gt;&gt; def fib(n):
&gt;&gt;&gt;     a, b = 0, 1
&gt;&gt;&gt;     while a &lt; n:
&gt;&gt;&gt;         print(a, end=' ')
&gt;&gt;&gt;         a, b = b, a+b
&gt;&gt;&gt;     print()
&gt;&gt;&gt; fib(1000)
<span class="output">0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987</span></code></pre></div>
<div class="slide-copy"><h1>Functions Defined</h1>
<p>The core of extensible programming is defining functions. Python allows mandatory and optional arguments, keyword arguments, and even arbitrary argument lists. <a href="//docs.python.org/3/tutorial/controlflow.html#defining-functions">More about defining functions in Python 3</a></p></div>
</li>
<li>
<div class="slide-code"><pre><code><span class="comment"># Python 3: List comprehensions</span>
&gt;&gt;&gt; fruits = ['Banana', 'Apple', 'Lime']
&gt;&gt;&gt; loud_fruits = [fruit.upper() for fruit in fruits]
&gt;&gt;&gt; print(loud_fruits)
<span class="output">['BANANA', 'APPLE', 'LIME']</span>

<span class="comment"># List and the enumerate function</span>
&gt;&gt;&gt; list(enumerate(fruits))
<span class="output">[(0, 'Banana'), (1, 'Apple'), (2, 'Lime')]</span></code></pre></div>
<div class="slide-copy"><h1>Compound Data Types</h1>
<p>Lists (known as arrays in other languages) are one of the compound data types that Python understands. Lists can be indexed, sliced and manipulated with other built-in functions. <a href="//docs.python.org/3/tutorial/introduction.html#lists">More about lists in Python 3</a></p></div>
</li>
<li>
<div class="slide-code"><pre><code><span class="comment"># Python 3: Simple arithmetic</span>
&gt;&gt;&gt; 1 / 2
<span class="output">0.5</span>
&gt;&gt;&gt; 2 ** 3
<span class="output">8</span>
&gt;&gt;&gt; 17 / 3  <span class="comment"># classic division returns a float</span>
<span class="output">5.666666666666667</span>
&gt;&gt;&gt; 17 // 3  <span class="comment"># floor division</span>
<span class="output">5</span></code></pre></div>
<div class="slide-copy"><h1>Intuitive Interpretation</h1>
<p>Calculations are simple with Python, and expression syntax is straightforward: the operators <code>+</code>, <code>-</code>, <code>*</code> and <code>/</code> work as expected; parentheses <code>()</code> can be used for grouping. <a href="http://docs.python.org/3/tutorial/introduction.html#using-python-as-a-calculator">More about simple math functions in Python 3</a>.</p></div>
</li>
<li>
<div class="slide-code"><pre><code><span class="comment"># For loop on a list</span>
&gt;&gt;&gt; numbers = [2, 4, 6, 8]
&gt;&gt;&gt; product = 1
&gt;&gt;&gt; for number in numbers:
...    product = product * number
... 
&gt;&gt;&gt; print('The product is:', product)
<span class="output">The product is: 384</span></code></pre></div>
<div class="slide-copy"><h1>All the Flow You’d Expect</h1>
<p>Python knows the usual control flow statements that other languages speak — <code>if</code>, <code>for</code>, <code>while</code> and <code>range</code> — with some of its own twists, of course. <a href="//docs.python.org/3/tutorial/controlflow.html">More control flow tools in Python 3</a></p></div>
</li>
<li>
<div class="slide-code"><pre><code><span class="comment"># Simple output (with Unicode)</span>
&gt;&gt;&gt; print("Hello, I'm Python!")
<span class="output">Hello, I'm Python!</span>
<span class="comment"># Input, assignment</span>
&gt;&gt;&gt; name = input('What is your name?\n')
<span class="output">What is your name?
Python</span>
&gt;&gt;&gt; print(f'Hi, {name}.')
<span class="output">Hi, Python.</span></code>
</pre></div>
<div class="slide-copy"><h1>Quick &amp; Easy to Learn</h1>
<p>Experienced programmers in any other language can pick up Python very quickly, and beginners find the clean syntax and indentation structure easy to learn. <a href="//docs.python.org/3/tutorial/">Whet your appetite</a> with our Python 3 overview.</p></div>
</li>
</ul>
</div>
</div>
<div class="introduction">
<p>Python is a programming language that lets you work quickly <span class="breaker"></span>and integrate systems more effectively. <a class="readmore" href="/doc/">Learn More</a></p>
</div>
</div><!-- end .container -->
</header>
<div class="content-wrapper" id="content">
<!-- Main Content Column -->
<div class="container">
<section class="main-content" role="main">
<div class="row">
<div class="small-widget get-started-widget">
<h2 class="widget-title"><span aria-hidden="true" class="icon-get-started"></span>Get Started</h2>
<p>Whether you're new to programming or an experienced developer, it's easy to learn and use Python.</p>
<p><a href="/about/gettingstarted/">Start with our Beginner’s Guide</a></p>
</div>
<div class="small-widget download-widget">
<h2 class="widget-title"><span aria-hidden="true" class="icon-download"></span>Download</h2>
<p>Python source code and installers are available for download for all versions!</p>
<p>Latest: <a href="/downloads/release/python-3135/">Python 3.13.5</a></p>
</div>
<div class="small-widget documentation-widget">
<h2 class="widget-title"><span aria-hidden="true" class="icon-documentation"></span>Docs</h2>
<p>Documentation for Python's standard library, along with tutorials and guides, are available online.</p>
<p><a href="https://docs.python.org">docs.python.org</a></p>
</div>
<div class="small-widget jobs-widget last">
<h2 class="widget-title"><span aria-hidden="true" class="icon-jobs"></span>Jobs</h2>
<p>Looking for work or have a Python related position that you're trying to hire for? Our <strong>relaunched community-run job board</strong> is the place to go.</p>
<p><a href="//jobs.python.org">jobs.python.org</a></p>
</div>
</div>
<div class="list-widgets row">
<div class="medium-widget blog-widget">
<div class="shrubbery">
<h2 class="widget-title"><span aria-hidden="true" class="icon-news"></span>Latest News</h2>
<p class="give-me-more"><a href="https://blog.python.org" title="More News">More</a></p>
<ul class="menu">
<li>
<time datetime="2025-07-24T13:55:00.000003+00:00"><span class="say-no-more">2025-</span>07-24</time>
<a href="https://pyfound.blogspot.com/2025/07/psf-board-nominations-opening-july-29th.html">PSF Board Election Nominations Opening July 29th</a></li>
<li>
<time datetime="2025-07-22T19:47:00.000001+00:00"><span class="say-no-more">2025-</span>07-22</time>
<a href="https://pythoninsider.blogspot.com/2025/07/python-314-release-candidate-1-is-go.html">Python 3.14 release candidate 1 is go!</a></li>
<li>
<time datetime="2025-07-16T12:43:00.000002+00:00"><span class="say-no-more">2025-</span>07-16</time>
<a href="https://pyfound.blogspot.com/2025/07/affirm-your-psf-membership-voting-status.html">Affirm Your PSF Membership Voting Status</a></li>
<li>
<time datetime="2025-07-09T01:00:00.000002+00:00"><span class="say-no-more">2025-</span>07-09</time>
<a href="https://mailchi.mp/python/python-software-foundation-july-2024-newsletter-19880429">PSF News: PyPI Orgs, Board Election, &amp; Yearly Reports</a></li>
<li>
<time datetime="2025-07-08T15:21:00.000001+00:00"><span class="say-no-more">2025-</span>07-08</time>
<a href="https://pyfound.blogspot.com/2025/07/notice-of-python-software-foundation.html">Notice of Python Software Foundation Bylaws Change - Effective July 23, 2025</a></li>
</ul>
</div><!-- end .shrubbery -->
</div>
<div class="medium-widget event-widget last">
<div class="shrubbery">
<h2 class="widget-title"><span aria-hidden="true" class="icon-calendar"></span>Upcoming Events</h2>
<p class="give-me-more"><a href="/events/calendars/" title="More Events">More</a></p>
<ul class="menu">
<li>
<time datetime="2025-08-08T00:00:00+00:00"><span class="say-no-more">2025-</span>08-08</time>
<a href="/events/python-user-group/2081/">Buea - Creating Python Communities and outreach</a></li>
<li>
<time datetime="2025-08-11T00:00:00+00:00"><span class="say-no-more">2025-</span>08-11</time>
<a href="/events/python-events/2011/">DjangoCon Africa 2025</a></li>
<li>
<time datetime="2025-08-13T00:00:00+00:00"><span class="say-no-more">2025-</span>08-13</time>
<a href="/events/python-events/2077/">PyCon Somalia 2025</a></li>
<li>
<time datetime="2025-08-15T00:00:00+00:00"><span class="say-no-more">2025-</span>08-15</time>
<a href="/events/python-events/1973/">PyCon Korea 2025</a></li>
<li>
<time datetime="2025-08-18T00:00:00+00:00"><span class="say-no-more">2025-</span>08-18</time>
<a href="/events/python-events/1971/">EuroSciPy 2025</a></li>
</ul>
</div>
</div>
</div>
<div class="row">
<div class="medium-widget success-stories-widget">
<div class="shrubbery">
<h2 class="widget-title"><span aria-hidden="true" class="icon-success-stories"></span>Success Stories</h2>
<p class="give-me-more"><a href="/success-stories/" title="More Success Stories">More</a></p>
<div class="success-story-item" id="success-story-932">
<blockquote>
<a href="/success-stories/abridging-clinical-conversations-using-python/">Python powers major aspects of Abridge’s ML lifecycle, including data annotation,  research and experimentation, and ML model deployment to production.</a>
</blockquote>
<table border="0" cellpadding="0" cellspacing="0" class="quote-from" width="100%">
<tbody>
<tr>
<td><p><a href="/success-stories/abridging-clinical-conversations-using-python/">Abridging clinical conversations using Python</a> <em>by Nimshi Venkat and Sandeep Konam</em></p></td>
</tr>
</tbody>
</table>
</div>
</div><!-- end .shrubbery -->
</div>
<div class="medium-widget applications-widget last">
<div class="shrubbery">
<h2 class="widget-title"><span aria-hidden="true" class="icon-python"></span>Use Python for…</h2>
<p class="give-me-more"><a href="/about/apps" title="More Applications">More</a></p>
<ul class="menu">
<li><b>Web Development</b>:
        <span class="tag-wrapper"><a class="tag" href="http://www.djangoproject.com/">Django</a>, <a class="tag" href="http://www.pylonsproject.org/">Pyramid</a>, <a class="tag" href="http://bottlepy.org">Bottle</a>, <a class="tag" href="http://tornadoweb.org">Tornado</a>, <a class="tag" href="http://flask.pocoo.org/">Flask</a>, <a class="tag" href="http://www.web2py.com/">web2py</a></span></li>
<li><b>GUI Development</b>:
        <span class="tag-wrapper"><a class="tag" href="http://wiki.python.org/moin/TkInter">tkInter</a>, <a class="tag" href="https://wiki.gnome.org/Projects/PyGObject">PyGObject</a>, <a class="tag" href="http://www.riverbankcomputing.co.uk/software/pyqt/intro">PyQt</a>, <a class="tag" href="https://wiki.qt.io/PySide">PySide</a>, <a class="tag" href="https://kivy.org/">Kivy</a>, <a class="tag" href="http://www.wxpython.org/">wxPython</a>, <a class="tag" href="https://dearpygui.readthedocs.io/en/latest/">DearPyGui</a></span></li>
<li><b>Scientific and Numeric</b>:
        <span class="tag-wrapper">
<a class="tag" href="http://www.scipy.org">SciPy</a>, <a class="tag" href="http://pandas.pydata.org/">Pandas</a>, <a class="tag" href="http://ipython.org">IPython</a></span></li>
<li><b>Software Development</b>:
        <span class="tag-wrapper"><a class="tag" href="http://buildbot.net/">Buildbot</a>, <a class="tag" href="http://trac.edgewall.org/">Trac</a>, <a class="tag" href="http://roundup.sourceforge.net/">Roundup</a></span></li>
<li><b>System Administration</b>:
        <span class="tag-wrapper"><a class="tag" href="http://www.ansible.com">Ansible</a>, <a class="tag" href="https://saltproject.io">Salt</a>, <a class="tag" href="https://www.openstack.org">OpenStack</a>, <a class="tag" href="https://xon.sh">xonsh</a></span></li>
</ul>
</div><!-- end .shrubbery -->
</div>
</div>
<div class="psf-widget">
<div class="python-logo"></div>
<h2 class="widget-title">
<span class="prompt">&gt;&gt;&gt;</span> <a href="/psf/">Python Software Foundation</a>
</h2>
<p>The mission of the Python Software Foundation is to promote, protect, and advance the Python programming language, and to support and facilitate the growth of a diverse and international community of Python programmers. <a class="readmore" href="/psf/">Learn more</a> </p>
<p class="click-these">
<a class="button" href="/psf/membership/">Become a Member</a>
<a class="button" href="/psf/donations/">Donate to the PSF</a>
</p>
</div>
</section>
</div><!-- end .container -->
</div><!-- end #content .content-wrapper -->
<!-- Footer and social media list -->
<footer class="main-footer" id="site-map" role="contentinfo">
<div class="main-footer-links">
<div class="container">
<a class="jump-link" href="#python-network" id="back-to-top-1"><span aria-hidden="true" class="icon-arrow-up"><span>▲</span></span> Back to Top</a>
<ul class="sitemap navigation menu do-not-print" id="container" role="tree">
<li class="tier-1 element-1">
<a href="/about/">About</a>
<ul class="subnav menu">
<li class="tier-2 element-1" role="treeitem"><a href="/about/apps/" title="">Applications</a></li>
<li class="tier-2 element-2" role="treeitem"><a href="/about/quotes/" title="">Quotes</a></li>
<li class="tier-2 element-3" role="treeitem"><a href="/about/gettingstarted/" title="">Getting Started</a></li>
<li class="tier-2 element-4" role="treeitem"><a href="/about/help/" title="">Help</a></li>
<li class="tier-2 element-5" role="treeitem"><a href="http://brochure.getpython.info/" title="">Python Brochure</a></li>
</ul>
</li>
<li class="tier-1 element-2">
<a href="/downloads/">Downloads</a>
<ul class="subnav menu">
<li class="tier-2 element-1" role="treeitem"><a href="/downloads/" title="">All releases</a></li>
<li class="tier-2 element-2" role="treeitem"><a href="/downloads/source/" title="">Source code</a></li>
<li class="tier-2 element-3" role="treeitem"><a href="/downloads/windows/" title="">Windows</a></li>
<li class="tier-2 element-4" role="treeitem"><a href="/downloads/macos/" title="">macOS</a></li>
<li class="tier-2 element-5" role="treeitem"><a href="/download/other/" title="">Other Platforms</a></li>
<li class="tier-2 element-6" role="treeitem"><a href="https://docs.python.org/3/license.html" title="">License</a></li>
<li class="tier-2 element-7" role="treeitem"><a href="/download/alternatives" title="">Alternative Implementations</a></li>
</ul>
</li>
<li class="tier-1 element-3">
<a href="/doc/">Documentation</a>
<ul class="subnav menu">
<li class="tier-2 element-1" role="treeitem"><a href="/doc/" title="">Docs</a></li>
<li class="tier-2 element-2" role="treeitem"><a href="/doc/av" title="">Audio/Visual Talks</a></li>
<li class="tier-2 element-3" role="treeitem"><a href="https://wiki.python.org/moin/BeginnersGuide" title="">Beginner's Guide</a></li>
<li class="tier-2 element-4" role="treeitem"><a href="https://devguide.python.org/" title="">Developer's Guide</a></li>
<li class="tier-2 element-5" role="treeitem"><a href="https://docs.python.org/faq/" title="">FAQ</a></li>
<li class="tier-2 element-6" role="treeitem"><a href="http://wiki.python.org/moin/Languages" title="">Non-English Docs</a></li>
<li class="tier-2 element-7" role="treeitem"><a href="https://peps.python.org" title="">PEP Index</a></li>
<li class="tier-2 element-8" role="treeitem"><a href="https://wiki.python.org/moin/PythonBooks" title="">Python Books</a></li>
<li class="tier-2 element-9" role="treeitem"><a href="/doc/essays/" title="">Python Essays</a></li>
</ul>
</li>
<li class="tier-1 element-4">
<a href="/community/">Community</a>
<ul class="subnav menu">
<li class="tier-2 element-1" role="treeitem"><a href="/community/diversity/" title="">Diversity</a></li>
<li class="tier-2 element-2" role="treeitem"><a href="/community/lists/" title="">Mailing Lists</a></li>
<li class="tier-2 element-3" role="treeitem"><a href="/community/irc/" title="">IRC</a></li>
<li class="tier-2 element-4" role="treeitem"><a href="/community/forums/" title="">Forums</a></li>
<li class="tier-2 element-5" role="treeitem"><a href="/psf/annual-report/2024/" title="">PSF Annual Impact Report</a></li>
<li class="tier-2 element-6" role="treeitem"><a href="/community/workshops/" title="">Python Conferences</a></li>
<li class="tier-2 element-7" role="treeitem"><a href="/community/sigs/" title="">Special Interest Groups</a></li>
<li class="tier-2 element-8" role="treeitem"><a href="/community/logos/" title="">Python Logo</a></li>
<li class="tier-2 element-9" role="treeitem"><a href="https://wiki.python.org/moin/" title="">Python Wiki</a></li>
<li class="tier-2 element-10" role="treeitem"><a href="/psf/conduct/" title="">Code of Conduct</a></li>
<li class="tier-2 element-11" role="treeitem"><a href="/community/awards" title="">Community Awards</a></li>
<li class="tier-2 element-12" role="treeitem"><a href="/psf/get-involved/" title="">Get Involved</a></li>
<li class="tier-2 element-13" role="treeitem"><a href="/psf/community-stories/" title="">Shared Stories</a></li>
</ul>
</li>
<li class="tier-1 element-5">
<a href="/success-stories/" title="success-stories">Success Stories</a>
<ul class="subnav menu">
<li class="tier-2 element-1" role="treeitem"><a href="/success-stories/category/arts/" title="">Arts</a></li>
<li class="tier-2 element-2" role="treeitem"><a href="/success-stories/category/business/" title="">Business</a></li>
<li class="tier-2 element-3" role="treeitem"><a href="/success-stories/category/education/" title="">Education</a></li>
<li class="tier-2 element-4" role="treeitem"><a href="/success-stories/category/engineering/" title="">Engineering</a></li>
<li class="tier-2 element-5" role="treeitem"><a href="/success-stories/category/government/" title="">Government</a></li>
<li class="tier-2 element-6" role="treeitem"><a href="/success-stories/category/scientific/" title="">Scientific</a></li>
<li class="tier-2 element-7" role="treeitem"><a href="/success-stories/category/software-development/" title="">Software Development</a></li>
</ul>
</li>
<li class="tier-1 element-6">
<a href="/blogs/" title="News from around the Python world">News</a>
<ul class="subnav menu">
<li class="tier-2 element-1" role="treeitem"><a href="/blogs/" title="Python Insider Blog Posts">Python News</a></li>
<li class="tier-2 element-2" role="treeitem"><a href="/psf/newsletter/" title="Python Software Foundation Newsletter">PSF Newsletter</a></li>
<li class="tier-2 element-3" role="treeitem"><a href="http://pyfound.blogspot.com/" title="PSF Blog">PSF News</a></li>
<li class="tier-2 element-4" role="treeitem"><a href="http://pycon.blogspot.com/" title="PyCon Blog">PyCon US News</a></li>
<li class="tier-2 element-5" role="treeitem"><a href="http://planetpython.org/" title="Planet Python">News from the Community</a></li>
</ul>
</li>
<li class="tier-1 element-7">
<a href="/events/">Events</a>
<ul class="subnav menu">
<li class="tier-2 element-1" role="treeitem"><a href="/events/python-events/" title="">Python Events</a></li>
<li class="tier-2 element-2" role="treeitem"><a href="/events/python-user-group/" title="">User Group Events</a></li>
<li class="tier-2 element-3" role="treeitem"><a href="/events/python-events/past/" title="">Python Events Archive</a></li>
<li class="tier-2 element-4" role="treeitem"><a href="/events/python-user-group/past/" title="">User Group Events Archive</a></li>
<li class="tier-2 element-5" role="treeitem"><a href="https://wiki.python.org/moin/PythonEventsCalendar#Submitting_an_Event" title="">Submit an Event</a></li>
</ul>
</li>
<li class="tier-1 element-8">
<a href="/dev/">Contributing</a>
<ul class="subnav menu">
<li class="tier-2 element-1" role="treeitem"><a href="https://devguide.python.org/" title="">Developer's Guide</a></li>
<li class="tier-2 element-2" role="treeitem"><a href="https://github.com/python/cpython/issues" title="">Issue Tracker</a></li>
<li class="tier-2 element-3" role="treeitem"><a href="https://mail.python.org/mailman/listinfo/python-dev" title="">python-dev list</a></li>
<li class="tier-2 element-4" role="treeitem"><a href="/dev/core-mentorship/" title="">Core Mentorship</a></li>
<li class="tier-2 element-5" role="treeitem"><a href="/dev/security/" title="">Report a Security Issue</a></li>
</ul>
</li>
</ul>
<a class="jump-link" href="#python-network" id="back-to-top-2"><span aria-hidden="true" class="icon-arrow-up"><span>▲</span></span> Back to Top</a>
</div><!-- end .container -->
</div> <!-- end .main-footer-links -->
<div class="site-base">
<div class="container">
<ul class="footer-links navigation menu do-not-print" role="tree">
<li class="tier-1 element-1"><a href="/about/help/">Help &amp; <span class="say-no-more">General</span> Contact</a></li>
<li class="tier-1 element-2"><a href="/community/diversity/">Diversity <span class="say-no-more">Initiatives</span></a></li>
<li class="tier-1 element-3"><a href="https://github.com/python/pythondotorg/issues">Submit Website Bug</a></li>
<li class="tier-1 element-4">
<a href="https://status.python.org/">Status <span class="python-status-indicator-default" id="python-status-indicator"></span></a>
</li>
</ul>
<div class="copyright">
<p><small>
<span class="pre">Copyright ©2001-2025.</span>
                             <span class="pre"><a href="/psf-landing/">Python Software Foundation</a></span>
                             <span class="pre"><a href="/about/legal/">Legal Statements</a></span>
                             <span class="pre"><a href="https://policies.python.org/python.org/Privacy-Notice/">Privacy Notice</a></span>
<!--&nbsp;<span class="pre"><a href="/psf/community-infrastructure">Powered by PSF Community Infrastructure</a></span>-->
</small></p>
</div>
</div><!-- end .container -->
</div><!-- end .site-base -->
</footer>
</div><!-- end #touchnav-wrapper -->
<script src="//ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js"></script>
<script>window.jQuery || document.write('<script src="/static/js/libs/jquery-1.8.2.min.js"><\/script>')</script>
<script src="//ajax.googleapis.com/ajax/libs/jqueryui/1.12.1/jquery-ui.min.js"></script>
<script>window.jQuery || document.write('<script src="/static/js/libs/jquery-ui-1.12.1.min.js"><\/script>')</script>
<script src="/static/js/libs/masonry.pkgd.min.js"></script>
<script src="/static/js/libs/html-includes.js"></script>
<script charset="utf-8" src="/static/js/main-min.ef82c06437cf.js" type="text/javascript"></script>
<!--[if lte IE 7]>
    <script type="text/javascript" src="/static/js/plugins/IE8-min.8af6e26c7a3b.js" charset="utf-8"></script>
    
    
    <![endif]-->
<!--[if lte IE 8]>
    <script type="text/javascript" src="/static/js/plugins/getComputedStyle-min.d41d8cd98f00.js" charset="utf-8"></script>
    
    
    <![endif]-->
</body>
</html>

########################################

Neatly display the html content
--------------------
<!DOCTYPE html>
<!--[if lt IE 7]>   <html class="no-js ie6 lt-ie7 lt-ie8 lt-ie9">   <![endif]-->
<!--[if IE 7]>      <html class="no-js ie7 lt-ie8 lt-ie9">          <![endif]-->
<!--[if IE 8]>      <html class="no-js ie8 lt-ie9">                 <![endif]-->
<!--[if gt IE 8]><!-->
<html class="no-js" dir="ltr" lang="en">
 <!--<![endif]-->
 <head>
  <script data-domain="python.org" defer="" src="https://analytics.python.org/js/script.outbound-links.js">
  </script>
  <meta charset="utf-8"/>
  <meta content="IE=edge" http-equiv="X-UA-Compatible"/>
  <link href="//ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js" rel="prefetch"/>
  <link href="//ajax.googleapis.com/ajax/libs/jqueryui/1.12.1/jquery-ui.min.js" rel="prefetch"/>
  <meta content="Python.org" name="application-name"/>
  <meta content="The official home of the Python Programming Language" name="msapplication-tooltip"/>
  <meta content="Python.org" name="apple-mobile-web-app-title"/>
  <meta content="yes" name="apple-mobile-web-app-capable"/>
  <meta content="black" name="apple-mobile-web-app-status-bar-style"/>
  <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
  <meta content="True" name="HandheldFriendly"/>
  <meta content="telephone=no" name="format-detection"/>
  <meta content="on" http-equiv="cleartype"/>
  <meta content="false" http-equiv="imagetoolbar"/>
  <script async="" crossorigin="anonymous" integrity="sha256-U3hKDidudIaxBDEzwGJApJgPEf2mWk6cfMWghrAa6i0= sha384-UcmsCqcNRSLW/dV3Lo1oCi2/VaurXbib6p4HyUEOeIa/4OpsrnucrugAefzVZJfI sha512-q4t1L4xEjGV2R4hzqCa41P8jrgFUS8xTb8rdNv4FGvw7FpydVj/kkxBJHOiaoxHa8olCcx1Slk9K+3sNbsM4ug==" src="https://media.ethicalads.io/media/client/v1.4.0/ethicalads.min.js">
  </script>
  <script src="/static/js/libs/modernizr.js">
  </script>
  <link href="/static/stylesheets/style.08a078d0aa02.css" media="all" rel="stylesheet" title="default" type="text/css">
   <link href="/static/stylesheets/mq.98d6092b2ada.css" media="not print, braille, embossed, speech, tty" rel="stylesheet" type="text/css">
    <link href="/static/stylesheets/no-mq.bf0c425cdb73.css" media="screen" rel="stylesheet" type="text/css"/>
    <!--[if (lte IE 8)&(!IEMobile)]>
    <link href="/static/stylesheets/no-mq.bf0c425cdb73.css" rel="stylesheet" type="text/css" media="screen" />
    
    
    <![endif]-->
    <link href="//ajax.googleapis.com/ajax/libs/jqueryui/1.12.1/themes/smoothness/jquery-ui.css" rel="stylesheet"/>
    <link href="/static/favicon.ico" rel="icon" type="image/x-icon"/>
    <link href="/static/apple-touch-icon-144x144-precomposed.png" rel="apple-touch-icon-precomposed" sizes="144x144"/>
    <link href="/static/apple-touch-icon-114x114-precomposed.png" rel="apple-touch-icon-precomposed" sizes="114x114"/>
    <link href="/static/apple-touch-icon-72x72-precomposed.png" rel="apple-touch-icon-precomposed" sizes="72x72"/>
    <link href="/static/apple-touch-icon-precomposed.png" rel="apple-touch-icon-precomposed"/>
    <link href="/static/apple-touch-icon-precomposed.png" rel="apple-touch-icon"/>
    <meta content="/static/metro-icon-144x144.png" name="msapplication-TileImage"/>
    <!-- white shape -->
    <meta content="#3673a5" name="msapplication-TileColor"/>
    <!-- python blue -->
    <meta content="#3673a5" name="msapplication-navbutton-color"/>
    <title>
     Welcome to Python.org
    </title>
    <meta content="The official home of the Python Programming Language" name="description"/>
    <meta content="Python programming language object oriented web free open source software license documentation download community" name="keywords"/>
    <meta content="website" property="og:type"/>
    <meta content="Python.org" property="og:site_name"/>
    <meta content="Welcome to Python.org" property="og:title"/>
    <meta content="The official home of the Python Programming Language" property="og:description"/>
    <meta content="https://www.python.org/static/opengraph-icon-200x200.png" property="og:image"/>
    <meta content="https://www.python.org/static/opengraph-icon-200x200.png" property="og:image:secure_url"/>
    <meta content="https://www.python.org/" property="og:url"/>
    <link href="/humans.txt" rel="author"/>
    <link href="https://peps.python.org/peps.rss" rel="alternate" title="Python Enhancement Proposals" type="application/rss+xml"/>
    <link href="https://www.python.org/jobs/feed/rss/" rel="alternate" title="Python Job Opportunities" type="application/rss+xml"/>
    <link href="https://feeds.feedburner.com/PythonSoftwareFoundationNews" rel="alternate" title="Python Software Foundation News" type="application/rss+xml"/>
    <link href="https://feeds.feedburner.com/PythonInsider" rel="alternate" title="Python Insider" type="application/rss+xml"/>
    <link href="https://www.python.org/downloads/feed.rss" rel="alternate" title="Python Releases" type="application/rss+xml"/>
    <script type="application/ld+json">
     {
       "@context": "https://schema.org",
       "@type": "WebSite",
       "url": "https://www.python.org/",
       "potentialAction": {
         "@type": "SearchAction",
         "target": "https://www.python.org/search/?q={search_term_string}",
         "query-input": "required name=search_term_string"
       }
     }
    </script>
    <script type="text/javascript">
     var _gaq = _gaq || [];
    _gaq.push(['_setAccount', 'UA-39055973-1']);
    _gaq.push(['_trackPageview']);

    (function() {
        var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
        ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
        var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
    })();
    </script>
   </link>
  </link>
 </head>
 <body class="python home" id="homepage">
  <div id="touchnav-wrapper">
   <div class="do-not-print" id="nojs">
    <p>
     <strong>
      Notice:
     </strong>
     While JavaScript is not essential for this website, your interaction with the content will be limited. Please turn JavaScript on for the full experience.
    </p>
   </div>
   <!--[if lte IE 8]>
        <div id="oldie-warning" class="do-not-print">
            <p>
                <strong>Notice:</strong> Your browser is <em>ancient</em>. Please
                <a href="http://browsehappy.com/">upgrade to a different browser</a> to experience a better web.
            </p>
        </div>
        <![endif]-->
   <!-- Sister Site Links -->
   <div class="top-bar do-not-print" id="top">
    <nav class="meta-navigation container" role="navigation">
     <div class="skip-link screen-reader-text">
      <a href="#content" title="Skip to content">
       Skip to content
      </a>
     </div>
     <a aria-hidden="true" class="jump-link" href="#python-network" id="close-python-network">
      <span aria-hidden="true" class="icon-arrow-down">
       <span>
        ▼
       </span>
      </span>
      Close
     </a>
     <ul class="menu" role="tree">
      <li class="python-meta current_item selectedcurrent_branch selected">
       <a class="current_item selectedcurrent_branch selected" href="/" title="The Python Programming Language">
        Python
       </a>
      </li>
      <li class="psf-meta">
       <a href="https://www.python.org/psf/" title="The Python Software Foundation">
        PSF
       </a>
      </li>
      <li class="docs-meta">
       <a href="https://docs.python.org" title="Python Documentation">
        Docs
       </a>
      </li>
      <li class="pypi-meta">
       <a href="https://pypi.org/" title="Python Package Index">
        PyPI
       </a>
      </li>
      <li class="jobs-meta">
       <a href="/jobs/" title="Python Job Board">
        Jobs
       </a>
      </li>
      <li class="shop-meta">
       <a href="/community/">
        Community
       </a>
      </li>
     </ul>
     <a aria-hidden="true" class="jump-link" href="#top" id="python-network">
      <span aria-hidden="true" class="icon-arrow-up">
       <span>
        ▲
       </span>
      </span>
      The Python Network
     </a>
    </nav>
   </div>
   <!-- Header elements -->
   <header class="main-header" role="banner">
    <div class="container">
     <h1 class="site-headline">
      <a href="/">
       <img alt="python™" class="python-logo" src="/static/img/python-logo.png"/>
      </a>
     </h1>
     <div class="options-bar-container do-not-print">
      <a class="donate-button" href="https://psfmember.org/civicrm/contribute/transact?reset=1&amp;id=2">
       Donate
      </a>
      <div class="options-bar">
       <a class="jump-to-menu" href="#site-map" id="site-map-link">
        <span class="menu-icon">
         ≡
        </span>
        Menu
       </a>
       <form action="/search/" class="search-the-site" method="get">
        <fieldset title="Search Python.org">
         <span aria-hidden="true" class="icon-search">
         </span>
         <label class="screen-reader-text" for="id-search-field">
          Search This Site
         </label>
         <input class="search-field" id="id-search-field" name="q" placeholder="Search" role="textbox" tabindex="1" type="search" value=""/>
         <button class="search-button" id="submit" name="submit" tabindex="3" title="Submit this Search" type="submit">
          GO
         </button>
         <!--[if IE]><input type="text" style="display: none;" disabled="disabled" size="1" tabindex="4"><![endif]-->
        </fieldset>
       </form>
       <span class="breaker">
       </span>
       <div aria-hidden="true" class="adjust-font-size">
        <ul aria-label="Adjust Text Size on Page" class="navigation menu">
         <li aria-haspopup="true" class="tier-1 last">
          <a class="action-trigger" href="#">
           <strong>
            <small>
             A
            </small>
            A
           </strong>
          </a>
          <ul class="subnav menu">
           <li class="tier-2 element-1" role="treeitem">
            <a class="text-shrink" href="javascript:;" title="Make Text Smaller">
             Smaller
            </a>
           </li>
           <li class="tier-2 element-2" role="treeitem">
            <a class="text-grow" href="javascript:;" title="Make Text Larger">
             Larger
            </a>
           </li>
           <li class="tier-2 element-3" role="treeitem">
            <a class="text-reset" href="javascript:;" title="Reset any font size changes I have made">
             Reset
            </a>
           </li>
          </ul>
         </li>
        </ul>
       </div>
       <div class="winkwink-nudgenudge">
        <ul aria-label="Social Media Navigation" class="navigation menu">
         <li aria-haspopup="true" class="tier-1 last">
          <a class="action-trigger" href="#">
           Socialize
          </a>
          <ul class="subnav menu">
           <li class="tier-2 element-1" role="treeitem">
            <a href="https://www.linkedin.com/company/python-software-foundation/">
             <i aria-hidden="true" class="fa fa-linkedin-square">
             </i>
             LinkedIn
            </a>
           </li>
           <li class="tier-2 element-2" role="treeitem">
            <a href="https://fosstodon.org/@ThePSF">
             <span aria-hidden="true" class="icon-mastodon">
             </span>
             Mastodon
            </a>
           </li>
           <li class="tier-2 element-3" role="treeitem">
            <a href="/community/irc/">
             <span aria-hidden="true" class="icon-freenode">
             </span>
             Chat on IRC
            </a>
           </li>
           <li class="tier-2 element-4" role="treeitem">
            <a href="https://twitter.com/ThePSF">
             <span aria-hidden="true" class="icon-twitter">
             </span>
             Twitter
            </a>
           </li>
          </ul>
         </li>
        </ul>
       </div>
       <span data-html-include="/authenticated">
       </span>
      </div>
      <!-- end options-bar -->
     </div>
     <nav class="python-navigation main-navigation do-not-print" id="mainnav" role="navigation">
      <ul aria-label="Main Navigation" class="navigation menu" role="menubar">
       <li aria-haspopup="true" class="tier-1 element-1" id="about">
        <a class="" href="/about/" title="">
         About
        </a>
        <ul aria-hidden="true" class="subnav menu" role="menu">
         <li class="tier-2 element-1" role="treeitem">
          <a href="/about/apps/" title="">
           Applications
          </a>
         </li>
         <li class="tier-2 element-2" role="treeitem">
          <a href="/about/quotes/" title="">
           Quotes
          </a>
         </li>
         <li class="tier-2 element-3" role="treeitem">
          <a href="/about/gettingstarted/" title="">
           Getting Started
          </a>
         </li>
         <li class="tier-2 element-4" role="treeitem">
          <a href="/about/help/" title="">
           Help
          </a>
         </li>
         <li class="tier-2 element-5" role="treeitem">
          <a href="http://brochure.getpython.info/" title="">
           Python Brochure
          </a>
         </li>
        </ul>
       </li>
       <li aria-haspopup="true" class="tier-1 element-2" id="downloads">
        <a class="" href="/downloads/" title="">
         Downloads
        </a>
        <ul aria-hidden="true" class="subnav menu" role="menu">
         <li class="tier-2 element-1" role="treeitem">
          <a href="/downloads/" title="">
           All releases
          </a>
         </li>
         <li class="tier-2 element-2" role="treeitem">
          <a href="/downloads/source/" title="">
           Source code
          </a>
         </li>
         <li class="tier-2 element-3" role="treeitem">
          <a href="/downloads/windows/" title="">
           Windows
          </a>
         </li>
         <li class="tier-2 element-4" role="treeitem">
          <a href="/downloads/macos/" title="">
           macOS
          </a>
         </li>
         <li class="tier-2 element-5" role="treeitem">
          <a href="/download/other/" title="">
           Other Platforms
          </a>
         </li>
         <li class="tier-2 element-6" role="treeitem">
          <a href="https://docs.python.org/3/license.html" title="">
           License
          </a>
         </li>
         <li class="tier-2 element-7" role="treeitem">
          <a href="/download/alternatives" title="">
           Alternative Implementations
          </a>
         </li>
        </ul>
       </li>
       <li aria-haspopup="true" class="tier-1 element-3" id="documentation">
        <a class="" href="/doc/" title="">
         Documentation
        </a>
        <ul aria-hidden="true" class="subnav menu" role="menu">
         <li class="tier-2 element-1" role="treeitem">
          <a href="/doc/" title="">
           Docs
          </a>
         </li>
         <li class="tier-2 element-2" role="treeitem">
          <a href="/doc/av" title="">
           Audio/Visual Talks
          </a>
         </li>
         <li class="tier-2 element-3" role="treeitem">
          <a href="https://wiki.python.org/moin/BeginnersGuide" title="">
           Beginner's Guide
          </a>
         </li>
         <li class="tier-2 element-4" role="treeitem">
          <a href="https://devguide.python.org/" title="">
           Developer's Guide
          </a>
         </li>
         <li class="tier-2 element-5" role="treeitem">
          <a href="https://docs.python.org/faq/" title="">
           FAQ
          </a>
         </li>
         <li class="tier-2 element-6" role="treeitem">
          <a href="http://wiki.python.org/moin/Languages" title="">
           Non-English Docs
          </a>
         </li>
         <li class="tier-2 element-7" role="treeitem">
          <a href="https://peps.python.org" title="">
           PEP Index
          </a>
         </li>
         <li class="tier-2 element-8" role="treeitem">
          <a href="https://wiki.python.org/moin/PythonBooks" title="">
           Python Books
          </a>
         </li>
         <li class="tier-2 element-9" role="treeitem">
          <a href="/doc/essays/" title="">
           Python Essays
          </a>
         </li>
        </ul>
       </li>
       <li aria-haspopup="true" class="tier-1 element-4" id="community">
        <a class="" href="/community/" title="">
         Community
        </a>
        <ul aria-hidden="true" class="subnav menu" role="menu">
         <li class="tier-2 element-1" role="treeitem">
          <a href="/community/diversity/" title="">
           Diversity
          </a>
         </li>
         <li class="tier-2 element-2" role="treeitem">
          <a href="/community/lists/" title="">
           Mailing Lists
          </a>
         </li>
         <li class="tier-2 element-3" role="treeitem">
          <a href="/community/irc/" title="">
           IRC
          </a>
         </li>
         <li class="tier-2 element-4" role="treeitem">
          <a href="/community/forums/" title="">
           Forums
          </a>
         </li>
         <li class="tier-2 element-5" role="treeitem">
          <a href="/psf/annual-report/2024/" title="">
           PSF Annual Impact Report
          </a>
         </li>
         <li class="tier-2 element-6" role="treeitem">
          <a href="/community/workshops/" title="">
           Python Conferences
          </a>
         </li>
         <li class="tier-2 element-7" role="treeitem">
          <a href="/community/sigs/" title="">
           Special Interest Groups
          </a>
         </li>
         <li class="tier-2 element-8" role="treeitem">
          <a href="/community/logos/" title="">
           Python Logo
          </a>
         </li>
         <li class="tier-2 element-9" role="treeitem">
          <a href="https://wiki.python.org/moin/" title="">
           Python Wiki
          </a>
         </li>
         <li class="tier-2 element-10" role="treeitem">
          <a href="/psf/conduct/" title="">
           Code of Conduct
          </a>
         </li>
         <li class="tier-2 element-11" role="treeitem">
          <a href="/community/awards" title="">
           Community Awards
          </a>
         </li>
         <li class="tier-2 element-12" role="treeitem">
          <a href="/psf/get-involved/" title="">
           Get Involved
          </a>
         </li>
         <li class="tier-2 element-13" role="treeitem">
          <a href="/psf/community-stories/" title="">
           Shared Stories
          </a>
         </li>
        </ul>
       </li>
       <li aria-haspopup="true" class="tier-1 element-5" id="success-stories">
        <a class="" href="/success-stories/" title="success-stories">
         Success Stories
        </a>
        <ul aria-hidden="true" class="subnav menu" role="menu">
         <li class="tier-2 element-1" role="treeitem">
          <a href="/success-stories/category/arts/" title="">
           Arts
          </a>
         </li>
         <li class="tier-2 element-2" role="treeitem">
          <a href="/success-stories/category/business/" title="">
           Business
          </a>
         </li>
         <li class="tier-2 element-3" role="treeitem">
          <a href="/success-stories/category/education/" title="">
           Education
          </a>
         </li>
         <li class="tier-2 element-4" role="treeitem">
          <a href="/success-stories/category/engineering/" title="">
           Engineering
          </a>
         </li>
         <li class="tier-2 element-5" role="treeitem">
          <a href="/success-stories/category/government/" title="">
           Government
          </a>
         </li>
         <li class="tier-2 element-6" role="treeitem">
          <a href="/success-stories/category/scientific/" title="">
           Scientific
          </a>
         </li>
         <li class="tier-2 element-7" role="treeitem">
          <a href="/success-stories/category/software-development/" title="">
           Software Development
          </a>
         </li>
        </ul>
       </li>
       <li aria-haspopup="true" class="tier-1 element-6" id="news">
        <a class="" href="/blogs/" title="News from around the Python world">
         News
        </a>
        <ul aria-hidden="true" class="subnav menu" role="menu">
         <li class="tier-2 element-1" role="treeitem">
          <a href="/blogs/" title="Python Insider Blog Posts">
           Python News
          </a>
         </li>
         <li class="tier-2 element-2" role="treeitem">
          <a href="/psf/newsletter/" title="Python Software Foundation Newsletter">
           PSF Newsletter
          </a>
         </li>
         <li class="tier-2 element-3" role="treeitem">
          <a href="http://pyfound.blogspot.com/" title="PSF Blog">
           PSF News
          </a>
         </li>
         <li class="tier-2 element-4" role="treeitem">
          <a href="http://pycon.blogspot.com/" title="PyCon Blog">
           PyCon US News
          </a>
         </li>
         <li class="tier-2 element-5" role="treeitem">
          <a href="http://planetpython.org/" title="Planet Python">
           News from the Community
          </a>
         </li>
        </ul>
       </li>
       <li aria-haspopup="true" class="tier-1 element-7" id="events">
        <a class="" href="/events/" title="">
         Events
        </a>
        <ul aria-hidden="true" class="subnav menu" role="menu">
         <li class="tier-2 element-1" role="treeitem">
          <a href="/events/python-events/" title="">
           Python Events
          </a>
         </li>
         <li class="tier-2 element-2" role="treeitem">
          <a href="/events/python-user-group/" title="">
           User Group Events
          </a>
         </li>
         <li class="tier-2 element-3" role="treeitem">
          <a href="/events/python-events/past/" title="">
           Python Events Archive
          </a>
         </li>
         <li class="tier-2 element-4" role="treeitem">
          <a href="/events/python-user-group/past/" title="">
           User Group Events Archive
          </a>
         </li>
         <li class="tier-2 element-5" role="treeitem">
          <a href="https://wiki.python.org/moin/PythonEventsCalendar#Submitting_an_Event" title="">
           Submit an Event
          </a>
         </li>
        </ul>
       </li>
      </ul>
     </nav>
     <div class="header-banner">
      <!-- for optional "do-not-print" class -->
      <div class="flex-slideshow slideshow" id="dive-into-python">
       <ul class="launch-shell menu" id="launch-shell">
        <li>
         <a class="button prompt" data-shell-container="#dive-into-python" href="/shell/" id="start-shell">
          &gt;_
          <span class="message">
           Launch Interactive Shell
          </span>
         </a>
        </li>
       </ul>
       <ul class="slides menu">
        <li>
         <div class="slide-code">
          <pre><code><span class="comment"># Python 3: Fibonacci series up to n</span>
&gt;&gt;&gt; def fib(n):
&gt;&gt;&gt;     a, b = 0, 1
&gt;&gt;&gt;     while a &lt; n:
&gt;&gt;&gt;         print(a, end=' ')
&gt;&gt;&gt;         a, b = b, a+b
&gt;&gt;&gt;     print()
&gt;&gt;&gt; fib(1000)
<span class="output">0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987</span></code></pre>
         </div>
         <div class="slide-copy">
          <h1>
           Functions Defined
          </h1>
          <p>
           The core of extensible programming is defining functions. Python allows mandatory and optional arguments, keyword arguments, and even arbitrary argument lists.
           <a href="//docs.python.org/3/tutorial/controlflow.html#defining-functions">
            More about defining functions in Python 3
           </a>
          </p>
         </div>
        </li>
        <li>
         <div class="slide-code">
          <pre><code><span class="comment"># Python 3: List comprehensions</span>
&gt;&gt;&gt; fruits = ['Banana', 'Apple', 'Lime']
&gt;&gt;&gt; loud_fruits = [fruit.upper() for fruit in fruits]
&gt;&gt;&gt; print(loud_fruits)
<span class="output">['BANANA', 'APPLE', 'LIME']</span>

<span class="comment"># List and the enumerate function</span>
&gt;&gt;&gt; list(enumerate(fruits))
<span class="output">[(0, 'Banana'), (1, 'Apple'), (2, 'Lime')]</span></code></pre>
         </div>
         <div class="slide-copy">
          <h1>
           Compound Data Types
          </h1>
          <p>
           Lists (known as arrays in other languages) are one of the compound data types that Python understands. Lists can be indexed, sliced and manipulated with other built-in functions.
           <a href="//docs.python.org/3/tutorial/introduction.html#lists">
            More about lists in Python 3
           </a>
          </p>
         </div>
        </li>
        <li>
         <div class="slide-code">
          <pre><code><span class="comment"># Python 3: Simple arithmetic</span>
&gt;&gt;&gt; 1 / 2
<span class="output">0.5</span>
&gt;&gt;&gt; 2 ** 3
<span class="output">8</span>
&gt;&gt;&gt; 17 / 3  <span class="comment"># classic division returns a float</span>
<span class="output">5.666666666666667</span>
&gt;&gt;&gt; 17 // 3  <span class="comment"># floor division</span>
<span class="output">5</span></code></pre>
         </div>
         <div class="slide-copy">
          <h1>
           Intuitive Interpretation
          </h1>
          <p>
           Calculations are simple with Python, and expression syntax is straightforward: the operators
           <code>
            +
           </code>
           ,
           <code>
            -
           </code>
           ,
           <code>
            *
           </code>
           and
           <code>
            /
           </code>
           work as expected; parentheses
           <code>
            ()
           </code>
           can be used for grouping.
           <a href="http://docs.python.org/3/tutorial/introduction.html#using-python-as-a-calculator">
            More about simple math functions in Python 3
           </a>
           .
          </p>
         </div>
        </li>
        <li>
         <div class="slide-code">
          <pre><code><span class="comment"># For loop on a list</span>
&gt;&gt;&gt; numbers = [2, 4, 6, 8]
&gt;&gt;&gt; product = 1
&gt;&gt;&gt; for number in numbers:
...    product = product * number
... 
&gt;&gt;&gt; print('The product is:', product)
<span class="output">The product is: 384</span></code></pre>
         </div>
         <div class="slide-copy">
          <h1>
           All the Flow You’d Expect
          </h1>
          <p>
           Python knows the usual control flow statements that other languages speak —
           <code>
            if
           </code>
           ,
           <code>
            for
           </code>
           ,
           <code>
            while
           </code>
           and
           <code>
            range
           </code>
           — with some of its own twists, of course.
           <a href="//docs.python.org/3/tutorial/controlflow.html">
            More control flow tools in Python 3
           </a>
          </p>
         </div>
        </li>
        <li>
         <div class="slide-code">
          <pre><code><span class="comment"># Simple output (with Unicode)</span>
&gt;&gt;&gt; print("Hello, I'm Python!")
<span class="output">Hello, I'm Python!</span>
<span class="comment"># Input, assignment</span>
&gt;&gt;&gt; name = input('What is your name?\n')
<span class="output">What is your name?
Python</span>
&gt;&gt;&gt; print(f'Hi, {name}.')
<span class="output">Hi, Python.</span></code>
</pre>
         </div>
         <div class="slide-copy">
          <h1>
           Quick &amp; Easy to Learn
          </h1>
          <p>
           Experienced programmers in any other language can pick up Python very quickly, and beginners find the clean syntax and indentation structure easy to learn.
           <a href="//docs.python.org/3/tutorial/">
            Whet your appetite
           </a>
           with our Python 3 overview.
          </p>
         </div>
        </li>
       </ul>
      </div>
     </div>
     <div class="introduction">
      <p>
       Python is a programming language that lets you work quickly
       <span class="breaker">
       </span>
       and integrate systems more effectively.
       <a class="readmore" href="/doc/">
        Learn More
       </a>
      </p>
     </div>
    </div>
    <!-- end .container -->
   </header>
   <div class="content-wrapper" id="content">
    <!-- Main Content Column -->
    <div class="container">
     <section class="main-content" role="main">
      <div class="row">
       <div class="small-widget get-started-widget">
        <h2 class="widget-title">
         <span aria-hidden="true" class="icon-get-started">
         </span>
         Get Started
        </h2>
        <p>
         Whether you're new to programming or an experienced developer, it's easy to learn and use Python.
        </p>
        <p>
         <a href="/about/gettingstarted/">
          Start with our Beginner’s Guide
         </a>
        </p>
       </div>
       <div class="small-widget download-widget">
        <h2 class="widget-title">
         <span aria-hidden="true" class="icon-download">
         </span>
         Download
        </h2>
        <p>
         Python source code and installers are available for download for all versions!
        </p>
        <p>
         Latest:
         <a href="/downloads/release/python-3135/">
          Python 3.13.5
         </a>
        </p>
       </div>
       <div class="small-widget documentation-widget">
        <h2 class="widget-title">
         <span aria-hidden="true" class="icon-documentation">
         </span>
         Docs
        </h2>
        <p>
         Documentation for Python's standard library, along with tutorials and guides, are available online.
        </p>
        <p>
         <a href="https://docs.python.org">
          docs.python.org
         </a>
        </p>
       </div>
       <div class="small-widget jobs-widget last">
        <h2 class="widget-title">
         <span aria-hidden="true" class="icon-jobs">
         </span>
         Jobs
        </h2>
        <p>
         Looking for work or have a Python related position that you're trying to hire for? Our
         <strong>
          relaunched community-run job board
         </strong>
         is the place to go.
        </p>
        <p>
         <a href="//jobs.python.org">
          jobs.python.org
         </a>
        </p>
       </div>
      </div>
      <div class="list-widgets row">
       <div class="medium-widget blog-widget">
        <div class="shrubbery">
         <h2 class="widget-title">
          <span aria-hidden="true" class="icon-news">
          </span>
          Latest News
         </h2>
         <p class="give-me-more">
          <a href="https://blog.python.org" title="More News">
           More
          </a>
         </p>
         <ul class="menu">
          <li>
           <time datetime="2025-07-24T13:55:00.000003+00:00">
            <span class="say-no-more">
             2025-
            </span>
            07-24
           </time>
           <a href="https://pyfound.blogspot.com/2025/07/psf-board-nominations-opening-july-29th.html">
            PSF Board Election Nominations Opening July 29th
           </a>
          </li>
          <li>
           <time datetime="2025-07-22T19:47:00.000001+00:00">
            <span class="say-no-more">
             2025-
            </span>
            07-22
           </time>
           <a href="https://pythoninsider.blogspot.com/2025/07/python-314-release-candidate-1-is-go.html">
            Python 3.14 release candidate 1 is go!
           </a>
          </li>
          <li>
           <time datetime="2025-07-16T12:43:00.000002+00:00">
            <span class="say-no-more">
             2025-
            </span>
            07-16
           </time>
           <a href="https://pyfound.blogspot.com/2025/07/affirm-your-psf-membership-voting-status.html">
            Affirm Your PSF Membership Voting Status
           </a>
          </li>
          <li>
           <time datetime="2025-07-09T01:00:00.000002+00:00">
            <span class="say-no-more">
             2025-
            </span>
            07-09
           </time>
           <a href="https://mailchi.mp/python/python-software-foundation-july-2024-newsletter-19880429">
            PSF News: PyPI Orgs, Board Election, &amp; Yearly Reports
           </a>
          </li>
          <li>
           <time datetime="2025-07-08T15:21:00.000001+00:00">
            <span class="say-no-more">
             2025-
            </span>
            07-08
           </time>
           <a href="https://pyfound.blogspot.com/2025/07/notice-of-python-software-foundation.html">
            Notice of Python Software Foundation Bylaws Change - Effective July 23, 2025
           </a>
          </li>
         </ul>
        </div>
        <!-- end .shrubbery -->
       </div>
       <div class="medium-widget event-widget last">
        <div class="shrubbery">
         <h2 class="widget-title">
          <span aria-hidden="true" class="icon-calendar">
          </span>
          Upcoming Events
         </h2>
         <p class="give-me-more">
          <a href="/events/calendars/" title="More Events">
           More
          </a>
         </p>
         <ul class="menu">
          <li>
           <time datetime="2025-08-08T00:00:00+00:00">
            <span class="say-no-more">
             2025-
            </span>
            08-08
           </time>
           <a href="/events/python-user-group/2081/">
            Buea - Creating Python Communities and outreach
           </a>
          </li>
          <li>
           <time datetime="2025-08-11T00:00:00+00:00">
            <span class="say-no-more">
             2025-
            </span>
            08-11
           </time>
           <a href="/events/python-events/2011/">
            DjangoCon Africa 2025
           </a>
          </li>
          <li>
           <time datetime="2025-08-13T00:00:00+00:00">
            <span class="say-no-more">
             2025-
            </span>
            08-13
           </time>
           <a href="/events/python-events/2077/">
            PyCon Somalia 2025
           </a>
          </li>
          <li>
           <time datetime="2025-08-15T00:00:00+00:00">
            <span class="say-no-more">
             2025-
            </span>
            08-15
           </time>
           <a href="/events/python-events/1973/">
            PyCon Korea 2025
           </a>
          </li>
          <li>
           <time datetime="2025-08-18T00:00:00+00:00">
            <span class="say-no-more">
             2025-
            </span>
            08-18
           </time>
           <a href="/events/python-events/1971/">
            EuroSciPy 2025
           </a>
          </li>
         </ul>
        </div>
       </div>
      </div>
      <div class="row">
       <div class="medium-widget success-stories-widget">
        <div class="shrubbery">
         <h2 class="widget-title">
          <span aria-hidden="true" class="icon-success-stories">
          </span>
          Success Stories
         </h2>
         <p class="give-me-more">
          <a href="/success-stories/" title="More Success Stories">
           More
          </a>
         </p>
         <div class="success-story-item" id="success-story-932">
          <blockquote>
           <a href="/success-stories/abridging-clinical-conversations-using-python/">
            Python powers major aspects of Abridge’s ML lifecycle, including data annotation,  research and experimentation, and ML model deployment to production.
           </a>
          </blockquote>
          <table border="0" cellpadding="0" cellspacing="0" class="quote-from" width="100%">
           <tbody>
            <tr>
             <td>
              <p>
               <a href="/success-stories/abridging-clinical-conversations-using-python/">
                Abridging clinical conversations using Python
               </a>
               <em>
                by Nimshi Venkat and Sandeep Konam
               </em>
              </p>
             </td>
            </tr>
           </tbody>
          </table>
         </div>
        </div>
        <!-- end .shrubbery -->
       </div>
       <div class="medium-widget applications-widget last">
        <div class="shrubbery">
         <h2 class="widget-title">
          <span aria-hidden="true" class="icon-python">
          </span>
          Use Python for…
         </h2>
         <p class="give-me-more">
          <a href="/about/apps" title="More Applications">
           More
          </a>
         </p>
         <ul class="menu">
          <li>
           <b>
            Web Development
           </b>
           :
           <span class="tag-wrapper">
            <a class="tag" href="http://www.djangoproject.com/">
             Django
            </a>
            ,
            <a class="tag" href="http://www.pylonsproject.org/">
             Pyramid
            </a>
            ,
            <a class="tag" href="http://bottlepy.org">
             Bottle
            </a>
            ,
            <a class="tag" href="http://tornadoweb.org">
             Tornado
            </a>
            ,
            <a class="tag" href="http://flask.pocoo.org/">
             Flask
            </a>
            ,
            <a class="tag" href="http://www.web2py.com/">
             web2py
            </a>
           </span>
          </li>
          <li>
           <b>
            GUI Development
           </b>
           :
           <span class="tag-wrapper">
            <a class="tag" href="http://wiki.python.org/moin/TkInter">
             tkInter
            </a>
            ,
            <a class="tag" href="https://wiki.gnome.org/Projects/PyGObject">
             PyGObject
            </a>
            ,
            <a class="tag" href="http://www.riverbankcomputing.co.uk/software/pyqt/intro">
             PyQt
            </a>
            ,
            <a class="tag" href="https://wiki.qt.io/PySide">
             PySide
            </a>
            ,
            <a class="tag" href="https://kivy.org/">
             Kivy
            </a>
            ,
            <a class="tag" href="http://www.wxpython.org/">
             wxPython
            </a>
            ,
            <a class="tag" href="https://dearpygui.readthedocs.io/en/latest/">
             DearPyGui
            </a>
           </span>
          </li>
          <li>
           <b>
            Scientific and Numeric
           </b>
           :
           <span class="tag-wrapper">
            <a class="tag" href="http://www.scipy.org">
             SciPy
            </a>
            ,
            <a class="tag" href="http://pandas.pydata.org/">
             Pandas
            </a>
            ,
            <a class="tag" href="http://ipython.org">
             IPython
            </a>
           </span>
          </li>
          <li>
           <b>
            Software Development
           </b>
           :
           <span class="tag-wrapper">
            <a class="tag" href="http://buildbot.net/">
             Buildbot
            </a>
            ,
            <a class="tag" href="http://trac.edgewall.org/">
             Trac
            </a>
            ,
            <a class="tag" href="http://roundup.sourceforge.net/">
             Roundup
            </a>
           </span>
          </li>
          <li>
           <b>
            System Administration
           </b>
           :
           <span class="tag-wrapper">
            <a class="tag" href="http://www.ansible.com">
             Ansible
            </a>
            ,
            <a class="tag" href="https://saltproject.io">
             Salt
            </a>
            ,
            <a class="tag" href="https://www.openstack.org">
             OpenStack
            </a>
            ,
            <a class="tag" href="https://xon.sh">
             xonsh
            </a>
           </span>
          </li>
         </ul>
        </div>
        <!-- end .shrubbery -->
       </div>
      </div>
      <div class="psf-widget">
       <div class="python-logo">
       </div>
       <h2 class="widget-title">
        <span class="prompt">
         &gt;&gt;&gt;
        </span>
        <a href="/psf/">
         Python Software Foundation
        </a>
       </h2>
       <p>
        The mission of the Python Software Foundation is to promote, protect, and advance the Python programming language, and to support and facilitate the growth of a diverse and international community of Python programmers.
        <a class="readmore" href="/psf/">
         Learn more
        </a>
       </p>
       <p class="click-these">
        <a class="button" href="/psf/membership/">
         Become a Member
        </a>
        <a class="button" href="/psf/donations/">
         Donate to the PSF
        </a>
       </p>
      </div>
     </section>
    </div>
    <!-- end .container -->
   </div>
   <!-- end #content .content-wrapper -->
   <!-- Footer and social media list -->
   <footer class="main-footer" id="site-map" role="contentinfo">
    <div class="main-footer-links">
     <div class="container">
      <a class="jump-link" href="#python-network" id="back-to-top-1">
       <span aria-hidden="true" class="icon-arrow-up">
        <span>
         ▲
        </span>
       </span>
       Back to Top
      </a>
      <ul class="sitemap navigation menu do-not-print" id="container" role="tree">
       <li class="tier-1 element-1">
        <a href="/about/">
         About
        </a>
        <ul class="subnav menu">
         <li class="tier-2 element-1" role="treeitem">
          <a href="/about/apps/" title="">
           Applications
          </a>
         </li>
         <li class="tier-2 element-2" role="treeitem">
          <a href="/about/quotes/" title="">
           Quotes
          </a>
         </li>
         <li class="tier-2 element-3" role="treeitem">
          <a href="/about/gettingstarted/" title="">
           Getting Started
          </a>
         </li>
         <li class="tier-2 element-4" role="treeitem">
          <a href="/about/help/" title="">
           Help
          </a>
         </li>
         <li class="tier-2 element-5" role="treeitem">
          <a href="http://brochure.getpython.info/" title="">
           Python Brochure
          </a>
         </li>
        </ul>
       </li>
       <li class="tier-1 element-2">
        <a href="/downloads/">
         Downloads
        </a>
        <ul class="subnav menu">
         <li class="tier-2 element-1" role="treeitem">
          <a href="/downloads/" title="">
           All releases
          </a>
         </li>
         <li class="tier-2 element-2" role="treeitem">
          <a href="/downloads/source/" title="">
           Source code
          </a>
         </li>
         <li class="tier-2 element-3" role="treeitem">
          <a href="/downloads/windows/" title="">
           Windows
          </a>
         </li>
         <li class="tier-2 element-4" role="treeitem">
          <a href="/downloads/macos/" title="">
           macOS
          </a>
         </li>
         <li class="tier-2 element-5" role="treeitem">
          <a href="/download/other/" title="">
           Other Platforms
          </a>
         </li>
         <li class="tier-2 element-6" role="treeitem">
          <a href="https://docs.python.org/3/license.html" title="">
           License
          </a>
         </li>
         <li class="tier-2 element-7" role="treeitem">
          <a href="/download/alternatives" title="">
           Alternative Implementations
          </a>
         </li>
        </ul>
       </li>
       <li class="tier-1 element-3">
        <a href="/doc/">
         Documentation
        </a>
        <ul class="subnav menu">
         <li class="tier-2 element-1" role="treeitem">
          <a href="/doc/" title="">
           Docs
          </a>
         </li>
         <li class="tier-2 element-2" role="treeitem">
          <a href="/doc/av" title="">
           Audio/Visual Talks
          </a>
         </li>
         <li class="tier-2 element-3" role="treeitem">
          <a href="https://wiki.python.org/moin/BeginnersGuide" title="">
           Beginner's Guide
          </a>
         </li>
         <li class="tier-2 element-4" role="treeitem">
          <a href="https://devguide.python.org/" title="">
           Developer's Guide
          </a>
         </li>
         <li class="tier-2 element-5" role="treeitem">
          <a href="https://docs.python.org/faq/" title="">
           FAQ
          </a>
         </li>
         <li class="tier-2 element-6" role="treeitem">
          <a href="http://wiki.python.org/moin/Languages" title="">
           Non-English Docs
          </a>
         </li>
         <li class="tier-2 element-7" role="treeitem">
          <a href="https://peps.python.org" title="">
           PEP Index
          </a>
         </li>
         <li class="tier-2 element-8" role="treeitem">
          <a href="https://wiki.python.org/moin/PythonBooks" title="">
           Python Books
          </a>
         </li>
         <li class="tier-2 element-9" role="treeitem">
          <a href="/doc/essays/" title="">
           Python Essays
          </a>
         </li>
        </ul>
       </li>
       <li class="tier-1 element-4">
        <a href="/community/">
         Community
        </a>
        <ul class="subnav menu">
         <li class="tier-2 element-1" role="treeitem">
          <a href="/community/diversity/" title="">
           Diversity
          </a>
         </li>
         <li class="tier-2 element-2" role="treeitem">
          <a href="/community/lists/" title="">
           Mailing Lists
          </a>
         </li>
         <li class="tier-2 element-3" role="treeitem">
          <a href="/community/irc/" title="">
           IRC
          </a>
         </li>
         <li class="tier-2 element-4" role="treeitem">
          <a href="/community/forums/" title="">
           Forums
          </a>
         </li>
         <li class="tier-2 element-5" role="treeitem">
          <a href="/psf/annual-report/2024/" title="">
           PSF Annual Impact Report
          </a>
         </li>
         <li class="tier-2 element-6" role="treeitem">
          <a href="/community/workshops/" title="">
           Python Conferences
          </a>
         </li>
         <li class="tier-2 element-7" role="treeitem">
          <a href="/community/sigs/" title="">
           Special Interest Groups
          </a>
         </li>
         <li class="tier-2 element-8" role="treeitem">
          <a href="/community/logos/" title="">
           Python Logo
          </a>
         </li>
         <li class="tier-2 element-9" role="treeitem">
          <a href="https://wiki.python.org/moin/" title="">
           Python Wiki
          </a>
         </li>
         <li class="tier-2 element-10" role="treeitem">
          <a href="/psf/conduct/" title="">
           Code of Conduct
          </a>
         </li>
         <li class="tier-2 element-11" role="treeitem">
          <a href="/community/awards" title="">
           Community Awards
          </a>
         </li>
         <li class="tier-2 element-12" role="treeitem">
          <a href="/psf/get-involved/" title="">
           Get Involved
          </a>
         </li>
         <li class="tier-2 element-13" role="treeitem">
          <a href="/psf/community-stories/" title="">
           Shared Stories
          </a>
         </li>
        </ul>
       </li>
       <li class="tier-1 element-5">
        <a href="/success-stories/" title="success-stories">
         Success Stories
        </a>
        <ul class="subnav menu">
         <li class="tier-2 element-1" role="treeitem">
          <a href="/success-stories/category/arts/" title="">
           Arts
          </a>
         </li>
         <li class="tier-2 element-2" role="treeitem">
          <a href="/success-stories/category/business/" title="">
           Business
          </a>
         </li>
         <li class="tier-2 element-3" role="treeitem">
          <a href="/success-stories/category/education/" title="">
           Education
          </a>
         </li>
         <li class="tier-2 element-4" role="treeitem">
          <a href="/success-stories/category/engineering/" title="">
           Engineering
          </a>
         </li>
         <li class="tier-2 element-5" role="treeitem">
          <a href="/success-stories/category/government/" title="">
           Government
          </a>
         </li>
         <li class="tier-2 element-6" role="treeitem">
          <a href="/success-stories/category/scientific/" title="">
           Scientific
          </a>
         </li>
         <li class="tier-2 element-7" role="treeitem">
          <a href="/success-stories/category/software-development/" title="">
           Software Development
          </a>
         </li>
        </ul>
       </li>
       <li class="tier-1 element-6">
        <a href="/blogs/" title="News from around the Python world">
         News
        </a>
        <ul class="subnav menu">
         <li class="tier-2 element-1" role="treeitem">
          <a href="/blogs/" title="Python Insider Blog Posts">
           Python News
          </a>
         </li>
         <li class="tier-2 element-2" role="treeitem">
          <a href="/psf/newsletter/" title="Python Software Foundation Newsletter">
           PSF Newsletter
          </a>
         </li>
         <li class="tier-2 element-3" role="treeitem">
          <a href="http://pyfound.blogspot.com/" title="PSF Blog">
           PSF News
          </a>
         </li>
         <li class="tier-2 element-4" role="treeitem">
          <a href="http://pycon.blogspot.com/" title="PyCon Blog">
           PyCon US News
          </a>
         </li>
         <li class="tier-2 element-5" role="treeitem">
          <a href="http://planetpython.org/" title="Planet Python">
           News from the Community
          </a>
         </li>
        </ul>
       </li>
       <li class="tier-1 element-7">
        <a href="/events/">
         Events
        </a>
        <ul class="subnav menu">
         <li class="tier-2 element-1" role="treeitem">
          <a href="/events/python-events/" title="">
           Python Events
          </a>
         </li>
         <li class="tier-2 element-2" role="treeitem">
          <a href="/events/python-user-group/" title="">
           User Group Events
          </a>
         </li>
         <li class="tier-2 element-3" role="treeitem">
          <a href="/events/python-events/past/" title="">
           Python Events Archive
          </a>
         </li>
         <li class="tier-2 element-4" role="treeitem">
          <a href="/events/python-user-group/past/" title="">
           User Group Events Archive
          </a>
         </li>
         <li class="tier-2 element-5" role="treeitem">
          <a href="https://wiki.python.org/moin/PythonEventsCalendar#Submitting_an_Event" title="">
           Submit an Event
          </a>
         </li>
        </ul>
       </li>
       <li class="tier-1 element-8">
        <a href="/dev/">
         Contributing
        </a>
        <ul class="subnav menu">
         <li class="tier-2 element-1" role="treeitem">
          <a href="https://devguide.python.org/" title="">
           Developer's Guide
          </a>
         </li>
         <li class="tier-2 element-2" role="treeitem">
          <a href="https://github.com/python/cpython/issues" title="">
           Issue Tracker
          </a>
         </li>
         <li class="tier-2 element-3" role="treeitem">
          <a href="https://mail.python.org/mailman/listinfo/python-dev" title="">
           python-dev list
          </a>
         </li>
         <li class="tier-2 element-4" role="treeitem">
          <a href="/dev/core-mentorship/" title="">
           Core Mentorship
          </a>
         </li>
         <li class="tier-2 element-5" role="treeitem">
          <a href="/dev/security/" title="">
           Report a Security Issue
          </a>
         </li>
        </ul>
       </li>
      </ul>
      <a class="jump-link" href="#python-network" id="back-to-top-2">
       <span aria-hidden="true" class="icon-arrow-up">
        <span>
         ▲
        </span>
       </span>
       Back to Top
      </a>
     </div>
     <!-- end .container -->
    </div>
    <!-- end .main-footer-links -->
    <div class="site-base">
     <div class="container">
      <ul class="footer-links navigation menu do-not-print" role="tree">
       <li class="tier-1 element-1">
        <a href="/about/help/">
         Help &amp;
         <span class="say-no-more">
          General
         </span>
         Contact
        </a>
       </li>
       <li class="tier-1 element-2">
        <a href="/community/diversity/">
         Diversity
         <span class="say-no-more">
          Initiatives
         </span>
        </a>
       </li>
       <li class="tier-1 element-3">
        <a href="https://github.com/python/pythondotorg/issues">
         Submit Website Bug
        </a>
       </li>
       <li class="tier-1 element-4">
        <a href="https://status.python.org/">
         Status
         <span class="python-status-indicator-default" id="python-status-indicator">
         </span>
        </a>
       </li>
      </ul>
      <div class="copyright">
       <p>
        <small>
         <span class="pre">
          Copyright ©2001-2025.
         </span>
         <span class="pre">
          <a href="/psf-landing/">
           Python Software Foundation
          </a>
         </span>
         <span class="pre">
          <a href="/about/legal/">
           Legal Statements
          </a>
         </span>
         <span class="pre">
          <a href="https://policies.python.org/python.org/Privacy-Notice/">
           Privacy Notice
          </a>
         </span>
         <!--&nbsp;<span class="pre"><a href="/psf/community-infrastructure">Powered by PSF Community Infrastructure</a></span>-->
        </small>
       </p>
      </div>
     </div>
     <!-- end .container -->
    </div>
    <!-- end .site-base -->
   </footer>
  </div>
  <!-- end #touchnav-wrapper -->
  <script src="//ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js">
  </script>
  <script>
   window.jQuery || document.write('<script src="/static/js/libs/jquery-1.8.2.min.js"><\/script>')
  </script>
  <script src="//ajax.googleapis.com/ajax/libs/jqueryui/1.12.1/jquery-ui.min.js">
  </script>
  <script>
   window.jQuery || document.write('<script src="/static/js/libs/jquery-ui-1.12.1.min.js"><\/script>')
  </script>
  <script src="/static/js/libs/masonry.pkgd.min.js">
  </script>
  <script src="/static/js/libs/html-includes.js">
  </script>
  <script charset="utf-8" src="/static/js/main-min.ef82c06437cf.js" type="text/javascript">
  </script>
  <!--[if lte IE 7]>
    <script type="text/javascript" src="/static/js/plugins/IE8-min.8af6e26c7a3b.js" charset="utf-8"></script>
    
    
    <![endif]-->
  <!--[if lte IE 8]>
    <script type="text/javascript" src="/static/js/plugins/getComputedStyle-min.d41d8cd98f00.js" charset="utf-8"></script>
    
    
    <![endif]-->
 </body>
</html>

########################################

Only head tag
--------------------
<head>
<script data-domain="python.org" defer="" src="https://analytics.python.org/js/script.outbound-links.js"></script>
<meta charset="utf-8"/>
<meta content="IE=edge" http-equiv="X-UA-Compatible"/>
<link href="//ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js" rel="prefetch"/>
<link href="//ajax.googleapis.com/ajax/libs/jqueryui/1.12.1/jquery-ui.min.js" rel="prefetch"/>
<meta content="Python.org" name="application-name"/>
<meta content="The official home of the Python Programming Language" name="msapplication-tooltip"/>
<meta content="Python.org" name="apple-mobile-web-app-title"/>
<meta content="yes" name="apple-mobile-web-app-capable"/>
<meta content="black" name="apple-mobile-web-app-status-bar-style"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<meta content="True" name="HandheldFriendly"/>
<meta content="telephone=no" name="format-detection"/>
<meta content="on" http-equiv="cleartype"/>
<meta content="false" http-equiv="imagetoolbar"/>
<script async="" crossorigin="anonymous" integrity="sha256-U3hKDidudIaxBDEzwGJApJgPEf2mWk6cfMWghrAa6i0= sha384-UcmsCqcNRSLW/dV3Lo1oCi2/VaurXbib6p4HyUEOeIa/4OpsrnucrugAefzVZJfI sha512-q4t1L4xEjGV2R4hzqCa41P8jrgFUS8xTb8rdNv4FGvw7FpydVj/kkxBJHOiaoxHa8olCcx1Slk9K+3sNbsM4ug==" src="https://media.ethicalads.io/media/client/v1.4.0/ethicalads.min.js"></script>
<script src="/static/js/libs/modernizr.js"></script>
<link href="/static/stylesheets/style.08a078d0aa02.css" media="all" rel="stylesheet" title="default" type="text/css">
<link href="/static/stylesheets/mq.98d6092b2ada.css" media="not print, braille, embossed, speech, tty" rel="stylesheet" type="text/css">
<link href="/static/stylesheets/no-mq.bf0c425cdb73.css" media="screen" rel="stylesheet" type="text/css"/>
<!--[if (lte IE 8)&(!IEMobile)]>
    <link href="/static/stylesheets/no-mq.bf0c425cdb73.css" rel="stylesheet" type="text/css" media="screen" />
    
    
    <![endif]-->
<link href="//ajax.googleapis.com/ajax/libs/jqueryui/1.12.1/themes/smoothness/jquery-ui.css" rel="stylesheet"/>
<link href="/static/favicon.ico" rel="icon" type="image/x-icon"/>
<link href="/static/apple-touch-icon-144x144-precomposed.png" rel="apple-touch-icon-precomposed" sizes="144x144"/>
<link href="/static/apple-touch-icon-114x114-precomposed.png" rel="apple-touch-icon-precomposed" sizes="114x114"/>
<link href="/static/apple-touch-icon-72x72-precomposed.png" rel="apple-touch-icon-precomposed" sizes="72x72"/>
<link href="/static/apple-touch-icon-precomposed.png" rel="apple-touch-icon-precomposed"/>
<link href="/static/apple-touch-icon-precomposed.png" rel="apple-touch-icon"/>
<meta content="/static/metro-icon-144x144.png" name="msapplication-TileImage"/><!-- white shape -->
<meta content="#3673a5" name="msapplication-TileColor"/><!-- python blue -->
<meta content="#3673a5" name="msapplication-navbutton-color"/>
<title>Welcome to Python.org</title>
<meta content="The official home of the Python Programming Language" name="description"/>
<meta content="Python programming language object oriented web free open source software license documentation download community" name="keywords"/>
<meta content="website" property="og:type"/>
<meta content="Python.org" property="og:site_name"/>
<meta content="Welcome to Python.org" property="og:title"/>
<meta content="The official home of the Python Programming Language" property="og:description"/>
<meta content="https://www.python.org/static/opengraph-icon-200x200.png" property="og:image"/>
<meta content="https://www.python.org/static/opengraph-icon-200x200.png" property="og:image:secure_url"/>
<meta content="https://www.python.org/" property="og:url"/>
<link href="/humans.txt" rel="author"/>
<link href="https://peps.python.org/peps.rss" rel="alternate" title="Python Enhancement Proposals" type="application/rss+xml"/>
<link href="https://www.python.org/jobs/feed/rss/" rel="alternate" title="Python Job Opportunities" type="application/rss+xml"/>
<link href="https://feeds.feedburner.com/PythonSoftwareFoundationNews" rel="alternate" title="Python Software Foundation News" type="application/rss+xml"/>
<link href="https://feeds.feedburner.com/PythonInsider" rel="alternate" title="Python Insider" type="application/rss+xml"/>
<link href="https://www.python.org/downloads/feed.rss" rel="alternate" title="Python Releases" type="application/rss+xml"/>
<script type="application/ld+json">
     {
       "@context": "https://schema.org",
       "@type": "WebSite",
       "url": "https://www.python.org/",
       "potentialAction": {
         "@type": "SearchAction",
         "target": "https://www.python.org/search/?q={search_term_string}",
         "query-input": "required name=search_term_string"
       }
     }
    </script>
<script type="text/javascript">
    var _gaq = _gaq || [];
    _gaq.push(['_setAccount', 'UA-39055973-1']);
    _gaq.push(['_trackPageview']);

    (function() {
        var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
        ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
        var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
    })();
    </script>
</link></link></head>
########################################

Only Body tag
--------------------
<body class="python home" id="homepage">
<div id="touchnav-wrapper">
<div class="do-not-print" id="nojs">
<p><strong>Notice:</strong> While JavaScript is not essential for this website, your interaction with the content will be limited. Please turn JavaScript on for the full experience. </p>
</div>
<!--[if lte IE 8]>
        <div id="oldie-warning" class="do-not-print">
            <p>
                <strong>Notice:</strong> Your browser is <em>ancient</em>. Please
                <a href="http://browsehappy.com/">upgrade to a different browser</a> to experience a better web.
            </p>
        </div>
        <![endif]-->
<!-- Sister Site Links -->
<div class="top-bar do-not-print" id="top">
<nav class="meta-navigation container" role="navigation">
<div class="skip-link screen-reader-text">
<a href="#content" title="Skip to content">Skip to content</a>
</div>
<a aria-hidden="true" class="jump-link" href="#python-network" id="close-python-network">
<span aria-hidden="true" class="icon-arrow-down"><span>▼</span></span> Close
                </a>
<ul class="menu" role="tree">
<li class="python-meta current_item selectedcurrent_branch selected">
<a class="current_item selectedcurrent_branch selected" href="/" title="The Python Programming Language">Python</a>
</li>
<li class="psf-meta">
<a href="https://www.python.org/psf/" title="The Python Software Foundation">PSF</a>
</li>
<li class="docs-meta">
<a href="https://docs.python.org" title="Python Documentation">Docs</a>
</li>
<li class="pypi-meta">
<a href="https://pypi.org/" title="Python Package Index">PyPI</a>
</li>
<li class="jobs-meta">
<a href="/jobs/" title="Python Job Board">Jobs</a>
</li>
<li class="shop-meta">
<a href="/community/">Community</a>
</li>
</ul>
<a aria-hidden="true" class="jump-link" href="#top" id="python-network">
<span aria-hidden="true" class="icon-arrow-up"><span>▲</span></span> The Python Network
                </a>
</nav>
</div>
<!-- Header elements -->
<header class="main-header" role="banner">
<div class="container">
<h1 class="site-headline">
<a href="/"><img alt="python™" class="python-logo" src="/static/img/python-logo.png"/></a>
</h1>
<div class="options-bar-container do-not-print">
<a class="donate-button" href="https://psfmember.org/civicrm/contribute/transact?reset=1&amp;id=2">Donate</a>
<div class="options-bar">
<a class="jump-to-menu" href="#site-map" id="site-map-link"><span class="menu-icon">≡</span> Menu</a><form action="/search/" class="search-the-site" method="get">
<fieldset title="Search Python.org">
<span aria-hidden="true" class="icon-search"></span>
<label class="screen-reader-text" for="id-search-field">Search This Site</label>
<input class="search-field" id="id-search-field" name="q" placeholder="Search" role="textbox" tabindex="1" type="search" value=""/>
<button class="search-button" id="submit" name="submit" tabindex="3" title="Submit this Search" type="submit">
                                    GO
                                </button>
<!--[if IE]><input type="text" style="display: none;" disabled="disabled" size="1" tabindex="4"><![endif]-->
</fieldset>
</form><span class="breaker"></span><div aria-hidden="true" class="adjust-font-size">
<ul aria-label="Adjust Text Size on Page" class="navigation menu">
<li aria-haspopup="true" class="tier-1 last">
<a class="action-trigger" href="#"><strong><small>A</small> A</strong></a>
<ul class="subnav menu">
<li class="tier-2 element-1" role="treeitem"><a class="text-shrink" href="javascript:;" title="Make Text Smaller">Smaller</a></li>
<li class="tier-2 element-2" role="treeitem"><a class="text-grow" href="javascript:;" title="Make Text Larger">Larger</a></li>
<li class="tier-2 element-3" role="treeitem"><a class="text-reset" href="javascript:;" title="Reset any font size changes I have made">Reset</a></li>
</ul>
</li>
</ul>
</div><div class="winkwink-nudgenudge">
<ul aria-label="Social Media Navigation" class="navigation menu">
<li aria-haspopup="true" class="tier-1 last">
<a class="action-trigger" href="#">Socialize</a>
<ul class="subnav menu">
<li class="tier-2 element-1" role="treeitem"><a href="https://www.linkedin.com/company/python-software-foundation/"><i aria-hidden="true" class="fa fa-linkedin-square"></i>LinkedIn</a></li>
<li class="tier-2 element-2" role="treeitem"><a href="https://fosstodon.org/@ThePSF"><span aria-hidden="true" class="icon-mastodon"></span>Mastodon</a></li>
<li class="tier-2 element-3" role="treeitem"><a href="/community/irc/"><span aria-hidden="true" class="icon-freenode"></span>Chat on IRC</a></li>
<li class="tier-2 element-4" role="treeitem"><a href="https://twitter.com/ThePSF"><span aria-hidden="true" class="icon-twitter"></span>Twitter</a></li>
</ul>
</li>
</ul>
</div>
<span data-html-include="/authenticated"></span>
</div><!-- end options-bar -->
</div>
<nav class="python-navigation main-navigation do-not-print" id="mainnav" role="navigation">
<ul aria-label="Main Navigation" class="navigation menu" role="menubar">
<li aria-haspopup="true" class="tier-1 element-1" id="about">
<a class="" href="/about/" title="">About</a>
<ul aria-hidden="true" class="subnav menu" role="menu">
<li class="tier-2 element-1" role="treeitem"><a href="/about/apps/" title="">Applications</a></li>
<li class="tier-2 element-2" role="treeitem"><a href="/about/quotes/" title="">Quotes</a></li>
<li class="tier-2 element-3" role="treeitem"><a href="/about/gettingstarted/" title="">Getting Started</a></li>
<li class="tier-2 element-4" role="treeitem"><a href="/about/help/" title="">Help</a></li>
<li class="tier-2 element-5" role="treeitem"><a href="http://brochure.getpython.info/" title="">Python Brochure</a></li>
</ul>
</li>
<li aria-haspopup="true" class="tier-1 element-2" id="downloads">
<a class="" href="/downloads/" title="">Downloads</a>
<ul aria-hidden="true" class="subnav menu" role="menu">
<li class="tier-2 element-1" role="treeitem"><a href="/downloads/" title="">All releases</a></li>
<li class="tier-2 element-2" role="treeitem"><a href="/downloads/source/" title="">Source code</a></li>
<li class="tier-2 element-3" role="treeitem"><a href="/downloads/windows/" title="">Windows</a></li>
<li class="tier-2 element-4" role="treeitem"><a href="/downloads/macos/" title="">macOS</a></li>
<li class="tier-2 element-5" role="treeitem"><a href="/download/other/" title="">Other Platforms</a></li>
<li class="tier-2 element-6" role="treeitem"><a href="https://docs.python.org/3/license.html" title="">License</a></li>
<li class="tier-2 element-7" role="treeitem"><a href="/download/alternatives" title="">Alternative Implementations</a></li>
</ul>
</li>
<li aria-haspopup="true" class="tier-1 element-3" id="documentation">
<a class="" href="/doc/" title="">Documentation</a>
<ul aria-hidden="true" class="subnav menu" role="menu">
<li class="tier-2 element-1" role="treeitem"><a href="/doc/" title="">Docs</a></li>
<li class="tier-2 element-2" role="treeitem"><a href="/doc/av" title="">Audio/Visual Talks</a></li>
<li class="tier-2 element-3" role="treeitem"><a href="https://wiki.python.org/moin/BeginnersGuide" title="">Beginner's Guide</a></li>
<li class="tier-2 element-4" role="treeitem"><a href="https://devguide.python.org/" title="">Developer's Guide</a></li>
<li class="tier-2 element-5" role="treeitem"><a href="https://docs.python.org/faq/" title="">FAQ</a></li>
<li class="tier-2 element-6" role="treeitem"><a href="http://wiki.python.org/moin/Languages" title="">Non-English Docs</a></li>
<li class="tier-2 element-7" role="treeitem"><a href="https://peps.python.org" title="">PEP Index</a></li>
<li class="tier-2 element-8" role="treeitem"><a href="https://wiki.python.org/moin/PythonBooks" title="">Python Books</a></li>
<li class="tier-2 element-9" role="treeitem"><a href="/doc/essays/" title="">Python Essays</a></li>
</ul>
</li>
<li aria-haspopup="true" class="tier-1 element-4" id="community">
<a class="" href="/community/" title="">Community</a>
<ul aria-hidden="true" class="subnav menu" role="menu">
<li class="tier-2 element-1" role="treeitem"><a href="/community/diversity/" title="">Diversity</a></li>
<li class="tier-2 element-2" role="treeitem"><a href="/community/lists/" title="">Mailing Lists</a></li>
<li class="tier-2 element-3" role="treeitem"><a href="/community/irc/" title="">IRC</a></li>
<li class="tier-2 element-4" role="treeitem"><a href="/community/forums/" title="">Forums</a></li>
<li class="tier-2 element-5" role="treeitem"><a href="/psf/annual-report/2024/" title="">PSF Annual Impact Report</a></li>
<li class="tier-2 element-6" role="treeitem"><a href="/community/workshops/" title="">Python Conferences</a></li>
<li class="tier-2 element-7" role="treeitem"><a href="/community/sigs/" title="">Special Interest Groups</a></li>
<li class="tier-2 element-8" role="treeitem"><a href="/community/logos/" title="">Python Logo</a></li>
<li class="tier-2 element-9" role="treeitem"><a href="https://wiki.python.org/moin/" title="">Python Wiki</a></li>
<li class="tier-2 element-10" role="treeitem"><a href="/psf/conduct/" title="">Code of Conduct</a></li>
<li class="tier-2 element-11" role="treeitem"><a href="/community/awards" title="">Community Awards</a></li>
<li class="tier-2 element-12" role="treeitem"><a href="/psf/get-involved/" title="">Get Involved</a></li>
<li class="tier-2 element-13" role="treeitem"><a href="/psf/community-stories/" title="">Shared Stories</a></li>
</ul>
</li>
<li aria-haspopup="true" class="tier-1 element-5" id="success-stories">
<a class="" href="/success-stories/" title="success-stories">Success Stories</a>
<ul aria-hidden="true" class="subnav menu" role="menu">
<li class="tier-2 element-1" role="treeitem"><a href="/success-stories/category/arts/" title="">Arts</a></li>
<li class="tier-2 element-2" role="treeitem"><a href="/success-stories/category/business/" title="">Business</a></li>
<li class="tier-2 element-3" role="treeitem"><a href="/success-stories/category/education/" title="">Education</a></li>
<li class="tier-2 element-4" role="treeitem"><a href="/success-stories/category/engineering/" title="">Engineering</a></li>
<li class="tier-2 element-5" role="treeitem"><a href="/success-stories/category/government/" title="">Government</a></li>
<li class="tier-2 element-6" role="treeitem"><a href="/success-stories/category/scientific/" title="">Scientific</a></li>
<li class="tier-2 element-7" role="treeitem"><a href="/success-stories/category/software-development/" title="">Software Development</a></li>
</ul>
</li>
<li aria-haspopup="true" class="tier-1 element-6" id="news">
<a class="" href="/blogs/" title="News from around the Python world">News</a>
<ul aria-hidden="true" class="subnav menu" role="menu">
<li class="tier-2 element-1" role="treeitem"><a href="/blogs/" title="Python Insider Blog Posts">Python News</a></li>
<li class="tier-2 element-2" role="treeitem"><a href="/psf/newsletter/" title="Python Software Foundation Newsletter">PSF Newsletter</a></li>
<li class="tier-2 element-3" role="treeitem"><a href="http://pyfound.blogspot.com/" title="PSF Blog">PSF News</a></li>
<li class="tier-2 element-4" role="treeitem"><a href="http://pycon.blogspot.com/" title="PyCon Blog">PyCon US News</a></li>
<li class="tier-2 element-5" role="treeitem"><a href="http://planetpython.org/" title="Planet Python">News from the Community</a></li>
</ul>
</li>
<li aria-haspopup="true" class="tier-1 element-7" id="events">
<a class="" href="/events/" title="">Events</a>
<ul aria-hidden="true" class="subnav menu" role="menu">
<li class="tier-2 element-1" role="treeitem"><a href="/events/python-events/" title="">Python Events</a></li>
<li class="tier-2 element-2" role="treeitem"><a href="/events/python-user-group/" title="">User Group Events</a></li>
<li class="tier-2 element-3" role="treeitem"><a href="/events/python-events/past/" title="">Python Events Archive</a></li>
<li class="tier-2 element-4" role="treeitem"><a href="/events/python-user-group/past/" title="">User Group Events Archive</a></li>
<li class="tier-2 element-5" role="treeitem"><a href="https://wiki.python.org/moin/PythonEventsCalendar#Submitting_an_Event" title="">Submit an Event</a></li>
</ul>
</li>
</ul>
</nav>
<div class="header-banner"> <!-- for optional "do-not-print" class -->
<div class="flex-slideshow slideshow" id="dive-into-python">
<ul class="launch-shell menu" id="launch-shell">
<li>
<a class="button prompt" data-shell-container="#dive-into-python" href="/shell/" id="start-shell">&gt;_
                        <span class="message">Launch Interactive Shell</span>
</a>
</li>
</ul>
<ul class="slides menu">
<li>
<div class="slide-code"><pre><code><span class="comment"># Python 3: Fibonacci series up to n</span>
&gt;&gt;&gt; def fib(n):
&gt;&gt;&gt;     a, b = 0, 1
&gt;&gt;&gt;     while a &lt; n:
&gt;&gt;&gt;         print(a, end=' ')
&gt;&gt;&gt;         a, b = b, a+b
&gt;&gt;&gt;     print()
&gt;&gt;&gt; fib(1000)
<span class="output">0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987</span></code></pre></div>
<div class="slide-copy"><h1>Functions Defined</h1>
<p>The core of extensible programming is defining functions. Python allows mandatory and optional arguments, keyword arguments, and even arbitrary argument lists. <a href="//docs.python.org/3/tutorial/controlflow.html#defining-functions">More about defining functions in Python 3</a></p></div>
</li>
<li>
<div class="slide-code"><pre><code><span class="comment"># Python 3: List comprehensions</span>
&gt;&gt;&gt; fruits = ['Banana', 'Apple', 'Lime']
&gt;&gt;&gt; loud_fruits = [fruit.upper() for fruit in fruits]
&gt;&gt;&gt; print(loud_fruits)
<span class="output">['BANANA', 'APPLE', 'LIME']</span>

<span class="comment"># List and the enumerate function</span>
&gt;&gt;&gt; list(enumerate(fruits))
<span class="output">[(0, 'Banana'), (1, 'Apple'), (2, 'Lime')]</span></code></pre></div>
<div class="slide-copy"><h1>Compound Data Types</h1>
<p>Lists (known as arrays in other languages) are one of the compound data types that Python understands. Lists can be indexed, sliced and manipulated with other built-in functions. <a href="//docs.python.org/3/tutorial/introduction.html#lists">More about lists in Python 3</a></p></div>
</li>
<li>
<div class="slide-code"><pre><code><span class="comment"># Python 3: Simple arithmetic</span>
&gt;&gt;&gt; 1 / 2
<span class="output">0.5</span>
&gt;&gt;&gt; 2 ** 3
<span class="output">8</span>
&gt;&gt;&gt; 17 / 3  <span class="comment"># classic division returns a float</span>
<span class="output">5.666666666666667</span>
&gt;&gt;&gt; 17 // 3  <span class="comment"># floor division</span>
<span class="output">5</span></code></pre></div>
<div class="slide-copy"><h1>Intuitive Interpretation</h1>
<p>Calculations are simple with Python, and expression syntax is straightforward: the operators <code>+</code>, <code>-</code>, <code>*</code> and <code>/</code> work as expected; parentheses <code>()</code> can be used for grouping. <a href="http://docs.python.org/3/tutorial/introduction.html#using-python-as-a-calculator">More about simple math functions in Python 3</a>.</p></div>
</li>
<li>
<div class="slide-code"><pre><code><span class="comment"># For loop on a list</span>
&gt;&gt;&gt; numbers = [2, 4, 6, 8]
&gt;&gt;&gt; product = 1
&gt;&gt;&gt; for number in numbers:
...    product = product * number
... 
&gt;&gt;&gt; print('The product is:', product)
<span class="output">The product is: 384</span></code></pre></div>
<div class="slide-copy"><h1>All the Flow You’d Expect</h1>
<p>Python knows the usual control flow statements that other languages speak — <code>if</code>, <code>for</code>, <code>while</code> and <code>range</code> — with some of its own twists, of course. <a href="//docs.python.org/3/tutorial/controlflow.html">More control flow tools in Python 3</a></p></div>
</li>
<li>
<div class="slide-code"><pre><code><span class="comment"># Simple output (with Unicode)</span>
&gt;&gt;&gt; print("Hello, I'm Python!")
<span class="output">Hello, I'm Python!</span>
<span class="comment"># Input, assignment</span>
&gt;&gt;&gt; name = input('What is your name?\n')
<span class="output">What is your name?
Python</span>
&gt;&gt;&gt; print(f'Hi, {name}.')
<span class="output">Hi, Python.</span></code>
</pre></div>
<div class="slide-copy"><h1>Quick &amp; Easy to Learn</h1>
<p>Experienced programmers in any other language can pick up Python very quickly, and beginners find the clean syntax and indentation structure easy to learn. <a href="//docs.python.org/3/tutorial/">Whet your appetite</a> with our Python 3 overview.</p></div>
</li>
</ul>
</div>
</div>
<div class="introduction">
<p>Python is a programming language that lets you work quickly <span class="breaker"></span>and integrate systems more effectively. <a class="readmore" href="/doc/">Learn More</a></p>
</div>
</div><!-- end .container -->
</header>
<div class="content-wrapper" id="content">
<!-- Main Content Column -->
<div class="container">
<section class="main-content" role="main">
<div class="row">
<div class="small-widget get-started-widget">
<h2 class="widget-title"><span aria-hidden="true" class="icon-get-started"></span>Get Started</h2>
<p>Whether you're new to programming or an experienced developer, it's easy to learn and use Python.</p>
<p><a href="/about/gettingstarted/">Start with our Beginner’s Guide</a></p>
</div>
<div class="small-widget download-widget">
<h2 class="widget-title"><span aria-hidden="true" class="icon-download"></span>Download</h2>
<p>Python source code and installers are available for download for all versions!</p>
<p>Latest: <a href="/downloads/release/python-3135/">Python 3.13.5</a></p>
</div>
<div class="small-widget documentation-widget">
<h2 class="widget-title"><span aria-hidden="true" class="icon-documentation"></span>Docs</h2>
<p>Documentation for Python's standard library, along with tutorials and guides, are available online.</p>
<p><a href="https://docs.python.org">docs.python.org</a></p>
</div>
<div class="small-widget jobs-widget last">
<h2 class="widget-title"><span aria-hidden="true" class="icon-jobs"></span>Jobs</h2>
<p>Looking for work or have a Python related position that you're trying to hire for? Our <strong>relaunched community-run job board</strong> is the place to go.</p>
<p><a href="//jobs.python.org">jobs.python.org</a></p>
</div>
</div>
<div class="list-widgets row">
<div class="medium-widget blog-widget">
<div class="shrubbery">
<h2 class="widget-title"><span aria-hidden="true" class="icon-news"></span>Latest News</h2>
<p class="give-me-more"><a href="https://blog.python.org" title="More News">More</a></p>
<ul class="menu">
<li>
<time datetime="2025-07-24T13:55:00.000003+00:00"><span class="say-no-more">2025-</span>07-24</time>
<a href="https://pyfound.blogspot.com/2025/07/psf-board-nominations-opening-july-29th.html">PSF Board Election Nominations Opening July 29th</a></li>
<li>
<time datetime="2025-07-22T19:47:00.000001+00:00"><span class="say-no-more">2025-</span>07-22</time>
<a href="https://pythoninsider.blogspot.com/2025/07/python-314-release-candidate-1-is-go.html">Python 3.14 release candidate 1 is go!</a></li>
<li>
<time datetime="2025-07-16T12:43:00.000002+00:00"><span class="say-no-more">2025-</span>07-16</time>
<a href="https://pyfound.blogspot.com/2025/07/affirm-your-psf-membership-voting-status.html">Affirm Your PSF Membership Voting Status</a></li>
<li>
<time datetime="2025-07-09T01:00:00.000002+00:00"><span class="say-no-more">2025-</span>07-09</time>
<a href="https://mailchi.mp/python/python-software-foundation-july-2024-newsletter-19880429">PSF News: PyPI Orgs, Board Election, &amp; Yearly Reports</a></li>
<li>
<time datetime="2025-07-08T15:21:00.000001+00:00"><span class="say-no-more">2025-</span>07-08</time>
<a href="https://pyfound.blogspot.com/2025/07/notice-of-python-software-foundation.html">Notice of Python Software Foundation Bylaws Change - Effective July 23, 2025</a></li>
</ul>
</div><!-- end .shrubbery -->
</div>
<div class="medium-widget event-widget last">
<div class="shrubbery">
<h2 class="widget-title"><span aria-hidden="true" class="icon-calendar"></span>Upcoming Events</h2>
<p class="give-me-more"><a href="/events/calendars/" title="More Events">More</a></p>
<ul class="menu">
<li>
<time datetime="2025-08-08T00:00:00+00:00"><span class="say-no-more">2025-</span>08-08</time>
<a href="/events/python-user-group/2081/">Buea - Creating Python Communities and outreach</a></li>
<li>
<time datetime="2025-08-11T00:00:00+00:00"><span class="say-no-more">2025-</span>08-11</time>
<a href="/events/python-events/2011/">DjangoCon Africa 2025</a></li>
<li>
<time datetime="2025-08-13T00:00:00+00:00"><span class="say-no-more">2025-</span>08-13</time>
<a href="/events/python-events/2077/">PyCon Somalia 2025</a></li>
<li>
<time datetime="2025-08-15T00:00:00+00:00"><span class="say-no-more">2025-</span>08-15</time>
<a href="/events/python-events/1973/">PyCon Korea 2025</a></li>
<li>
<time datetime="2025-08-18T00:00:00+00:00"><span class="say-no-more">2025-</span>08-18</time>
<a href="/events/python-events/1971/">EuroSciPy 2025</a></li>
</ul>
</div>
</div>
</div>
<div class="row">
<div class="medium-widget success-stories-widget">
<div class="shrubbery">
<h2 class="widget-title"><span aria-hidden="true" class="icon-success-stories"></span>Success Stories</h2>
<p class="give-me-more"><a href="/success-stories/" title="More Success Stories">More</a></p>
<div class="success-story-item" id="success-story-932">
<blockquote>
<a href="/success-stories/abridging-clinical-conversations-using-python/">Python powers major aspects of Abridge’s ML lifecycle, including data annotation,  research and experimentation, and ML model deployment to production.</a>
</blockquote>
<table border="0" cellpadding="0" cellspacing="0" class="quote-from" width="100%">
<tbody>
<tr>
<td><p><a href="/success-stories/abridging-clinical-conversations-using-python/">Abridging clinical conversations using Python</a> <em>by Nimshi Venkat and Sandeep Konam</em></p></td>
</tr>
</tbody>
</table>
</div>
</div><!-- end .shrubbery -->
</div>
<div class="medium-widget applications-widget last">
<div class="shrubbery">
<h2 class="widget-title"><span aria-hidden="true" class="icon-python"></span>Use Python for…</h2>
<p class="give-me-more"><a href="/about/apps" title="More Applications">More</a></p>
<ul class="menu">
<li><b>Web Development</b>:
        <span class="tag-wrapper"><a class="tag" href="http://www.djangoproject.com/">Django</a>, <a class="tag" href="http://www.pylonsproject.org/">Pyramid</a>, <a class="tag" href="http://bottlepy.org">Bottle</a>, <a class="tag" href="http://tornadoweb.org">Tornado</a>, <a class="tag" href="http://flask.pocoo.org/">Flask</a>, <a class="tag" href="http://www.web2py.com/">web2py</a></span></li>
<li><b>GUI Development</b>:
        <span class="tag-wrapper"><a class="tag" href="http://wiki.python.org/moin/TkInter">tkInter</a>, <a class="tag" href="https://wiki.gnome.org/Projects/PyGObject">PyGObject</a>, <a class="tag" href="http://www.riverbankcomputing.co.uk/software/pyqt/intro">PyQt</a>, <a class="tag" href="https://wiki.qt.io/PySide">PySide</a>, <a class="tag" href="https://kivy.org/">Kivy</a>, <a class="tag" href="http://www.wxpython.org/">wxPython</a>, <a class="tag" href="https://dearpygui.readthedocs.io/en/latest/">DearPyGui</a></span></li>
<li><b>Scientific and Numeric</b>:
        <span class="tag-wrapper">
<a class="tag" href="http://www.scipy.org">SciPy</a>, <a class="tag" href="http://pandas.pydata.org/">Pandas</a>, <a class="tag" href="http://ipython.org">IPython</a></span></li>
<li><b>Software Development</b>:
        <span class="tag-wrapper"><a class="tag" href="http://buildbot.net/">Buildbot</a>, <a class="tag" href="http://trac.edgewall.org/">Trac</a>, <a class="tag" href="http://roundup.sourceforge.net/">Roundup</a></span></li>
<li><b>System Administration</b>:
        <span class="tag-wrapper"><a class="tag" href="http://www.ansible.com">Ansible</a>, <a class="tag" href="https://saltproject.io">Salt</a>, <a class="tag" href="https://www.openstack.org">OpenStack</a>, <a class="tag" href="https://xon.sh">xonsh</a></span></li>
</ul>
</div><!-- end .shrubbery -->
</div>
</div>
<div class="psf-widget">
<div class="python-logo"></div>
<h2 class="widget-title">
<span class="prompt">&gt;&gt;&gt;</span> <a href="/psf/">Python Software Foundation</a>
</h2>
<p>The mission of the Python Software Foundation is to promote, protect, and advance the Python programming language, and to support and facilitate the growth of a diverse and international community of Python programmers. <a class="readmore" href="/psf/">Learn more</a> </p>
<p class="click-these">
<a class="button" href="/psf/membership/">Become a Member</a>
<a class="button" href="/psf/donations/">Donate to the PSF</a>
</p>
</div>
</section>
</div><!-- end .container -->
</div><!-- end #content .content-wrapper -->
<!-- Footer and social media list -->
<footer class="main-footer" id="site-map" role="contentinfo">
<div class="main-footer-links">
<div class="container">
<a class="jump-link" href="#python-network" id="back-to-top-1"><span aria-hidden="true" class="icon-arrow-up"><span>▲</span></span> Back to Top</a>
<ul class="sitemap navigation menu do-not-print" id="container" role="tree">
<li class="tier-1 element-1">
<a href="/about/">About</a>
<ul class="subnav menu">
<li class="tier-2 element-1" role="treeitem"><a href="/about/apps/" title="">Applications</a></li>
<li class="tier-2 element-2" role="treeitem"><a href="/about/quotes/" title="">Quotes</a></li>
<li class="tier-2 element-3" role="treeitem"><a href="/about/gettingstarted/" title="">Getting Started</a></li>
<li class="tier-2 element-4" role="treeitem"><a href="/about/help/" title="">Help</a></li>
<li class="tier-2 element-5" role="treeitem"><a href="http://brochure.getpython.info/" title="">Python Brochure</a></li>
</ul>
</li>
<li class="tier-1 element-2">
<a href="/downloads/">Downloads</a>
<ul class="subnav menu">
<li class="tier-2 element-1" role="treeitem"><a href="/downloads/" title="">All releases</a></li>
<li class="tier-2 element-2" role="treeitem"><a href="/downloads/source/" title="">Source code</a></li>
<li class="tier-2 element-3" role="treeitem"><a href="/downloads/windows/" title="">Windows</a></li>
<li class="tier-2 element-4" role="treeitem"><a href="/downloads/macos/" title="">macOS</a></li>
<li class="tier-2 element-5" role="treeitem"><a href="/download/other/" title="">Other Platforms</a></li>
<li class="tier-2 element-6" role="treeitem"><a href="https://docs.python.org/3/license.html" title="">License</a></li>
<li class="tier-2 element-7" role="treeitem"><a href="/download/alternatives" title="">Alternative Implementations</a></li>
</ul>
</li>
<li class="tier-1 element-3">
<a href="/doc/">Documentation</a>
<ul class="subnav menu">
<li class="tier-2 element-1" role="treeitem"><a href="/doc/" title="">Docs</a></li>
<li class="tier-2 element-2" role="treeitem"><a href="/doc/av" title="">Audio/Visual Talks</a></li>
<li class="tier-2 element-3" role="treeitem"><a href="https://wiki.python.org/moin/BeginnersGuide" title="">Beginner's Guide</a></li>
<li class="tier-2 element-4" role="treeitem"><a href="https://devguide.python.org/" title="">Developer's Guide</a></li>
<li class="tier-2 element-5" role="treeitem"><a href="https://docs.python.org/faq/" title="">FAQ</a></li>
<li class="tier-2 element-6" role="treeitem"><a href="http://wiki.python.org/moin/Languages" title="">Non-English Docs</a></li>
<li class="tier-2 element-7" role="treeitem"><a href="https://peps.python.org" title="">PEP Index</a></li>
<li class="tier-2 element-8" role="treeitem"><a href="https://wiki.python.org/moin/PythonBooks" title="">Python Books</a></li>
<li class="tier-2 element-9" role="treeitem"><a href="/doc/essays/" title="">Python Essays</a></li>
</ul>
</li>
<li class="tier-1 element-4">
<a href="/community/">Community</a>
<ul class="subnav menu">
<li class="tier-2 element-1" role="treeitem"><a href="/community/diversity/" title="">Diversity</a></li>
<li class="tier-2 element-2" role="treeitem"><a href="/community/lists/" title="">Mailing Lists</a></li>
<li class="tier-2 element-3" role="treeitem"><a href="/community/irc/" title="">IRC</a></li>
<li class="tier-2 element-4" role="treeitem"><a href="/community/forums/" title="">Forums</a></li>
<li class="tier-2 element-5" role="treeitem"><a href="/psf/annual-report/2024/" title="">PSF Annual Impact Report</a></li>
<li class="tier-2 element-6" role="treeitem"><a href="/community/workshops/" title="">Python Conferences</a></li>
<li class="tier-2 element-7" role="treeitem"><a href="/community/sigs/" title="">Special Interest Groups</a></li>
<li class="tier-2 element-8" role="treeitem"><a href="/community/logos/" title="">Python Logo</a></li>
<li class="tier-2 element-9" role="treeitem"><a href="https://wiki.python.org/moin/" title="">Python Wiki</a></li>
<li class="tier-2 element-10" role="treeitem"><a href="/psf/conduct/" title="">Code of Conduct</a></li>
<li class="tier-2 element-11" role="treeitem"><a href="/community/awards" title="">Community Awards</a></li>
<li class="tier-2 element-12" role="treeitem"><a href="/psf/get-involved/" title="">Get Involved</a></li>
<li class="tier-2 element-13" role="treeitem"><a href="/psf/community-stories/" title="">Shared Stories</a></li>
</ul>
</li>
<li class="tier-1 element-5">
<a href="/success-stories/" title="success-stories">Success Stories</a>
<ul class="subnav menu">
<li class="tier-2 element-1" role="treeitem"><a href="/success-stories/category/arts/" title="">Arts</a></li>
<li class="tier-2 element-2" role="treeitem"><a href="/success-stories/category/business/" title="">Business</a></li>
<li class="tier-2 element-3" role="treeitem"><a href="/success-stories/category/education/" title="">Education</a></li>
<li class="tier-2 element-4" role="treeitem"><a href="/success-stories/category/engineering/" title="">Engineering</a></li>
<li class="tier-2 element-5" role="treeitem"><a href="/success-stories/category/government/" title="">Government</a></li>
<li class="tier-2 element-6" role="treeitem"><a href="/success-stories/category/scientific/" title="">Scientific</a></li>
<li class="tier-2 element-7" role="treeitem"><a href="/success-stories/category/software-development/" title="">Software Development</a></li>
</ul>
</li>
<li class="tier-1 element-6">
<a href="/blogs/" title="News from around the Python world">News</a>
<ul class="subnav menu">
<li class="tier-2 element-1" role="treeitem"><a href="/blogs/" title="Python Insider Blog Posts">Python News</a></li>
<li class="tier-2 element-2" role="treeitem"><a href="/psf/newsletter/" title="Python Software Foundation Newsletter">PSF Newsletter</a></li>
<li class="tier-2 element-3" role="treeitem"><a href="http://pyfound.blogspot.com/" title="PSF Blog">PSF News</a></li>
<li class="tier-2 element-4" role="treeitem"><a href="http://pycon.blogspot.com/" title="PyCon Blog">PyCon US News</a></li>
<li class="tier-2 element-5" role="treeitem"><a href="http://planetpython.org/" title="Planet Python">News from the Community</a></li>
</ul>
</li>
<li class="tier-1 element-7">
<a href="/events/">Events</a>
<ul class="subnav menu">
<li class="tier-2 element-1" role="treeitem"><a href="/events/python-events/" title="">Python Events</a></li>
<li class="tier-2 element-2" role="treeitem"><a href="/events/python-user-group/" title="">User Group Events</a></li>
<li class="tier-2 element-3" role="treeitem"><a href="/events/python-events/past/" title="">Python Events Archive</a></li>
<li class="tier-2 element-4" role="treeitem"><a href="/events/python-user-group/past/" title="">User Group Events Archive</a></li>
<li class="tier-2 element-5" role="treeitem"><a href="https://wiki.python.org/moin/PythonEventsCalendar#Submitting_an_Event" title="">Submit an Event</a></li>
</ul>
</li>
<li class="tier-1 element-8">
<a href="/dev/">Contributing</a>
<ul class="subnav menu">
<li class="tier-2 element-1" role="treeitem"><a href="https://devguide.python.org/" title="">Developer's Guide</a></li>
<li class="tier-2 element-2" role="treeitem"><a href="https://github.com/python/cpython/issues" title="">Issue Tracker</a></li>
<li class="tier-2 element-3" role="treeitem"><a href="https://mail.python.org/mailman/listinfo/python-dev" title="">python-dev list</a></li>
<li class="tier-2 element-4" role="treeitem"><a href="/dev/core-mentorship/" title="">Core Mentorship</a></li>
<li class="tier-2 element-5" role="treeitem"><a href="/dev/security/" title="">Report a Security Issue</a></li>
</ul>
</li>
</ul>
<a class="jump-link" href="#python-network" id="back-to-top-2"><span aria-hidden="true" class="icon-arrow-up"><span>▲</span></span> Back to Top</a>
</div><!-- end .container -->
</div> <!-- end .main-footer-links -->
<div class="site-base">
<div class="container">
<ul class="footer-links navigation menu do-not-print" role="tree">
<li class="tier-1 element-1"><a href="/about/help/">Help &amp; <span class="say-no-more">General</span> Contact</a></li>
<li class="tier-1 element-2"><a href="/community/diversity/">Diversity <span class="say-no-more">Initiatives</span></a></li>
<li class="tier-1 element-3"><a href="https://github.com/python/pythondotorg/issues">Submit Website Bug</a></li>
<li class="tier-1 element-4">
<a href="https://status.python.org/">Status <span class="python-status-indicator-default" id="python-status-indicator"></span></a>
</li>
</ul>
<div class="copyright">
<p><small>
<span class="pre">Copyright ©2001-2025.</span>
                             <span class="pre"><a href="/psf-landing/">Python Software Foundation</a></span>
                             <span class="pre"><a href="/about/legal/">Legal Statements</a></span>
                             <span class="pre"><a href="https://policies.python.org/python.org/Privacy-Notice/">Privacy Notice</a></span>
<!--&nbsp;<span class="pre"><a href="/psf/community-infrastructure">Powered by PSF Community Infrastructure</a></span>-->
</small></p>
</div>
</div><!-- end .container -->
</div><!-- end .site-base -->
</footer>
</div><!-- end #touchnav-wrapper -->
<script src="//ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js"></script>
<script>window.jQuery || document.write('<script src="/static/js/libs/jquery-1.8.2.min.js"><\/script>')</script>
<script src="//ajax.googleapis.com/ajax/libs/jqueryui/1.12.1/jquery-ui.min.js"></script>
<script>window.jQuery || document.write('<script src="/static/js/libs/jquery-ui-1.12.1.min.js"><\/script>')</script>
<script src="/static/js/libs/masonry.pkgd.min.js"></script>
<script src="/static/js/libs/html-includes.js"></script>
<script charset="utf-8" src="/static/js/main-min.ef82c06437cf.js" type="text/javascript"></script>
<!--[if lte IE 7]>
    <script type="text/javascript" src="/static/js/plugins/IE8-min.8af6e26c7a3b.js" charset="utf-8"></script>
    
    
    <![endif]-->
<!--[if lte IE 8]>
    <script type="text/javascript" src="/static/js/plugins/getComputedStyle-min.d41d8cd98f00.js" charset="utf-8"></script>
    
    
    <![endif]-->
</body>
########################################

1st title tag in entire website content
--------------------
title_tag: <title>Welcome to Python.org</title>
title_tag_content: Welcome to Python.org
type of title_tag_content: <class 'str'>
########################################

1st title tag inside head-tag
--------------------
title_tag: <title>Welcome to Python.org</title>
title_tag_content: Welcome to Python.org
type of title_tag_content: <class 'str'>
########################################

Content of title tag
--------------------
title_tag_content: Welcome to Python.org
type of title_tag_content: <class 'str'>
########################################

1st link tag in entire website content
--------------------
<link href="//ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js" rel="prefetch"/>
########################################

1st link tag inside head tag
--------------------
<link href="//ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js" rel="prefetch"/>
########################################

1st link tag and its attributes
--------------------
1st link tag: <link href="//ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js" rel="prefetch"/>
Attribute 'rel':  ['prefetch']
type of Attribute 'rel' value:  <class 'bs4.element.AttributeValueList'>
Attribute 'href':  //ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js
type of Attribute 'href' value:  <class 'str'>
########################################

All link tags present inside head-tag
--------------------
[<link href="//ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js" rel="prefetch"/>, <link href="//ajax.googleapis.com/ajax/libs/jqueryui/1.12.1/jquery-ui.min.js" rel="prefetch"/>, <link href="/static/stylesheets/style.08a078d0aa02.css" media="all" rel="stylesheet" title="default" type="text/css">
<link href="/static/stylesheets/mq.98d6092b2ada.css" media="not print, braille, embossed, speech, tty" rel="stylesheet" type="text/css">
<link href="/static/stylesheets/no-mq.bf0c425cdb73.css" media="screen" rel="stylesheet" type="text/css"/>
<!--[if (lte IE 8)&(!IEMobile)]>
    <link href="/static/stylesheets/no-mq.bf0c425cdb73.css" rel="stylesheet" type="text/css" media="screen" />
    
    
    <![endif]-->
<link href="//ajax.googleapis.com/ajax/libs/jqueryui/1.12.1/themes/smoothness/jquery-ui.css" rel="stylesheet"/>
<link href="/static/favicon.ico" rel="icon" type="image/x-icon"/>
<link href="/static/apple-touch-icon-144x144-precomposed.png" rel="apple-touch-icon-precomposed" sizes="144x144"/>
<link href="/static/apple-touch-icon-114x114-precomposed.png" rel="apple-touch-icon-precomposed" sizes="114x114"/>
<link href="/static/apple-touch-icon-72x72-precomposed.png" rel="apple-touch-icon-precomposed" sizes="72x72"/>
<link href="/static/apple-touch-icon-precomposed.png" rel="apple-touch-icon-precomposed"/>
<link href="/static/apple-touch-icon-precomposed.png" rel="apple-touch-icon"/>
<meta content="/static/metro-icon-144x144.png" name="msapplication-TileImage"/><!-- white shape -->
<meta content="#3673a5" name="msapplication-TileColor"/><!-- python blue -->
<meta content="#3673a5" name="msapplication-navbutton-color"/>
<title>Welcome to Python.org</title>
<meta content="The official home of the Python Programming Language" name="description"/>
<meta content="Python programming language object oriented web free open source software license documentation download community" name="keywords"/>
<meta content="website" property="og:type"/>
<meta content="Python.org" property="og:site_name"/>
<meta content="Welcome to Python.org" property="og:title"/>
<meta content="The official home of the Python Programming Language" property="og:description"/>
<meta content="https://www.python.org/static/opengraph-icon-200x200.png" property="og:image"/>
<meta content="https://www.python.org/static/opengraph-icon-200x200.png" property="og:image:secure_url"/>
<meta content="https://www.python.org/" property="og:url"/>
<link href="/humans.txt" rel="author"/>
<link href="https://peps.python.org/peps.rss" rel="alternate" title="Python Enhancement Proposals" type="application/rss+xml"/>
<link href="https://www.python.org/jobs/feed/rss/" rel="alternate" title="Python Job Opportunities" type="application/rss+xml"/>
<link href="https://feeds.feedburner.com/PythonSoftwareFoundationNews" rel="alternate" title="Python Software Foundation News" type="application/rss+xml"/>
<link href="https://feeds.feedburner.com/PythonInsider" rel="alternate" title="Python Insider" type="application/rss+xml"/>
<link href="https://www.python.org/downloads/feed.rss" rel="alternate" title="Python Releases" type="application/rss+xml"/>
<script type="application/ld+json">
     {
       "@context": "https://schema.org",
       "@type": "WebSite",
       "url": "https://www.python.org/",
       "potentialAction": {
         "@type": "SearchAction",
         "target": "https://www.python.org/search/?q={search_term_string}",
         "query-input": "required name=search_term_string"
       }
     }
    </script>
<script type="text/javascript">
    var _gaq = _gaq || [];
    _gaq.push(['_setAccount', 'UA-39055973-1']);
    _gaq.push(['_trackPageview']);

    (function() {
        var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
        ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
        var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
    })();
    </script>
</link></link>, <link href="/static/stylesheets/mq.98d6092b2ada.css" media="not print, braille, embossed, speech, tty" rel="stylesheet" type="text/css">
<link href="/static/stylesheets/no-mq.bf0c425cdb73.css" media="screen" rel="stylesheet" type="text/css"/>
<!--[if (lte IE 8)&(!IEMobile)]>
    <link href="/static/stylesheets/no-mq.bf0c425cdb73.css" rel="stylesheet" type="text/css" media="screen" />
    
    
    <![endif]-->
<link href="//ajax.googleapis.com/ajax/libs/jqueryui/1.12.1/themes/smoothness/jquery-ui.css" rel="stylesheet"/>
<link href="/static/favicon.ico" rel="icon" type="image/x-icon"/>
<link href="/static/apple-touch-icon-144x144-precomposed.png" rel="apple-touch-icon-precomposed" sizes="144x144"/>
<link href="/static/apple-touch-icon-114x114-precomposed.png" rel="apple-touch-icon-precomposed" sizes="114x114"/>
<link href="/static/apple-touch-icon-72x72-precomposed.png" rel="apple-touch-icon-precomposed" sizes="72x72"/>
<link href="/static/apple-touch-icon-precomposed.png" rel="apple-touch-icon-precomposed"/>
<link href="/static/apple-touch-icon-precomposed.png" rel="apple-touch-icon"/>
<meta content="/static/metro-icon-144x144.png" name="msapplication-TileImage"/><!-- white shape -->
<meta content="#3673a5" name="msapplication-TileColor"/><!-- python blue -->
<meta content="#3673a5" name="msapplication-navbutton-color"/>
<title>Welcome to Python.org</title>
<meta content="The official home of the Python Programming Language" name="description"/>
<meta content="Python programming language object oriented web free open source software license documentation download community" name="keywords"/>
<meta content="website" property="og:type"/>
<meta content="Python.org" property="og:site_name"/>
<meta content="Welcome to Python.org" property="og:title"/>
<meta content="The official home of the Python Programming Language" property="og:description"/>
<meta content="https://www.python.org/static/opengraph-icon-200x200.png" property="og:image"/>
<meta content="https://www.python.org/static/opengraph-icon-200x200.png" property="og:image:secure_url"/>
<meta content="https://www.python.org/" property="og:url"/>
<link href="/humans.txt" rel="author"/>
<link href="https://peps.python.org/peps.rss" rel="alternate" title="Python Enhancement Proposals" type="application/rss+xml"/>
<link href="https://www.python.org/jobs/feed/rss/" rel="alternate" title="Python Job Opportunities" type="application/rss+xml"/>
<link href="https://feeds.feedburner.com/PythonSoftwareFoundationNews" rel="alternate" title="Python Software Foundation News" type="application/rss+xml"/>
<link href="https://feeds.feedburner.com/PythonInsider" rel="alternate" title="Python Insider" type="application/rss+xml"/>
<link href="https://www.python.org/downloads/feed.rss" rel="alternate" title="Python Releases" type="application/rss+xml"/>
<script type="application/ld+json">
     {
       "@context": "https://schema.org",
       "@type": "WebSite",
       "url": "https://www.python.org/",
       "potentialAction": {
         "@type": "SearchAction",
         "target": "https://www.python.org/search/?q={search_term_string}",
         "query-input": "required name=search_term_string"
       }
     }
    </script>
<script type="text/javascript">
    var _gaq = _gaq || [];
    _gaq.push(['_setAccount', 'UA-39055973-1']);
    _gaq.push(['_trackPageview']);

    (function() {
        var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
        ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
        var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
    })();
    </script>
</link>, <link href="/static/stylesheets/no-mq.bf0c425cdb73.css" media="screen" rel="stylesheet" type="text/css"/>, <link href="//ajax.googleapis.com/ajax/libs/jqueryui/1.12.1/themes/smoothness/jquery-ui.css" rel="stylesheet"/>, <link href="/static/favicon.ico" rel="icon" type="image/x-icon"/>, <link href="/static/apple-touch-icon-144x144-precomposed.png" rel="apple-touch-icon-precomposed" sizes="144x144"/>, <link href="/static/apple-touch-icon-114x114-precomposed.png" rel="apple-touch-icon-precomposed" sizes="114x114"/>, <link href="/static/apple-touch-icon-72x72-precomposed.png" rel="apple-touch-icon-precomposed" sizes="72x72"/>, <link href="/static/apple-touch-icon-precomposed.png" rel="apple-touch-icon-precomposed"/>, <link href="/static/apple-touch-icon-precomposed.png" rel="apple-touch-icon"/>, <link href="/humans.txt" rel="author"/>, <link href="https://peps.python.org/peps.rss" rel="alternate" title="Python Enhancement Proposals" type="application/rss+xml"/>, <link href="https://www.python.org/jobs/feed/rss/" rel="alternate" title="Python Job Opportunities" type="application/rss+xml"/>, <link href="https://feeds.feedburner.com/PythonSoftwareFoundationNews" rel="alternate" title="Python Software Foundation News" type="application/rss+xml"/>, <link href="https://feeds.feedburner.com/PythonInsider" rel="alternate" title="Python Insider" type="application/rss+xml"/>, <link href="https://www.python.org/downloads/feed.rss" rel="alternate" title="Python Releases" type="application/rss+xml"/>]
########################################

All href tags present inside each link-tag
--------------------
Tag: <link href="//ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js" rel="prefetch"/>
URL: //ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js
Tag: <link href="//ajax.googleapis.com/ajax/libs/jqueryui/1.12.1/jquery-ui.min.js" rel="prefetch"/>
URL: //ajax.googleapis.com/ajax/libs/jqueryui/1.12.1/jquery-ui.min.js
Tag: <link href="/static/stylesheets/style.08a078d0aa02.css" media="all" rel="stylesheet" title="default" type="text/css">
<link href="/static/stylesheets/mq.98d6092b2ada.css" media="not print, braille, embossed, speech, tty" rel="stylesheet" type="text/css">
<link href="/static/stylesheets/no-mq.bf0c425cdb73.css" media="screen" rel="stylesheet" type="text/css"/>
<!--[if (lte IE 8)&(!IEMobile)]>
    <link href="/static/stylesheets/no-mq.bf0c425cdb73.css" rel="stylesheet" type="text/css" media="screen" />
    
    
    <![endif]-->
<link href="//ajax.googleapis.com/ajax/libs/jqueryui/1.12.1/themes/smoothness/jquery-ui.css" rel="stylesheet"/>
<link href="/static/favicon.ico" rel="icon" type="image/x-icon"/>
<link href="/static/apple-touch-icon-144x144-precomposed.png" rel="apple-touch-icon-precomposed" sizes="144x144"/>
<link href="/static/apple-touch-icon-114x114-precomposed.png" rel="apple-touch-icon-precomposed" sizes="114x114"/>
<link href="/static/apple-touch-icon-72x72-precomposed.png" rel="apple-touch-icon-precomposed" sizes="72x72"/>
<link href="/static/apple-touch-icon-precomposed.png" rel="apple-touch-icon-precomposed"/>
<link href="/static/apple-touch-icon-precomposed.png" rel="apple-touch-icon"/>
<meta content="/static/metro-icon-144x144.png" name="msapplication-TileImage"/><!-- white shape -->
<meta content="#3673a5" name="msapplication-TileColor"/><!-- python blue -->
<meta content="#3673a5" name="msapplication-navbutton-color"/>
<title>Welcome to Python.org</title>
<meta content="The official home of the Python Programming Language" name="description"/>
<meta content="Python programming language object oriented web free open source software license documentation download community" name="keywords"/>
<meta content="website" property="og:type"/>
<meta content="Python.org" property="og:site_name"/>
<meta content="Welcome to Python.org" property="og:title"/>
<meta content="The official home of the Python Programming Language" property="og:description"/>
<meta content="https://www.python.org/static/opengraph-icon-200x200.png" property="og:image"/>
<meta content="https://www.python.org/static/opengraph-icon-200x200.png" property="og:image:secure_url"/>
<meta content="https://www.python.org/" property="og:url"/>
<link href="/humans.txt" rel="author"/>
<link href="https://peps.python.org/peps.rss" rel="alternate" title="Python Enhancement Proposals" type="application/rss+xml"/>
<link href="https://www.python.org/jobs/feed/rss/" rel="alternate" title="Python Job Opportunities" type="application/rss+xml"/>
<link href="https://feeds.feedburner.com/PythonSoftwareFoundationNews" rel="alternate" title="Python Software Foundation News" type="application/rss+xml"/>
<link href="https://feeds.feedburner.com/PythonInsider" rel="alternate" title="Python Insider" type="application/rss+xml"/>
<link href="https://www.python.org/downloads/feed.rss" rel="alternate" title="Python Releases" type="application/rss+xml"/>
<script type="application/ld+json">
     {
       "@context": "https://schema.org",
       "@type": "WebSite",
       "url": "https://www.python.org/",
       "potentialAction": {
         "@type": "SearchAction",
         "target": "https://www.python.org/search/?q={search_term_string}",
         "query-input": "required name=search_term_string"
       }
     }
    </script>
<script type="text/javascript">
    var _gaq = _gaq || [];
    _gaq.push(['_setAccount', 'UA-39055973-1']);
    _gaq.push(['_trackPageview']);

    (function() {
        var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
        ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
        var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
    })();
    </script>
</link></link>
URL: /static/stylesheets/style.08a078d0aa02.css
Tag: <link href="/static/stylesheets/mq.98d6092b2ada.css" media="not print, braille, embossed, speech, tty" rel="stylesheet" type="text/css">
<link href="/static/stylesheets/no-mq.bf0c425cdb73.css" media="screen" rel="stylesheet" type="text/css"/>
<!--[if (lte IE 8)&(!IEMobile)]>
    <link href="/static/stylesheets/no-mq.bf0c425cdb73.css" rel="stylesheet" type="text/css" media="screen" />
    
    
    <![endif]-->
<link href="//ajax.googleapis.com/ajax/libs/jqueryui/1.12.1/themes/smoothness/jquery-ui.css" rel="stylesheet"/>
<link href="/static/favicon.ico" rel="icon" type="image/x-icon"/>
<link href="/static/apple-touch-icon-144x144-precomposed.png" rel="apple-touch-icon-precomposed" sizes="144x144"/>
<link href="/static/apple-touch-icon-114x114-precomposed.png" rel="apple-touch-icon-precomposed" sizes="114x114"/>
<link href="/static/apple-touch-icon-72x72-precomposed.png" rel="apple-touch-icon-precomposed" sizes="72x72"/>
<link href="/static/apple-touch-icon-precomposed.png" rel="apple-touch-icon-precomposed"/>
<link href="/static/apple-touch-icon-precomposed.png" rel="apple-touch-icon"/>
<meta content="/static/metro-icon-144x144.png" name="msapplication-TileImage"/><!-- white shape -->
<meta content="#3673a5" name="msapplication-TileColor"/><!-- python blue -->
<meta content="#3673a5" name="msapplication-navbutton-color"/>
<title>Welcome to Python.org</title>
<meta content="The official home of the Python Programming Language" name="description"/>
<meta content="Python programming language object oriented web free open source software license documentation download community" name="keywords"/>
<meta content="website" property="og:type"/>
<meta content="Python.org" property="og:site_name"/>
<meta content="Welcome to Python.org" property="og:title"/>
<meta content="The official home of the Python Programming Language" property="og:description"/>
<meta content="https://www.python.org/static/opengraph-icon-200x200.png" property="og:image"/>
<meta content="https://www.python.org/static/opengraph-icon-200x200.png" property="og:image:secure_url"/>
<meta content="https://www.python.org/" property="og:url"/>
<link href="/humans.txt" rel="author"/>
<link href="https://peps.python.org/peps.rss" rel="alternate" title="Python Enhancement Proposals" type="application/rss+xml"/>
<link href="https://www.python.org/jobs/feed/rss/" rel="alternate" title="Python Job Opportunities" type="application/rss+xml"/>
<link href="https://feeds.feedburner.com/PythonSoftwareFoundationNews" rel="alternate" title="Python Software Foundation News" type="application/rss+xml"/>
<link href="https://feeds.feedburner.com/PythonInsider" rel="alternate" title="Python Insider" type="application/rss+xml"/>
<link href="https://www.python.org/downloads/feed.rss" rel="alternate" title="Python Releases" type="application/rss+xml"/>
<script type="application/ld+json">
     {
       "@context": "https://schema.org",
       "@type": "WebSite",
       "url": "https://www.python.org/",
       "potentialAction": {
         "@type": "SearchAction",
         "target": "https://www.python.org/search/?q={search_term_string}",
         "query-input": "required name=search_term_string"
       }
     }
    </script>
<script type="text/javascript">
    var _gaq = _gaq || [];
    _gaq.push(['_setAccount', 'UA-39055973-1']);
    _gaq.push(['_trackPageview']);

    (function() {
        var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
        ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
        var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
    })();
    </script>
</link>
URL: /static/stylesheets/mq.98d6092b2ada.css
Tag: <link href="/static/stylesheets/no-mq.bf0c425cdb73.css" media="screen" rel="stylesheet" type="text/css"/>
URL: /static/stylesheets/no-mq.bf0c425cdb73.css
Tag: <link href="//ajax.googleapis.com/ajax/libs/jqueryui/1.12.1/themes/smoothness/jquery-ui.css" rel="stylesheet"/>
URL: //ajax.googleapis.com/ajax/libs/jqueryui/1.12.1/themes/smoothness/jquery-ui.css
Tag: <link href="/static/favicon.ico" rel="icon" type="image/x-icon"/>
URL: /static/favicon.ico
Tag: <link href="/static/apple-touch-icon-144x144-precomposed.png" rel="apple-touch-icon-precomposed" sizes="144x144"/>
URL: /static/apple-touch-icon-144x144-precomposed.png
Tag: <link href="/static/apple-touch-icon-114x114-precomposed.png" rel="apple-touch-icon-precomposed" sizes="114x114"/>
URL: /static/apple-touch-icon-114x114-precomposed.png
Tag: <link href="/static/apple-touch-icon-72x72-precomposed.png" rel="apple-touch-icon-precomposed" sizes="72x72"/>
URL: /static/apple-touch-icon-72x72-precomposed.png
Tag: <link href="/static/apple-touch-icon-precomposed.png" rel="apple-touch-icon-precomposed"/>
URL: /static/apple-touch-icon-precomposed.png
Tag: <link href="/static/apple-touch-icon-precomposed.png" rel="apple-touch-icon"/>
URL: /static/apple-touch-icon-precomposed.png
Tag: <link href="/humans.txt" rel="author"/>
URL: /humans.txt
Tag: <link href="https://peps.python.org/peps.rss" rel="alternate" title="Python Enhancement Proposals" type="application/rss+xml"/>
URL: https://peps.python.org/peps.rss
Tag: <link href="https://www.python.org/jobs/feed/rss/" rel="alternate" title="Python Job Opportunities" type="application/rss+xml"/>
URL: https://www.python.org/jobs/feed/rss/
Tag: <link href="https://feeds.feedburner.com/PythonSoftwareFoundationNews" rel="alternate" title="Python Software Foundation News" type="application/rss+xml"/>
URL: https://feeds.feedburner.com/PythonSoftwareFoundationNews
Tag: <link href="https://feeds.feedburner.com/PythonInsider" rel="alternate" title="Python Insider" type="application/rss+xml"/>
URL: https://feeds.feedburner.com/PythonInsider
Tag: <link href="https://www.python.org/downloads/feed.rss" rel="alternate" title="Python Releases" type="application/rss+xml"/>
URL: https://www.python.org/downloads/feed.rss
########################################

All paragraph tags
--------------------
[<p><strong>Notice:</strong> While JavaScript is not essential for this website, your interaction with the content will be limited. Please turn JavaScript on for the full experience. </p>, <p>The core of extensible programming is defining functions. Python allows mandatory and optional arguments, keyword arguments, and even arbitrary argument lists. <a href="//docs.python.org/3/tutorial/controlflow.html#defining-functions">More about defining functions in Python 3</a></p>, <p>Lists (known as arrays in other languages) are one of the compound data types that Python understands. Lists can be indexed, sliced and manipulated with other built-in functions. <a href="//docs.python.org/3/tutorial/introduction.html#lists">More about lists in Python 3</a></p>, <p>Calculations are simple with Python, and expression syntax is straightforward: the operators <code>+</code>, <code>-</code>, <code>*</code> and <code>/</code> work as expected; parentheses <code>()</code> can be used for grouping. <a href="http://docs.python.org/3/tutorial/introduction.html#using-python-as-a-calculator">More about simple math functions in Python 3</a>.</p>, <p>Python knows the usual control flow statements that other languages speak — <code>if</code>, <code>for</code>, <code>while</code> and <code>range</code> — with some of its own twists, of course. <a href="//docs.python.org/3/tutorial/controlflow.html">More control flow tools in Python 3</a></p>, <p>Experienced programmers in any other language can pick up Python very quickly, and beginners find the clean syntax and indentation structure easy to learn. <a href="//docs.python.org/3/tutorial/">Whet your appetite</a> with our Python 3 overview.</p>, <p>Python is a programming language that lets you work quickly <span class="breaker"></span>and integrate systems more effectively. <a class="readmore" href="/doc/">Learn More</a></p>, <p>Whether you're new to programming or an experienced developer, it's easy to learn and use Python.</p>, <p><a href="/about/gettingstarted/">Start with our Beginner’s Guide</a></p>, <p>Python source code and installers are available for download for all versions!</p>, <p>Latest: <a href="/downloads/release/python-3135/">Python 3.13.5</a></p>, <p>Documentation for Python's standard library, along with tutorials and guides, are available online.</p>, <p><a href="https://docs.python.org">docs.python.org</a></p>, <p>Looking for work or have a Python related position that you're trying to hire for? Our <strong>relaunched community-run job board</strong> is the place to go.</p>, <p><a href="//jobs.python.org">jobs.python.org</a></p>, <p class="give-me-more"><a href="https://blog.python.org" title="More News">More</a></p>, <p class="give-me-more"><a href="/events/calendars/" title="More Events">More</a></p>, <p class="give-me-more"><a href="/success-stories/" title="More Success Stories">More</a></p>, <p><a href="/success-stories/abridging-clinical-conversations-using-python/">Abridging clinical conversations using Python</a> <em>by Nimshi Venkat and Sandeep Konam</em></p>, <p class="give-me-more"><a href="/about/apps" title="More Applications">More</a></p>, <p>The mission of the Python Software Foundation is to promote, protect, and advance the Python programming language, and to support and facilitate the growth of a diverse and international community of Python programmers. <a class="readmore" href="/psf/">Learn more</a> </p>, <p class="click-these">
<a class="button" href="/psf/membership/">Become a Member</a>
<a class="button" href="/psf/donations/">Donate to the PSF</a>
</p>, <p><small>
<span class="pre">Copyright ©2001-2025.</span>
                             <span class="pre"><a href="/psf-landing/">Python Software Foundation</a></span>
                             <span class="pre"><a href="/about/legal/">Legal Statements</a></span>
                             <span class="pre"><a href="https://policies.python.org/python.org/Privacy-Notice/">Privacy Notice</a></span>
<!--&nbsp;<span class="pre"><a href="/psf/community-infrastructure">Powered by PSF Community Infrastructure</a></span>-->
</small></p>]
########################################

all paragraphs content
--------------------
['Notice: While JavaScript is not essential for this website, your interaction with the content will be limited. Please turn JavaScript on for the full experience. ', 'The core of extensible programming is defining functions. Python allows mandatory and optional arguments, keyword arguments, and even arbitrary argument lists. More about defining functions in Python\xa03', 'Lists (known as arrays in other languages) are one of the compound data types that Python understands. Lists can be indexed, sliced and manipulated with other built-in functions. More about lists in Python\xa03', 'Calculations are simple with Python, and expression syntax is straightforward: the operators +, -, * and / work as expected; parentheses () can be used for grouping. More about simple math functions in Python\xa03.', 'Python knows the usual control flow statements that other languages speak — if, for, while and range — with some of its own twists, of course. More control flow tools in Python\xa03', 'Experienced programmers in any other language can pick up Python very quickly, and beginners find the clean syntax and indentation structure easy to learn. Whet your appetite with our Python\xa03 overview.', 'Python is a programming language that lets you work quickly and integrate systems more effectively. Learn More', "Whether you're new to programming or an experienced developer, it's easy to learn and use Python.", 'Start with our Beginner’s Guide', 'Python source code and installers are available for download for all versions!', 'Latest: Python 3.13.5', "Documentation for Python's standard library, along with tutorials and guides, are available online.", 'docs.python.org', "Looking for work or have a Python related position that you're trying to hire for? Our relaunched community-run job board is the place to go.", 'jobs.python.org', 'More', 'More', 'More', 'Abridging clinical conversations using Python by Nimshi Venkat and Sandeep Konam', 'More', 'The mission of the Python Software Foundation is to promote, protect, and advance the Python programming language, and to support and facilitate the growth of a diverse and international community of Python programmers. Learn more ', '\nBecome a Member\nDonate to the PSF\n', '\nCopyright ©2001-2025.\n                            \xa0Python Software Foundation\n                            \xa0Legal Statements\n                            \xa0Privacy Notice\n\n']
########################################

All anchor(<a>) tag
--------------------
[<a href="#content" title="Skip to content">Skip to content</a>, <a aria-hidden="true" class="jump-link" href="#python-network" id="close-python-network">
<span aria-hidden="true" class="icon-arrow-down"><span>▼</span></span> Close
                </a>, <a class="current_item selectedcurrent_branch selected" href="/" title="The Python Programming Language">Python</a>, <a href="https://www.python.org/psf/" title="The Python Software Foundation">PSF</a>, <a href="https://docs.python.org" title="Python Documentation">Docs</a>, <a href="https://pypi.org/" title="Python Package Index">PyPI</a>, <a href="/jobs/" title="Python Job Board">Jobs</a>, <a href="/community/">Community</a>, <a aria-hidden="true" class="jump-link" href="#top" id="python-network">
<span aria-hidden="true" class="icon-arrow-up"><span>▲</span></span> The Python Network
                </a>, <a href="/"><img alt="python™" class="python-logo" src="/static/img/python-logo.png"/></a>, <a class="donate-button" href="https://psfmember.org/civicrm/contribute/transact?reset=1&amp;id=2">Donate</a>, <a class="jump-to-menu" href="#site-map" id="site-map-link"><span class="menu-icon">≡</span> Menu</a>, <a class="action-trigger" href="#"><strong><small>A</small> A</strong></a>, <a class="text-shrink" href="javascript:;" title="Make Text Smaller">Smaller</a>, <a class="text-grow" href="javascript:;" title="Make Text Larger">Larger</a>, <a class="text-reset" href="javascript:;" title="Reset any font size changes I have made">Reset</a>, <a class="action-trigger" href="#">Socialize</a>, <a href="https://www.linkedin.com/company/python-software-foundation/"><i aria-hidden="true" class="fa fa-linkedin-square"></i>LinkedIn</a>, <a href="https://fosstodon.org/@ThePSF"><span aria-hidden="true" class="icon-mastodon"></span>Mastodon</a>, <a href="/community/irc/"><span aria-hidden="true" class="icon-freenode"></span>Chat on IRC</a>, <a href="https://twitter.com/ThePSF"><span aria-hidden="true" class="icon-twitter"></span>Twitter</a>, <a class="" href="/about/" title="">About</a>, <a href="/about/apps/" title="">Applications</a>, <a href="/about/quotes/" title="">Quotes</a>, <a href="/about/gettingstarted/" title="">Getting Started</a>, <a href="/about/help/" title="">Help</a>, <a href="http://brochure.getpython.info/" title="">Python Brochure</a>, <a class="" href="/downloads/" title="">Downloads</a>, <a href="/downloads/" title="">All releases</a>, <a href="/downloads/source/" title="">Source code</a>, <a href="/downloads/windows/" title="">Windows</a>, <a href="/downloads/macos/" title="">macOS</a>, <a href="/download/other/" title="">Other Platforms</a>, <a href="https://docs.python.org/3/license.html" title="">License</a>, <a href="/download/alternatives" title="">Alternative Implementations</a>, <a class="" href="/doc/" title="">Documentation</a>, <a href="/doc/" title="">Docs</a>, <a href="/doc/av" title="">Audio/Visual Talks</a>, <a href="https://wiki.python.org/moin/BeginnersGuide" title="">Beginner's Guide</a>, <a href="https://devguide.python.org/" title="">Developer's Guide</a>, <a href="https://docs.python.org/faq/" title="">FAQ</a>, <a href="http://wiki.python.org/moin/Languages" title="">Non-English Docs</a>, <a href="https://peps.python.org" title="">PEP Index</a>, <a href="https://wiki.python.org/moin/PythonBooks" title="">Python Books</a>, <a href="/doc/essays/" title="">Python Essays</a>, <a class="" href="/community/" title="">Community</a>, <a href="/community/diversity/" title="">Diversity</a>, <a href="/community/lists/" title="">Mailing Lists</a>, <a href="/community/irc/" title="">IRC</a>, <a href="/community/forums/" title="">Forums</a>, <a href="/psf/annual-report/2024/" title="">PSF Annual Impact Report</a>, <a href="/community/workshops/" title="">Python Conferences</a>, <a href="/community/sigs/" title="">Special Interest Groups</a>, <a href="/community/logos/" title="">Python Logo</a>, <a href="https://wiki.python.org/moin/" title="">Python Wiki</a>, <a href="/psf/conduct/" title="">Code of Conduct</a>, <a href="/community/awards" title="">Community Awards</a>, <a href="/psf/get-involved/" title="">Get Involved</a>, <a href="/psf/community-stories/" title="">Shared Stories</a>, <a class="" href="/success-stories/" title="success-stories">Success Stories</a>, <a href="/success-stories/category/arts/" title="">Arts</a>, <a href="/success-stories/category/business/" title="">Business</a>, <a href="/success-stories/category/education/" title="">Education</a>, <a href="/success-stories/category/engineering/" title="">Engineering</a>, <a href="/success-stories/category/government/" title="">Government</a>, <a href="/success-stories/category/scientific/" title="">Scientific</a>, <a href="/success-stories/category/software-development/" title="">Software Development</a>, <a class="" href="/blogs/" title="News from around the Python world">News</a>, <a href="/blogs/" title="Python Insider Blog Posts">Python News</a>, <a href="/psf/newsletter/" title="Python Software Foundation Newsletter">PSF Newsletter</a>, <a href="http://pyfound.blogspot.com/" title="PSF Blog">PSF News</a>, <a href="http://pycon.blogspot.com/" title="PyCon Blog">PyCon US News</a>, <a href="http://planetpython.org/" title="Planet Python">News from the Community</a>, <a class="" href="/events/" title="">Events</a>, <a href="/events/python-events/" title="">Python Events</a>, <a href="/events/python-user-group/" title="">User Group Events</a>, <a href="/events/python-events/past/" title="">Python Events Archive</a>, <a href="/events/python-user-group/past/" title="">User Group Events Archive</a>, <a href="https://wiki.python.org/moin/PythonEventsCalendar#Submitting_an_Event" title="">Submit an Event</a>, <a class="button prompt" data-shell-container="#dive-into-python" href="/shell/" id="start-shell">&gt;_
                        <span class="message">Launch Interactive Shell</span>
</a>, <a href="//docs.python.org/3/tutorial/controlflow.html#defining-functions">More about defining functions in Python 3</a>, <a href="//docs.python.org/3/tutorial/introduction.html#lists">More about lists in Python 3</a>, <a href="http://docs.python.org/3/tutorial/introduction.html#using-python-as-a-calculator">More about simple math functions in Python 3</a>, <a href="//docs.python.org/3/tutorial/controlflow.html">More control flow tools in Python 3</a>, <a href="//docs.python.org/3/tutorial/">Whet your appetite</a>, <a class="readmore" href="/doc/">Learn More</a>, <a href="/about/gettingstarted/">Start with our Beginner’s Guide</a>, <a href="/downloads/release/python-3135/">Python 3.13.5</a>, <a href="https://docs.python.org">docs.python.org</a>, <a href="//jobs.python.org">jobs.python.org</a>, <a href="https://blog.python.org" title="More News">More</a>, <a href="https://pyfound.blogspot.com/2025/07/psf-board-nominations-opening-july-29th.html">PSF Board Election Nominations Opening July 29th</a>, <a href="https://pythoninsider.blogspot.com/2025/07/python-314-release-candidate-1-is-go.html">Python 3.14 release candidate 1 is go!</a>, <a href="https://pyfound.blogspot.com/2025/07/affirm-your-psf-membership-voting-status.html">Affirm Your PSF Membership Voting Status</a>, <a href="https://mailchi.mp/python/python-software-foundation-july-2024-newsletter-19880429">PSF News: PyPI Orgs, Board Election, &amp; Yearly Reports</a>, <a href="https://pyfound.blogspot.com/2025/07/notice-of-python-software-foundation.html">Notice of Python Software Foundation Bylaws Change - Effective July 23, 2025</a>, <a href="/events/calendars/" title="More Events">More</a>, <a href="/events/python-user-group/2081/">Buea - Creating Python Communities and outreach</a>, <a href="/events/python-events/2011/">DjangoCon Africa 2025</a>, <a href="/events/python-events/2077/">PyCon Somalia 2025</a>, <a href="/events/python-events/1973/">PyCon Korea 2025</a>, <a href="/events/python-events/1971/">EuroSciPy 2025</a>, <a href="/success-stories/" title="More Success Stories">More</a>, <a href="/success-stories/abridging-clinical-conversations-using-python/">Python powers major aspects of Abridge’s ML lifecycle, including data annotation,  research and experimentation, and ML model deployment to production.</a>, <a href="/success-stories/abridging-clinical-conversations-using-python/">Abridging clinical conversations using Python</a>, <a href="/about/apps" title="More Applications">More</a>, <a class="tag" href="http://www.djangoproject.com/">Django</a>, <a class="tag" href="http://www.pylonsproject.org/">Pyramid</a>, <a class="tag" href="http://bottlepy.org">Bottle</a>, <a class="tag" href="http://tornadoweb.org">Tornado</a>, <a class="tag" href="http://flask.pocoo.org/">Flask</a>, <a class="tag" href="http://www.web2py.com/">web2py</a>, <a class="tag" href="http://wiki.python.org/moin/TkInter">tkInter</a>, <a class="tag" href="https://wiki.gnome.org/Projects/PyGObject">PyGObject</a>, <a class="tag" href="http://www.riverbankcomputing.co.uk/software/pyqt/intro">PyQt</a>, <a class="tag" href="https://wiki.qt.io/PySide">PySide</a>, <a class="tag" href="https://kivy.org/">Kivy</a>, <a class="tag" href="http://www.wxpython.org/">wxPython</a>, <a class="tag" href="https://dearpygui.readthedocs.io/en/latest/">DearPyGui</a>, <a class="tag" href="http://www.scipy.org">SciPy</a>, <a class="tag" href="http://pandas.pydata.org/">Pandas</a>, <a class="tag" href="http://ipython.org">IPython</a>, <a class="tag" href="http://buildbot.net/">Buildbot</a>, <a class="tag" href="http://trac.edgewall.org/">Trac</a>, <a class="tag" href="http://roundup.sourceforge.net/">Roundup</a>, <a class="tag" href="http://www.ansible.com">Ansible</a>, <a class="tag" href="https://saltproject.io">Salt</a>, <a class="tag" href="https://www.openstack.org">OpenStack</a>, <a class="tag" href="https://xon.sh">xonsh</a>, <a href="/psf/">Python Software Foundation</a>, <a class="readmore" href="/psf/">Learn more</a>, <a class="button" href="/psf/membership/">Become a Member</a>, <a class="button" href="/psf/donations/">Donate to the PSF</a>, <a class="jump-link" href="#python-network" id="back-to-top-1"><span aria-hidden="true" class="icon-arrow-up"><span>▲</span></span> Back to Top</a>, <a href="/about/">About</a>, <a href="/about/apps/" title="">Applications</a>, <a href="/about/quotes/" title="">Quotes</a>, <a href="/about/gettingstarted/" title="">Getting Started</a>, <a href="/about/help/" title="">Help</a>, <a href="http://brochure.getpython.info/" title="">Python Brochure</a>, <a href="/downloads/">Downloads</a>, <a href="/downloads/" title="">All releases</a>, <a href="/downloads/source/" title="">Source code</a>, <a href="/downloads/windows/" title="">Windows</a>, <a href="/downloads/macos/" title="">macOS</a>, <a href="/download/other/" title="">Other Platforms</a>, <a href="https://docs.python.org/3/license.html" title="">License</a>, <a href="/download/alternatives" title="">Alternative Implementations</a>, <a href="/doc/">Documentation</a>, <a href="/doc/" title="">Docs</a>, <a href="/doc/av" title="">Audio/Visual Talks</a>, <a href="https://wiki.python.org/moin/BeginnersGuide" title="">Beginner's Guide</a>, <a href="https://devguide.python.org/" title="">Developer's Guide</a>, <a href="https://docs.python.org/faq/" title="">FAQ</a>, <a href="http://wiki.python.org/moin/Languages" title="">Non-English Docs</a>, <a href="https://peps.python.org" title="">PEP Index</a>, <a href="https://wiki.python.org/moin/PythonBooks" title="">Python Books</a>, <a href="/doc/essays/" title="">Python Essays</a>, <a href="/community/">Community</a>, <a href="/community/diversity/" title="">Diversity</a>, <a href="/community/lists/" title="">Mailing Lists</a>, <a href="/community/irc/" title="">IRC</a>, <a href="/community/forums/" title="">Forums</a>, <a href="/psf/annual-report/2024/" title="">PSF Annual Impact Report</a>, <a href="/community/workshops/" title="">Python Conferences</a>, <a href="/community/sigs/" title="">Special Interest Groups</a>, <a href="/community/logos/" title="">Python Logo</a>, <a href="https://wiki.python.org/moin/" title="">Python Wiki</a>, <a href="/psf/conduct/" title="">Code of Conduct</a>, <a href="/community/awards" title="">Community Awards</a>, <a href="/psf/get-involved/" title="">Get Involved</a>, <a href="/psf/community-stories/" title="">Shared Stories</a>, <a href="/success-stories/" title="success-stories">Success Stories</a>, <a href="/success-stories/category/arts/" title="">Arts</a>, <a href="/success-stories/category/business/" title="">Business</a>, <a href="/success-stories/category/education/" title="">Education</a>, <a href="/success-stories/category/engineering/" title="">Engineering</a>, <a href="/success-stories/category/government/" title="">Government</a>, <a href="/success-stories/category/scientific/" title="">Scientific</a>, <a href="/success-stories/category/software-development/" title="">Software Development</a>, <a href="/blogs/" title="News from around the Python world">News</a>, <a href="/blogs/" title="Python Insider Blog Posts">Python News</a>, <a href="/psf/newsletter/" title="Python Software Foundation Newsletter">PSF Newsletter</a>, <a href="http://pyfound.blogspot.com/" title="PSF Blog">PSF News</a>, <a href="http://pycon.blogspot.com/" title="PyCon Blog">PyCon US News</a>, <a href="http://planetpython.org/" title="Planet Python">News from the Community</a>, <a href="/events/">Events</a>, <a href="/events/python-events/" title="">Python Events</a>, <a href="/events/python-user-group/" title="">User Group Events</a>, <a href="/events/python-events/past/" title="">Python Events Archive</a>, <a href="/events/python-user-group/past/" title="">User Group Events Archive</a>, <a href="https://wiki.python.org/moin/PythonEventsCalendar#Submitting_an_Event" title="">Submit an Event</a>, <a href="/dev/">Contributing</a>, <a href="https://devguide.python.org/" title="">Developer's Guide</a>, <a href="https://github.com/python/cpython/issues" title="">Issue Tracker</a>, <a href="https://mail.python.org/mailman/listinfo/python-dev" title="">python-dev list</a>, <a href="/dev/core-mentorship/" title="">Core Mentorship</a>, <a href="/dev/security/" title="">Report a Security Issue</a>, <a class="jump-link" href="#python-network" id="back-to-top-2"><span aria-hidden="true" class="icon-arrow-up"><span>▲</span></span> Back to Top</a>, <a href="/about/help/">Help &amp; <span class="say-no-more">General</span> Contact</a>, <a href="/community/diversity/">Diversity <span class="say-no-more">Initiatives</span></a>, <a href="https://github.com/python/pythondotorg/issues">Submit Website Bug</a>, <a href="https://status.python.org/">Status <span class="python-status-indicator-default" id="python-status-indicator"></span></a>, <a href="/psf-landing/">Python Software Foundation</a>, <a href="/about/legal/">Legal Statements</a>, <a href="https://policies.python.org/python.org/Privacy-Notice/">Privacy Notice</a>]
########################################

All URLS
--------------------
['#content', '#python-network', '/', 'https://www.python.org/psf/', 'https://docs.python.org', 'https://pypi.org/', '/jobs/', '/community/', '#top', '/', 'https://psfmember.org/civicrm/contribute/transact?reset=1&id=2', '#site-map', '#', 'javascript:;', 'javascript:;', 'javascript:;', '#', 'https://www.linkedin.com/company/python-software-foundation/', 'https://fosstodon.org/@ThePSF', '/community/irc/', 'https://twitter.com/ThePSF', '/about/', '/about/apps/', '/about/quotes/', '/about/gettingstarted/', '/about/help/', 'http://brochure.getpython.info/', '/downloads/', '/downloads/', '/downloads/source/', '/downloads/windows/', '/downloads/macos/', '/download/other/', 'https://docs.python.org/3/license.html', '/download/alternatives', '/doc/', '/doc/', '/doc/av', 'https://wiki.python.org/moin/BeginnersGuide', 'https://devguide.python.org/', 'https://docs.python.org/faq/', 'http://wiki.python.org/moin/Languages', 'https://peps.python.org', 'https://wiki.python.org/moin/PythonBooks', '/doc/essays/', '/community/', '/community/diversity/', '/community/lists/', '/community/irc/', '/community/forums/', '/psf/annual-report/2024/', '/community/workshops/', '/community/sigs/', '/community/logos/', 'https://wiki.python.org/moin/', '/psf/conduct/', '/community/awards', '/psf/get-involved/', '/psf/community-stories/', '/success-stories/', '/success-stories/category/arts/', '/success-stories/category/business/', '/success-stories/category/education/', '/success-stories/category/engineering/', '/success-stories/category/government/', '/success-stories/category/scientific/', '/success-stories/category/software-development/', '/blogs/', '/blogs/', '/psf/newsletter/', 'http://pyfound.blogspot.com/', 'http://pycon.blogspot.com/', 'http://planetpython.org/', '/events/', '/events/python-events/', '/events/python-user-group/', '/events/python-events/past/', '/events/python-user-group/past/', 'https://wiki.python.org/moin/PythonEventsCalendar#Submitting_an_Event', '/shell/', '//docs.python.org/3/tutorial/controlflow.html#defining-functions', '//docs.python.org/3/tutorial/introduction.html#lists', 'http://docs.python.org/3/tutorial/introduction.html#using-python-as-a-calculator', '//docs.python.org/3/tutorial/controlflow.html', '//docs.python.org/3/tutorial/', '/doc/', '/about/gettingstarted/', '/downloads/release/python-3135/', 'https://docs.python.org', '//jobs.python.org', 'https://blog.python.org', 'https://pyfound.blogspot.com/2025/07/psf-board-nominations-opening-july-29th.html', 'https://pythoninsider.blogspot.com/2025/07/python-314-release-candidate-1-is-go.html', 'https://pyfound.blogspot.com/2025/07/affirm-your-psf-membership-voting-status.html', 'https://mailchi.mp/python/python-software-foundation-july-2024-newsletter-19880429', 'https://pyfound.blogspot.com/2025/07/notice-of-python-software-foundation.html', '/events/calendars/', '/events/python-user-group/2081/', '/events/python-events/2011/', '/events/python-events/2077/', '/events/python-events/1973/', '/events/python-events/1971/', '/success-stories/', '/success-stories/abridging-clinical-conversations-using-python/', '/success-stories/abridging-clinical-conversations-using-python/', '/about/apps', 'http://www.djangoproject.com/', 'http://www.pylonsproject.org/', 'http://bottlepy.org', 'http://tornadoweb.org', 'http://flask.pocoo.org/', 'http://www.web2py.com/', 'http://wiki.python.org/moin/TkInter', 'https://wiki.gnome.org/Projects/PyGObject', 'http://www.riverbankcomputing.co.uk/software/pyqt/intro', 'https://wiki.qt.io/PySide', 'https://kivy.org/', 'http://www.wxpython.org/', 'https://dearpygui.readthedocs.io/en/latest/', 'http://www.scipy.org', 'http://pandas.pydata.org/', 'http://ipython.org', 'http://buildbot.net/', 'http://trac.edgewall.org/', 'http://roundup.sourceforge.net/', 'http://www.ansible.com', 'https://saltproject.io', 'https://www.openstack.org', 'https://xon.sh', '/psf/', '/psf/', '/psf/membership/', '/psf/donations/', '#python-network', '/about/', '/about/apps/', '/about/quotes/', '/about/gettingstarted/', '/about/help/', 'http://brochure.getpython.info/', '/downloads/', '/downloads/', '/downloads/source/', '/downloads/windows/', '/downloads/macos/', '/download/other/', 'https://docs.python.org/3/license.html', '/download/alternatives', '/doc/', '/doc/', '/doc/av', 'https://wiki.python.org/moin/BeginnersGuide', 'https://devguide.python.org/', 'https://docs.python.org/faq/', 'http://wiki.python.org/moin/Languages', 'https://peps.python.org', 'https://wiki.python.org/moin/PythonBooks', '/doc/essays/', '/community/', '/community/diversity/', '/community/lists/', '/community/irc/', '/community/forums/', '/psf/annual-report/2024/', '/community/workshops/', '/community/sigs/', '/community/logos/', 'https://wiki.python.org/moin/', '/psf/conduct/', '/community/awards', '/psf/get-involved/', '/psf/community-stories/', '/success-stories/', '/success-stories/category/arts/', '/success-stories/category/business/', '/success-stories/category/education/', '/success-stories/category/engineering/', '/success-stories/category/government/', '/success-stories/category/scientific/', '/success-stories/category/software-development/', '/blogs/', '/blogs/', '/psf/newsletter/', 'http://pyfound.blogspot.com/', 'http://pycon.blogspot.com/', 'http://planetpython.org/', '/events/', '/events/python-events/', '/events/python-user-group/', '/events/python-events/past/', '/events/python-user-group/past/', 'https://wiki.python.org/moin/PythonEventsCalendar#Submitting_an_Event', '/dev/', 'https://devguide.python.org/', 'https://github.com/python/cpython/issues', 'https://mail.python.org/mailman/listinfo/python-dev', '/dev/core-mentorship/', '/dev/security/', '#python-network', '/about/help/', '/community/diversity/', 'https://github.com/python/pythondotorg/issues', 'https://status.python.org/', '/psf-landing/', '/about/legal/', 'https://policies.python.org/python.org/Privacy-Notice/']
########################################

Cleanup All URLS
--------------------
['https://www.python.org/psf/', 'https://docs.python.org', 'https://pypi.org/', 'https://psfmember.org/civicrm/contribute/transact?reset=1&id=2', 'https://www.linkedin.com/company/python-software-foundation/', 'https://fosstodon.org/@ThePSF', 'https://twitter.com/ThePSF', 'http://brochure.getpython.info/', 'https://docs.python.org/3/license.html', 'https://wiki.python.org/moin/BeginnersGuide', 'https://devguide.python.org/', 'https://docs.python.org/faq/', 'http://wiki.python.org/moin/Languages', 'https://peps.python.org', 'https://wiki.python.org/moin/PythonBooks', 'https://wiki.python.org/moin/', 'http://pyfound.blogspot.com/', 'http://pycon.blogspot.com/', 'http://planetpython.org/', 'https://wiki.python.org/moin/PythonEventsCalendar#Submitting_an_Event', 'http://docs.python.org/3/tutorial/introduction.html#using-python-as-a-calculator', 'https://docs.python.org', 'https://blog.python.org', 'https://pyfound.blogspot.com/2025/07/psf-board-nominations-opening-july-29th.html', 'https://pythoninsider.blogspot.com/2025/07/python-314-release-candidate-1-is-go.html', 'https://pyfound.blogspot.com/2025/07/affirm-your-psf-membership-voting-status.html', 'https://mailchi.mp/python/python-software-foundation-july-2024-newsletter-19880429', 'https://pyfound.blogspot.com/2025/07/notice-of-python-software-foundation.html', 'http://www.djangoproject.com/', 'http://www.pylonsproject.org/', 'http://bottlepy.org', 'http://tornadoweb.org', 'http://flask.pocoo.org/', 'http://www.web2py.com/', 'http://wiki.python.org/moin/TkInter', 'https://wiki.gnome.org/Projects/PyGObject', 'http://www.riverbankcomputing.co.uk/software/pyqt/intro', 'https://wiki.qt.io/PySide', 'https://kivy.org/', 'http://www.wxpython.org/', 'https://dearpygui.readthedocs.io/en/latest/', 'http://www.scipy.org', 'http://pandas.pydata.org/', 'http://ipython.org', 'http://buildbot.net/', 'http://trac.edgewall.org/', 'http://roundup.sourceforge.net/', 'http://www.ansible.com', 'https://saltproject.io', 'https://www.openstack.org', 'https://xon.sh', 'http://brochure.getpython.info/', 'https://docs.python.org/3/license.html', 'https://wiki.python.org/moin/BeginnersGuide', 'https://devguide.python.org/', 'https://docs.python.org/faq/', 'http://wiki.python.org/moin/Languages', 'https://peps.python.org', 'https://wiki.python.org/moin/PythonBooks', 'https://wiki.python.org/moin/', 'http://pyfound.blogspot.com/', 'http://pycon.blogspot.com/', 'http://planetpython.org/', 'https://wiki.python.org/moin/PythonEventsCalendar#Submitting_an_Event', 'https://devguide.python.org/', 'https://github.com/python/cpython/issues', 'https://mail.python.org/mailman/listinfo/python-dev', 'https://github.com/python/pythondotorg/issues', 'https://status.python.org/', 'https://policies.python.org/python.org/Privacy-Notice/']
########################################

Create dictionary with all urls and paragraphs
--------------------
{'website_title': 'Welcome to Python.org', 'all_urls': ['https://www.python.org/psf/', 'https://docs.python.org', 'https://pypi.org/', 'https://psfmember.org/civicrm/contribute/transact?reset=1&id=2', 'https://www.linkedin.com/company/python-software-foundation/', 'https://fosstodon.org/@ThePSF', 'https://twitter.com/ThePSF', 'http://brochure.getpython.info/', 'https://docs.python.org/3/license.html', 'https://wiki.python.org/moin/BeginnersGuide', 'https://devguide.python.org/', 'https://docs.python.org/faq/', 'http://wiki.python.org/moin/Languages', 'https://peps.python.org', 'https://wiki.python.org/moin/PythonBooks', 'https://wiki.python.org/moin/', 'http://pyfound.blogspot.com/', 'http://pycon.blogspot.com/', 'http://planetpython.org/', 'https://wiki.python.org/moin/PythonEventsCalendar#Submitting_an_Event', 'http://docs.python.org/3/tutorial/introduction.html#using-python-as-a-calculator', 'https://docs.python.org', 'https://blog.python.org', 'https://pyfound.blogspot.com/2025/07/psf-board-nominations-opening-july-29th.html', 'https://pythoninsider.blogspot.com/2025/07/python-314-release-candidate-1-is-go.html', 'https://pyfound.blogspot.com/2025/07/affirm-your-psf-membership-voting-status.html', 'https://mailchi.mp/python/python-software-foundation-july-2024-newsletter-19880429', 'https://pyfound.blogspot.com/2025/07/notice-of-python-software-foundation.html', 'http://www.djangoproject.com/', 'http://www.pylonsproject.org/', 'http://bottlepy.org', 'http://tornadoweb.org', 'http://flask.pocoo.org/', 'http://www.web2py.com/', 'http://wiki.python.org/moin/TkInter', 'https://wiki.gnome.org/Projects/PyGObject', 'http://www.riverbankcomputing.co.uk/software/pyqt/intro', 'https://wiki.qt.io/PySide', 'https://kivy.org/', 'http://www.wxpython.org/', 'https://dearpygui.readthedocs.io/en/latest/', 'http://www.scipy.org', 'http://pandas.pydata.org/', 'http://ipython.org', 'http://buildbot.net/', 'http://trac.edgewall.org/', 'http://roundup.sourceforge.net/', 'http://www.ansible.com', 'https://saltproject.io', 'https://www.openstack.org', 'https://xon.sh', 'http://brochure.getpython.info/', 'https://docs.python.org/3/license.html', 'https://wiki.python.org/moin/BeginnersGuide', 'https://devguide.python.org/', 'https://docs.python.org/faq/', 'http://wiki.python.org/moin/Languages', 'https://peps.python.org', 'https://wiki.python.org/moin/PythonBooks', 'https://wiki.python.org/moin/', 'http://pyfound.blogspot.com/', 'http://pycon.blogspot.com/', 'http://planetpython.org/', 'https://wiki.python.org/moin/PythonEventsCalendar#Submitting_an_Event', 'https://devguide.python.org/', 'https://github.com/python/cpython/issues', 'https://mail.python.org/mailman/listinfo/python-dev', 'https://github.com/python/pythondotorg/issues', 'https://status.python.org/', 'https://policies.python.org/python.org/Privacy-Notice/'], 'all_paragraphs': ['Notice: While JavaScript is not essential for this website, your interaction with the content will be limited. Please turn JavaScript on for the full experience. ', 'The core of extensible programming is defining functions. Python allows mandatory and optional arguments, keyword arguments, and even arbitrary argument lists. More about defining functions in Python\xa03', 'Lists (known as arrays in other languages) are one of the compound data types that Python understands. Lists can be indexed, sliced and manipulated with other built-in functions. More about lists in Python\xa03', 'Calculations are simple with Python, and expression syntax is straightforward: the operators +, -, * and / work as expected; parentheses () can be used for grouping. More about simple math functions in Python\xa03.', 'Python knows the usual control flow statements that other languages speak — if, for, while and range — with some of its own twists, of course. More control flow tools in Python\xa03', 'Experienced programmers in any other language can pick up Python very quickly, and beginners find the clean syntax and indentation structure easy to learn. Whet your appetite with our Python\xa03 overview.', 'Python is a programming language that lets you work quickly and integrate systems more effectively. Learn More', "Whether you're new to programming or an experienced developer, it's easy to learn and use Python.", 'Start with our Beginner’s Guide', 'Python source code and installers are available for download for all versions!', 'Latest: Python 3.13.5', "Documentation for Python's standard library, along with tutorials and guides, are available online.", 'docs.python.org', "Looking for work or have a Python related position that you're trying to hire for? Our relaunched community-run job board is the place to go.", 'jobs.python.org', 'More', 'More', 'More', 'Abridging clinical conversations using Python by Nimshi Venkat and Sandeep Konam', 'More', 'The mission of the Python Software Foundation is to promote, protect, and advance the Python programming language, and to support and facilitate the growth of a diverse and international community of Python programmers. Learn more ', '\nBecome a Member\nDonate to the PSF\n', '\nCopyright ©2001-2025.\n                            \xa0Python Software Foundation\n                            \xa0Legal Statements\n                            \xa0Privacy Notice\n\n']}
########################################

Write to web_scrape_report.json file
--------------------
Created web_scrape_report.json file
########################################


Process finished with exit code 0

"""