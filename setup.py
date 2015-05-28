from setuptools import find_packages, setup
setup(name="stjornbord_google_api",
      version="0.1",
      description="Wrapper around google's provisioning api",
      author="Bjorn Swift",
      author_email='bjorn@swift.is',
      platforms=["any"],
      license="GPLv3",
      url="http://github.com/opinnmr/stjornbord-google-api",
      packages=find_packages(),
      install_requires=["google-api-python-client"]
      )