from setuptools import setup, find_packages
from requests import get

setup(
      name='programGUI',
      version=get("https://api.github.com/repos/CastellaniDavide/programGUI/tags").json()[0]['name'].replace("v", "") if len(get("https://api.github.com/repos/CastellaniDavide/programGUI/tags").json()) > 0 else "0.0", # Lastest release
      description=get("https://api.github.com/repos/CastellaniDavide/programGUI").json()['description'],
      long_description=get("https://raw.githubusercontent.com/CastellaniDavide/programGUI/master/docs/README.md").text,
      long_description_content_type="text/markdown",
      url=get("https://api.github.com/repos/CastellaniDavide/programGUI").json()['html_url'],
      author=get("https://api.github.com/repos/CastellaniDavide/programGUI").json()['owner']['login'],
      author_email=get(f"https://api.github.com/users/{get('https://api.github.com/repos/CastellaniDavide/programGUI').json()['owner']['login']}").json()['email'],
      license='GNU',
      packages=find_packages(),
      python_requires=">=3.7",
      platforms="linux_distibution",
      install_requires=[i for i in get("https://raw.githubusercontent.com/CastellaniDavide/programGUI/master/requirements/requirements.txt").text.split("\n") if not "#" in i and i != ''],
      zip_safe=True
      )
