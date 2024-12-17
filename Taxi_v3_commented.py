# Importing necessary libraries
import gym
# Importing necessary libraries
import numpy as np
# Importing necessary libraries
import time

# Initializing the Taxi-v3 environment
env=gym.make("Taxi-v3",render_mode="human")
nS=500
nA=6
P=env.P


# Function to compute the value function for a given policy
def value_function(currvaluefunction,prevvaluefunction,policy,P,nS,nA,gamma=.9,tol=1e-3):
    max_diff=float('inf')
    while(max_diff>tol):
        for s in range(nS):
            sum1=0
            action=policy[s]
            for prob,nextstate,reward,_ in P[s][action]:
                sum1=sum1+prob*(reward+gamma*prevvaluefunction[nextstate])
            currvaluefunction[s]=sum1
        max_diff=max(np.abs(currvaluefunction-prevvaluefunction))
        prevvaluefunction=currvaluefunction.copy()
    return currvaluefunction


# Function to evaluate a policy using the value function
def policy_evaluation(currvaluefunction,prevvaluefunction,policy,P,nS,nA,gamma=.9,tol=1e-3):
    vf=value_function(currvaluefunction,prevvaluefunction,policy,P,nS,nA,gamma=.9,tol=1e-3)
    return vf


# Function to improve a policy by finding the optimal action for each state
def policy_improvement(currvaluefunction,P,nA,nS,gamma,tol=1e-3):
    new_policy=np.zeros(nS)
    for s in range(nS):
        q=np.zeros(nA)
        for action in range(nA):
            for prob,nextstate,reward,_ in P[s][action]:
                q[action]=prob*(reward+gamma*currvaluefunction[nextstate])
        new_policy[s]=np.argmax(q)
    return new_policy


# Function to perform policy iteration to find the optimal policy
def policy_iteration(P,nS,nA,gamma=.9,tol=1e-3):
    currvaluefunction=np.zeros(nS)
    prevvaluefunction=np.zeros(nS)
    policy=np.array([0,1,2,3,4,5]*nS)
    valuefunction=policy_evaluation(currvaluefunction,prevvaluefunction,policy,P,nS,nA,gamma=.9,tol=1e-3)
    newpolicy=policy_improvement(currvaluefunction,P,nA,nS,gamma,tol=1e-3)
    while not np.array_equal(newpolicy,policy):
        policy=newpolicy.copy()
        valuefunction=policy_evaluation(currvaluefunction,prevvaluefunction,policy,P,nS,nA,gamma=.9,tol=1e-3)
        newpolicy=policy_improvement(currvaluefunction,P,nA,nS,gamma,tol=1e-3)
    return valuefunction,newpolicy



# Function to perform value iteration to find the optimal policy and value function
def Value_iteration(P,nS,nA,gamma=.9,tol=1e-3):
    currvaluefunction=np.zeros(nS)
    prevvaluefunction=np.zeros(nS)
    policy=np.array([0,1,2,3,4,5]*nS)
    for s in range(nS):
        sum1=0
        action =policy[s]
        for prob,nextstate,reward,_ in P[s][action]:
            sum1=sum1+prob*(reward+gamma*prevvaluefunction[nextstate])
        currvaluefunction[s]=sum1
    prevvaluefunction=currvaluefunction.copy()
    max_diff=float('inf')
    while(max_diff>tol):
        for s in range(nS):
            q=[]
            for i in range(nA):
                for prob,nextstate,reward,_ in P[s][i]:
                    k=prob*(reward+gamma*prevvaluefunction[nextstate])
                    q.append(k)
            currvaluefunction[s]=max(q)
        max_diff=np.max(abs(currvaluefunction-prevvaluefunction))
        prevvaluefunction=currvaluefunction.copy()
    new_policy=np.zeros(nS)
    for s in range(nS):
        q=np.zeros(nA)
        for i in range(nA):
            for prob,nextstate,reward,_ in P[s][i]:
                q[i]=prob*(reward+gamma*prevvaluefunction[nextstate])
        new_policy[s]=np.argmax(q)
    return currvaluefunction,new_policy



# Function to render a single episode using a given policy
def render_single(env,policy, max_steps=100):
    episode_reward = 0
    ob = env.reset()
    if isinstance(ob, tuple):  # Adjust if reset returns a tuple
        ob = ob[0]
    for t in range(max_steps):
        env.render()
        time.sleep(0.25)
        a = int(policy[ob])
        step_result = env.step(a)
        if len(step_result) == 4:
            ob, rew, done, info = step_result
        else:
            ob, rew, done, truncated, info = step_result
        episode_reward += rew
        if done:
            break
    env.render()
    if not done:
        print("The agent didn't reach a terminal state in {} steps.".format(max_steps))
    else:
        print("Episode reward: %f" % episode_reward)
            

# Perform policy iteration and get the optimal policy and value function
V_pi,P_pi=policy_iteration(P,nS,nA,gamma=.9,tol=1e-3)

# Perform value iteration and get the optimal policy and value function
V_vi,P_vi=Value_iteration(P,nS,nA,gamma=.9,tol=1e-3)


# Print section headers for clarity in output
print("-"*25 ,'\n'+"Beginning of policy evaluation",'\n'+ "-"*25)
render_single(env,P_pi,max_steps=100)


# Print section headers for clarity in output
print("-"*25 ,'\n'+"Beginning of value evaluation",'\n'+ "-"*25)
render_single(env,P_vi,max_steps=100)


# Close the environment after completing the simulations
env.close()