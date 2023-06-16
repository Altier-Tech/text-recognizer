import matplotlib.pyplot as plt 

im = plt.imread('input/test.png')
print(im.shape)

fig = plt.figure(figsize=(15,15))

plt.imshow(im)

for i in range(len(result_df)):
    row = result_df.iloc[i]
    if row['conf'] > 0:
        x = [row['left'], row['left']+row['width'], row['left']+row['width'], row['left'], row['left']]
        y = [row['top'], row['top'], row['top']+row['height'], row['top']+row['height'], row['top']]
        plt.fill(x,y, facecolor='none', edgecolor='red')
        plt.text(x[0],y[0], row['text'], color='red', fontsize=15)

plt.axis('off')
plt.savefig('output_pytesseract.png')
plt.show()