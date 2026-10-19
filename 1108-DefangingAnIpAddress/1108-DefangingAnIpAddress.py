# Last updated: 19/10/2026, 16:25:17
class Solution(object):
    def defangIPaddr(self, address):
        return address.replace(".","[.]")