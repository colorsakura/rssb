import re


class ParamsMatcher:
    """

    """

    def __init__(self):
        # 配对符号 (元组).
        self.parenthesis = ('(', ')', '[', ']', '{', '}', '【', '】')
        # 配对符号 (字典).
        self.pairs = {'(': ')', '[': ']', '{': '}', '【': '】'}

    def split(self, s):
        """ 将字符串s分割

        :param s:
        :return:
        """
        s = str(s)
        tmp = {}
        for index, c in enumerate(s):
            if c in self.parenthesis:
                tmp

