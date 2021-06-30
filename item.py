class Item():
    def __init__(self, tag_name, tag_attrs, item_name,
                get_attrs='text', get_all_tag=False):
        self.tag_name    = tag_name
        self.tag_attrs   = tag_attrs
        self.get_all_tag = get_all_tag
        self.get_attrs   = get_attrs
        self.item_name   = item_name

    def get_item_data(self, soup):
        tag = soup.find_all(self.tag_name, self.tag_attrs)
        
        if not self.get_all_tag:
            tag = tag[0]
            if self.get_attrs == "text":
                get_content = tag.get_text()
            else:
                get_content = tag.attrs[self.get_attrs]
            
        else:
            get_content = []
            if self.get_attrs == "text":
                for i in tag:
                    get_content.append(i.get_text())
            else:
                for i in tag:
                    get_content.append(i.attrs[self.get_attrs])
            
        self.item = {self.item_name: get_content}

        return self.item
