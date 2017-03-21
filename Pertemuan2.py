graph = {'Sarijadi': ['Sari Endah', 'Sarirasa'],
             'Sarirasa': ['Surya Sumantri'],
             'Surya Sumantri': ['Dr Djunjunan', 'Sukahaji'],
             'Sukahaji': ['Prof Dr Sutami'],
             'Prof Dr Sutami': ['Sindang Sirna'],
             'Sindang Sirna': ['Sukaresmi'],
             'Sukaresmi': ['Jurang'],
             'Jurang': ['Cipaganti'],
             'Cipaganti': ['Cihampelas'],
             'Cihampelas': ['Ir H Djuanda'],
             'Ir H Djuanda': ['Dago'],
             'Dr Djunjunan': ['Layang Pasupati'],
             'Layang Pasupati': ['Taman Sari'],
             'Taman Sari': ['Ir H Djuanda'],
             'Sari Endah': ['Gegerkalong'],
             'Gegerkalong': ['Setiabudhi'],
             'Setiabudhi': ['Sukawangi'],
             'Sukawangi': ['Cipaganti']
        }
def mencari_jalur_terpendek(graph, jalanawal, jalantujuan, jalur=[]):
        jalur = jalur + [jalanawal]
        if jalanawal == jalantujuan:
            return jalur
        if not graph.has_key(jalanawal):
            return None
        jalurpendek = None
        for node in graph[jalanawal]:
            if node not in jalur:
                newjalur = mencari_jalur_terpendek(graph, node, jalantujuan, jalur)
                if newjalur:
                    if not jalurpendek or len(newjalur) < len(jalurpendek):
                        jalurpendek = newjalur
        return jalurpendek
print("Jalur Jalan Raya Kota Bandung")
print("(Sarijadi,Sari Endah,Gegerkalong,Setiabudhi,Sukawangi,Cipaganti,Cihampelas)")
print("(Sarirasa,Surya Sumantri,Dr Djunjunan,Layang Pasupati,Taman Sari)")
print("(Sukahaji,Prof Dr Sutami, Sindang Sirna,Sukaresmi,Jurang,Ir H Juanda)")
print("\n")
jalanawal = raw_input("Masukan jalanawal : ")
jalantujuan = raw_input("Masukan jalantujuan : ")
hasil = mencari_jalur_terpendek(graph, jalanawal, jalantujuan, jalur=[])
print "Jalur Terpendek", hasil
