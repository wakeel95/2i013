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
            if id_team == 1:
                if v.player.x<GAME_WIDTH*2/8:
                    shoot = Vector2D(GAME_WIDTH*4/8, GAME_HEIGHT/2)
                    return SoccerAction(shoot = shoot.normalize()*3)
                else:
                    if v.playeradverse.y< GAME_HEIGHT/2 :
                        shoot = Vector2D(GAME_WIDTH*7.5/8, GAME_HEIGHT*3.5/4) - v.player
                        return SoccerAction(shoot = shoot.normalize()*100)
                    else :
                        shoot = Vector2D(GAME_WIDTH*7.5/8, GAME_HEIGHT*0.5/4) - v.player
                        return SoccerAction(shoot = shoot.normalize()*100)
            else :
                if v.player.x>GAME_WIDTH*6/8:
                    shoot = Vector2D(GAME_WIDTH*4/8, GAME_HEIGHT/2)
                    return SoccerAction(shoot = shoot.normalize()*3)
                else:
                    if v.playeradverse.y> GAME_HEIGHT/2 :
                        shoot = Vector2D(GAME_WIDTH*0.5/8, GAME_HEIGHT*0.5/4) - v.player
                        return SoccerAction(shoot = shoot.normalize()*100)
                    else :
                        shoot = Vector2D(GAME_WIDTH*0.5/8, GAME_HEIGHT*3.5/4) - v.player
                        return SoccerAction(shoot = shoot.normalize()*100)
        else :
            if v.ballecampadverse == 0:
                if id_team == 1 :
                    return a.deplacement(Vector2D(GAME_WIDTH*2/8, GAME_HEIGHT/2))
                else :
                    return a.deplacement(Vector2D(GAME_WIDTH*6/8, GAME_HEIGHT/2))
            else :
                return a.deplacement(v.ball)
        


class OneVsOne(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Random")

    def compute_strategy(self, state, id_team, id_player):
      
        s = Strategies(state, id_team, id_player)
        v = SuperState(state, id_team, id_player)
        a = Actions(state, id_team, id_player)
        
        if v.player.distance(v.ball) < PLAYER_RADIUS + BALL_RADIUS:
            if id_team == 1:
                if v.player.x<GAME_WIDTH*2/8:
                    shoot = Vector2D(GAME_WIDTH*4/8, GAME_HEIGHT/2)
                    return SoccerAction(shoot = shoot.normalize()*3)
                else:
                    if v.playeradverse.y< GAME_HEIGHT/2 :
                        shoot = Vector2D(GAME_WIDTH*7.5/8, GAME_HEIGHT*3.5/4) - v.player
                        return SoccerAction(shoot = shoot.normalize()*100)
                    else :
                        shoot = Vector2D(GAME_WIDTH*7.5/8, GAME_HEIGHT*0.5/4) - v.player
                        return SoccerAction(shoot = shoot.normalize()*100)
            else :
                if v.player.x>GAME_WIDTH*6/8:
                    shoot = Vector2D(GAME_WIDTH*4/8, GAME_HEIGHT/2)
                    return SoccerAction(shoot = shoot.normalize()*3)
                else:
                    if v.playeradverse.y> GAME_HEIGHT/2 :
                        shoot = Vector2D(GAME_WIDTH*0.5/8, GAME_HEIGHT*0.5/4) - v.player
                        return SoccerAction(shoot = shoot.normalize()*100)
                    else :
                        shoot = Vector2D(GAME_WIDTH*0.5/8, GAME_HEIGHT*3.5/4) - v.player
                        return SoccerAction(shoot = shoot.normalize()*100)
        else :
            if v.ballecampadverse == 0:
                if id_team == 1 :
                    return a.deplacement(Vector2D((GAME_WIDTH/2)-5, v.ball.y))
                else :
                    return a.deplacement(Vector2D((GAME_WIDTH/2)+5, v.ball.y))
            else :
                return a.deplacement(v.ball)
       

# Create teams
team1 = SoccerTeam(name="Team 1")
team2 = SoccerTeam(name="Team 2")

# Add players
team1.add("Player 1", OneVsOne())  # Random strategy
team2.add("Player 2", OneVsOne())   # Random strategy

# Create a match
simu = VolleySimulation(team1, team2)

# Simulate and display the match
volley_show_simu(simu)
