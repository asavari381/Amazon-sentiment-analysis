Python 3.12.3 (v3.12.3:f6650f9ad7, Apr  9 2024, 08:18:48) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> from setuptools import setup, find_packages
... 
... setup(
...     name='amazon_sentiment_analysis',
...     version='0.1',
...     description='Amazon product sentiment analysis using NLP',
...     author='Asavari Shejwal',
...     author_email='asavari2404@gmail.com',
...     packages=find_packages(),
...     install_requires=[
...         'numpy',
...         'pandas',
...         'scikit-learn',
...         'matplotlib',
...         'seaborn',
...         'nltk',
...         'spacy',
...         'textblob',
...         'tqdm',
...         'torch',
...         'transformers',
...     ],
...     classifiers=[
...         'Programming Language :: Python :: 3',
...         'License :: OSI Approved :: MIT License',
...         'Operating System :: OS Independent',
...     ],
...     python_requires='>=3.7',
... )
