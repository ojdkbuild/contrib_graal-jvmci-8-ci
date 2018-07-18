# -*- coding: utf-8 -*-
#
# Copyright 2018, akashche at redhat.com
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import re, sys

if __name__ != "__main__":
    print("ERROR: Invalid non-main usage")
    sys.exit(1)

if 3 != len(sys.argv):
    print("ERROR: Invalid arguments specified")
    print("USAGE: python regex.py <regex> <text>")
    sys.exit(1)

arg_rx = sys.argv[1]
rx = re.compile(arg_rx)
arg_text = sys.argv[2]
mt = rx.match(arg_text)
if mt is None:
    print("ERROR: Text not matched, regex: [%s], text: [%s]" % (arg_rx, arg_text))
    sys.exit(1)

groups = mt.groups()
if 1 != len(groups):
    print("ERROR: Single match group expected, found: [%d]" % len(groups))
    sys.exit(1)

print(groups[0])
sys.exit(0)
