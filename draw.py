import matplotlib.pyplot as plt
x1=range(0,21)
x2=[]
x3=[]
y1=[0.85,0.8,0.75,0.84,0.81,0.82,0.88,0.81,0.93,0.92,0.9,0.78,0.94,0.92,0.93,0.76,0.76,0.75,0.96,0.97,0.93]
y2=[0.76,0.81,0.82,0.76,0.82,0.77,0.72,0.78,0.75,0.8,0.74,0.78,0.76,0.78,0.78,0.77,0.84,0.77,0.77,0.85,0.74]
y3=[0.85,0.86,0.89,0.79,0.86,0.79,0.82,0.88,0.82,0.87,0.8,0.85,0.8,0.83,0.83,0.83,0.89,0.8,0.83,0.88,0.79]
y4=[0.73,0.7,0.7,0.72,0.71,0.73,0.7,0.72,0.71,0.74,0.72,0.71,0.71,0.72,0.71,0.73,0.73,0.72,0.71,0.72,0.73]
y5=[0.73,0.76,0.78,0.71,0.82,0.75,0.71,0.78,0.74,0.77,0.73,0.76,0.77,0.75,0.84,0.75,0.81,0.73,0.73,0.78,0.7]
y6=[0.98,0.98,0.99,0.98,0.97,0.98,0.98,0.98,0.97,0.97,0.97,0.98,0.96,0.98,0.98,0.97,0.97,0.97,0.98,0.97,0.98]
y7=[0.87,0.88,0.83,0.85,0.86,0.88,0.85,0.87,0.87,0.86,0.86,0.86,0.85,0.87,0.87,0.87,0.85,0.86,0.89,0.83,0.87]

yy1=[0.24,0.11,0.09,0.27,0.33,0.28,0.06,0.07,0,0,0.2,0.5,0,0,0.04,0.01,0,0,0,0.02,0.11]
yy2=[0.51,0.58,0.6,0.51,0.55,0.43,0.63,0.63,0.78,0.48,0.68,0.73,0.64,0.57,0.45,0.6,0.56,0.44,0.52,0.73,0.39]
yy3=[0.56,0.61,0.65,0.57,0.58,0.44,0.65,0.66,0.53,0.47,0.68,0.78,0.58,0.59,0.43,0.52,0.58,0.47,0.61,0.39,0.34]
yy4=[0.52,0.47,0.51,0.49,0.52,0.52,0.66,0.65,0.8,0.46,0.85,0.66,0.67,0.46,0.68,0.64,0.49,0.64,0.43,0.83,0.43]
yy5=[0.02,0.02,0.75,0.02,0.88,0.87,1,0.24,1,0.1,0.11,0.24,1,1,0.12,0.24,0.7,0.65,0.1,0.11,0.79]
yy6=[0.93,0.94,0.96,0.94,0.95,0.97,0.93,0.94,0.9,0.92,0.94,0.94,0.9,0.91,0.94,0.96,0.97,0.95,0.98,0.93,0.94]
yy7=[0.81,0.76,0.78,0.8,0.66,0.86,0.77,0.77,0.81,0.68,0.85,0.8,0.8,0.73,0.8,0.77,0.69,0.8,0.71,0.83,0.64]

# plt.subplot(1,2,1)
# plt.plot(x3,x2,label='Out_Sa',linewidth=3,color='r',marker='o',
# markerfacecolor='blue',markersize=12)
# plt.plot(x3,x2,label='Ave_Sa',color='b',marker='o')
# plt.plot(x3,x2,label='Blo_Sa',color='c',marker='o')
# plt.plot(x3,x2,label='Dif_Sa',color='m',marker='o')
# plt.plot(x3,x2,label='Med_Sa',color='g',marker='o')
# plt.plot(x3,x2,label='Per_Sa',color='y',marker='o')
# plt.plot(x3,x2,label='Wav_Sa',color='k',marker='o')
#
# plt.plot(x3,x2,label='Out_Un',linewidth=3,color='r',marker='v',
# markerfacecolor='blue',markersize=12)
# plt.plot(x3,x2,label='Ave_Un',color='b',marker='v')
# plt.plot(x3,x2,label='Blo_Un',color='c',marker='v')
# plt.plot(x3,x2,label='Dif_Un',color='m',marker='v')
# plt.plot(x3,x2,label='Med_Un',color='g',marker='v')
# plt.plot(x3,x2,label='Per_Un',color='y',marker='v')
# plt.plot(x3,x2,label='Wav_Un',color='k',marker='v')
# plt.xlabel('method')
# plt.title('method label')
# plt.legend(loc=1)



# plt.subplot(1,2,2)
plt.plot(x1,y1,label='Out_Same',linewidth=3,color='orangered',marker='o',
markerfacecolor='lawngreen',markersize=12)
# plt.plot(x1,y2,label='Ave_Same',color='deepskyblue',marker='o',markerfacecolor='grey')
# plt.plot(x1,y3,label='Blo_Same',color='deepskyblue',marker='o',markerfacecolor='grey')
# plt.plot(x1,y4,label='Dif_Same',color='deepskyblue',marker='o',markerfacecolor='grey')
# plt.plot(x1,y5,label='Med_Same',color='deepskyblue',marker='o',markerfacecolor='grey')
# plt.plot(x1,y6,label='Per_Same',color='deepskyblue',marker='o',markerfacecolor='grey')
plt.plot(x1,y7,label='Wav_Same',color='deepskyblue',marker='o',markerfacecolor='grey')

plt.plot(x1,yy1,label='Out_Unsame',linewidth=3,color='orangered',marker='v',
markerfacecolor='lawngreen',markersize=12)
# plt.plot(x1,yy2,label='Ave_Unsame',color='deepskyblue',marker='v',markerfacecolor='grey')
# plt.plot(x1,yy3,label='Blo_Unsame',color='deepskyblue',marker='v',markerfacecolor='grey')
# plt.plot(x1,yy4,label='Dif_Unsame',color='deepskyblue',marker='v',markerfacecolor='grey')
# plt.plot(x1,yy5,label='Med_Unsame',color='deepskyblue',marker='v',markerfacecolor='grey')
# plt.plot(x1,yy6,label='Per_Unsame',color='deepskyblue',marker='v',markerfacecolor='grey')
plt.plot(x1,yy7,label='Wav_Unsame',color='deepskyblue',marker='v',markerfacecolor='grey')
plt.xlabel('Test image')
plt.ylabel('Similarity')
plt.title('')
# box = plt.get_position()
# plt.set_position([box.x0, box.y0, box.width , box.height* 0.8])
plt.legend(loc='center', bbox_to_anchor=(0.47, 1.07),ncol=2)
# plt.legend(loc=1)
x_label=['AB','AC','AD','AE','AF','AG','BC','BD','BE','BF','BG','CD','CE','CF','CG','DE','DF','DG','EF','EG','FG']
plt.xticks(x1, x_label, rotation='vertical')

plt.show()