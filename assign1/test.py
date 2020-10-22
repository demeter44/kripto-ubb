import assign1.crypto as c

print(c.encrypt_scytale("IAMHURTVERYBADLYHELP", 5))
print(c.decrypt_scytale("IRYYATBHMVAEHEDLURLP", 5))
print(c.encrypt_railfence("WEAREDISCOVEREDFLEEATONCE", 3))
print(c.decrypt_railfence("WECRLTEERDSOEEFEAOCAIVDEN",3))
c.encrypt_scytale_file("not_a_secret_message.txt",5)
c.decrypt_scytale_file("encrypted",5)