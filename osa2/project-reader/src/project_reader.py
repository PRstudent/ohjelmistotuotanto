from logging import config
from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        #print("/=======================Print START====================/")
        #print(content)
        #print("/=======================Print DONE=====================/")

        parsed_content = toml.loads(content)

        name = parsed_content['project']['name']
        description = parsed_content['project']['description']
        license = parsed_content['project'].get('license')
        authors = parsed_content['project'].get('authors', [])
        dependencies = parsed_content['project'].get('dependencies', [])
        dev_dependencies = parsed_content['dependency-groups'].get('dev', [])

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, license, authors, dependencies, dev_dependencies)