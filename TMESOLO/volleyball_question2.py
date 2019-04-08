# coding: utf-8
from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu, GAME_WIDTH, GAME_HEIGHT, PLAYER_RADIUS, BALL_RADIUS
from soccersimulator import VolleySimulation, volley_show_simu
from tools      import SuperState
from actions    import Actions
from strategies import Strategies


class Attaque(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Random")

    def compute_strategy(self, state, id_team, id_player):
      
        s = Strategies(state, id_team, id_player)
        v = SuperState(state, id_team, id_player)
        a = Actions(state, id_team, id_player)
        if v.player.distance(v.ball) < PLAYER_RADIUS + BALL_RADIUS:
            shoot = v.playeradverse - v.player
            return SoccerAction(shoot = shoot.normalize()*10)
        else :
            return a.deplacement(v.ball)
        


# Create teams
team1 = SoccerTeam(name="Team 1")
team2 = SoccerTeam(name="Team 2")

# Add players
team1.add("Player 1", Attaque())  # Random strategy
team2.add("Player 2", Attaque())   # Random strategy

# Create a match
simu = VolleySimulation(team1, team2)

# Simulate and display the match
volley_show_simu(simu)
