#!/usr/bin/python
# tocrawl could be implemented as a queue
from urllib import urlopen

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

def add_to_index(index,keyword,url):
    if keyword in index:
        index[keyword].append(url)
    else:
        index[keyword] = [url]

def add_page_to_index(index,url,content):
    for word in content.split():
        add_to_index(index, word, url)

def get_page(url):
    try:
        return urlopen(url).read()
    except:
        return ""

def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    index = {}
    graph = {}
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            content = get_page(page)
            add_page_to_index(index, page, content)
            outlinks = get_all_links(content)
            graph[page] = outlinks
            union(tocrawl, outlinks)
            crawled.append(page)
    return index, graph

def lookup(index,keyword):
    if keyword in index:
        return index[keyword]
    else:
        return []

def page_rank(graph):
    d = 0.8 # damping factor
    numloops = 5

    ranks = {}
    npages = len(graph)
    for page in graph:
        ranks[page] = 1.0 / npages

    for i in range(0, numloops):
        newranks = {}
        for page in graph:
            newrank = (1 - d) / npages
            for node in graph:
                if page in graph[node]:
                    newrank = newrank + d * ranks[node] / len(graph[node])
            newranks[page] = newrank
        ranks = newranks
    return ranks

def lucky_search(index, ranks, keyword):
    potential_urls = lookup(index, keyword)
    if not potential_urls:
        return None
    best_url = potential_urls[0]
    for p_url in potential_urls:
        if ranks[p_url] > ranks[best_url]:
            best_url = p_url
    return best_url

def ordered_search(index, ranks, keyword):
    hits = lookup(index, keyword)
    if not hits:
        return None
    quickSort(hits, ranks, 0, len(hits) - 1)
    return hits

def quickSort(hits, ranks, start, end):
    if end <= start:
        return hits
    p = partition(hits, ranks, start, end)
    quickSort(hits, ranks, start, p - 1)
    quickSort(hits, ranks, p + 1, end)

def partition(hits, ranks, start, end):
    pivot_value = ranks[hits[0]]
    i = start + 1
    for j in range(start + 1, end + 1):
        if ranks[hits[j]] > pivot_value:
            hits[j], hits[i] = hits[i], hits[j]
            i = i + 1
    hits[start], hits[i - 1] = hits[i - 1], hits[start]
    return i - 1

