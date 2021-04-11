from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='cryptoanalysis',
    version='0.0.1',
    description='Basic analysis and visualization of cryptocurrency digital assets',
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='',
    author='Branimir Raguž',
    author_email='branimir.raguz11@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords=['cryptocurrency', 'finance', 'stocks'],
    packages=find_packages(),
    install_requires=['pandas', 'matplotlib', 'sklearn', 'requests']
)