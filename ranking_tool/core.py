from ranking_tool.utils import split_score_string


class Game:
    def __init__(self, home_team_name: str, home_team_score: int, away_team_name: str, away_team_score: int):
        home_team_points, away_team_points = self.calculate_points(home_team_score, away_team_score)
        self.points = {home_team_name: home_team_points, away_team_name: away_team_points}

    @classmethod
    def from_string(cls, match_string: str):
        home_team_str, away_team_str = match_string.split(',')
        home_team_name, home_team_score = split_score_string(home_team_str)
        away_team_name, away_team_score = split_score_string(away_team_str)
        return cls(
            home_team_name,
            int(home_team_score),
            away_team_name,
            int(away_team_score)
        )

    @staticmethod
    def calculate_points(home_team_score: int, away_team_score: int) -> tuple:
        if home_team_score < away_team_score:
            return 0, 3
        elif home_team_score > away_team_score:
            return 3, 0
        else:
            return 1, 1

    def __eq__(self, other):
        return self.points == other.points


class League:
    def __init__(self, games: list[Game]):
        self.games = games
        self.rank = self.calculate_ranking(games)

    @staticmethod
    def calculate_ranking(games: list[Game]):
        overall_points = dict()
        for game in games:
            for team, points in game.points.items():
                overall_points[team] = overall_points.get(team, 0) + points
        sorted_overall_points = sorted(overall_points.items(), key=lambda x: (-x[1], x[0]))

        position = 0
        hold = 0
        rank = []
        past_points = 0
        for team, points in sorted_overall_points:
            if points == past_points:
                hold += 1
            else:
                position += hold + 1
                hold = 0
                past_points = points
            rank.append((position, team, points))
        return rank

    @classmethod
    def from_string(cls, s: str, sep='\n'):
        return cls([Game.from_string(s) for s in s.split(sep) if s.strip()])

    def __str__(self):
        return '\n'.join(
            [f"{position}. {team}, {points} pt{'s' if points != 1 else ''}" for position, team, points in self.rank])
