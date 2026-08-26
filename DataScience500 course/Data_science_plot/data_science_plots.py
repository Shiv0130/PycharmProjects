import matplotlib.pyplot as plt
# fig,ax = plt.subplots(figsize =(10,6))
# x = ['Q1','Q2','Q3','Q4']
# y = [120,150,135,180]
# ax.plot(x,y,marker='o',label ='Sales')
# ax.set_xlabel('Quarter')
# ax.set_ylabel('Sales')
# ax.set_title('Quarterly Sales')
# ax.legend()
# fig.tight_layout()
# plt.savefig('sales.png',dpi=300)
# plt.show()

#Scatter
# x = ['Q1','Q2','Q3','Q4']
# y = [120,150,175,180]
#
# plt.scatter(x, y)
# plt.show()

#bar
# x = ['Q1','Q2','Q3','Q4']
# y = [120,150,175,180]
# plt.bar(x,y, color = 'lightblue')
# plt.show()

#pie chart
# x = ['Q1','Q2','Q3','Q4']
# y = [120,150,175,180]
# plt.pie(y)
# plt.show()

#histogram
x = ['Q1','Q2','Q3','Q4','Q5']
y = [120,160,175,180,190]
plt.hist(y)
plt.show()