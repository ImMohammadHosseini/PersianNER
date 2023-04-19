
"""

"""

import polars as pl

def read_data (self, path):
    list_columns = {'sentence #':pl.Int64, 'word':pl.Utf8, 'label':pl.Utf8} 

    word_df = pl.DataFrame(schema=list_columns)
    #sent_df = pl.DataFrame(schema=list_columns1)
    
    sent_num = 1
    with open(path, encoding="utf-8") as infile:
        for line in infile:
            temp=line.split()
            if len(temp)==2:
                word_df.extend(pl.DataFrame({'sentence #': [sent_num], 
                                             'Word': [temp[0]], 
                                             'label': [temp[1]]}))
            if not temp: sent_num +=1
    sent_df=word_df.groupby('sentence #', maintain_order=True).agg(
        [pl.col("Word").alias("text"),pl.col("label")])
    sent_df.apply(lambda t: (t[0], [' '.join(t[1])], [' '.join(t[2])]))
    return word_df, sent_df