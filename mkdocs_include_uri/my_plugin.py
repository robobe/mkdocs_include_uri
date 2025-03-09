from mkdocs.plugins import BasePlugin
from mkdocs.config import config_options

class MyPlugin(BasePlugin):
    config_scheme = (
        ('message', config_options.Type(str, default='Hello, MkDocs!')),
    )

    def on_pre_build(self, config):
        print(f"MyPlugin: {self.config['message']}")

    def on_page_markdown(self, markdown, page, config, files):
        """Modify the Markdown before rendering."""
        return markdown.replace("{{PLUGIN}}", self.config['message'])