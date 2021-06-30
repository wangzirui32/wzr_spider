class CrawlerTag():
    def __init__(self, tag_name, tag_attrs={}, get_all_tag=False):
        self.tag_name    = tag_name
        self.tag_attrs   = tag_attrs
        self.get_all_tag = get_all_tag

    def get_this_tag(self, soup):
        if len(self.tag_attrs.items()) > 0:
            tags = soup.find_all(self.tag_name, self.tag_attrs)
        else:
            tags = soup.find_all(self.tag_name)
        
        if self.get_all_tag:
            return tags
        else:
            return tags[0]

