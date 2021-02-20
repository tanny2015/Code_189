
#Solution 1
def add_and_check(key, hmap):  # key is char
    if key in hmap:
        hmap[key] += 1
    else:
        hmap[key] = 1

    if hmap[key] > 1:
        return False  # has duplicate
    else:
        return True  # unique


def check_duplicate(str):
    hmap = dict()
    for ch in str:
        if add_and_check(ch, hmap):
            continue
        else:
            print("not all unique1！ \n")
            #break
            return False
    print("all unique! \n")
    return True

#check_duplicate("hkhkjhkjhkj")
#check_duplicate("hkdqe")



class Solution(object):
    def add_and_check(self, key, hmap):  # key is char
        if key in hmap:
            hmap[key] += 1
        else:
            hmap[key] = 1

        if hmap[key] > 1:
            return False  # has duplicate
        else:
            return True  # unique


    def isUnique(self, astr):
        hmap = dict()
        for ch in astr:
            if self.add_and_check(ch, hmap):
                continue
            else:
                print("not all unique1！ \n")
                #break
                return False
        print("all unique! \n")
        return True
















