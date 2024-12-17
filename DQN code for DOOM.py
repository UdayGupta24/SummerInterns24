import gymnasium as gym
from stable_baselines3 import PPO
from gymnasium import Env
from gymnasium.spaces import Discrete, Box
import numpy as np
from vizdoom import *
import os
#downloaded the required libraries 

class udayenv(gym.Env):
    def __init__(self):
        super(udayenv, self).__init__()
        self.game = vizdoom.DoomGame()#taking the game 
        self.game.load_config('E:\\RL\\DRL\\resources\\ViZDoom-master\\ViZDoom-master\\scenarios\\basic.cfg')#loading the basic version of doom
        self.action_space = Discrete(3)#move left,right,attack
        self.observation_space = Box(low=0, high=255, shape=(3, 240, 320), dtype=np.uint8)#here the observation space is continuous
        self.game.set_window_visible(False)#to stop the rendering 
        self.game.init()#initiating the game

    def step(self, action):
        actions = [[1, 0, 0],  # 0
                  [0, 1, 0],  # 1
                  [0, 0, 1]]  # 2
        #seen on overstackflow to represent the actions in terms of Identity matrix
        reward = self.game.make_action(actions[action], 4)
        done = self.game.is_episode_finished()#checking the termination condition.done is true if terminated otherwise false
        
        if not done:
            state = self.game.get_state().screen_buffer#episode not terminated and obtaining the next state
        else:
            state = np.zeros(self.observation_space.shape)#episode terminated.Now the next state is a black window.
            
        info = {}
        # Adding truncated=False as per Gymnasium requirements
        return state, reward, done, False, info
    
    def reset(self, seed=42, options=None):
        super().reset(seed=seed)
        self.game.new_episode()  # Initialising a new episode 
        state = self.game.get_state().screen_buffer# for getting the initial state of the episode
        info = {}  # Added info dict as per Gymnasium requirements
        return state, info

    def close(self):
        self.game.close()

# Training setup
models_dir = "MODELS/PPO"#this is the folder where my models will get save
logdir = "logs"#this is the folder where my information like reward,length,time_elapsed etc will get store.Using this folder only tensorboard will make graphs.

if not os.path.exists(models_dir):
    os.makedirs(models_dir)

if not os.path.exists(logdir):
    os.makedirs(logdir)

# Create and train the model
env = udayenv()
model = PPO("CnnPolicy", env, verbose=1, tensorboard_log=logdir)
'''we are using PPO model in which we are using CnnPolicy,verbose means how much amount of data we have to display
verbose=0:No display 
verbose=1:more display
verbose=2 more more display'''

TIMESTEPS = 1000# Number of timesteps per training iteration
N_STEPS = 5 # Number of training iterations

for step in range(N_STEPS):
    model.learn(total_timesteps=TIMESTEPS, reset_num_timesteps=False, tb_log_name="PPO")
    model.save(f"{models_dir}/{TIMESTEPS*step}")

env.close()
