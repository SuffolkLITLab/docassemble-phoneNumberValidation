import os
import sys
from setuptools import setup, find_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')
def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.phoneNumberValidation',
      version='0.0.1',
      description=('A docassemble extension.'),
      long_description="## About\r\n\r\nDocassemble real-time (client-side) phone number validator.\r\nSee example for example use.\r\n\r\nThis package allows you to import a .yml file to install a `dal-phone`\r\ndatatype for a text field. That datatype gives the user feedback about\r\nwhether their phone number input is valid. Gets triggered when the user\r\nclicks outside the field (or it otherwise loses focus.\r\n\r\nUnless the user uses an international code for the number, they\r\nhave to pick a country from an inline country picker\r\ndropdown (which does have flag images). Research indicates that\r\nguessing at the country otherwise isn't feasible. The default country\r\nis USA (sorry everyone else).\r\n\r\n**WARNING:** There currently isn't a way to store the country that the\r\nuser selected for a certain input, so when the user clicks 'Back'\r\nthe field, which is a whole new field as far as this code is concerned,\r\ngets the default country again - 'US' - and the user has to\r\nre-select the phone's country for their number to be valid.\r\n\r\n## Dependancies\r\n\r\nThis package uses\r\n[intl-tel-input npm package](https://www.npmjs.com/package/intl-tel-input),\r\nwhich adds input field features that use\r\n[google's phone number validator](https://www.npmjs.com/package/google-libphonenumber) to validate the number.\r\n\r\n## TODO\r\n\r\n1. Allow package users to set the default country.\r\n1. ~Fix CSS for dropdown height being affected by error message in DA.~\r\n\r\n## CHANGELOG\r\n* 06/19/2020 Adjusted dropdown CSS specifically for DA. Hard-coded with `em`.",
      long_description_content_type='text/markdown',
      author='',
      author_email='mb.restless.tech@gmail.com',
      license='The MIT License (MIT)',
      url='https://docassemble.org',
      packages=find_packages(),
      namespace_packages=['docassemble'],
      install_requires=[],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/phoneNumberValidation/', package='docassemble.phoneNumberValidation'),
     )

