__author__ = 'pavang'
__Date___ = ''


class dummy:
    a = 1



if __name__ == '__main__':
    d1 = dummy()
    d2 = dummy()
    dummy.append_new = "New Attribute Appended"


    d1.add_new = "added"
    print(d1.a)
    print(d1.add_new)
    print(d1.append_new)

    print(d2.a)
    # print(d2.add_new)                 # Won't Print because add_new
                                        # is part of d1 namespace not d2
    print(d2.append_new)




    print("\n\nPrinting Namespaces\n\n")
    print("d1--> " + str(d1.__dict__))
    print("d2--> " + str(d2.__dict__))
    print("dummy--> " + str(dummy.__dict__.keys()))
