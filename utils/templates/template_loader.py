import os


class TemplateLoader:
    """
    This class read all expected files in a directory.
    """
    files = []
    file_ext = ".json"

    def __init__(self, path):
        self.load_templates(path)

    def load_templates(self, path):
        """
        This method read and load all json files to list of templates.
        :param path: Path for templates directory
        """
        for root, directories, files in os.walk(path):
            for file in files:
                if self.file_ext in file:
                    self.files.append(os.path.join(root, file))

    def get_template(self, endpoint_name):
        """
        Search a file into the list of files and return it if it was found.
        :param endpoint_name: Endpoint name to looking for in the templates directory
        :return: A file content when the file is found. None is the file was not found.
        """
        for file in self.files:
            if endpoint_name in file:
                return open(file).read()
        return None

