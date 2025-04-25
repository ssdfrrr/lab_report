from sklearn.datasets import load_diabetes
import matplotlib.pyplot as plt
import pandas as pd
data = load_diabetes()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target
df['class'] = pd.cut(df['target'], bins=[-float('inf'), 100, 200, float('inf')],
                       labels=['<100', '100-200', '>200'])
plt.figure(figsize=(10, 6))
scatter = plt.scatter(df['age'], df['bmi'], c=df['target'], cmap='viridis', alpha=0.7)
plt.colorbar(scatter, label='Уровень прогрессирования диабета (target)')
plt.xlabel('Возраст (стандартизированный)')
plt.ylabel('Индекс массы тела (стандартизированный)')
plt.title('Диаграмма рассеяния: age vs bmi (набор diabetes)')
plt.grid(True)
plt.show()
