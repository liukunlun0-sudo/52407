import numpy as np

def generate_mock_signal(samples=100):
    """生成模拟的一维信号数据（包含正弦波和随机噪声）"""
    t = np.linspace(0, 1, samples)
    base_signal = np.sin(2 * np.pi * 5 * t)
    noise = np.random.normal(0, 0.5, samples)
    return base_signal + noise

def process_signal(data):
    """
    信号处理模块
    当前状态：未处理，直接返回原始数据
    """
    data=data*2
    # TODO: 练习1 - 在这里添加一个简单的滑动平均滤波 (Moving Average)
    # TODO: 练习2 - 或者尝试添加一个简单的阈值过滤，将小于0的值设为0
    return data

if __name__ == "__main__":
    print("--- 信号处理模拟器启动 ---")
    
    # 1. 生成 10 个采样点的数据
    raw_data = generate_mock_signal(10)
    print(f"原始数据示例 (前5个点):\n{raw_data[:5]}\n")

    # 2. 处理数据
    processed_data = process_signal(raw_data)
    print(f"处理后数据 (前5个点):\n{processed_data[:5]}")