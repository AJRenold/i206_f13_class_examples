from urllib2 import urlopen
from bs4 import BeautifulSoup
from xml.etree import ElementTree


# Learn urllib2
# The web is messy, learn error handling!

def openUrl(url,verbose=False):
    """ Read more:
        http://docs.python.org/2/library/urllib2.html
        http://pymotw.com/2/urllib2/index.html 
    """

    #url = 'http://www.google.com'
    response = urlopen(url)
    if verbose:
        print 'RESPONSE:', response
        print 'URL     :', response.geturl()

        headers = response.info()
        print 'DATE    :', headers['date']
        print 'HEADERS :'
        print '---------'
        print headers

    data = response.read()

    if verbose:
        print 'LENGTH  :', len(data)
        print 'DATA    :'
        print '---------'
        print data

    return data

# Learn how to install Python Libraries with pip http://www.pip-installer.org/en/latest/installing.html
# More on pip http://www.pythonforbeginners.com/basics/python-pip-usage/
# More on pip and virtualenv http://dabapps.com/blog/introduction-to-pip-and-virtualenv-python/
def beautifulSoupSearchDom(html_data):
    """ Read more on BeautifulSoup:
        http://www.crummy.com/software/BeautifulSoup/bs4/doc/
    """
    soup = BeautifulSoup(html_data)
    print 'TITLE Tag'
    print soup.title

    print 'p Tag'
    print soup.p

    print 'a Tags'
    print soup.find_all('a')

    print 'a Tags attribute href'
    for tag in soup.find_all('a'):
        print tag.get('href')


# Recognize df and bf
# use lxml.etree Element Tree and getting node attributes with node.attrib.get('href')
def traverseDom(html_data, traverseRoute):
    """ Read more on xml.etree
        http://docs.python.org/2/library/xml.etree.elementtree.html
    """
    root = ElementTree.fromstring(html_data)
    print root
    
    def hasChildren(node):
        return len(list(node)) != 0
    
    def printDepthFirst(node, level=0):
        print '    '*level + node.tag
        if hasChildren(node):
            for child in list(node):
                printDepthFirst(child, level+1)

    if traverseRoute == 'df':
        print "depth first traversal"
        printDepthFirst(root)

    def printBreadthFirst(root):
        q = []
        q.append((root,0))
        while len(q) > 0:
            current_node, level = q.pop(0)
            print '    '*level + current_node.tag
            for child in list(current_node):
                q.append((child, level+1))

    if traverseRoute == 'bf':
        print 'breadth first traversal'
        printBreadthFirst(root)

if __name__ == '__main__':

    # Test URLs
    sandbox_url = 'http://courses.ischool.berkeley.edu/i206/f13/a6-sandbox/index.html'

    page_data = openUrl(sandbox_url, verbose=True)

    ## Uncomment to inspect different functions
    #beautifulSoupSearchDom(page_data)

    ## run with 'df' or 'bf'
    #traverseDom(page_data, 'bf')
