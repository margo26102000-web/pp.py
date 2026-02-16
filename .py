from dataclasses import dataclass, field
from typing import List

# Вспомогательная функция для ID (для примера)
id_counter = 0
def next_id():
    global id_counter
    id_counter += 1
    return id_counter

@dataclass
class Game:
    id: int = field(default_factory=next_id)
    name: str = ""
    genre: str = ""
    platform: str = ""
    age_rating: int = 0
    price: float = 0.0
    player_ratings: float = 0.0
    status: str = ""
    number_of_copies: int = 0

# --- РЕАЛИЗАЦИЯ ФУНКЦИЙ ---

# 1. Поиск игр по части названия (подстрока)
def search_games_by_partial_name(game_list: List[Game], search_term: str) -> List[Game]:
    # Приводим к нижнему регистру, чтобы поиск был независим от регистра
    return [game for game in game_list if search_term.lower() in game.name.lower()]

# 2. Фильтрация игр (например, по платформе)
def filter_games_by_platform(game_list: List[Game], platform: str) -> List[Game]:
    return [game for game in game_list if game.platform == platform]

# 3. Сортировка игр (например, по цене по возрастанию)
def sort_games_by_price(game_list: List[Game]) -> List[Game]:
    return sorted(game_list, key=lambda x: x.price)

# 4. Изменить цену всех игр выбранного жанра (скидка -20%)
def apply_discount_to_genre(game_list: List[Game], genre: str, discount_percent: int):
    multiplier = 1 - (discount_percent / 100)
    for game in game_list:
        if game.genre == genre:
            game.price *= multiplier

# 5. Подсчитать среднюю цену всех игр
def get_average_price(game_list: List[Game]) -> float:
    if not game_list: return 0.0
    total_price = sum(game.price for game in game_list)
    return total_price / len(game_list)

# 6. Найти игру с максимальной оценкой
def get_best_rated_game(game_list: List[Game]) -> Game:
    if not game_list: return None
    return max(game_list, key=lambda x: x.player_ratings)

# 7. Пометить игру как «хит», если оценка ≥ 8.5
def mark_hits(game_list: List[Game]):
    for game in game_list:
        if game.player_ratings >= 8.5:
            game.status = "Хит"

# 8. Удалить все игры, у которых количество копий равно 0
def remove_out_of_stock(game_list: List[Game]) -> List[Game]:
    # В Python проще создать новый список без «нулевых» игр
    return [game for game in game_list if game.number_of_copies > 0]

