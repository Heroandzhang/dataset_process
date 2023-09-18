import SimpleITK as sitk
import matplotlib.pyplot as plt
#%matplotlib inline
import os

# path='./SaveRaw'
# for f in os.listdir(path):
#     if f.endswith('.mhd'):
#         os.path.join(path, f)
#         data =sitk.ReadImage(os.path.join(path,f))
#         print(data)
#
#         spacing = data.GetSpacing()
#         scan = sitk.GetArrayFromImage(data)
#         # print('spacing: ', spacing)
#         # print('# slice: ', len(scan))
#         for i in range(len(scan)):
#             print(i)
#             plt.imshow(scan[i],cmap=plt.cm.gray)
#             plt.show()

data=sitk.ReadImage( r'D:\重新排序数据集\data\1.25mm\mhd\100_20220217.mhd')
spacing = data.GetSpacing()
scan = sitk.GetArrayFromImage(data)
print('spacing: ', spacing)
print('# slice: ', len(scan))
for i in range(len(scan)):
    print(i)
    plt.imshow(scan[i],cmap=plt.cm.gray)
    plt.show()
