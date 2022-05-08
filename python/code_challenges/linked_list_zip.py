def zip_lists(a, b):
    current1 = a.head
    current2 = b.head

    if current1 == None or current2 == None:
        if current2:
            return b
        if current1:
            return a
    while current2 and current1:
        a.insert_after(current1.value, current2.value)
        current1 = current1.next
        if current1.next:
            current1 = current1.next
        current2 = current2.next
    return a





    # current1 = a.head
    # current2 = b.head
    # if current1 == None or current2 == None:
    #     if current1:
    #         return a
    #     if current2:
    #         return b
    # while current1 and current2:
    #   temp1 = current1.next
    #   temp2 = current2.next
    #   current1.next = current2
    #   current2.next = temp1
    #   current1 = temp1
    #   current2 = temp2
    # return a
