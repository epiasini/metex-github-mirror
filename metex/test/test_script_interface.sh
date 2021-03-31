#! /bin/bash

# Copyright (C) 2021 Eugenio Piasini.
#
# This file is part of metex.
#
# Metex is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Metex is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
# or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public
# License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Metex. If not, see <https://www.gnu.org/licenses/>.

tfile=$(mktemp)
metex --prefix $tfile. 10 && test -f $tfile.0.png && rm $tfile.0.png
