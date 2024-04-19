import matplotlib.pyplot as plt
plt.rc("font", family='YouYuan')

cities = ['Beijing', 'Shanghai', 'London', 'Boston', 'New York', 'Paris', 'Tokyo', 'Seoul', 'Los Angeles', 'Moscow',
          'San Francisco', 'Toronto', 'Chicago', 'Berlin', 'Singapore', 'Hong Kong', 'Shenzhen', 'Stockholm', 'Osaka',
          'Amsterdam']

researchers = [476644, 232201, 187324, 185779, 161885, 129790, 128862, 127102, 110414, 109533, 93371, 83356, 78414,
               75502, 74841, 61547, 55508, 51760, 50866, 50490]

plt.figure(figsize=(15, 8))
plt.barh(cities, researchers, align='center', color='skyblue')

plt.title('各城市永久定居科研人员数量')
plt.xlabel('科研人员数量')
plt.ylabel('城市')

plt.gca().invert_yaxis()

for i, v in enumerate(researchers):
    plt.text(v + 5000, i, str(v), va='center', fontweight='bold')

plt.grid(axis='x', alpha=0.75)

plt.show()
