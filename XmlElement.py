class XmlElement:
    def __init__ (self, name='', parent='', children=[], attributes=dict(), text=''):
        self.name = name
        self.parent = parent
        self.children = children
        self.attributes = attributes
        self.text = text

    