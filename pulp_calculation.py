import pulp

def main():
    # model to maximize production count
    model = pulp.LpProblem("Оптимізувати виробництво по кількості", pulp.LpMaximize) 

    # products we can produce
    lemonade = pulp.LpVariable(name = 'Лимонад', lowBound = 0, cat='Integer')
    fruit_juice = pulp.LpVariable(name = 'Фруктовий_сік', lowBound = 0, cat='Integer')

    # boundaries of resources
    model += 2 * lemonade + 1 * fruit_juice <= 100, 'Вода' # water boundaries
    model += 1 * lemonade <= 50, 'Цукор' # sugar boundaries
    model += 1 * lemonade <= 30, 'Лимонний_сік' # lemon juice boundaries
    model += 2 * fruit_juice <= 40, 'Фруктове_пюре' # fruits boundaries

    # our goal
    model += 1 * lemonade + 1 * fruit_juice, 'Виробництво'

    # find optimal solution
    model.solve()

    # display results
    lemonade_optimal_count = lemonade.varValue
    fruit_juice_optimal_count = fruit_juice.varValue
    print("Оптимальна кількість виробницвтва:")
    print(f"Лимонад: {lemonade_optimal_count}, Фруктовий сік: {fruit_juice_optimal_count}, всього продукції: {pulp.value(model.objective)}\n")

    print(f"Скільки ресурсів буде задіяно:")
    print(f"Вода: {2 * lemonade_optimal_count + 1 * fruit_juice_optimal_count}")
    print(f"Цукор: {1 * lemonade_optimal_count}")
    print(f"Лимонний сік: {1 * lemonade_optimal_count}")
    print(f"Фруктове пюре: {2 * fruit_juice_optimal_count}")


if __name__ == '__main__':
    main()