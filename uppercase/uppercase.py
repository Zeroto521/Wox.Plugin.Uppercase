# -*- coding: utf-8 -*-

import copy

import pyperclip

from wox import Wox

from .constants import *


class Main(Wox):

    def query(self, param):
        result = []
        param = param.strip()

        res_format = copy.deepcopy(RESULT_TEMPLATE)

        if param:
            value = str(param).upper()
            res_format['Title'] = "{} -> {}".format(param, value)
            res_format['SubTitle'] = "Click copy to clipboard"

            action = copy.deepcopy(ACTION_TEMPLATE)
            action['JsonRPCAction']['parameters'] = [value]

            res_format.update(action)
        else:
            res_format['Title'] = "Capitalize letters"
            res_format['SubTitle'] = "Follow your words after the keyword."

        result.append(res_format)

        return result

    def copy2clipboard(self, value):
        pyperclip.copy(value)
