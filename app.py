import streamlit as st

# Захардкоженная цена за м²
BASE_PRICE = 180000  

def regulator(area):
    """Регулятор скидки по твоей формуле Excel"""
    if area < 7:
        return 0
    elif area <= 10:
        return 0 + (area - 7) * (0 - 0) / (10 - 7)
    elif area <= 15:
        return 3 + (area - 10) * (3 - 0) / (15 - 10)
    elif area <= 20:
        return 17 + (area - 15) * (17 - 12) / (20 - 15)
    elif area <= 30:
        return 26 + (area - 20) * (28 - 22) / (30 - 20)
    elif area <= 50:
        return 28 + (area - 30) * (32 - 28) / (50 - 30)
    elif area <= 80:
        return 28 + (area - 50) * (35 - 28) / (80 - 50)
    elif area <= 120:
        return 32 + (area - 80) * (40 - 32) / (120 - 80)
    elif area <= 200:
        return 40 + (area - 120) * (50 - 40) / (200 - 120)
    else:
        return 50  # максимум

st.title("📐 Pergola калькулятор")

# Ввод длины и ширины
length = st.number_input("Введите длину (м)", min_value=0.0, step=0.1)
width = st.number_input("Введите ширину (м)", min_value=0.0, step=0.1)

# Вычисляем квадратуру
area = length * width
st.write(f"Квадратура: **{area:.2f} м²**")

# Считаем базовую цену
discount_percent = regulator(area)
final_price_m2 = BASE_PRICE * (1 - discount_percent / 100)
total_price = final_price_m2 * area

st.write(f"Базовая цена за м²: {BASE_PRICE} ₸")
st.write(f"Скидка по регулятору: {discount_percent:.2f}%")
st.write(f"Цена за м² после скидки: {final_price_m2:,.0f} ₸")
st.write(f"Итого без налогов: {total_price:,.0f} ₸")

# Выбор ИП или ТОО
company_type = st.radio("Выберите тип компании:", ["Без наценки", "ИП (+5%)", "ТОО (+15%)"])

if company_type == "ИП (+5%)":
    total_price *= 1.05
elif company_type == "ТОО (+15%)":
    total_price *= 1.15

st.success(f"💰 Итоговая цена: {total_price:,.0f} ₸")