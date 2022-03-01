import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='api-rule-engine',
    version='0.0.1',
    scripts=['api-rule-engine'],
    author='Omer London',
    description='rule engine API',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/somerl20/api-rule-engine.git',
    project_urls={},
    license='GNU',
    packages=setuptools.find_packages(),
    install_requires=['requests>=2.25.1'],
)