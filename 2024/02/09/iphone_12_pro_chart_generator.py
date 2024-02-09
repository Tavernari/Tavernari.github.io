import matplotlib.pyplot as plt

# Updated Data including new categories and results
categories = ['Store Time', 'Retrieve Time', 'Delete Time']

new_data_avg = {
    'GRDB Dequeue Relational': [0.05410759449005127, 0.06059942245483398, 0.047901594638824464],
    'GRDB Pool Relational': [0.025569283962249757, 0.06118520498275757, 0.03620592355728149],
    'GRDB Queue Separated JSON': [0.037571704387664794, 0.02187931537628174, 0.06916229724884033],
    'GRDB Pool Separated JSON': [0.009583020210266113, 0.020803797245025634, 0.017094516754150392],
    'GRDB Queue Unique JSON': [0.04450840950012207, 0.03632467985153198, 0.07472069263458252],
    'GRDB Pool Unique JSON': [0.022487807273864745, 0.04017020463943481, 0.0531670093536377],
    'Separated File Storage': [0.00024312734603881836, 0.011354780197143555, 0.017024314403533934],
    'Unique File Storage': [0.023803091049194335, 0.03913459777832031, 0.05392289161682129]
}

# Standard Deviations
new_data_std = {
    'GRDB Dequeue Relational': [0.0018584598381146675, 0.0021391018386472376, 0.0019910149232025016],
    'GRDB Pool Relational': [0.010465289577689918, 0.0028147430418301845, 0.0022600997902171524],
    'GRDB Queue Separated JSON': [0.008485407273967889, 0.002073545935309319, 0.0036986848309728242],
    'GRDB Pool Separated JSON': [0.0015880061556794902, 0.0019296657799966863, 0.004288628744812087],
    'GRDB Queue Unique JSON': [0.012669454670222553, 0.005911335210173019, 0.014600969306249325],
    'GRDB Pool Unique JSON': [0.0050163916715775855, 0.00594428373598925, 0.020141980508079593],
    'Separated File Storage': [4.503809155460785e-05, 0.003982765159966546, 0.004294758378144133],
    'Unique File Storage': [0.003768626292550069, 0.005144937914644579, 0.012730775530731639]
}

# Plotting the updated results
fig, axs = plt.subplots(3, 1, figsize=(9, 14))

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
plt.savefig('iphone_12_pro_chart_generator.png')
