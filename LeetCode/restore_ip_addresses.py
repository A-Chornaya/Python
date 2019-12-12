'''
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

Example:
Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]

Note: start with 0 - incorrect
'''


def restoreIpAddresses(s: str):
    len_s = len(s)
    if len_s < 4:
        return []

    result = []
    parts = [3] * 4

    while parts[0] > 0:
        part_1 = s[:parts[0]]
        if int(part_1) > 255 or (part_1[0] == '0' and len(part_1) > 1):
            parts[0] -= 1
            continue

        while parts[1] > 0:
            start_2 = parts[0] + parts[1]
            if start_2 >= len_s:
                parts[1] -= 1
                continue
            part_2 = s[parts[0]:start_2]
            if int(part_2) > 255 or (part_2[0] == '0' and len(part_2) > 1):
                parts[1] -= 1
                continue

            while parts[2] > 0:
                start_3 = parts[0] + parts[1] + parts[2]
                if start_3 >= len_s:
                    parts[2] -= 1
                    continue
                part_3 = s[start_2:start_3]
                if int(part_3) > 255 or (part_3[0] == '0' and len(part_3) > 1):
                    parts[2] -= 1
                    continue

                part_4 = s[start_3:]
                if int(part_4) <= 255 and not(part_4[0] == '0' and len(part_4) > 1):
                    result.append('.'.join((part_1, part_2, part_3, part_4)))

                parts[2] -= 1

            parts[1] -= 1
            parts[2] = 3
            parts[3] = 3

        parts[0] -= 1
        parts[1] = 3
        parts[2] = 3
        parts[3] = 3


    return result

s1 = "25525511135"
ip1 = restoreIpAddresses(s1)
print(ip1)
# ['255.255.111.35', '255.255.11.135']
print('###############')

s2 = "18123503"
ip2 = restoreIpAddresses(s2)
print(ip2)
# ['181.235.0.3', '181.23.50.3', '18.123.50.3']
print('###############')

s3 = "255"
ip3 = restoreIpAddresses(s3)
print(ip3)
# []
print('###############')

s4 = "010010"
ip4 = restoreIpAddresses(s4)
print(ip4)
# ['0.100.1.0', '0.10.0.10']
