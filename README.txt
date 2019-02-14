Setup:

Install Python 3

Install pip3

Install cryptography using pip

Might need to do chmod +rwx encryption_demo.py

--------------------------------------- Key Generation Instructions ----------------------------------

You can either use the examples at the bottom of this file or follow the directions to generate your 
own encryption keys.

For rotational encryption the only thing required is a number from 1 to 25.

For map encryption, what is needed is a 26 character long string with one of each alphabetic character 
in it in any order.

For symmetric key encryption, run the program make_sym_key.py to get a randomly generated symmetric key.

For asymmetric key encryption, run the program make_asym_keys.py to get a randomly generated private 
key with a corresponding public key.

------------------------------------------ Premade Examples --------------------------------------------

Map Example: newjobfixmrgluckshazytvpdq

Map Example(which is the same as rotation 7) : hijklmnopqrstuvwxyzabcdefg

Symmetric key example: kRLOD0MLI7aNdHSbSY6V0RY4lGSNIPEIwWqQShWVV-w=

Asymmetric Key Example

Bob's Private Key
-----BEGIN RSA PRIVATE KEY-----
MIIEDAIBAAKB4QC8I+2h2HbP10VZM450joqFi4mdcKaxFCNyLEHl5u6bYVfBDI3Y
wK1CwZj9098YqMEOoZWwnW474e+ToKRrGBIFQapvZPupJ/TjKewOGIuFvb2bqBXn
/Vv245zI3ttPFYSqKhQDPoG5XAquyWtvtCMDfYRiwAg0aZYYIRv6RFSNwAkA6fYa
OKrJn2ChVymYGcgwXWL+aWYTJcdoHzG5DHUE77dhwXwCj90mfR7q/rbJIKuCx7R+
7vM9Z1lfBIWB+bONWtk+noXah4CNf4D+EbpOi6feDv49Vp9zpIqwei2PBwIDAQAB
AoHgZz/YY5+l5H4hYsi2fyTSxGNFjI+MC1Yf9cJwD7libQdI33sCRVfIPgB885/Y
qXHDMUJgIeLj4h0mG4BnexZknVniLOvgaH6zGA+jqkCyIR119vyRuRUD6UQUgPA8
rvQCMFiTTwx4qL7oZe/H9C+JnqkhFl1/aAQKYAlNtdtVNn8yjFblwsY7lgmKaQL1
fr571hzh48xhw/hXHOIK+gmJZ3sqHR4MjrNkUwug6CDog9Vj/998DLQ477luuGY1
t7vMBprHrsEfYFoso7bNvrNW4mR6EleJjGkfIS8FCiTJFQECcQDLCEPZoZ7BQNAM
tG+rQewo/2760IDKFAy88siM/X215mcnZARabBmhMub8mc8vTSLXTosi7V2N+KzP
AVD1GpDzV9TBh7OPUT2WzFFn44S6tZSNwyKVH4oJy43oGNevWUG95EjzcpNNrmf6
2xF8MWNHAnEA7TkWqulXuNujIiEjRJ6DGCIZ9by947tHY7bX6V+Niul7tPMdFy3n
ZSd+Q/of9K1V12006k64mJV+IuB9XkPhwMRRT5a/yKbh6si+mOb2IbYFnyj5n5XE
AKAZ6sn7IO0scKGGYGAz/O4RcQMiKSrWQQJxALKmtCVU3H+KC0eSocwc9rPgh4P1
Yc3utIKyUxwUlcAwW8ZCcL4r7qV0R+IvaSpjAmxX9YAnQzIAhfakXts9pBwrxc8B
HFPYlYwSfvMeNRWhX3UaJlz3YpxZ26VF7suhi4KO1E47HDi3ZVFL4GfagVMCcDfX
P2m+AeNG+HC5QjcN5SgSJvA8nKp11Ek5qjuKPaRcb71ZmRhyusyJ7mQMBeevwcwz
LciV/UgVsJp/I6PD8OlSjR1iDAUsm3OMC6msfHXVBh/AInqZY4kOJuuo3g+TJOni
a+JV4wb/92UV6r2sEsECcH+QIqP77/+Y7mKvYAjyHOTCMC65wKE4XyrZ89UA92cT
RP0e/gteukv1GFUkHjK3u3jDJomcT21CQHiz13Eo5UuFDBewR1V+Br24uBxcyCBJ
NEk50Re9PpHTCc6MoJpWCEEWZ8HMsrg2+FQOI8QrJAQ=
-----END RSA PRIVATE KEY-----

