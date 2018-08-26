from setuptools import setup, find_packages

with open('README.md', mode='r', encoding='utf-8') as f:
    readme = f.read()

test_requirements = [
    'pytest', 'pytest-cov', 'codecov'
]
required = ['pluggy']

setup(
    name='repomate-plug',
    version='0.2.0',
    description=(
        'A CLI tool for managing large amounts of GitHub repositories'),
    long_description=readme,
    long_description_content_type='text/markdown',
    author='Simon Larsén',
    author_email='slarse@kth.se',
    url='https://github.com/slarse/repomate-plug',
    download_url='https://github.com/slarse/repomate-plug/archive/v0.2.0.tar.gz',
    license='MIT',
    packages=find_packages(exclude=('tests', 'docs')),
    tests_require=test_requirements,
    install_requires=required,
    extras_require=dict(TEST=test_requirements),
    include_package_data=True,
    zip_save=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Education',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
    ])
