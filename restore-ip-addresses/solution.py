class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        poss_first_dot = []
        poss_sec_dot = []
        poss_third_dot = []
        allowed_ips = []
        length = len(s)

        for i in range(1, 4):
            if 3 <= length - i <= 9:
                poss_first_dot.append(i)
        #25525511135
        for i in range(2, 7):
            if 2 <= length - i <= 6:
                poss_sec_dot.append(i)

        for i in range(3, 10):
            if 1 <= length - i <= 3:
                poss_third_dot.append(i)

        # print(length)
        # print(poss_first_dot)
        # print(poss_sec_dot)
        # print(poss_third_dot)
        # return

        for i in poss_first_dot:
            # print("i is " + str(i))
            # print("first " + s[:i])
            if int(s[:i]) > 255:
                continue
                
            if len(s[:i]) > 1 and s[:i][0] == "0":
                continue
                
            for j in poss_sec_dot:
                # print("j is " + str(j))
                # print("second " + s[i:j])
                if i >= j or int(s[i:j]) > 255:
                    continue
                if len(s[i:j]) > 1 and s[i:j][0] == "0":
                    continue

                for k in poss_third_dot:
                    # print("k is " + str(k))
                    # print("third " + s[j:k])
                    # print("fourth " + s[k:])
                    if j >= k or int(s[j:k]) > 255 or int(s[k:]) > 255:
                        continue
                    if len(s[j:k]) > 1 and s[j:k][0] == "0":
                        continue
                    if len(s[k:]) > 1 and s[k:][0] == "0":
                        continue


                    allowed_ips.append(s[:i] + "." + s[i:j] + "." + s[j:k] + "." +s[k:])


        return allowed_ips
