import os
import pandas as pd
import glob
from sklearn.model_selection import train_test_split

data_dir = 'data/custom/images/*.jpg'

test_size = 0.2

if __name__ == '__main__':
    newdf = pd.DataFrame(columns=['image'])
    files = glob.glob(data_dir)
    for f in files:
        newrow = [f]
        newdf.loc[len(newdf)] = newrow
    newdf.head()
    train_df, val_df = train_test_split(
        newdf,
        test_size=test_size,
        random_state=13579
    )
    print('train:', len(train_df), 'test:', len(val_df))
    train_df.to_csv('data/custom/train.txt', index=False, header=False)
    val_df.to_csv('data/custom/valid.txt', index=False, header=False)
