class Html:
    def __init__(self, tag_name, *class_names, **attributes):
        """Initializes a new html tag."""
        self.name = tag_name
        self.class_names = class_names
        self.attributes = attributes
        self.children = []

    def render(self):
        """Renders the html tag as a string."""
        html = f'<{self.name}'

        if self.class_names.__len__() > 0:
            classes_list = ' '.join(self.class_names)
            html += f' class="{classes_list}"'
            
        for key, value in self.attributes.items():
            html += f' {key}="{value}"'

        rendered_children = self.__render_children()

        html += f'>{rendered_children}</{self.name}>'

        return html

    def __render_children(self):
        """Renders the tag's children"""
        rendered_children = ''

        for child in self.children:
            rendered_children += '\n    '
            if type(child) is str:
                rendered_children += child
            else:
                rendered_children += child.render().replace('\n','\n    ')
        
        rendered_children += '\n'
        
        return rendered_children
