from distutils.core import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='op_text',
    packages=['op_text'],
    version='0.1.2',
    license='MIT',
    description='Identify the sentiment of a piece of text',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Dean Knudson',
    author_email='knuddj1@student.op.ac.nz',
    url='https://github.com/knuddj1/op_text',
    keywords='NLP deep learning transformer pytorch BERT GPT GPT-2 google openai CMU sentiment text',
    install_requires=[
        'numpy',
        'torch>=1.0.0',
        'boto3',
        'requests',
        'tqdm',
        'regex',
        'sentencepiece',
        'pytorch-transformers'
        ],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],

    
)