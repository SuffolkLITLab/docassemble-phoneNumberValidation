## About

Docassemble real-time (client-side) phone number validator.
See example for example use.

This package allows you to import a .yml file to install a `dal-phone`
datatype for a text field. That datatype gives the user feedback about
whether their phone number input is valid. Gets triggered when the user
clicks outside the field (or it otherwise loses focus.

Unless the user uses an international code for the number, they
have to pick a country from an inline country picker
dropdown (which does have flag images). Research indicates that
guessing at the country otherwise isn't feasible. The default country
is USA (sorry everyone else).

**WARNING:** There currently isn't a way to store the country that the
user selected for a certain input, so when the user clicks 'Back'
the field, which is a whole new field as far as this code is concerned,
gets the default country again - 'US' - and the user has to
re-select the phone's country for their number to be valid.

## Dependancies

This package uses
[intl-tel-input npm package](https://www.npmjs.com/package/intl-tel-input),
which adds input field features that use
[google's phone number validator](https://www.npmjs.com/package/google-libphonenumber) to validate the number.

## TODO

1. Allow package users to set the default country.
1. ~Fix CSS for dropdown height being affected by error message in DA.~

## CHANGELOG
* 06/19/2020 Adjusted dropdown CSS specifically for DA. Hard-coded with `em`.