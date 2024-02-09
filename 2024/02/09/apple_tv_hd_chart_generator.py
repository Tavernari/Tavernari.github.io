import matplotlib.pyplot as plt

# Updated Data including new categories and results
categories = ['Store Time', 'Retrieve Time', 'Delete Time']

new_data_avg = {
    'GRDB Dequeue Relational': [1.3712650895118714, 0.17592599391937255, 0.13696610927581787],
    'GRDB Pool Relational': [0.07745068073272705, 0.16851660013198852, 0.09169411659240723],
    'GRDB Queue Separated JSON': [1.5054787993431091, 0.049019801616668704, 1.3300469160079955],
    'GRDB Pool Separated JSON': [0.02789628505706787, 0.0538195013999939, 0.05096428394317627],
    'GRDB Queue Unique JSON': [1.5210529923439027, 0.11044330596923828, 1.3433026790618896],
    'GRDB Pool Unique JSON': [0.07977900505065919, 0.10678452253341675, 0.13733960390090943],
    'Separated File Storage': [0.0006147980690002442, 0.31745860576629636, 0.051162219047546385],
    'Unique File Storage': [0.5016327977180481, 0.21079367399215698, 0.567218005657196]
}

# Standard Deviations
new_data_std = {
    'GRDB Dequeue Relational': [0.11664386033448162, 0.004776562578306588, 0.007664486297103074],
    'GRDB Pool Relational': [0.031570518008116416, 0.0033596480458202215, 0.0038529907548512173],
    'GRDB Queue Separated JSON': [0.0736697600239474, 0.002960628440270984, 0.002939381670924807],
    'GRDB Pool Separated JSON': [0.003234126856896667, 0.0066789205800950055, 0.03154474439163905],
    'GRDB Queue Unique JSON': [0.0862286481463726, 0.003460897881870525, 0.002220265749593013],
    'GRDB Pool Unique JSON': [0.002192744778779806, 0.008535974752791522, 0.03450071034607358],
    'Separated File Storage': [5.129028827946028e-05, 0.0010110711248106138, 0.0045830708822261045],
    'Unique File Storage': [0.008545808634085552, 0.0071058529225063345, 0.01701832527340012]
}

fig, axs = plt.subplots(3, 1, figsize=(9, 14))

plt.rcParams['font.family'] = 'DejaVu Sans'

for i, category in enumerate(categories):
    names = list(new_data_avg.keys())
    values = [new_data_avg[name][i] for name in names]
    errors = [new_data_std[name][i] for name in names]

    # set the color, if the winner it should have green color if loser it should have red color, if draw it should have yellow color, otherwise blue
    if category == 'Store Time':
        colors = ['green' if value == min(values) else 'red' if value == max(
            values) else 'yellow' if value == min(values) and value == max(values) else 'blue' for value in values]
    elif category == 'Retrieve Time':
        colors = ['green' if value == min(values) else 'red' if value == max(
            values) else 'yellow' if value == min(values) and value == max(values) else 'blue' for value in values]
    elif category == 'Delete Time':
        colors = ['green' if value == min(values) else 'red' if value == max(
            values) else 'yellow' if value == min(values) and value == max(values) else 'blue' for value in values]
    else:
        colors = ['blue' for value in values]

    axs[i].barh(names, values, xerr=errors, capsize=5, color=colors)
    axs[i].set_title(category)

plt.tight_layout()

# save the plot on the folder with the name of the file
plt.savefig('apple_tv_hd_chart_generator.png')
