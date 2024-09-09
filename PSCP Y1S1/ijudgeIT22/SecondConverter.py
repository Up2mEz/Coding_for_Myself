""" secondconverter """
def converter():
    """ calculate time """
    time = int(input())
    sh = int(input())
    mh = int(input())
    hh = int(input())
    day = time>=(hh*mh*sh)
    update = time
    if day:
        update = time-(time//(hh*mh*sh))*(hh*mh*sh)
    hour = update//(mh*sh)
    update = update-(hour*(mh*sh))
    minute = update//sh
    update = update-(minute*sh)
    print(f"{hour}:{minute}:{update:}")
converter()
