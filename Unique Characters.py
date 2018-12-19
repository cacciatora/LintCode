class Solution:
    """
    @param: str: A string
    @return: a boolean
    """
    def isUnique(self, str):
        str_list = list(str)
        str_set = set(str_list)
        if len(str_list) == len(str_set):
            return True
        else:
            return False