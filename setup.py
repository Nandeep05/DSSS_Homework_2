from setuptools import setup, find_packages

setup(
    name='math_quiz',
    version='0.1',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'math_quiz=math_quiz.math_quiz:math_quiz',
        ],
    },
    license='Apache License 2.0',
    description='A simple math quiz game for learning Git and Python packaging.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Nandeep05/DSSS_Homework_2',  # Replace with your repository URL.
    author='Nandeep Bhadravathi Somashekar',
    author_email='Nandeepsomashekar1999@gmail.com',
)
