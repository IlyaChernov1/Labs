def main():
    # Запрос списка товаров
    products = input("Введите список товаров через запятую: ").split(',')
    products = [product.strip() for product in products]

    # Запрос цен в магазинах
    store_prices = {}
    while True:
        store_name = input("Введите название магазина (или 'стоп' для завершения ввода): ")
        if store_name.lower() == 'стоп':
            break
        prices = input(f"Введите цены на товары в магазине '{store_name}' через запятую: ").split(',')
        prices = [float(price.strip()) for price in prices]

        # Добавление цен в словарь
        store_prices[store_name] = prices

    # Вычисление общей стоимости покупок в каждом магазине
    total_costs = {}
    for store, prices in store_prices.items():
        total_costs[store] = sum(prices)

    # Вывод результатов
    print("\nОбщая стоимость покупок в каждом магазине:")
    for store, total in total_costs.items():
        print(f"{store}: {total:.2f} руб.")

    # Определение магазина с наибольшей экономией
    min_cost_store = min(total_costs, key=total_costs.get)
    min_cost_value = total_costs[min_cost_store]
    
    print(f"\nВы можете сэкономить больше всего, купив товары в магазине '{min_cost_store}' с общей стоимостью {min_cost_value:.2f} руб.")

if __name__ == "__main__":
    main()