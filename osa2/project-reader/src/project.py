import re

class Project:
    def __init__(self, name, description, license, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license = license
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_dependencies(self, dependencies):
        return ", ".join(dependencies) if len(dependencies) > 0 else "-"

    def __str__(self):
        printout = f"Name: {self.name}"
        printout += f"\nDescription: {self.description or '-'}"
        printout += f"\nLisence: {self.license or '-'}"
        printout += f"\n"

        printout += f"\nAuthors:"
        for author in self.authors:
            printout += f"\n - {author.get('name')}"
        printout += f"\n"

        printout += f"\nDependencies:"
        for dep in self.dependencies:
            stripped_dep = re.sub(r'[^a-zA-Z]', '', dep)
            printout += f"\n - {stripped_dep}"
        printout += f"\n"

        printout += f"\nDevelopment dependencies:"
        for dev_dep in self.dev_dependencies:
            stripped_dev_dep = re.sub(r'[^a-zA-Z]', '', dev_dep)
            printout += f"\n - {stripped_dev_dep}"
            
        return printout
