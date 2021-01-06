# --- Your main imports --- #
#Imports
import requests
import pandas as pd
import lxml.html as lh
import numpy as np
import matplotlib.pyplot as plt

# --- Preliminary Code to set up --- #

url = 'https://pokemondb.net/pokedex/stats/gen4#'
response = requests.get(url)
headers = response.headers
body = response.text
doc = lh.fromstring(response.text)

# --- Code to extract data from url --- #

pokemonStats = doc.xpath('//tr')

# --- Main Code (EXCLUDES LEGENDARIES)--- #

col = []
i = 0

for t in pokemonStats[0]:
    i += 1
    name=t.text_content()
    #print('%d:"%s"'%(i,name))
    col.append((name,[]))


#Since out first row is the header, data is stored on the second row onwards
for j in range(1,len(pokemonStats)):
    #T is our j'th row
    T = pokemonStats[j]
    
    #If row is not of size 10, the //tr data is not from our table 
    if len(T)!= 10:
        break
    
    #i is the index of our column
    i = 0
     
    for t in T.iterchildren():
        data = t.text_content() 
        #Check if row is empty
        if i > 0:
        #Convert any numerical value to integers
            try:
                data = int(data)
            except:
                pass
        #Append the data to the empty list of the i'th column
        col[i][1].append(data)
        
        i += 1

Dict = {title:column for (title,column) in col}
df = pd.DataFrame(Dict)

# --- Code shows you the pokemon from url excluding the legendaries --- #

df = df[:-22]
#print(df)


        # set height of bar
    bars1 = [78, 96.7, 68.3, 56.7, 61.7, 75.3]
    bars2 = [85, 50, 95, 120, 115, 80]
    bars3 = [62, 56.5, 101, 51.5, 101, 28]

        # Set position of bar on X axis
    r1 = np.arange(len(bars1))
    r2 = [x + barWidth for x in r1]
    r3 = [x + barWidth for x in r2]

        # Make the plot
    plt.bar(r1, bars1, color='#1f77b4', width=barWidth, edgecolor='white', label='Dragon Ground')
    plt.bar(r2, bars2, color='#ff7f0e', width=barWidth, edgecolor='white', label='Fairy Flying')
    plt.bar(r3, bars3, color='#2ca02c', width=barWidth, edgecolor='white', label='Steel Psychic')
        # Add xticks on the middle of the group bars
    plt.xlabel('Stats', fontweight='bold')
    plt.xticks([r + barWidth for r in range(len(bars1))], ['Hp', 'Atk', 'Def', 'Sp. Atk', 'Sp. Def', 'Speed'])
 
        # Create legend & Show graphic
    plt.legend(loc='upper right',prop={'size': 6})
    plt.show()  

def waterTypes():
        # set width of bar
    barWidth = 0.15
 
        # set height of bar
    bars1 = [64.4, 64.7, 55.9, 66, 60.1, 68.7]
    bars2 = [45, 20, 50, 60, 120, 50]
    bars3 = [111, 83, 68, 92, 82, 39]
    bars4 = [84, 86, 88, 111, 101, 60]
 
        # Set position of bar on X axis
    r1 = np.arange(len(bars1))
    r2 = [x + barWidth for x in r1]
    r3 = [x + barWidth for x in r2]
    r4 = [x + barWidth for x in r3]

        # Make the plot
    plt.bar(r1, bars1, color='#1f77b4', width=barWidth, edgecolor='white', label='Water')
    plt.bar(r2, bars2, color='#ff7f0e', width=barWidth, edgecolor='white', label='Water Flying')
    plt.bar(r3, bars3, color='#2ca02c', width=barWidth, edgecolor='white', label='Water Ground')
    plt.bar(r4, bars4, color='#d62728', width=barWidth, edgecolor='white', label='Water Steel')
 
        # Add xticks on the middle of the group bars
    plt.xlabel('Stats', fontweight='bold')
    plt.xticks([r + barWidth for r in range(len(bars1))], ['Hp', 'Atk', 'Def', 'Sp. Atk', 'Sp. Def', 'Speed'])
 
        # Create legend & Show graphic
    plt.legend(loc='upper right',prop={'size': 6})
    plt.show()

