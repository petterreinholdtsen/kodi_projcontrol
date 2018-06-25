# -*- coding: utf-8 -*-
# Copyright (c) 2015 Fredrik Eriksson <git@wb9.se>
# This file is covered by the BSD-3-Clause license, read LICENSE for details.

# Add lib/ext/ to Python search path to find embedded pyserial.
import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), 'ext'))

CMD_PWR_ON="poweron"
CMD_PWR_OFF="poweroff"
CMD_PWR_QUERY="powerquery"

CMD_SRC_QUERY="sourcequery"
CMD_SRC_SET="sourceset"

CMD_BRT_QUERY="brightnessquery"
CMD_BRT_SET="brightnessset"

