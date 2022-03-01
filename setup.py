
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='api-rule-engine',
    version='0.0.1',
    author='Omer London',
    description='rule engine API',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://momerl20@bitbucket.org/minereye/api-rule-engine.git',
    license='GNU',
    packages=['api-rule-engine'],
    install_requires=['requests>=2.25.1'],
)