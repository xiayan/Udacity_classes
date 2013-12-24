#!/usr/bin/python

# The web crawler we built at the
# end of Unit 2 has some serious
# flaws if we were going to use
# it in a real crawler. One
# problem is if we start with
# a good seed page, it might
# run for an extremely long
# time (even forever, since the
# number of URLS on the web is not
# actually finite). The final two
# questions of the homework ask
# you to explore two different ways
# to limit the pages that it can
# crawl.

#######

# TWO GOLD STARS#

# Modify the crawl_web procedure
# to take a second parameter,
# max_depth, that limits the
# minimum number of consecutive
# links that would need to be followed
# from the seed page to reach this
# page. For example, if max_depth
# is 0, the only page that should
# be crawled is the seed page.
# If max_depth is 1, the pages
# that should be crawled are the
# seed page and every page that links
# to it directly. If max_depth is 2,
# the crawl should also include all pages
# that are linked to by these pages.

# The following definition of
# get_page provides an interface
# to the website found at
# http://www.udacity.com/cs101x/index.html

# The function output order does not affect grading.

def get_page(url):
    try:
        if url == "http://www.udacity.com/cs101x/index.html":
            return ('<html> <body> This is a test page for learning to crawl! '
            '<p> It is a good idea to '
            '<a href="http://www.udacity.com/cs101x/crawling.html">learn to '
            'crawl</a> before you try to  '
            '<a href="http://www.udacity.com/cs101x/walking.html">walk</a> '
            'or  <a href="http://www.udacity.com/cs101x/flying.html">fly</a>. '
            '</p> </body> </html> ')
        elif url == "http://www.udacity.com/cs101x/crawling.html":
            return ('<html> <body> I have not learned to crawl yet, but I '
            'am quite good at '
            '<a href="http://www.udacity.com/cs101x/kicking.html">kicking</a>.'
            '</body> </html>')
        elif url == "http://www.udacity.com/cs101x/walking.html":
            return ('<html> <body> I cant get enough '
            '<a href="http://www.udacity.com/cs101x/index.html">crawling</a>! '
            '</body> </html>')
        elif url == "http://www.udacity.com/cs101x/flying.html":
            return ('<html> <body> The magic words are Squeamish Ossifrage! '
            '</body> </html>')
        elif url == "http://top.contributors/velak.html":
            return ('<a href="http://top.contributors/jesyspa.html">'
        '<a href="http://top.contributors/forbiddenvoid.html">')
        elif url == "http://top.contributors/jesyspa.html":
            return  ('<a href="http://top.contributors/elssar.html">'
        '<a href="http://top.contributors/kilaws.html">')
        elif url == "http://top.contributors/forbiddenvoid.html":
            return ('<a href="http://top.contributors/charlzz.html">'
        '<a href="http://top.contributors/johang.html">'
        '<a href="http://top.contributors/graemeblake.html">')
        elif url == "http://top.contributors/kilaws.html":
            return ('<a href="http://top.contributors/tomvandenbosch.html">'
        '<a href="http://top.contributors/mathprof.html">')
        elif url == "http://top.contributors/graemeblake.html":
            return ('<a href="http://top.contributors/dreyescat.html">'
        '<a href="http://top.contributors/angel.html">')
        elif url == "A1":
            return  '<a href="B1"> <a href="C1">  '
        elif url == "B1":
            return  '<a href="E1">'
        elif url == "C1":
            return '<a href="D1">'
        elif url == "D1":
            return '<a href="E1"> '
        elif url == "E1":
            return '<a href="F1"> '
    except:
        return ""
    return ""

def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)

def get_all_links(page):
    links = []
    while True:
        url,endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links

def crawl_web_bfs(seed,max_depth):
    tocrawl = [[seed, 0]]
    crawled = []
    level = max_depth
    current_level = 0
    if max_depth:
        while max_depth:
            max_depth = max_depth - 1
            while tocrawl:
                url, depth = tocrawl.pop(0)
                if url not in crawled:
                    crawled.append(url)
                    if current_level < level:
                        for next_url in get_all_links(get_page(url)):
                            tocrawl.append([next_url, current_level + 1])
                if tocrawl and tocrawl[0][1] == current_level:
                    continue
                else:
                    current_level = current_level + 1
    else:
        crawled = [seed]
    return crawled

def crawl_web_dfs(seed, max_depth):
    tocrawl = [[seed, 0]]
    crawled = {}
    while tocrawl:
        page,depth = tocrawl.pop()
        if ((page not in crawled) or (crawled[page] > depth)) and (depth <= max_depth):
            for link in get_all_links(get_page(page)):
                tocrawl.append([link, depth + 1])
            crawled[page] = depth
    return crawled.keys()

print crawl_web_dfs("http://www.udacity.com/cs101x/index.html",0)
#>>> ['http://www.udacity.com/cs101x/index.html']

print crawl_web_dfs("http://www.udacity.com/cs101x/index.html",1)
#>>> ['http://www.udacity.com/cs101x/index.html',
#>>> 'http://www.udacity.com/cs101x/flying.html',
#>>> 'http://www.udacity.com/cs101x/walking.html',
#>>> 'http://www.udacity.com/cs101x/crawling.html']

print crawl_web_dfs("http://www.udacity.com/cs101x/index.html",50)
#>>> ['http://www.udacity.com/cs101x/index.html',
#>>> 'http://www.udacity.com/cs101x/flying.html',
#>>> 'http://www.udacity.com/cs101x/walking.html',
#>>> 'http://www.udacity.com/cs101x/crawling.html',
#>>> 'http://www.udacity.com/cs101x/kicking.html']

print crawl_web_dfs("http://top.contributors/forbiddenvoid.html",2)
#>>> ['http://top.contributors/forbiddenvoid.html',
#>>> 'http://top.contributors/graemeblake.html',
#>>> 'http://top.contributors/angel.html',
#>>> 'http://top.contributors/dreyescat.html',
#>>> 'http://top.contributors/johang.html',
#>>> 'http://top.contributors/charlzz.html']

print crawl_web_dfs("A1",3)
#>>> ['A1', 'B1', 'C1', 'D1', 'E1', 'F1']