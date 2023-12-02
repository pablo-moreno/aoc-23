# What I learned

By default, regex expressions do not find overlapping values.

In the case `oneight`, searching for `one` and `eight`, if they overlap, a normal regex would only find `one`.

To allow overlapping, we have to add `(?=(<your regex here>))`.

Example saved [here](https://regex101.com/r/ghsFyd/2)
