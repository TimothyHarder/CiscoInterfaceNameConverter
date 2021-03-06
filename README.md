# Cisco Interface Name Converter

Written because some Cisco CLI commands output a short version of the interface name, and some
output a long version of the interface name. I needed a way to consistently map this relationship,
and since I couldn't find something like this online, I decided to share the knowledge with the
community.

You can use the interface_abbreviations dictionary in your own code, or use the
supplied convert_interface method to convert interface names.


> ### Getting started
> 
> > from CiscoInterfaceNameConverter import converter
> >converter.convert_interface(
> >- interface_name="GigabitEthernet1/0/1" **(REQUIRED)**
> >- return_short=False *(Optional)*
> >- return_long=False *(Optional)*
> >- simple_mode=True *(Optional)*
> >- silent=False *(Optional)*
> >
> >)
> 
> This will convert the interface name to the opposite of whatever you passed into
> the function.
> 
> You can force the return of the short or long version of the interface name.
> I tend to do this to all interfaces, even if I know it's already in one form. That way it's always consistent.
> 
> Simple mode will use a string slicing method to convert the long to short if the name doesn't
> match any known abbreviations.
> 
> Silent will disable output to stdout when names don't match.
> 
> If you don't want to use the converter function, feel free to just take the dictionary.
> 
> >from CiscoInterfaceNameConverter.converter import interface_abbreviations
> 
> This dictionary has the long form as the key and the short form as the value.

## Contributing
If suggesting a new abbreviation get added to the dictionary, please do so in a pull request.
Please attach screenshots of the output from the Cisco device showing both the long and short versions
of the interface name.