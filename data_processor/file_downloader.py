import urllib2

class FileDownloader(object):

    def download_file(self, url):
        response = urllib2.urlopen(url)
        file = open("./data/raw_data/temp_file.pdf", 'w')
        file.write(response.read())
        file.close()