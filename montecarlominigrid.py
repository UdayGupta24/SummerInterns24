# -*- coding: utf-8 -*-
"""22.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1r2-gD5H0_9pvMzhYGI4DnRJj3UD82kO0
"""

!pip install gym-minigrid
import gym_minigrid
import numpy as np
import gym
import matplotlib.pyplot as plt
import random


#Making the environment 
env=gym.make('MiniGrid-Empty-6x6-v0',render_mode="human")
env.reset()


#Initialising q-values
q_value={}
reward=[]
step_taken=[]
for x in range(1,5):
  for y in range(1,5):
    for z in range(4):
      q_value[((x,y),z)]={0:0,1:0,2:0}


#Making a initial policy as equiprobable.
policy={}
for x in range(1,5):
  for y in range(1,5):
    for z in range(4):
      policy[((x,y),z)]={0:1/3,1:1/3,2:1/3}


max_steps=100
gamma=.9
alpha=.4
k=1
old_epsilon=1
no_of_episodes=100


'''This is function which will decay epsilon,Reason for this is that if we do (epsilon/no. of episodes) only 
 then it may happens that due to some reason epsilon becomes too small which will affect our exploration so a minimum value is required.''' 
def epsilon_decay(old_epsilon,episode_no,min_epsilon=.01):
  new_epsilon=max(min_epsilon,(old_epsilon/episode_no))
  return new_epsilon


def episode_generator(env,max_steps,policy):
  env.reset()
  state=(env.agent_pos,env.agent_dir)
  episode=[]
  t=0
  while(True):
    '''here how to choose a action is written basically If we randomly choose actions without using policy then the learning is not nice
    so I have used chatgpt to know how can I use policy or involve the policy in taking actions...'''
    r=random.random()
    action = None
    cumulative_prob = 0.0
    for a in range(3):
      cumulative_prob += policy[state][a]
      if r < cumulative_prob:
        action = a
        break
    obs,reward,done,truncated,info=env.step(action)
    direction=obs['direction']
    time_step=[state,action,reward]
    episode.append(time_step)
    state=(env.agent_pos,direction)
    t=t+1
    '''Termination is being checked'''
    if(t>max_steps or done):
      break
  return episode,t

'''episode will be=[state,action which I took in that state,reward which I get from taking action in that state,....................these 3
terms will be present at each time step]'''

def q_value_generator(epi,gamma,alpha,q_value):
  G=0
  ts=len(epi)-1
  while(ts>=0):
    '''q_value calculation is starting from timestep just before termination. Similarly the return target is also calculated backward
    we are moving back to forward'''
    G=gamma*G+epi[ts][2]
    q_value[epi[ts][0]][epi[ts][1]]=q_value[epi[ts][0]][epi[ts][1]]+alpha*(G-q_value[epi[ts][0]][epi[ts][1]])
    ts=ts-1
  return q_value


def improve_policy(q,policy,episode_no,old_epsilon):
  E=epsilon_decay(old_epsilon,episode_no,min_epsilon=.01)
  for s in q.keys():
    max_action = max(q[s], key=q[s].get)
    '''This is the main content basically in GPI as seen in dynamic programming we were calculating true q_value so we preceeded
     with greedy policy but here the difference is that we don't have true q_value so we are applying epsilon-greedy policy
      which says that don't make probability 1 of greedy action make it less than 1 so we decreased it by  -2E/3 and similarly with non-greedy 
       action don't make probability as 0 make it some value which is E/3,here 3 tells that no. of actions to perform is 3. '''
    for m in range(3):
      if(m==max_action):
        policy[s][m]=1-E+E/3
      else:
        policy[s][m]=E/3
  return(policy)


episode_no=0
'''Now I have statred a loop,, environment generate---->q_values generates----->epsilon_decay----->policy_improve---->environment generate'''
while(episode_no<=no_of_episodes):
  epi,t=episode_generator(env,max_steps,policy)

  step_taken.append(t)
  G1=0

  ts=len(epi)-1

  while(ts>=0):
    G1=gamma*G1+epi[ts][2]
    ts=ts-1
  reward.append(G1)

  q=q_value_generator(epi,gamma,alpha,q_value)
  episode_no=episode_no+1
  older_epsilon=epsilon_decay(old_epsilon,episode_no,min_epsilon=.01)
  policy=improve_policy(q,policy,episode_no,older_epsilon)
print(policy)
print(reward)
print(step_taken)
episodes_list=np.arange(1,len(step_taken)+1)
plt.plot(episodes_list,step_taken)
plt.xlabel('Episodes')
plt.ylabel('steps')
plt.show()

episodes_list=np.arange(1,len(reward)+1)
plt.plot(episodes_list,reward)
plt.xlabel('Episodes')
plt.ylabel('reward')
plt.show()