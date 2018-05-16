import io

from setuptools import setup, find_packages

with io.open('README.md', 'rt', encoding="utf8") as f:
    readme = f.read()

setup(
    author=u'Javier Lopez',
    author_email='javier@lopezmunoz.name',
    description='Adds support for Google Tag Manager to Lektor CMS',
    keywords='Lektor plugin static-site google-tag-manager',
    license='BSD',
    long_description=readme,
    long_description_content_type='text/markdown',
    name='lektor-google-tag-manager',
    packages=find_packages(),
    py_modules=['lektor_google_tag_manager'],
    url='http://github.com/JavierLopezMunoz/lektor-google-tag-manager/',
    version='0.1',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Lektor',
        'Environment :: Web Environment',
        'Environment :: Plugins',
        'License :: OSI Approved :: BSD License',
    ],
    entry_points={
        'lektor.plugins': [
            'google-tag-manager = lektor_google_tag_manager:GoogleTagManagerPlugin',
        ]
    },
)
