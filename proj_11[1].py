print("name:amrutha;usn:1AY24AI007;SECTION:M")

class Kangaroo:
    def __init__(self, name):
        self.name = name
        self.pouch_contents = []

    def put_in_pouch(self, item):
        self.pouch_contents.append(item)

    def __str__(self):
        contents = []
        for item in self.pouch_contents:
            if isinstance(item, Kangaroo):
                contents.append(f"{item.name} (Kangaroo)")
            else:
                contents.append(str(item))
        contents_str = ', '.join(contents) if contents else 'empty'
        return f"{self.name}'s pouch contains: {contents_str}"

kanga = Kangaroo("Kanga")
roo = Kangaroo("Roo")

kanga.put_in_pouch(roo)

roo.put_in_pouch("baby bottle")
roo.put_in_pouch("stuffed toy")

print(kanga)
print(roo)
