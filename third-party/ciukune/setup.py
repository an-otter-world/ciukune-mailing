"""MarshPy installation configuration."""
from pathlib import Path
from re import compile as re_compile
from subprocess import CalledProcessError
from subprocess import DEVNULL
from subprocess import check_output

from setuptools import setup
from setuptools import find_packages


def get_git_version() -> str:
    """Get package version from git tags."""
    pattern = re_compile(
        r'^v(?P<version>\d*\.\d*\.\d*)(-\d*-g(?P<commit>\d*))?'
    )
    try:
        command = [
            'git', 'describe',
            '--tags',
            '--match', 'v[0-9]*.[0-9]*.[0-9]*'
        ]
        version_bytes = check_output(command, stderr=DEVNULL)
        version = version_bytes.decode('utf-8')
        match = pattern.match(version)
        if match is not None:
            commit = match.group('commit')
            version = match.group('version')
            if commit is not None:
                version = '{}.dev{}'.format(version, commit)
            return version.rstrip()
    except CalledProcessError:
        pass

    return '0.0.0'


setup(
    name="ciukune",
    description="Python Yaml Object deserializer based on PyYAML.",
    long_description=(Path(__file__).parent / "README.md").read_text(),
    long_description_content_type="text/markdown",
    version=get_git_version(),
    keywords=['Portal', 'Anarchism'],
    packages=find_packages(include=['ciukune', 'ciukune.*']),
    license='WTFPL',
    classifiers=[
        "Development Status :: 3 - Alpha",
    ],
    install_requires=[
	'django',
	'django-split-settings',
	'djangorestframework',
	'djangorestframework_simplejwt',
	'pillow'
    ],
    author="An Otter World",
    author_email="an-otter-world@ki-dour.org",
    url="http://github.com/an-otter-world/ciukune/",
    zip_safe=False,
)