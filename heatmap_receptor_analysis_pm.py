import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

df = pd.ExcelFile(r'/Users/karolina/Desktop/output-number.xlsx')
sheets = ['exp1', 'exp2', 'exp3']
for sheet in sheets:
    new_df = pd.read_excel(df, sheet, index_col="Receptor")
    new_df = new_df.fillna(0)
    fig, ax = plt.subplots(figsize=(11, 7))
    ax.figure.subplots_adjust(left=0.4, bottom=0.2)
    sb.heatmap(new_df, cmap="Oranges", annot=True, cbar_kws={'label': 'Number of significant matches'},)
    ax.figure.axes[-1].yaxis.label.set_size(12)
    plt.title('Cytokine receptors enriched on the plasma membrane', y=1.04, fontsize=14)
    plt.ylabel('Receptors', fontsize=12)
    # plt.show()
    # name = r'/Users/karolina/Desktop/'+str(sheet) + '.tiff'
    # plt.savefig(name)