# PrettifyJSON

_A simple Python script for formatting JSON data piped over stdin or from a specified file_

## Requirements

* Python 3

## Platform compatibility

In principle, anything that supports Python 3!

## Example usage

Run the script with no parameters to see a brief description of usage:

	me@here$ ./PrettifyJSON.py

	Usage:

	  Either pipe JSON data into the script, or specify an explicit input file, e.g.:

	  cat <whatever> | ./PrettifyJSON.py [indent=n] [sort=x]
	  ./PrettifyJSON.py input=whatever.json [indent=n] [sort=x]

	Here,

	  - n = number of spaces for indentation (optional, default: 2)
	  - key sorting is false if x = (false|no|f|0), else true (optional, default: True)

As we can see, the script accepts two general parameters, `indent` and `sort`:

* `indent` (_optional_): an integer parameter controlling the indentation level (in spaces) used for the JSON output
* `sort` (_optional_): specifies whether to print the JSON data using sorted keys

A further parameter, `input`, specifies an input file to use where JSON data is not being provided over `stdin`. 

### Example: JSON data from `stdin`

	curl -X "Get" https://api.osf.io/v2/users/ | ./PrettifyJSON.py

	cat whatever.json | ./PrettifyJSON.py

### Example: JSON data from file

	./PrettifyJSON.py input=whatever.json
