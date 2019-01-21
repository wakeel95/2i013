#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 17:43:43 2019

@author: 3704116
"""

# coding: utf-8
from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu, GAME_WIDTH, GAME_HEIGHT, GAME_GOAL_HEIGHT, PLAYER_RADIUS, BALL_RADIUS


class RandomStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Random")

    def compute_strategy(self, state, id_team, id_player):
        # id_team is 1 or 2
        # id_player starts at 0
        
        d = PLAYER_RADIUS + BALL_RADIUS 
        mvt = state.ball.position - state.player_state(id_team,id_player).position
        
       
    
        
        if id_team == 1:
            tir = Vector2D(GAME_WIDTH,GAME_HEIGHT/2) - state.ball.position
        else :
            tir = Vector2D(0,GAME_HEIGHT/2) - state.ball.position
       
       
        return SoccerAction(mvt,tir)


# Create teams
team1 = SoccerTeam(name="Team 1")
team2 = SoccerTeam(name="Team 2")

# Add players
team1.add("CR7", RandomStrategy())  # Random strategy
team2.add("Static", Strategy())   # Static strategy

# Create a match
simu = Simulation(team1, team2)

# Simulate and display the match
show_simu(simu)