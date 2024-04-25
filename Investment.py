from matplotlib import pyplot as plt


class Investment:
    def __init__(self, ticker, start_date, end_date):
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date
        self.data = self.load_data()

    def load_data(self):
        # 使用pandas_datareader从Yahoo Finance加载数据
        import pandas_datareader as pdr
        return pdr.get_data_yahoo(self.ticker, self.start_date, self.end_date)

    def calculate_indicators(self):
        # 计算交易所需的技术指标，例如移动平均线、RSI等
        pass

    def execute_strategy(self):
        # 实现交易策略
        pass

    def evaluate_performance(self):
        """评估投资的总体表现"""
        # 计算投资回报率
        self.data['Market Return'] = self.data['Close'].pct_change()
        self.data['Strategy Return'] = self.data['Market Return'] * self.data['Signal'].shift(1)
        self.data['Cumulative Market Returns'] = (1 + self.data['Market Return']).cumprod()
        self.data['Cumulative Strategy Returns'] = (1 + self.data['Strategy Return']).cumprod()

        # 绘制收益曲线
        plt.figure(figsize=(10,5))
        plt.plot(self.data['Cumulative Market Returns'], label='Market Returns')
        plt.plot(self.data['Cumulative Strategy Returns'], label='Strategy Returns')
        plt.legend()
        plt.show()

        # 总体策略评估
        total_market_return = self.data['Cumulative Market Returns'].iloc[-1]
        total_strategy_return = self.data['Cumulative Strategy Returns'].iloc[-1]
        print(f"Market Return: {total_market_return - 1:.2%}")
        print(f"Strategy Return: {total_strategy_return - 1:.2%}")