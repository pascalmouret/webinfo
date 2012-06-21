from setuptools import setup, find_packages

setup(
    name='webinfo',
    version='0.1',
    url='http://github.com/pascalmouret/webinfo',
    license='BSD',
    platforms=['OS Independent'],
    description="Get some info about a domain.",
    long_description=open('README').read(),
    author='Pascal Mouret',
    author_email='pascal.mouret@me.com',
    packages=find_packages(),
    install_requires=('dnspython'),
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': ['webinfo=webinfo.main:cmd',],
    },
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
)