def grassTypes():
        # set width of bar
    barWidth = 0.15
 
        # set height of bar
    bars1 = [69.1, 80.3, 84.4, 72.7, 62.6, 54]
    bars2 = [95, 109, 105, 75, 85, 56]
    bars3 = [75, 77, 62.5, 77, 72.5, 50]
    bars4 = [50, 50, 50, 87.5, 87.5, 72.5]
 
        # Set position of bar on X axis
    r1 = np.arange(len(bars1))
    r2 = [x + barWidth for x in r1]
    r3 = [x + barWidth for x in r2]
    r4 = [x + barWidth for x in r3]

        # Make the plot
    plt.bar(r1, bars1, color='#1f77b4', width=barWidth, edgecolor='white', label='Grass')
    plt.bar(r2, bars2, color='#ff7f0e', width=barWidth, edgecolor='white', label='Grass Ice')
    plt.bar(r3, bars3, color='#2ca02c', width=barWidth, edgecolor='white', label='Grass Ground')
    plt.bar(r4, bars4, color='#d62728', width=barWidth, edgecolor='white', label='Grass Poison')
 
        # Add xticks on the middle of the group bars
    plt.xlabel('Stats', fontweight='bold')
    plt.xticks([r + barWidth for r in range(len(bars1))], ['Hp', 'Atk', 'Def', 'Sp. Atk', 'Sp. Def', 'Speed'])
 
        # Create legend & Show graphic
    plt.legend(loc='upper right',prop={'size': 6})
    plt.show()

def bugTypes():
        # set width of bar
    barWidth = 0.15
 
        # set height of bar
    bars1 = [51.3, 46.3, 45.7, 36.3, 45.7, 42]
    bars2 = [95, 109, 105, 75, 85, 56]
    bars3 = [60, 59, 85, 79, 105 ,36]
    bars4 = [60, 79, 105, 59, 85, 36]
    bars5 = [60, 69, 95, 69, 95, 36]
 
        # Set position of bar on X axis
    r1 = np.arange(len(bars1))
    r2 = [x + barWidth for x in r1]
    r3 = [x + barWidth for x in r2]
    r4 = [x + barWidth for x in r3]
    r5 = [x + barWidth for x in r4]

        # Make the plot
    plt.bar(r1, bars1, color='#1f77b4', width=barWidth, edgecolor='white', label='Bug')
    plt.bar(r2, bars2, color='#ff7f0e', width=barWidth, edgecolor='white', label='Bug Flying')
    plt.bar(r3, bars3, color='#2ca02c', width=barWidth, edgecolor='white', label='Bug Grass')
    plt.bar(r4, bars4, color='#d62728', width=barWidth, edgecolor='white', label='Bug Ground')
    plt.bar(r5, bars5, color='#9467bd', width=barWidth, edgecolor='white', label='Bug Steel')
 
        # Add xticks on the middle of the group bars
    plt.xlabel('Stats', fontweight='bold')
    plt.xticks([r + barWidth for r in range(len(bars1))], ['Hp', 'Atk', 'Def', 'Sp. Atk', 'Sp. Def', 'Speed'])
 
        # Create legend & Show graphic
    plt.legend(loc='upper right',prop={'size': 6})
    plt.show()

# ---To check yourself to see if your barcharts are accurate --- #

def hp():
    pokemon_avg = df.groupby(['Type'])['HP'].mean() 

    df_max_avg_hp = pd.DataFrame()

    pokemon_typing = pokemon_avg.idxmax()
    avg_hp = pokemon_avg.max()
    
    print('The best type for HP is:', pokemon_typing)
    print('The HP is:', avg_hp)

def attack():
    pokemon_avg = df.groupby(['Type'])['Attack'].mean() 

    df_max_avg_atk = pd.DataFrame()

    pokemon_typing = pokemon_avg.idxmax()
    avg_atk = pokemon_avg.max()
    
    print('The best type for Atk is:', pokemon_typing)
    print('The Atk is:', avg_atk)

def defense():
    pokemon_avg = df.groupby(['Type'])['Defense'].mean() 

    df_max_avg_def = pd.DataFrame()

    pokemon_typing = pokemon_avg.idxmax()
    avg_defense = pokemon_avg.max()
    
    print('The best type for Def is:', pokemon_typing)
    print('The Def is:', avg_defense)

def sp_atk():
    pokemon_avg = df.groupby(['Type'])['Sp. Atk'].mean() 

    df_max_avg_sp_atk = pd.DataFrame()

    pokemon_typing = pokemon_avg.idxmax()
    avg_sp_atk = pokemon_avg.max()
    
    print('The best type for Sp. Atk is:', pokemon_typing)
    print('The Sp. Atk is:', avg_sp_atk)

def sp_def():
    pokemon_avg = df.groupby(['Type'])['Sp. Def'].mean() 

    df_max_avg_sp_def = pd.DataFrame()

    pokemon_typing = pokemon_avg.idxmax()
    avg_sp_def = pokemon_avg.max()
    
    print('The best type for Sp. Def is:', pokemon_typing)
    print('The Sp. Def is:', avg_sp_def)

def speed():
    pokemon_avg = df.groupby(['Type'])['Speed'].mean() 

    df_max_avg_speed = pd.DataFrame()

    pokemon_typing = pokemon_avg.idxmax()
    avg_speed = pokemon_avg.max()
    
    print('The best type for Speed is:', pokemon_typing)
    print('The Speed is:', avg_speed)
