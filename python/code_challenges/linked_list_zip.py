def zip_lists(a, b):
    current1 = a.head
    current2 = b.head
    while current1 and current2:
      temp1 = current1.next
      temp2 = current2.next
      current1.next = current2
      current2.next = temp1
      current1 = temp1
      current2 = temp2
    b.head = current2
    return a
