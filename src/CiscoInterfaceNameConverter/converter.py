"""
Cisco Interface Name Converter

Written because some Cisco CLI commands output a short version of the interface name, and some
output a long version of the interface name. I needed a way to consistently map this relationship,
and since I couldn't find something like this online, I decided to share the knowledge with the
community.

Happy Automating!

Author: Timothy Harder
"""

# Standard Imports
import re

interface_abbreviations = {
        'Ethernet': 'Eth',
        'FastEthernet': 'Fa',
        'GigabitEthernet': 'Gi',
        'TwoGigabitEthernet': 'Tw',
        'FiveGigabitEthernet': 'Fi',
        'TenGigabitEthernet': 'Te',
        'TenGigE': 'Te',
        'TwentyFiveGigE': 'Twe',
        'FortyGigabitEthernet': 'Fo',
        'HundredGigE': 'Hu',
        'Port-channel': 'Po',
        'Loopback': 'Lo',
        'Tunnel': 'Tu',
        'mgmt': 'mgmt',
        'Embedded-Service-Engine': 'Em',
        'Bundle-Ether': 'BE',
        'Null': 'Nu',
        'tunnel-ip': 'ti',
        'MgmtEth': 'Mg',
        'Vlan': 'Vl',
        'GMPLS': 'GM',
        'pseudowire': 'pw',
        'BDI': 'BD',
        'LISP': 'LI',
        'nve': 'nv',
        'AppGigabitEthernet': 'Ap',
        "fc": "fc",  # Fiber Channel, couldn't find any "long version" of this interface type.
        "ucse": "uc",
        "Virtual-Access": "Vi",
        "Dialer": "Di",
}


def convert_interface(interface_name, return_short=False, return_long=False, simple_mode=True, silent=False):
    """
    Converts the interface name into the opposite version of the interface name.
    Ex. GigabitEthernet1/1 will return Gi1/1
    Ex. Gi1/1 will return GigabitEthernet1/1

    :param interface_name: Interface name to convert
    :param return_short: BOOL to force short return
    :param return_long: BOOL to force long return
    :param simple_mode: BOOL. Will allow the function to shorten the name of the interface by using a dissection
        if the interface type isn't found.
    :param silent: BOOL. Will disable output to stdout.
    :return: string of converted interface name
    """

    # If the interface name isn't a string, it's not something we can convert.
    if type(interface_name) != str:
        return interface_name

    # If the interface name is an inherently falsey object, we can't convert it.
    if not interface_name:
        return interface_name

    # If you've asked for both the long and short version of the interface name, you deserve
    # this error.
    if return_short and return_long:
        return AttributeError("Can't return both the long and short interface names.")

    # Regular Expression to separate the first part of the name from the numbers of the interface.
    interface_regex = r'^([^\d]+)(\d+.*)$'

    match = re.match(interface_regex, interface_name)
    if not match:
        if not silent:
            print(f'{interface_name} does not seem to follow typical Cisco interface naming standards.')
        return interface_name

    interface_type = match.group(1)
    interface_number = match.group(2)

    # Searching the interface abbreviation dictionary.
    for long, short in interface_abbreviations.items():
        if long.lower() == interface_type.lower():
            if not return_long:
                return short + interface_number
            else:
                return interface_name

        if short.lower() == interface_type.lower():
            if not return_short:
                return long + interface_number
            else:
                return interface_name

    if not silent:
        print(f"The interface {interface_name} does not match any known cisco interface abbreviations.")

    if simple_mode:
        if len(interface_type) > 3:
            if return_long or not return_short:
                return interface_name
        else:
            if return_short or not return_long:
                return interface_type[:2] + interface_number

    # Catchall to return the user's interface name if we weren't able to convert it.
    return interface_name
