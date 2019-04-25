#!/usr/bin/env python3

import sys, json

false_vals = ['false', 'no', 'f', '0']
parameters = { 'indent':2,   'sort':True }
converters = { 'indent':int, 'sort':lambda x: not (x.lower() in false_vals) }

def printUsage( prog ):
	print ('')
	print ('Usage:')
	print ('')
	print ('  Either pipe JSON data into the script, or specify an explicit input file, e.g.:')
	print ('')
	print ('  cat <whatever> | %s [indent=n] [sort=x]' % (prog))
	print ('  %s input=whatever.json [indent=n] [sort=x]' % (prog))
	print ('')
	print ('Here,')
	print ('')
	print ('  - n = number of spaces for indentation (optional, default: %s)' % (parameters['indent']))
	print ('  - key sorting is false if x = (%s), else true (optional, default: %s)' % ('|'.join(false_vals), parameters['sort']))
	print ('')
	sys.exit( -1 )

# Get any key=val pairs from command line
for arg in sys.argv[1:]:
	toks = arg.split( '=' )
	if len(toks)<2: continue
	parameters[ toks[0].lower() ] = toks[1]

# Ensure specific command line parameters are correct type
for key,val in parameters.items():
	if isinstance(val,str) and (key in converters): parameters[key] = converters[key](val)

# Get input JSON data from stdin, or specified input file
if (sys.stdin.isatty()==False):
	lines = sys.stdin.readlines()
else:
	if 'input' not in parameters: printUsage( sys.argv[0] )
	lines = open( parameters['input'], "r" ).readlines()

# Prettify JSON, send to stdout
parsed = json.loads( ''.join(l for l in lines) )
print (json.dumps(parsed, indent=parameters['indent'], sort_keys=parameters['sort']))
