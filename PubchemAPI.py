#!/usr/bin/env python

import sys
import pubchempy as pcp

smiles=str("CCCCCOC")
print(smiles)
s=pcp.get_compounds(smiles,'smiles')
print(s[0].synonyms[2])
