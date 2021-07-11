class Item():
    def __init__(self, tag_xpath, item_name, get_all_tag=False, default=None):
        self.tag_xpath   = tag_xpath
        self.get_all_tag = get_all_tag
        self.item_name   = item_name
        self.default     = default

    def get_item_data(self, html_obj):
        self.tag_data = html_obj.xpath(self.tag_xpath)

        if self.tag_data:
            if not self.get_all_tag:
                self.tag_data = self.tag_data[0]
        else:
            self.tag_data = self.default
            
        self.item = {self.item_name: self.tag_data}

        return self.item
