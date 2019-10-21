from distutils.core import setup
from io import open

setup(
    name='op_text',
    packages=['op_text'],
    version='0.1',
    license='MIT',
    description='Identify the sentiment of a piece of text',
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