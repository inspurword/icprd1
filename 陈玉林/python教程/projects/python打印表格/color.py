class Color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


if __name__ == '__main__':
    output = Color.RED + '输出红色字体' + Color.END
    print(output)

# 开头部分：\033[显示方式;前景色;背景色m 
# 结尾部分：\033[0m
# 数值含义:
# 显示方式: 
#     0(默认值) 1(高亮) 22(非粗体) 4(下划线)
#     24(非下划线) 5(闪烁) 25(非闪烁) 7(反显) 27(非反显)
#前景色: 
#    30(黑色) 31(红色) 32(绿色) 33(黄色) 34(蓝色) 35(洋红) 36(青色) 37(白色)
#背景色: 
#    40(黑色) 41(红色) 42(绿色) 43(黄色) 44(蓝色) 45(洋红) 46(青色) 47(白色)
