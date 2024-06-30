# import libraries

import pandas as pd 
import streamlit as st
import altair as alt
from PIL import Image

# page title

image = Image.open('dna.jpg')
st.image(image, use_column_width=True)

st.write("""
# DNA Nucleotide compition of query DNA!
 
This app counts the nucleotide composition of query DNA!

      
""")

#input

st.header('Enter DNA sequence')

sequence_input = ">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

sequence = st.text_area("Sequence input", sequence_input, height = 250)
sequence= sequence.splitlines()
sequence = sequence[1:]
sequence = ''.join(sequence)

st.write("""
***
""")
# ***adds line

st.header('Input (DNA Query)')
sequence

st.header('OUTPUT (DNA Nucleotide Count)')

## 1.Print Dictionary
st.subheader('1. Print dictionary')
def DNA_nucleotide_count(seq):
    d = dict([
        ('A',seq.count('A')),
        ('T',seq.count('T')),
        ('G',seq.count('G')),
        ('C',seq.count('C'))
    ])
    return d

X = DNA_nucleotide_count(sequence)

# x_label = list(X)
# x_values = list(x.values())

X

## 2. Print text
st.subheader('2. Print text')
st.write('There are ' + str( X['A'] ) + ' adenine (A)')
st.write('There are ' + str( X['T'] ) + ' thymine (T)')
st.write('There are ' + str( X['G'] ) + ' guanine (G)')
st.write('There are ' + str( X['C'] ) + ' cytosine (C)')

## 3. Display DataFrame
st.subheader('3. Display DataFrame')
df = pd.DataFrame.from_dict(X, orient='index')
df
df = df.rename({0: 'count'}, axis='columns')
df
df.reset_index(inplace=True)
df
df = df.rename(columns= {'index':'nucleotide'})
st.write(df)

## 4. Display Bar Chart using Altair

st.subheader('4. Display Bar Chart')
p = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
)

p = p.properties(
    width=alt.Step(80)
)

st.write(p)