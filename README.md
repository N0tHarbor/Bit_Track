# Bit_Track
Project to track Crypto Transaction Hops using API's &amp; Python3
- Created for a MSU Denver Term Paper to watch of how money was launder in the WannaCry ransomware attack.

[+] APITest.py - Full bitcoin transaction tracker that uses the "hxxps[://]blockchain[.]info/rawaddr/" API. Currently has a bad check for next hop which results in ocassional loops on transactions since the rand function is used and I didnt sort the data properly. Will update one day but probably not any time soon!

[+] BitFind.py - Suposed to be the MAIN driver of the tool but I ran out to time in my term paper and had to cut the tools productions short. Was suposed to implement cmd-line flags and unify the project to just run from here. NOT FINISHED. 

[+] Test_Out.py & Tans.py - Tesing the ingestion on the API and how to manip it the way I wanted to with out effecting the main code source. Also nice to see what data the API will give. 

[+] mon_send - A file containing either the WannaCry public address or one of my old Public Addresses.
