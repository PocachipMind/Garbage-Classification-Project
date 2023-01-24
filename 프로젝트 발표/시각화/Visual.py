import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = range(1,21)


# 1번 문제 Train Loss 그래프
efficientnet_b0 = [ 1.151, 0.914, 0.835,0.794,0.784,0.725,0.678,0.664,0.652,0.644,0.646,0.641,0.636,0.631,0.635,0.627,0.639,0.627,0.644, 0.624 ]
ResNet50 = [1.692,1.041,0.901,0.819,0.783,0.759,0.739,0.726,0.706,0.691,0.668,0.657,0.665,0.654,0.654,0.647,0.637,0.64,0.635,0.646]
DenseNet201 = [1.903,1.676,1.533,1.465,1.395,1.347,1.296,1.28,1.229,1.202,1.177,1.13,1.084,1.082,1.039,1.032,1.005,0.994,0.975,0.959]
SwinTransformer = [3.076,2.475,2.345,2.197,2.022,1.813,1.622,1.498,1.436,1.387,1.379,1.345,1.346,1.334,1.306,1.288,1.273,1.251,1.279,1.263]
AlexNet = [1.679,1.337,1.264,1.218,1.168,1.148,1.131,1.128,1.136,1.143,1.125,1.127,1.133,1.121,1.121,1.124,1.123,1.134,1.129,1.145]

plt.title('Train Loss Graph')
plt.plot( x, efficientnet_b0, label="efficientnet_b0")
plt.plot( x, ResNet50, label="ResNet50")
plt.plot( x, DenseNet201, label="DenseNet201")
plt.plot( x, SwinTransformer, label="SwinTransformer")
plt.plot( x, AlexNet, label="AlexNet")
plt.xlabel('Epoch')
plt.ylabel('Train Loss')
plt.legend()
plt.show()






# 1번 문제 Train Acc 그래프
efficientnet_b0 = [0.741,0.839,0.866,0.885,0.886,0.914,0.93,0.938,0.938,0.94,0.939,0.943,0.947,0.949,0.946,0.948,0.94,0.945,0.939,0.947]
ResNet50 = [0.517,0.776,0.832,0.864,0.884,0.888,0.906,0.905,0.914,0.925,0.927,0.937,0.931,0.932,0.937,0.939,0.944,0.943,0.94,0.937]
DenseNet201 = [0.334,0.412,0.465,0.48,0.511,0.526,0.544,0.561,0.573,0.58,0.596,0.606,0.621,0.631,0.63,0.628,0.651,0.638,0.662,0.656]
SwinTransformer =[0.303,0.449,0.491,0.547,0.613,0.707,0.786,0.839,0.855,0.865,0.881,0.888,0.883,0.885,0.9,0.908,0.914,0.919,0.908,0.913]
AlexNet = [0.503,0.636,0.664,0.685,0.705,0.723,0.726,0.724,0.725,0.721,0.729,0.73,0.73,0.727,0.731,0.731,0.731,0.726,0.732,0.723]

plt.title('Train Accuracy Graph')
plt.plot( x, efficientnet_b0, label="efficientnet_b0")
plt.plot( x, ResNet50, label="ResNet50")
plt.plot( x, DenseNet201, label="DenseNet201")
plt.plot( x, SwinTransformer, label="SwinTransformer")
plt.plot( x, AlexNet, label="AlexNet")
plt.xlabel('Epoch')
plt.ylabel('Train Accuracy')
plt.legend()
plt.show()



# 1번 문제 Test Acc 비교
efficientnet_b0 = 96.111
ResNet = 96.38
DenseNet201 = 63.05
SwinTransformer = 94.44
AlexNet = 78.05

years = ['efficientnet_b0', 'ResNet', 'DenseNet201','SwinTransformer','AlexNet']
values = [efficientnet_b0, ResNet, DenseNet201, SwinTransformer, AlexNet]

