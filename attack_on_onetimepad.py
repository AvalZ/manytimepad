# Comportamento normale del One-Time Pad:
#
# Genero un pad da 4096 bit
# Dopo aver generato il messaggio, lo cifro col pad e invio.
# 
# PROBLEMA: se non modifico il pad ogni volta, il One-Time Pad diventa attaccabile.
#
#### MANY TIME PAD
# c1 ^ c2 = m1 ^ pad ^ m2 ^ pad = m1 ^ m2
#
# Alice e Bob stanno usando il protocollo per scambiarsi dei messaggi.
# I messaggi sono solo lettere e spazi, codificati in ASCII
#
#   base        10      2
# Spazio        32      00100000
#   A           65      01000001      
#   B           66      01000010
#   a           97      01100001
#
#
#  Costriuiamo la tabella degli XOR:
#
#          +--------+-------+-------+
#          | Spazio |  A-Z  |  a-z  |
# +--------+--------+-------+-------+
# | Spazio |    0   |  a-z  |  A-Z  |
# +--------+--------+-------+-------+
# | A-Z    |   a-z  | < 32  | 32-63 |
# +--------+--------+-------+-------+
# | a-z    |   A-Z  | 32-63 | < 32  |
# +--------+--------+-------+-------+
#
# Sapendo questo, poniamo che c1^c2 = A!b@0
# A vuol dire che m1^m2 aveva spazio+a al primo posto, e così via
#
#
# Avendone tanti, posso fare
#       m1^m2
#       m1^m3
#       m1^m4
# eccetera, finchè non esce una lettera su una colonna
#
# se faccio c1^c7
# Se esce una lettera, devo sapere se metterlo in C1 o C7
#  Dove è lo spazio? Conto quante lettere escono con c1^tutti gli altri, conto quante volte escono le lettere.
#  se ne escono di più in c1, assumo che sia in m1, altrimenti è in m7.
# Scelto lo spazio, possiamo decodificare tutta la colonna perchè abbiamo ottenuto il PAD di quella posizione.
#
#

