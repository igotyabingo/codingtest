from itertools import product

def solution(users, emoticons):
    discount_rates = [10, 20, 30, 40]
    best_result = [0, 0]  # [가입자 수, 구매 총액]

    for discounts in product(discount_rates, repeat=len(emoticons)):
        join_count = 0
        total_purchase = 0

        for rate_limit, price_limit in users:
            user_total = 0
            for discount, price in zip(discounts, emoticons):
                if discount >= rate_limit:
                    user_total += int(price * (100 - discount) / 100)

            if user_total >= price_limit:
                join_count += 1
            else:
                total_purchase += user_total

        # 최적값 갱신
        if join_count > best_result[0]:
            best_result = [join_count, total_purchase]
        elif join_count == best_result[0] and total_purchase > best_result[1]:
            best_result[1] = total_purchase

    return best_result
