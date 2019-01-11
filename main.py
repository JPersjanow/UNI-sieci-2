import struct
import binascii
import random

class sieci:
    def __init__(self):
        a = 5

    def open_file(self,filename):
        with open(filename,'br') as f:
            data = f.read()
        print("entered data:")
        print(binascii.hexlify(data))
        print("")

        f.closed
        return data

    def cut_file(self,x):

        info = [x[i:i+2] for i in range(0, len(x), 2)]

        print("cut data:")
        print(info)
        print("")


        return info

    def structure(self, data):


        format ='2h'
        structs = []
        package = []
        x = 0

        for i in data:
            i = struct.pack(format,*i)
            structs.append(i)

        for i in structs:
            # i.pack(*data)
            package.append([x, i, len(i)])
            x = x + 1

        print("package [id, struct, size]")
        print(package)
        print("")

        # rand = random.randint(0,len(structs) - 1)
        # # print(rand)

        return package

    def transfer(self,list):
        transfered = []

        for i in range(len(list)):
            element = random.choice(list)
            list.remove(element)
            transfered.append(element)

        print("transfered file:")
        print(transfered)
        print("")
        return transfered


    def sort(self,list):

        sorted_list = sorted(list, key=lambda x: x[0])
        print("sorted file:")
        print(sorted_list)
        print("")

        return sorted_list

    def unpack(self,list):

        structs = []
        # x = struct.Struct("hhl")
        # x.unpack_from()
        offset = 0

        for i in list:
            structs.append(i[1])

        print(structs)

        for i in structs:
            unpacked = struct.unpack("2h",i)

        print(unpacked)










s = sieci()
dane = s.open_file('test.txt')

# print("cut data:")
dane1 = s.cut_file(dane)
pack = s.structure(dane1)
# print(pack)
trans = s.transfer(pack)
# print(trans)
sort = s.sort(trans)
s.unpack(sort)
# print(sort[0][1])