Bob's Public Key
-----BEGIN PUBLIC KEY-----
MIH/MA0GCSqGSIb3DQEBAQUAA4HtADCB6QKB4QC8I+2h2HbP10VZM450joqFi4md
cKaxFCNyLEHl5u6bYVfBDI3YwK1CwZj9098YqMEOoZWwnW474e+ToKRrGBIFQapv
ZPupJ/TjKewOGIuFvb2bqBXn/Vv245zI3ttPFYSqKhQDPoG5XAquyWtvtCMDfYRi
wAg0aZYYIRv6RFSNwAkA6fYaOKrJn2ChVymYGcgwXWL+aWYTJcdoHzG5DHUE77dh
wXwCj90mfR7q/rbJIKuCx7R+7vM9Z1lfBIWB+bONWtk+noXah4CNf4D+EbpOi6fe
Dv49Vp9zpIqwei2PBwIDAQAB
-----END PUBLIC KEY-----

Sally's Private Key
-----BEGIN RSA PRIVATE KEY-----
MIIEDAIBAAKB4QDA7ONTPnokrnysfaUJ0BYpEofpKIUmjOOdM+3ZKY1Qktcgtv/m
wAAP+Azzwfl4RPUsPBTwemy6EA7lnzdFi1ukhCV3yMD7jyKd6eU+GwHATmlEoU3B
dfK8s9VRUd+y+QTt/DQeBeqp9GqKcYA0xWlmD1p8mg0RG4lbtcvt0YF4pWb9veWh
7aEwhHWynTbTLrFG7CzuMAQZPtwzN/IlHZTrvOPy3Nv1/+q/ZMpMuA8uEYB3geLd
aut2y+90Q+2tvFr0sLwq3H4/d8wqSgAf5GzNPZywBy6HEv7ialWJHy9BpwIDAQAB
AoHgPPrjg81suCl6+N6iCu7+Ai98TCNlquC/lVHzrT+oDj7LxuhxDJPFsUZ7eZTn
cK+DO18mUzivI0SuIMBprQ62gdLPMQSAk0MT8wwaTL4mmI1wUqQVur+4YRMKqzCQ
37Y8a6jbJF5EZUH/ZxEnMAbyICYIVtdvLP7u3rPuh0vP5DDE8DhppmxBCQ0v3GPf
NXg4FOMJnaRpZQ4Df/jLbUST5B6ZSTeZjXg6aK1XljYaLvBv1ZCMWdj2RBO5XDr/
IplAlTtsng+25yPoJGiencQee0b0hT2sErBlCwzq+u6oxtECcQDHRjmzNc0SWVDo
VS6EU9xgzGyN30UPcY7+mk6enuRkMNIErQ0/t/jb3mTgYmjQqwtOopS+C3TFy2Z3
dnPjlkIZADzzWkBZpVaUzaZr0AKpTS1FbMx3mTetIROc+avBkk9EEvhjbtEBSHJ4
08S3xdaJAnEA99f98h+qx9OrUDLGPhlOTehshDkLtnxiSIMSYmDlw6YGNeGfozsw
pSApd7y+SkEtv/Z0XdTtnHIcgsvv5OqOCm94k+xAtfheGvZabTaGjRniT35cZn1C
rkpYQFv63lMBGidbJgZrmvQmCredG/5KrwJwDnYWMd8xpqc8q9+ipI/BanTrW9Bc
HqbLDcb89Z3qTSsN0rEMSRd8w9f70hzSJnKDO42o5bHHI6ODKCA8gMOiwFW4FqDy
Eo9hHSNfdGuABfFH28XtgLBpzfKcjcPApyeLARGvXOfp2wH67LHRkNSWoQJwCOUH
iBj62BEQpOAtnSzrUoB05InnkbUFEfUiQ8WWeV8L+gMO55zIMiTlWBa9/Yw5SBpg
Mr3hiSvPOiJ3iY+haV52xVhFOkKfnfgZZrH+QjIbnR670jHMotSoNicW6cOw1m9z
Jfo1AmqgsuHEEa0eoQJxAIN5BS+h91tmuxSPI+SQ3S8q/ebK2bsXLwcul+3vIZwn
LL0fDTY5FlLNe2oZpdE84o8sVOephqNUh7sPN4iahHftK5d2u/BTS4n6bmtIhdAc
4mveNopikrSQqPXvGSAQ7uGkAi7Se+3eFFLEl4mjZiI=
-----END RSA PRIVATE KEY-----

Sally's Public Key
-----BEGIN PUBLIC KEY-----
MIH/MA0GCSqGSIb3DQEBAQUAA4HtADCB6QKB4QDA7ONTPnokrnysfaUJ0BYpEofp
KIUmjOOdM+3ZKY1Qktcgtv/mwAAP+Azzwfl4RPUsPBTwemy6EA7lnzdFi1ukhCV3
yMD7jyKd6eU+GwHATmlEoU3BdfK8s9VRUd+y+QTt/DQeBeqp9GqKcYA0xWlmD1p8
mg0RG4lbtcvt0YF4pWb9veWh7aEwhHWynTbTLrFG7CzuMAQZPtwzN/IlHZTrvOPy
3Nv1/+q/ZMpMuA8uEYB3geLdaut2y+90Q+2tvFr0sLwq3H4/d8wqSgAf5GzNPZyw
By6HEv7ialWJHy9BpwIDAQAB
-----END PUBLIC KEY-----