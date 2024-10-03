from setuptools import setup, find_packages

setup(
    name='apple_cleanup_remover',
    version='0.1.0',
    author='0x0060',
    author_email='ren@0x0060.dev',
    description='A Python package designed to remove specific metadata fields from image files, specifically focusing on eliminating the Apple AI cleanup logo / watermark.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/0x0060/apple_cleanup_remover',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        'Pillow',
        'piexif',
    ],
)
