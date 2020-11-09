class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        if capacity < MIN_CAPACITY:
            capacity = MIN_CAPACITY
            return
        else:
            self.capacity = capacity
            self.hash_table = [None] * capacity
            self.count = 0
        


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.count / self.capacity #total number of items / table size


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        # hash = 14695981039346656037 # offset_basis
        # for s in key:
        #     hash = hash * 1099511628211 # FNV_prime
        #     hash = hash ^ ord(s)
        # return hash % len(self.array)

        """ If I'm being honest here, DJB2 looks a lot cleaner and a lot easier of a number to memorize"""


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        for x in key:
            hash = (( hash << 5) + hash) + ord(x)
        return hash

        """ This function is based off of integer arithmatic using the string values.
        So what does it do? and why 5381. Well, It's a prime number and it works pretty darn well.
        Why 33? No clue. """


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        i = self.hash_index(key)
        # entry = HashTableEntry(key, value)

        if self.hash_table[i] is None:
            self.hash_table[i] = HashTableEntry(key, value)
            self.count += 1
            return

        else:
            curr = self.hash_table[i]
            if curr.key == key:
                curr.value = value
            else:
                entry = HashTableEntry(key, value)
                entry.next = curr
                self.hash_table[i] = entry
                self.count += 1

        load_factor = self.get_load_factor()
        if load_factor > .7:
            self.resize(int(self.capacity * 2))

        # node = self.hash_table[i]
        # self.hash_table[i] = entry
        # self.hash_table[i].next = node
        # self.count += 1


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        i = self.hash_index(key)
        curr = self.hash_table[i]
        prev = None

        if curr.key == key:
            self.hash_table[i] = curr.next
            return
        while(curr is not None):
            if curr.key == key:
                pre.next = curr.next
                self.hash_table[i].next = None
                return
            else:
                prev = curr
                curr = curr.next
            self.count -= 1
            load_factor = self.get_load_factor()
            if load_factor > .2:
                self.resize(self.capacity //2)
            return


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        entry = self.hash_table[index]


        while entry:
            if entry.key == key:
                return entry.value
            entry = entry.next
        return entry


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        temp_hash_table = self.hash_table
        self.capacity = new_capacity
        self.hash_table = [None] * new_capacity
        self.count = 0

        for entry in temp_hash_table:
            curr = entry
            while curr:
                self.put(curr.key, curr.value)
                curr = curr.next



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
