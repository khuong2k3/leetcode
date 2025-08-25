import ipaddress

class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        nums = queryIP.split('.')
        if len(nums) == 4:
            try:
                _ = ipaddress.IPv4Address(queryIP)
                return 'IPv4'
            except ipaddress.AddressValueError:
                return "Neither"
        elif len(nums) == 1:
            nums = queryIP.split(':')
            if len(nums) == 8:
                if min(map(lambda n: len(n), nums)) == 0:
                    return "Neither"
                try:
                    _ = ipaddress.IPv6Address(queryIP)
                    return "IPv6"
                except ipaddress.AddressValueError:
                    return "Neither"

        return "Neither"

sol = Solution()
print(
    sol.validIPAddress("2001:db8:85a3:0::8a2E:0370:7334")
)
