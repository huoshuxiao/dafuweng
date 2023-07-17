import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

from com.sun.dushen.common import utils


def run():
    df = utils.read_csv('ssq')
    # 拟合ARIMA模型并进行预测
    forecast_results = {}
    for column in df.columns:
        model = ARIMA(df[column], order=([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16], 1, [0, 1]))
        # model = ARIMA(df[column], order=([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36], 5, [0,1]))
        model_fit = model.fit()
        forecast = model_fit.forecast(steps=1)
        forecast_results[column] = forecast[len(df)]

    # 打印预测结果
    print("预测的xx销售量为:", forecast_results['no'])
    # print("预测的苹果销售量为:", forecast_results['red1'])
    # print("预测的香蕉销售量为:", forecast_results['red2'])
    # print("预测的橘子销售量为:", forecast_results['red3'])
    # print("预测的菠萝销售量为:", forecast_results['red4'])
    # print("预测的西瓜销售量为:", forecast_results['red5'])
    # print("预测的哈密瓜销售量为:", forecast_results['red6'])
    print("预测的桃子销售量为:", forecast_results['blue1'])

    # 绘制时间序列图
    # plt.figure(figsize=(10, 7))

    # plt.plot(df['date'], df['red1'], label='Apple')
    # plt.plot(df['date'], df['red2'], label='Banana')
    # plt.plot(df['date'], df['red3'], label='Orange')
    # plt.plot(df['date'], df['red4'], label='Jackfruit')
    # plt.plot(df['date'], df['red5'], label='Watermelon')
    # plt.plot(df['date'], df['red6'], label='Honeydew')
    # plt.plot(df['date'], df['blue1'], label='Peach')
    # plt.xlabel('Date')
    # plt.ylabel('Sales')
    # plt.title('Fruit Sales Time Series')
    # plt.legend()
    # plt.show()
    #
    # # 预测未来一天的每种水果的销售量
    # forecast_apple = arima_forecast(df['red1'])
    # forecast_banana = arima_forecast(df['red2'])
    # forecast_orange = arima_forecast(df['red3'])
    # forecast_jackfruit = arima_forecast(df['red4'])
    # forecast_watermelon = arima_forecast(df['red5'])
    # forecast_honeydew = arima_forecast(df['red6'])
    # forecast_peach = arima_forecast(df['blue1'])
    #
    # # 打印预测结果
    # print("预测的苹果销售量为:", forecast_apple)
    # print("预测的香蕉销售量为:", forecast_banana)
    # print("预测的橘子销售量为:", forecast_orange)
    # print("预测的菠萝销售量为:", forecast_jackfruit)
    # print("预测的西瓜销售量为:", forecast_watermelon)
    # print("预测的哈密瓜销售量为:", forecast_honeydew)
    # print("预测的桃子销售量为:", forecast_peach)


# # 定义一个函数用于拟合ARIMA模型并进行预测
# def arima_forecast(data):
#     model = ARIMA(data, order=(1, 1, 0))
#     model_fit = model.fit()
#     forecast = model_fit.forecast(steps=1)[0]
#     return forecast


run()
