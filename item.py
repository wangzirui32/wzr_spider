class Item():
    def __init__(self, tag_name, tag_attrs, item_name,
                get_attrs='text', get_all_tag=False):
        self.tag_name    = tag_name
        self.tag_attrs   = tag_attrs
        self.get_all_tag = get_all_tag
        self.get_attrs   = get_attrs
        self.item_name   = item_name

    def get_item_data(self, soup):
        self.tag = soup.find_all(self.tag_name, self.tag_attrs)

        if not self.get_all_tag:
            self.tag = self.tag[0]
        get_content = self.get_tag_data()
        self.item = {self.item_name: get_content}

        return self.item

    def get_tag_data(self):
        if not self.get_all_tag:
            self.tag = self.tag[0]
            get_content = self.get_tag_attrs(self.tag)
        else:
            get_content = []
            for tag in self.tag:
                get_content.append(self.get_tag_attrs(tag))
        
        return get_content
    
    def get_tag_attrs(self, tag):
        if self.get_attrs == 'text':
            return tag.get_text()
        else:
            return tag.attrs[self.get_attrs]
