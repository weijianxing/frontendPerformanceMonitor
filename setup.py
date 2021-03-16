#-*- coding: utf-8 -*-
# ------ wuage.com testing team ---------
# __author__ : jianxing.wei@wuage.com
from setuptools import setup, find_packages

setup(
    name='frontend-sdk',
    version='1.0.2.dev1',
    description='frontend performance monitor sdk, ',
    url='https://gitlab.wuage-inc.com/jianxing.wei/dingchatbot.git',
    author='Jianxing.wei',
    author_email='jianxing.wei@wuage.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='frontend performance analyse monitor',
    packages=find_packages(),
)