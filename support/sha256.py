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

import hashlib, sys

if __name__ != "__main__":
    print("ERROR: Invalid non-main usage")
    sys.exit(1)

if 2 != len(sys.argv):
    print("ERROR: Invalid arguments specified")
    print("USAGE: python sha256.py <file>")
    sys.exit(1)

sha256 = hashlib.sha256()
filename=sys.argv[1]
block_size=65536
with open(filename, 'rb') as f:
    for block in iter(lambda: f.read(block_size), b''):
        sha256.update(block)

print(sha256.hexdigest())
