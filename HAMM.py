str_1 = 'GCCAGCAGCCATTGTGACTCATCCTCGAAAATAACGTGGTTATCCAGGATACGGCCTACAACGCACCGTCATGTGATCCGCGTTCGTCGTGTTTCATTCCGGAGCTCGCCTAGCGTGATGGTTCAGCTCCCTGAGGCCAATCCGTCGGCTTCCCGTGTAATGAGAATCAAGTAATCAAAAATCTGAAGATCCCCTACAACCCACCCGAGAGGCCTGACTGAAAAAACGGCGAGCGTTTGGACCAAGGAACATGTTCTATGCGTCGGGGGCCAGAAACCATATGGGATCAGGGGTAGAACAATCTAGAGTGTTGGGACAGTTTCACAGCCGTCCTTATGCCAAAGATATGGACCCATGCCTATTCGAAGATCCGATACACCCTATGACTGTGTTATGAGGTGCTTTGGCCCCTTAGCCACATCATTTGCTCGTTTAGCTACTCGACGCTCAGATCAACAAGGAACACACCGTCGAAATCCGAGGTTGCTAAGCAGGTAGTGTCAGACATTCTATGTAGGGAAATCGGTAAAAAACCAAATGCCAGTCCGAACCCGAGTACTCCCTCATACGGGTGAGCTCGTAACTGGTGTCTGACTGGTTTTTAGCCGCAAAGCCGTTGGAGGGCTCGAGGACTGGACCCCCTAACCGAACATATGACTGATCAGATTTCAATGTGCGGACCCTCACTAGGTCCCAATAACCGAGGGGCCAACGCTCAAGGGTTGGGGAAGGGATCCACACTAATGCCATATGGATTTTCTAGGTTAGAATCTAACACTCAAAATGCCTTAGTCCGTTCAACGTCAGTGGTAGCTATCCTTAGTGTGTCAAAGGCTGACCTGGAATTTAGGACTGCGATTTTTAAAGTCATCGAGCATCCGCGGGGTGGCGACTGGCCATCCGTCATTATACCAGACATTGTTCACGCGGCGGTTGATCTTTGGTCAAAGCAGCGTGGGTTGCTCCCT'
str_2 = 'ACTAACCGCAACGGTAACACATCGACAGTGGTGACGTAGATTCACAGGTTACATAGGGTAAAGCCCCGTCAGGATACCCGCTCTCTTTACGTTTCATACACCCAAGCGCTTTTTACTATTGGCAAATTGGCCAACGTGACTCGATCTTATCTCAGGAGTAGGGGAATTGAGTAGGCAGAATCCGAAAGACTATCAGTAACGCGCTCGTCAGGCTGGACTGATCCAATGTATTAACGAGTGACGAGGGAGTTTGCTTGTTGAATCGGGGGAACGAAACCACTCAGGTTGGGTCGAAAAACCGTGTCCTCAGGTAATTCCGGTTAAAACACGTCCCATTCTCCAGTATATGGAGCCTCGCGTATACTCCGACCAGCTCCGCCAGCCAAATGAGCTGGAAAGCGGCTCGGCCCGTGAACTCCTTCAAATGGTCTGGCCCCGAGATGCAGTTGAAACAGGCAAGGAAGAAGTAGGAGATATGCCATTCTGCTGAGCACTCCGTGGAAAAGATGCTACGCAGCGAAATAGCTTTAAAGCCAGGGGCCAATCCTCCACTGTGAAATTGCCTGCCGGATTAATCACGAAACTTGCGTGTAAGCTCTTTTTAGTCCCTATGTCGGTCTTAGGTTCCGGGACTAGCGGCGCCGACTGGGCAAATGAGATATCAGAAGGGAAAGTGCATACCGACCCCAGCTTAGAAAAACACGCTCGACTACGTTCCCAGGGCTGGGAGCGGAAGCCGACTAAAGCAATGTGGAATTAATGCGCCTCACTCGAACAGTCGGAATAGTCGCATCCCTTAAGGTTAAGTGGTAGGAATAGCTAGACAAACATCAACTGTCGTTGATTCGAGTAATGGACTTTTCAGAATCATCTTGCACCCTCGTAACCGGTCGAGGCCCCCGTTCCAAGCACCAACTGTTGTTTTGGACTCCGGTCAGCACAGGTCAACGCCACACGCGACTCTCCCG'
count = 0
for i in range(len(str_1)):
    if str_1[i] != str_2[i]:
        count += 1
print(count)