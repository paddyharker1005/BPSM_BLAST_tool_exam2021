# BPSM_BLAST_tool_exam2021

A Python3 BLAST programme created for the 3 hour BPSM course exam capable of performing all components of a BLAST analysis.

## The programme:
1. Provides the opportunity for the user to specify their own fasta sequences for creating a BLAST database.

2. Has the flexibility of producing either a nucleotide or protein database to search against and allows the user to perform multiple types of BLAST searches (nucleotide-nucleotide, protein-nucleotide, protein-protein etc.) based on the type of database created.

3. Provides the user with an option to have a preview of the top 10 HSPs from the BLAST search, which is useful for preliminary analysis or if the user wants to check their search was completed as intended.

4. Has numerous in-built error traps to prevent the user from providing incorrect inputs and breaking the programme. In some cases, the error traps simply ask for new input, but where this is not possible, the user is presented with an error message and the programme terminates gracefully.
