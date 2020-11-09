#! /usr/bin/python3
#
# MIT License
#
# Copyright (c) 2020 Cyril MORISSE (@cmorisse)
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
import gettext
import os
import json
import pkg_resources

warning_messages = []
def warn(out):
    warning_messages.append(out)

try:
    import ufw.util
    ufw.util.warn = warn  # monkey patch 'warn' to avoid garbage in console output.
    import ufw.frontend
    import ufw.common
    import ufw.parser
except:
    print("Error: ufw must be available. Aborting")
    sys.exit(126)
gettext.install(ufw) 

__version__ = '0.1'

ufw_frontend = ufw.frontend.UFWFrontend(dryrun=False)
ufw_backend = ufw_frontend.backend

def _is_active():
    for direction in ["input", "output", "forward"]:
        (rc, out) = ufw.util.cmd([
            ufw_backend.iptables, 
            '-L', 
            'ufw-user-%s' % direction, 
            '-n'
        ])
        if rc == 1:
            return False
        elif rc != 0:
            raise ufw.common.UFWError("iptables: %s\n" % out)
    return True

def get_rules_as_dict():
    """ Returns all attributes of all rules as a list of dict """
    all_rules = ufw_backend.get_rules()
    all_rules_dict = []
    rule_number = 1
    for rule in all_rules:
        rule.number = rule_number
        rule.command = ufw.parser.UFWCommandRule.get_command(rule)
        rule_dict = {attrname: rule.__dict__[attrname] for attrname in rule.__dict__.keys()}
        all_rules_dict.append(rule_dict)
        rule_number += 1
    return all_rules_dict

def get_ufw_version():
    try:
        version = pkg_resources.get_distribution('ufw').version
    except:
        version = None
    return version


if __name__ == '__main__':
    rdl = get_rules_as_dict()
    output = {
        "ufw_get_status_json_version": __version__,
        "ufw_version": get_ufw_version(),
        "ufw_active": _is_active(),
        "rules": rdl,
        "warnings": warning_messages
    }
    print(json.dumps(output, indent=4))