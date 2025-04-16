from ranking_tool.utils import split_score_string


class Game:
    """
    Represents a game between two teams and stores only the points each team earned from that game.
    """

    def __init__(self, home_team_name: str, home_team_score: int, away_team_name: str, away_team_score: int):
        """
        Initialize a Game instance by assigning points to each team based on scores.

        Args:
            home_team_name (str): Name of the home team.
            home_team_score (int): Score of the home team.
            away_team_name (str): Name of the away team.
            away_team_score (int): Score of the away team.
        """
        home_team_points, away_team_points = self.calculate_points(home_team_score, away_team_score)
        self.points = {home_team_name: home_team_points, away_team_name: away_team_points}

    @classmethod
    def from_string(cls, match_string: str):
        """
        Parses a formatted match string and creates a Game instance.

        The expected format is: "<home_team_name> <home_team_score>, <away_team_name> <away_team_score>"

        Example:
            >>> Game.from_string("Lions 3, Snakes 3")

        Args:
            match_string (str): A match result as a single string.

        Returns:
            Game: A new instance representing the parsed game.
        """
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
        """
        Determine how many points each team earns based on the game result.

        Args:
            home_team_score (int): Home team score.
            away_team_score (int): Away team score.

        Returns:
            tuple: Points for home and away teams respectively.
        """
        if home_team_score < away_team_score:
            return 0, 3
        elif home_team_score > away_team_score:
            return 3, 0
        else:
            return 1, 1

    def __eq__(self, other):
        """
        Check if two Game instances are equal based on their point distributions.

        Primarily used for testing.

        Args:
            other (Game): Another Game instance to compare.

        Returns:
            bool: True if both games have identical point mappings, False otherwise.
        """
        return self.points == other.points


class League:
    """
    Represents a league consisting of multiple games and calculates team rankings.
    """

    def __init__(self, games: list[Game]):
        """
        Initialize a League instance and calculate the rankings.

        Args:
            games (list[Game]): A list of Game instances.
        """
        self.games = games
        self.standard_rank = self.calculate_ranking(games)

    @staticmethod
    def calculate_ranking(games: list[Game]):
        """
        Compute the team rankings based on total points across all games.

        Teams are ranked in descending order of points. In case of a tie,
        teams share the same rank, and the next rank is adjusted accordingly.
        This is also known as standard competition ranking (e.g., 1, 2, 2, 4...).

        Args:
           games (list[Game]): A list of Game instances.

        Returns:
           list[tuple]: A list of (position, team name, points) tuples sorted by ranking.
        """
        overall_points = dict()
        for game in games:
            for team, points in game.points.items():
                overall_points[team] = overall_points.get(team, 0) + points
        sorted_overall_points = sorted(overall_points.items(), key=lambda x: (-x[1], x[0]))

        position = 0
        hold = 0
        standard_rank = []
        past_points = 0
        for team, points in sorted_overall_points:
            if points == past_points:
                hold += 1
            else:
                position += hold + 1
                hold = 0
                past_points = points
            standard_rank.append((position, team, points))
        return standard_rank

    @classmethod
    def from_string(cls, s: str, sep='\n'):
        """
        Create a League instance from a string of match results.

        Args:
            s (str): A multi-line string with one game per line.
            sep (str, optional): Separator between games. Defaults to newline.

        Returns:
            League: An instance of the League class.
        """
        return cls([Game.from_string(s) for s in s.split(sep) if s.strip()])

    def __str__(self):
        """
        Return the string representation of the league rankings.

        Each line in the output follows the format:
            "<rank>. <team name>, <points> pt[s]"

        The suffix "pt" is used for singular (1 point), and "pts" is used for plural.

        Returns:
            str: A formatted multi-line string representing the ranked list of teams.
        """
        return '\n'.join(
            [f"{position}. {team}, {points} pt{'s' if points != 1 else ''}" for position, team, points in
             self.standard_rank])
