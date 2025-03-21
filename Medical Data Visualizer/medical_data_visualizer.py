import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv("medical_examination.csv")

# 2
df['overweight'] = (df['weight'] / (df['height'] / 100) ** 2 > 25).astype(int)

# 3
df['cholesterol'] = df['cholesterol'].replace([1, 2, 3], [0, 1, 1])
df['gluc'] = df['gluc'].replace([1, 2, 3], [0, 1, 1])


# 4
def draw_cat_plot():
    # 5
    df_cat = df.melt(id_vars=['cardio'], value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'], var_name='variable', value_name='value' )



    # 6
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')
    
    

    # 7

    sns.set_theme(style='ticks')


    # 8
    fig = sns.catplot(x='variable', y='total', hue='value', kind='bar', col='cardio', data=df_cat)
    fig.set_axis_labels('Variable', 'Total')
    fig.set_titles('Cardio: {col_name}')




    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[(df['height'] >= df['height'].quantile(0.025)) & ((df['height'] <= df['height'].quantile(0.975))) & (df['weight'] >= df['weight'].quantile(0.025)) & ((df['weight'] <= df['weight'].quantile(0.975)))] 
    df_heat.reset_index()

    # 12
    corr = df_heat.corr()
    annot_array=np.round(corr, decimals=1)

    # 13
    mask = np.triu(corr)

    # 14
    fig, ax = plt.subplots()

    # 15
    sns.heatmap(corr, annot=annot_array ,fmt=".1f", mask=mask, center = 0, vmin=-0.08, vmax=0.24, cbar_kws={'shrink': 0.5, 'extend':'both', 'extendrect':'true', 'ticks': [-0.08, 0.00, 0.08, 0.16, 0.24]})

    # 16
    fig.savefig('heatmap.png')
    return fig
