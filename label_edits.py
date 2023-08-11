#### Editing the legend properties ####
fig, ax = plt.subplots(proj='3D')
plt.scatter3D(xMW, yMW, zMW, label = 'MW stars', color = 'tab:blue', alpha = 0.01)
plt.scatter3D(xDM, yDM, zDM, label = 'MW DM', color = 'gray', alpha = 0.01)
plt.scatter3D(xLeo, yLeo, zLeo, label = 'Leo I stars', color = 'tab:red', alpha = 0.01)
han, lab = ax.get_legend_handles_labels()
#h are the circles that will show up in the legend

for h in han:
	h.set_alpha(1.0)
	size = h.get_sizes()[0]
	h.set_sizes([size*5])

plt.legend(han, lab)


#### Editing the galaxy property label ####
Mstar = value_from_IC_file * 1e10
label = r'$M_*$ = %0.1e $M_\odot$' % (Mstar) 

#### Color code (RA, DEC) scatter plot by distance
from matplotlib import cm

dist = array_of_stellar_distances_from_the_sun
plt.scatter(ra, dec, c=dist, cmap=cm.viridis, vmin=0, vmax=300) #feel free to edit cmap, vmin and vmax
plt.grid()