plt.title('Test Accuracy Graph')
plt.bar(years, values, color=['b','y','g','r','m'])
# plt.xticks(z, years)

plt.show()







# 2번 문제 Valid Loss 비교
efficientnet_b0 = [1.951,1.545,1.467,1.526,1.393,1.306,1.292,1.307,1.29,1.284,1.282,1.281,1.285,1.278,1.277,1.28,1.278,1.278,1.277,1.278]
ResNet = [1.521,1.445,1.423,1.346,1.326,1.351,1.275,1.259,1.264,1.253,1.247,1.256,1.254,1.256,1.253,1.252,1.259,1.257,1.254,1.253]
DenseNet201 = [2.261,2.238,2.227,2.206,2.19,2.189,2.182,2.186,2.182,2.182,2.181,2.18,2.183,2.18,2.182,2.179,2.187,2.177,2.179,2.18]
SwinTransformer = [2.786,2.638,2.625,2.581,2.444,2.449,2.45,2.45,2.449,2.443,2.44,2.438,2.441,2.443,2.439,2.439,2.439,2.439,2.439,2.439]
AlexNet = [1.368,1.329,1.319,1.298,1.286,1.278,1.276,1.277,1.274,1.275,1.274,1.274,1.273,1.273,1.273,1.273,1.273,1.273,1.273,1.273]

plt.title('Valid Loss Graph')
plt.plot( x, efficientnet_b0, label="efficientnet_b0")
plt.plot( x, ResNet50, label="ResNet50")
plt.plot( x, DenseNet201, label="DenseNet201")
plt.plot( x, SwinTransformer, label="SwinTransformer")
plt.plot( x, AlexNet, label="AlexNet")
plt.xlabel('Epoch')
plt.ylabel('Valid Loss')
plt.legend()
plt.show()






# 2번 문제 Valid Accuracy 비교
efficientnet_b0 = [0.428,0.524,0.564,0.544,0.613,0.658,0.662,0.655,0.67,0.683,0.689,0.687,0.69,0.691,0.693,0.691,0.692,0.693,0.692,0.692]
ResNet = [0.523,0.559,0.58,0.619,0.636,0.632,0.654,0.671,0.672,0.676,0.676,0.683,0.682,0.68,0.683,0.683,0.68,0.683,0.686,0.682]
DenseNet201 = [0.155,0.159,0.178,0.196,0.189,0.193,0.2,0.193,0.2,0.199,0.201,0.201,0.198,0.203,0.203,0.202,0.198,0.206,0.201,0.2]
SwinTransformer = [0.252,0.324,0.371,0.399,0.455,0.45,0.446,0.453,0.449,0.448,0.454,0.454,0.453,0.454,0.459,0.458,0.456,0.457,0.457,0.457]
AlexNet = [0.583,0.601,0.605,0.611,0.617,0.621,0.622,0.619,0.623,0.622,0.622,0.622,0.623,0.623,0.623,0.623,0.623,0.623,0.623,0.623]

plt.title('Valid Accuracy Graph')
plt.plot( x, efficientnet_b0, label="efficientnet_b0")
plt.plot( x, ResNet50, label="ResNet50")
plt.plot( x, DenseNet201, label="DenseNet201")
plt.plot( x, SwinTransformer, label="SwinTransformer")
plt.plot( x, AlexNet, label="AlexNet")
plt.xlabel('Epoch')
plt.ylabel('Valid Accuracy')
plt.legend()
plt.show()




# 2번 문제 Test Acc 비교
efficientnet_b0 = 25.42
ResNet = 36.44
DenseNet201 = 18.64
SwinTransformer = 20.0
AlexNet = 29.66

years = ['efficientnet_b0', 'ResNet', 'DenseNet201','SwinTransformer','AlexNet']
values = [efficientnet_b0, ResNet, DenseNet201, SwinTransformer, AlexNet]

plt.title('Test Accuracy Graph')
plt.bar(years, values, color=['b','y','g','r','m'])
# plt.xticks(z, years)

plt.show()
